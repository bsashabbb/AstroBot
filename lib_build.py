import json
from pathlib import Path
from typing import List, Dict, Set, Any, Union

class CodeGenerator:
    TYPE_MAP = {
        "Integer": "int",
        "String": "str",
        "Boolean": "bool",
        "Float": "float",
        "Int": "int",
        "True": "bool",
        "False": "bool",
        "Message": "Union[Message, InaccessibleMessage]"
    }

    def __init__(self, api_spec: Dict[str, Any]):
        self.api_spec = api_spec
        self.classes = {obj["name"] for obj in self.api_spec.get("objects", [])}

    def generate(self, output_dir: str):
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Генерация файлов
        (output_path / "models.py").write_text(self._generate_models())
        (output_path / "methods.py").write_text(self._generate_methods())
        (output_path / "client.py").write_text(self._generate_client())

    def _generate_models(self) -> str:
        code = [
            "from typing import Optional, Union, List, Dict, Any",
            "from datetime import datetime\n",
            self._generate_type_checker(),
        ]
        
        for obj in self.api_spec.get("objects", []):
            code.append(self._generate_model_class(obj))
        
        return "\n\n".join(code)

    def _generate_model_class(self, obj: Dict) -> str:
        class_name = obj.get("name", "UnknownClass")
        fields = obj.get("fields", [])
        
        lines = [
            f"class {class_name}:",
            f'    """{" ".join(obj.get("description", []))}"""',
            "    def __init__(self, **kwargs: Any):"
        ]
        
        # Инициализация полей
        for field in fields:
            name = field.get("snake_name", "unknown")
            lines.extend([
                f"        self._{name} = None",
                f"        if '{name}' in kwargs:",
                f"            self.{name} = kwargs['{name}']"
            ])
        
        # Геттеры/сеттеры
        for field in fields:
            name = field.get("snake_name", "unknown")
            py_type = self._convert_type(field.get("type", "Any"))
            if not field.get("required", False):
                py_type += " | None"
            
            lines.extend([
                f"\n    @property",
                f"    def {name}(self) -> {py_type}:",
                f"        return self._{name}",
                f"\n    @{name}.setter",
                f"    def {name}(self, value: {py_type}) -> None:",
                f"        TypeChecker.check(value, '{py_type}')",
                f"        self._{name} = value"
            ])
        
        # Метод to_dict()
        lines.extend([
            "\n    def to_dict(self) -> Dict[str, Any]:",
            "        return {"
        ])
        for field in fields:
            name = field.get("snake_name", "unknown")
            lines.append(f"            '{name}': self._{name},")
        lines.append("        }")
        
        return "\n".join(lines)

    def _generate_methods(self) -> str:
        code = [
            "from typing import Optional, Dict, Any, Union, List",
            "from .client import TelegramClient",
            "from .models import *\n",
            "class BotAPI(TelegramClient):"
        ]
        
        for method in self.api_spec.get("methods", []):
            code.append(self._generate_api_method(method))
        
        return "\n\n".join(code)

    def _generate_api_method(self, method: Dict) -> str:
        method_name = method.get("snake_name", "unknown_method")
        params = []
        param_dict = []
        
        for param in method.get("fields", []):
            name = param.get("snake_name", "unknown")
            py_type = self._convert_type(param.get("type", "Any"))
            if not param.get("required", False):
                py_type += " | None"
            
            params.append(f"        {name}: {py_type} = None")
            param_dict.append(f"            '{param['name']}': {name}")
        
        return (
            f"    async def {method_name}(self,\n" + 
            ",\n".join(params) + "\n    ) -> Dict[str, Any]:\n" +
            f'        """{" ".join(method.get("description", ["No description"]))}"""\n' +
            "        params = {\n" + 
            ",\n".join(param_dict) + "\n        }\n" +
            "        return await self._request(\n" +
            f"            '{method.get('name', 'unknown')}',\n" +
            "            {k: v for k, v in params.items() if v is not None}\n" +
            "        )"
        )

    def _convert_type(self, type_str: str) -> str:
        if "Array of " in type_str:
            inner = type_str.replace("Array of ", "").strip()
            return f"List[{self._convert_type(inner)}]"
        
        for sep in [" or ", "/", ", "]:
            if sep in type_str:
                types = [self._convert_type(t) for t in type_str.split(sep)]
                return " | ".join(types)
        
        return self.TYPE_MAP.get(type_str, type_str) if type_str not in self.classes else type_str

    @staticmethod
    def _generate_type_checker() -> str:
        return """class TypeChecker:
    @staticmethod
    def check(value: Any, expected_type: str) -> None:
        if value is None:
            return
        type_list = [t.strip() for t in expected_type.split("|")]
        if any(isinstance(value, eval(t)) for t in type_list):
            return
        raise TypeError(f"Expected {expected_type}, got {type(value).__name__}")
\n"""

    @staticmethod
    def _generate_client() -> str:
        return """import httpx

class TelegramClient:
    def __init__(self, token: str):
        self.base_url = f"https://api.telegram.org/bot{token}/"
        self.client = httpx.AsyncClient()
    
    async def _request(self, method: str, params: dict) -> dict:
        response = await self.client.post(
            f"{self.base_url}{method}",
            json={k: v for k, v in params.items() if v is not None}
        )
        response.raise_for_status()
        return response.json()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *exc):
        await self.client.aclose()
"""

if __name__ == "__main__":
    with open("telegram_api.json") as f:
        api_spec = json.load(f)
    
    CodeGenerator(api_spec).generate("tg_api")