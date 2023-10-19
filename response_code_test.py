import sender_stand_request

# Евгений Макаренко, 9-ая когорта - финальный проект. Инженер по тестированию плюс.

# Функция проверки статуса кода
def response_code_assert():
    response = sender_stand_request.get_new_order_track()
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200

# Тест. Проверка статуса кода
def test_response():
    response_code_assert()