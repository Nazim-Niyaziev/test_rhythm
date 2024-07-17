from api import Regres


get_users = Regres()


def test_golden_path():
    """Позитивный сценарий. Запрос отрабатывает в соответствии с требованиями"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = get_users.get_users(0, 0, 0, 0)

    # статус код 200
    assert status == 200
    # тело ответа непустое
    assert len(result) > 0
    # тело ответа в формате json
    assert isinstance(result, dict)
    # тело ответа содержит требуемые ключи значений
    assert set(result.keys()) == {'data', 'total_pages', 'support', 'per_page', 'page', 'total'}
    # в теле ответа содержатся ссылки на изображения пользователей
    for user in result['data']:
        assert 'avatar' in user, f"У пользователя {user['id']} отсутствует аватар."
        assert user['avatar'].startswith('https://'), f"У пользователя {user['id']} остутствует URL его аватара."


def test_one_user_per_page():
    """Позитивный сценарий. Запрос с параметрами для отображения одного пользователя"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = get_users.get_users(1, 1, 0, 0)

    # статус код 200
    assert status == 200
    # тело ответа содержит информацию об одном пользователе
    assert len(result['data']) == 1
    assert set(result['data'][0].keys()) == {'id', 'email', 'first_name', 'last_name', 'avatar'}


def test_empty_params():
    """Негативный сценарий. Запрос с пустыми параметрами. Ожидаем 400 статус код"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = get_users.get_users("", "", "", "")

    # статус код 400
    assert status == 400
    # тело ответа содержит информацию об ошибке. Закомментировал, потому что нет явных требований на случай
    # такого кейса в документации
    # assert 'error' in result


def test_change_sys_status():
    """Проверка того что запрос не меняет состояния системы"""

    # Отправляем два одинаковых запроса и сохраняем полученные ответы
    result = get_users.get_users(1, 6, 0, 0)
    result_second = get_users.get_users(1, 6, 0, 0)
    # Проверка того что ответы идентичны
    assert result == result_second


def test_invalid_params_symbols_str():
    """Негативный сценарий. Запрос с невалидными необязательными параметрами. Ожидаем 400 статус код"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = get_users.get_users("rQW", "@#$", 0, 0)

    # статус код 400
    assert status == 400
    # тело ответа содержит информацию об ошибке. Закомментировал, потому что нет явных требований на случай
    # такого кейса в документации
    # assert 'error' in result


def test_destructed_params_long_str():
    """Негативный сценарий. Деструктивная проверка на ввод очень большой строки в параметрах. Ожидаем 400 статус код"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = get_users.get_users("yryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryry"
                                         "ryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryry"
                                         "ryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryry"
                                         "ryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryryry"
                                         "ryryryryryryryryryryryr", 0, 0, 0)

    # статус код 400
    assert status == 400
    # тело ответа содержит информацию об ошибке. Закомментировал, потому что нет явных требований на случай
    # такого кейса в документации
    # assert 'error' in result
