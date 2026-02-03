from django.db import models


class Chat(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название чата"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    text = models.TextField(verbose_name="Текст сообщения")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
