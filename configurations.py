import json


# Запись в конфиг
def write(to_json: dict) -> None:
    try:
        with open("config.json", "r") as f:
            template = json.load(f)
        if template is None:
            raise FileNotFoundError
        template = dict(template)
        template.update(to_json)
        with open("config.json", "w") as f:
            json.dump(template, f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        with open("config.json", "w") as f:
            json.dump(to_json, f)


# Считывание данных из конфига
def read() -> dict:
    try:
        with open("config.json", "r") as f:
            template = json.load(f)
        if template is None:
            raise FileNotFoundError
    except (json.JSONDecodeError, FileNotFoundError) as e:
        template = dict()
    return template


# Считывание вашего логина и пароля
def register() -> None:
    email = input("Enter e-mail: ")
    write({'email': email})
    password = input("Enter password: ")
    write({'password': password})
