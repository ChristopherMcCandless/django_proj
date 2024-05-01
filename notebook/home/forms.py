from .models import Note
from django.forms import ModelForm, TextInput, Textarea


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'content']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название заметки'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст заметки'
            }),
        }