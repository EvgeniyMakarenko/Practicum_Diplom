import configuration
import requests
import data

# Функция создания заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

# Функция получения номера трека
def get_new_track():
    # запись ответа в переменную response
    response = post_new_order(data.order_body)
    # запись номера трека в переменную track
    track = response.json()["track"];
    return track

# Функция запроса на получение заказа по треку заказа
def get_new_order_track():
    # запись номера трека в переменную track
    track = get_new_track()
    # запись номера трека в URL
    payload = {'t': track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_NEW_ORDER,  params=payload) # подставляем полный url





