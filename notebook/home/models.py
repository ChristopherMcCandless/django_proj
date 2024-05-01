from django.db import models

class Note(models.Model):
    name = models.CharField('Наименование', max_length=100)
    content = models.CharField('Заметка', max_length=1000)

    def __str__(self):
        return f'Заметка: {self.name}'