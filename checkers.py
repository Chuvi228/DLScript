# Проверка, что в файле есть ссылки
def check_refs(data: dict) -> bool:
    if data.get('refs'):
        return True
    else:
        return False


# Проверка, что в файле есть регистрационные данные
def check_reg(data: dict) -> bool:
    if data.get('email') and data.get('password'):
        return True
    else:
        return False
