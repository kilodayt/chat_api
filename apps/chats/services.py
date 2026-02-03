"""
POST /chats/ — создать чат
 Body: title: str
 Response: созданный чат

POST /chats/{id}/messages/ — отправить сообщение в чат
 Body: text: str
 Response: созданное сообщение

GET /chats/{id} — получить чат и последние N сообщений
 Query: limit (по умолчанию 20, максимум 100)
 Response: чат
 messages: [] (сообщения отсортированы по created_at)

DELETE /chats/{id} — удалить чат вместе со всеми сообщениями
 Response: 204 No Content (или json-статус)
"""
from django.shortcuts import get_object_or_404

from .models import Chat, Message


class ChatsService:
    @staticmethod
    def create_chat(title: str) -> Chat:
        chat = Chat.objects.create(title=title)
        return chat

    @staticmethod
    def add_message(chat_id: int, text: str) -> Message:
        chat = get_object_or_404(Chat, pk=chat_id)
        message = Message.objects.create(chat=chat, text=text)
        return message

    @staticmethod
    def get_chat_with_messages(chat_id: int, limit: int):
        chat = get_object_or_404(Chat, pk=chat_id)
        message = chat.messages.all().order_by('-created_at')[:limit]
        return chat, message

    @staticmethod
    def delete_chat(chat_id: int):
        chat = get_object_or_404(Chat, pk=chat_id)
        chat.delete()
