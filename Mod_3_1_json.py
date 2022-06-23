# Создайте простые словари и сконвертируйте их в JSON. Сохраните JSON в файл и попробуйте загрузить данные из файла.
import json

manager_comp = [
    {"name": "Mike",
     "type": "laptop",
     "mark": "lenovo",
     "price": 300
    },
    {"name": "Sarah",
     "type": "laptop",
     "mark": "mac",
     "price": 1300
    },
    {"name": "Nataly",
     "type": "all-in-one",
     "mark": "acer",
     "price": 830
     }
]

json_maneger_comp = json.dumps(manager_comp)

with open("write_data.json", "w") as f:
    json.dump(manager_comp, f)

with open("write_data.json", "r") as f:
    jmk = json.load(f)
    print(jmk)
