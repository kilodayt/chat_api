import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_chat_and_message(api_client):
    # Создание чата
    response = api_client.post('/chats/',
                               {'title': ' test '},
                               format='json')
    assert response.status_code == 201

    # Получение названия чата (с удалением пробелов)
    chat_id = response.data['id']
    assert response.data['title'] == 'test'

    # Создание сообщения
    msg_response = api_client.post(f'/chats/{chat_id}/messages/',
                                   {'text': ' Hello '},
                                   format='json')
    assert msg_response.status_code == 201

    # Проверка что сообщение создалось
    get_response = api_client.get(f'/chats/{chat_id}/?limit=5')
    assert len(get_response.data['messages']) == 1

    # Удаление чата
    delete_response = api_client.delete(f'/chats/{chat_id}/',
                                        format='json')
    assert delete_response.status_code == 204


