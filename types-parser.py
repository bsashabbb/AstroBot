from typing import List, Dict, Set
from pathlib import Path
import requests
from bs4 import BeautifulSoup, Tag
import logging
import re

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

class TelegramAPIParser:
    BASE_URL = "https://core.telegram.org/bots/api"
    TYPES_DIR = Path("astrobot/types")

    TYPE_MAP = {
        "integer": "int",
        "string": "str",
        "boolean": "bool",
        "float": "float",
        "true": "bool",
        "false": "bool"
    }

    RESERVED_WORDS = {
        "from", "class", "def", "async", "await", "import",
        "is", "in", "and", "or", "not", "lambda", "None"
    }

    def __init__(self):
        self.all_types: Set[str] = set()

    def run(self):
        self._clean_dir()
        html = requests.get(self.BASE_URL).text
        types = self._parse_types(html)
        self.all_types = {t["name"] for t in types if t["name"] != "InvalidType"}

        for t in types:
            if t["name"] != "InvalidType":
                self._save_type(t)

        self._create_init()
        logger.info(f"Сгенерировано типов: {len(self.all_types)}")

    def _parse_types(self, html: str) -> List[Dict]:
        soup = BeautifulSoup(html, "html.parser")
        valid_h4 = []
        for h4 in soup.find_all("h4"):
            if isinstance(h4, Tag) and self._valid_type(h4):
                valid_h4.append(h4)
        return [self._parse_type(h4) for h4 in valid_h4]

    def _parse_type(self, h4: Tag) -> Dict:
        try:
            type_name = self._sanitize_name(h4.text.strip())
        except AttributeError:
            logger.error("Элемент не содержит текста")
            return {"name": "InvalidType", "fields": []}

        table = h4.find_next("table")
        fields = []

        if table:
            for row in table.find_all("tr")[1:]:
                try:
                    fields.append(self._parse_row(row))
                except Exception as e:
                    logger.error(f"Ошибка в типе {type_name}: {str(e)}")

        return {"name": type_name, "fields": fields}

    def _parse_row(self, row: Tag) -> Dict:
        cols = [td.text.strip() for td in row.find_all("td")]
        if len(cols) < 3:
            raise ValueError("Некорректный формат строки")

        raw_type = cols[1]
        description = cols[2]
        field_name = self._sanitize_name(cols[0].replace(" ", "_"))
        optional = any(s in description.lower() for s in {"optional", "may be empty"})

        return {
            "name": field_name,
            "type": self._process_type(raw_type, optional),
            "optional": optional
        }

    def _process_type(self, raw_type: str, optional: bool) -> str:
        type_str = re.sub(r'\b(or)\b', "Union", raw_type, flags=re.IGNORECASE)
        type_str = type_str.replace("Array of", "List").replace("array of", "List")

        if "Union" in type_str:
            types = [self._process_type(t.strip(), False) for t in type_str.split("Union")[1].split(",")]
            type_str = f"Union[{', '.join(types)}]"

        if "List" in type_str:
            match = re.match(r"List(?: of)? (.*)", type_str, re.IGNORECASE)
            if match:
                inner_type = self._process_type(match.group(1).strip(), False)
                type_str = f"List[{inner_type}]"

        base_type = type_str.split("[", 1)[0].strip()
        if base_type.lower() in self.TYPE_MAP:
            type_str = type_str.replace(base_type, self.TYPE_MAP[base_type.lower()], 1)

        if optional:
            type_str = f"Optional[{type_str}]"

        return type_str

    def _sanitize_name(self, name: str) -> str:
        if name in self.RESERVED_WORDS:
            return f"{name}_"
        return re.sub(r"[^a-zA-Z0-9_]", "_", name)

    def _valid_type(self, h4: Tag) -> bool:
        try:
            name = h4.text.strip()
        except AttributeError:
            return False
        return name and " " not in name and name not in ["InputFile", "Updates"]

    def _save_type(self, type_def: Dict):
        code = [
            "from __future__ import annotations",
            "from typing import Optional, List, Union\n",
            f"class {type_def['name']}:",
            "    def __init__(",
            "        self,"
        ]

        required_params = []
        optional_params = []

        for field in type_def['fields']:
            param = f"        {field['name']}: '{field['type']}'"
            if field["optional"]:
                optional_params.append(param + " = None")
            else:
                required_params.append(param)

        params = required_params + optional_params

        code.append(",\n".join(params) + "\n    ):")
        code.extend([f"        self.{f['name']} = {f['name']}" for f in type_def["fields"]])

        path = self.TYPES_DIR / f"{type_def['name'].lower()}.py"
        path.write_text("\n".join(code))
        logger.info(f"Файл создан: {path}")

    def _create_init(self):
        imports = [f"from .{t.lower()} import {t}" for t in self.all_types]
        (self.TYPES_DIR / "__init__.py").write_text("\n".join(sorted(imports)))

    def _clean_dir(self):
        self.TYPES_DIR.mkdir(exist_ok=True, parents=True)
        for f in self.TYPES_DIR.glob("*.py"):
            if f.name != "__init__.py":
                f.unlink()

if __name__ == "__main__":
    TelegramAPIParser().run()