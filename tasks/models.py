from django.db import models


class Task(models.Model):
    title = models.CharField("Название задачи", max_length=100)
    is_completed = models.BooleanField("Выполнена", default=False)
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        
    def __str__(self):
        return self.title
