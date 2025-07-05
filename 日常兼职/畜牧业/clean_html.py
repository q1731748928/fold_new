import json
import re

from lxml import etree

with open("./result.txt") as f:
    response = f.read()
    cleaned_response = response.replace("\\", "")  # 去除反斜杠
    print(cleaned_response)
tree = etree.HTML(cleaned_response)
script_data = tree.xpath("//script[contains(., 'var allinput_data =')]/text()")
if script_data:
    # Use regex to extract the JSON part
    json_match = re.search(r"var allinput_data = (\[.*?\]);", script_data, re.S)
    if json_match:
        json_string = json_match.group(1)
        try:
            allinput_data = json.loads(json_string)
            with open("allinput_data.json", "w") as f:
                f.write(allinput_data)
        except Exception as e:
            print(e)