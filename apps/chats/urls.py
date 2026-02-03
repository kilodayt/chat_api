from django.urls import path

from apps.chats.views import ChatListCreateView, ChatDetailView, MessageCreateView

urlpatterns = [
    # POST /chats/ - создание чата
    path('chats/', ChatListCreateView.as_view(), name='chat_list_create'),

    # POST /chats/{id} - получить сообщения в чате
    # DELETE /chats/{id} - удалить чат вместе с сообщениями
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='chat_detail'),

    # POST /chats/{id}/messages/ - создать сообщение в чате
    path('chats/<int:pk>/messages/', MessageCreateView.as_view(), name='message_create'),
]
