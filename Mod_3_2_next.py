from xml.etree import ElementTree as E

tree = E.parse('student_list.xml')
root = tree.getroot()

for student in root:
    print("faculty: ", (student.attrib, student.get("faculty")))
    print(f"{student.find('./name').text} {student.find('./surname').text}")

print()

name = root.findall("./student/name")
nationality = root.findall("./student/birthday")

for values in zip(name, nationality):
    row = {value.tag: value.text for value in values}
    print(row)

