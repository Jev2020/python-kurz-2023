import json

with open('body.json', encoding='utf-8') as file:
    hodnoceni = json.load(file)

with open("prospech.json", mode="w", encoding='utf-8') as file:
    json.dump(hodnoceni, file)

for jmena_zaku, body in hodnoceni.items():
    if body >= 60:
        print(hodnoceni.fromkeys(hodnoceni, 'Pass'))
    else:
        print(hodnoceni.fromkeys(hodnoceni, 'Fail'))
