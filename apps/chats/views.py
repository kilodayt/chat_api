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

from pydantic import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ChatSerializer, MessageSerializer
from .services import ChatsService
from apps.chats.schemas import ChatCreateSchema, MessageCreateSchema


class ChatListCreateView(APIView):
    def post(self, request):
        try:
            schema = ChatCreateSchema(**request.data)
            chat = ChatsService.create_chat(title=schema.title)
            return Response(ChatSerializer(chat).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e.messages, status=status.HTTP_400_BAD_REQUEST)


class ChatDetailView(APIView):
    def get(self, request, pk):
        try:
            limit = int(request.query_params.get('limit', 20))
            if limit > 100:
                limit = 100
        except ValueError:
            limit = 20

        chat, messages = ChatsService.get_chat_with_messages(chat_id=pk, limit=limit)

        return Response({
            "chat": ChatSerializer(chat).data,
            "messages": MessageSerializer(messages, many=True).data,
        })

    def delete(self, request, pk):
        ChatsService.delete_chat(chat_id=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageCreateView(APIView):
    def post(self, request, pk):
        try:
            schema = MessageCreateSchema(**request.data)
            message = ChatsService.add_message(chat_id=pk, text=schema.text)

            return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e.messages, status=status.HTTP_400_BAD_REQUEST)


