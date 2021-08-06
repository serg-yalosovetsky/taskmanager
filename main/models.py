from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField()
    done = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'