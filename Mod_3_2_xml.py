# Создайте XML файл с вложенными элементами и воспользуйтесь языком поиска XPATH.
# Попробуйте осуществить поиск содержимого по созданному документу XML, усложняя свои запросы и
# добавляя новые элементы, если потребуется.
from xml.etree import ElementTree as E

data = [
    {'name': "Ivan", "surname": "Ivanov", 'birthday': 1995, 'nationality': 'rus'},
    {'name': "Petro", "surname": "Petrenko", 'birthday': 1996, 'nationality': 'ukr'},
    {'name': "John", "surname": "Jonson", 'birthday': 1994, 'nationality': 'eng'},
    {'name': "Chan", "surname": "Chanyn", 'birthday': 1997, 'nationality': 'cn'},

]

root = E.Element("students")

for i in data:
    student = E.SubElement(root, "student")
    for key, value in i.items():
        el = E.SubElement(student, key)
        el.text = str(value)

tree = E.ElementTree(root)
tree.write("student_list.xml", encoding="utf-8")

