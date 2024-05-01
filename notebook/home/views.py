from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm

def all_notes(request):
	notes = Note.objects.all()
	return render(request, 'all_notes.html', {'notes': notes})


def create_note(request):
	if (request.method == 'POST'):
		form = NoteForm(request.POST)
		form.save()
		return redirect('all_notes')
	
	return render(request, 'create_note.html', { 'form': NoteForm })
	
	