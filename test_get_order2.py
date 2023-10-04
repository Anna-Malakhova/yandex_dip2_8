import sender_stand_request2
import data2

# Функция - выполнить запрос на получения заказа по треку заказа
def test_get_order_info_by_track():
    order_track = sender_stand_request2.create_order(data2.order_body)
    track = {"t": order_track.json()["track"]}
    response = sender_stand_request2.get_order_info_by_track(sender_stand_request2.track)
    assert response.status_code == 200

