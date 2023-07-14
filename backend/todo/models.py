import uuid
from django.db import models

class Todo(models.Model):
    STATUS_FINISHED = "FN"
    STATUS_STARTED = "ST"
    CHOICES = [
        (STATUS_FINISHED, "FINISHED"),
        (STATUS_STARTED, "STARTED")
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=CHOICES, default=STATUS_STARTED)

    def __str__(self):
        return f"{self.title} - {self.created_at}"