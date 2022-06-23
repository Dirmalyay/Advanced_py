# Поработайте с созданием собственных диалектов, произвольно выбирая правила для CSV файлов.
# Зарегистрируйте созданные диалекты и поработайте, используя их, с созданием/чтением файлом.

import csv


class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "'"
    delimiter = "*"
    lineterminator = "\n"


csv.register_dialect("mydialect", MyDialect)

with open("tiere.csv", "w") as f:
    writer = csv.writer(f, dialect="mydialect")
    writer.writerow(["Harry", "kater", 18])
    writer.writerow(["Sarah", "hund", 5])
    writer.writerow(["Pary", "vogel", 2])

sniffer = csv.Sniffer()
dialect = None

with open("tiere.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)

with open("tiere.csv", "r") as f:
    text = f.read()
    dialect = sniffer.sniff(text)

print(dialect.delimiter, dialect.doublequote, dialect.quoting)

with open("tiere.csv", "r") as f:
    reader = csv.reader(f, dialect=dialect)
    for i in reader:
        print(i)
