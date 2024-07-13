from .models import NoteBooks
import datetime
from django.contrib.auth.models import User
import os
from notebook import settings


class Data_Manpulation:

    def save_notebook_data(request,noteTitle,noteContent,image):
        '''This function will save the notes provided by the user'''

        try:
            user = User.objects.get(username = request.user.username)
            if image:
                notebook = NoteBooks.objects.create(user = user,title=noteTitle,
                                                description = noteContent,image=image)
            else:
                notebook = NoteBooks.objects.create(user=user,title=noteTitle,
                                                description = noteContent)
            notebook.save()

            return True
        except:
            return False

    def delete_note(pk):
        try:
            notebook = NoteBooks.objects.get(pk = pk)
            path = str(notebook.image)
            if (os.path.isfile(path)):
                os.remove(path)
            notebook.delete()

            return True
        except:
            return False
        
        
        
