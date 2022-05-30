# Проверка, что в файле есть ссылки
def check_refs(data: dict[str, str]) -> bool:
    return 'refs' in data


# Проверка, что в файле есть регистрационные данные
def check_reg(data: dict[str, str]) -> bool:
    return 'email' in data and 'password' in data
