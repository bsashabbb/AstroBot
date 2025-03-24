import httpx
import re
import json
from bs4 import BeautifulSoup

def camel_to_snake(name):
    if name.lower() == "from":
        return "from_user"
    
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return name

def convert_type(type_str, classes):
    type_map = {
        "Integer": "int",
        "String": "str", 
        "Boolean": "bool",
        "Float": "float",
        "Int": "int",
        "True": "bool",
        "False": "bool",
    }
    
    if "Array of " in type_str:
        inner = type_str.replace("Array of ", "").strip()
        return f"list[{convert_type(inner, classes)}]"
    
    for sep in [" or ", "/", ", "]:
        if sep in type_str:
            types = [convert_type(t, classes) for t in type_str.split(sep)]
            return " | ".join(sorted(set(types), key=types.index))
    
    return type_map.get(type_str, type_str) if type_str not in classes else type_str

def parse_table(table, is_method):
    rows = table.find_all("tr")
    if not rows:
        return []
    
    headers = [th.get_text().strip() for th in rows[0].find_all("th")]
    results = []
    
    for row in rows[1:]:
        cells = [td.get_text().strip() for td in row.find_all("td")]
        if len(cells) != len(headers):
            continue
            
        data = dict(zip(headers, cells))
        name = data.get("Parameter") or data.get("Field", "")
        
        required = (
            data.get("Required", "").lower() in ["yes", "required"]
            if is_method
            else "optional" not in data.get("Description", "").lower()
        )
        
        results.append({
            "name": name,
            "snake_name": camel_to_snake(name),
            "type": data.get("Type", ""),
            "description": " ".join(data.get("Description", "").split()),
            "required": required
        })
    
    return results

def parse_section(section, classes):
    items = []
    current = section.find_next_sibling()
    
    while current and current.name != "h3":
        if current.name == "h4":
            title = current.get_text().strip()
            if " " in title:
                current = current.find_next_sibling()
                continue
                
            item = {
                "name": title,
                "snake_name": camel_to_snake(title),
                "description": [],
                "fields": []
            }
            
            next_el = current.find_next_sibling()
            while next_el and next_el.name not in ["h4", "h3", "table"]:
                if next_el.name == "p":
                    item["description"].append(next_el.get_text().strip())
                next_el = next_el.find_next_sibling()
            
            if next_el and next_el.name == "table":
                is_method = "Parameter" in next_el.find("th").get_text()
                item["fields"] = parse_table(next_el, is_method)
            
            items.append(item)
            current = next_el
        else:
            current = current.find_next_sibling()
    
    return items

def main():
    response = httpx.get("https://core.telegram.org/bots/api")
    soup = BeautifulSoup(response.text, "html.parser")
    
    classes = set()
    result = {"methods": [], "objects": []}
    
    for section in soup.find_all("h3"):
        if "available types" in section.text.lower():
            items = parse_section(section, classes)
            classes.update(item["name"] for item in items)
            result["objects"].extend(items)
        elif "available methods" in section.text.lower():
            result["methods"].extend(parse_section(section, classes))
    
    with open("telegram_api.json", "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()