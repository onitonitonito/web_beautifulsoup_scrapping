"""
# Reading and Writing JSON to a File in Python
# By  Scott Robinson • August 17, 2016 • 5 Comments
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
"""
# print(__doc__)

import os
# script_run ... different dir           script_run  vs. terminal(cmd)
print(os.getcwd())                      # --> root    /  working
print(os.path.abspath(os.path.curdir))  # --> root    /  working
print(os.path.dirname(__file__))        # --> working /  working (this!)


import json

dir_current = os.path.dirname(__file__)
dir_read_write = f'{dir_current}/statics'
filename_with_dir = f'{dir_read_write}/_test_json.json'


data = {}

data['people'] = []

data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})

data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})

data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})


with open(file=filename_with_dir, mode='w', encoding='utf8') as file:
    json.dump(obj=data, fp=file, sort_keys=True, indent=2, ensure_ascii=False)

"""
{
  "people": [
    {
      "from": "Nebraska",
      "name": "Scott",
      "website": "stackabuse.com"
    },{
      "from": "Michigan",
      "name": "Larry",
      "website": "google.com"
    },{
      "from": "Alabama",
      "name": "Tim",
      "website": "apple.com"
    }
  ]
}
"""

with open(file=filename_with_dir, mode='r', encoding='utf8') as file:
    _test_json = json.load(fp=file)


for i, people in enumerate(_test_json['people'],1):
    [print(echo)
        for echo in [
                    f"\n\n"
                    f"-------------------------",
                    f" ({i}) PEOPLE INFORMATION",
                    f"-------------------------",
                    f"* Name     : {people['name']}",
                    f"* From     : {people['from']}",
                    f"* Web site : {people['website']}",
                    f"-------------------------",
                    ]
        ]



"""
-------------------------
 (1) PEOPLE INFORMATION
-------------------------
* Name     : Scott
* From     : Nebraska
* Web site : stackabuse.com
-------------------------


-------------------------
 (2) PEOPLE INFORMATION
-------------------------
* Name     : Larry
* From     : Michigan
* Web site : google.com
-------------------------


-------------------------
 (3) PEOPLE INFORMATION
-------------------------
* Name     : Tim
* From     : Alabama
* Web site : apple.com
-------------------------
"""
