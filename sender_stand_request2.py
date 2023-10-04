import configuration2
import requests
import data2

# Запрос на создание нового заказа
def create_order():
    return requests.post(configuration2.URL_SERVICE + configuration2.CREATE_ORDER_PATH,
                         json = body)

# Данные о заказе по номеру
def get_order_info_by_track(track):
    return requests.get(configuration2.URL_SERVICE+configuration2.ORDER_TRACK, params = track)
