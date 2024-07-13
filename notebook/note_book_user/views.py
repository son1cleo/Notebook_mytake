from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .renderData import Data_Manpulation
from .models import NoteBooks
from notebook import settings


# Create your views here.

@login_required #function decorator
def landingPage(request):
    return render(request,"index.html")

def login(request):

    if request.method == "POST":

        if request.POST.get('login_button'):

            username_ = request.POST.get('username')
            password_ = request.POST.get('password')

            user = auth.authenticate(username = username_,password = password_)

            if user is not None:
                auth.login(request,user)
                return redirect('note_book_user:dashboard')
            else:
                messages.error(request,'Invalid Credentials/User not registered')
                return redirect('note_book_user:login')

    return render(request,"login.html")



def signup(request):

    if request.method == "POST":

        if request.POST.get('sign_up'):
            #clicked sign up button

            username_ = request.POST.get('username')
            password_ = request.POST.get('password')
            confirm_password_ = request.POST.get('confirm_password')

            if password_ == confirm_password_:
                if User.objects.filter(username = username_).exists():
                    pass
                else:
                    user = User.objects.create_user(username = username_,password = password_)
                    user.save()
                    messages.success(request,"User created successfully")
                    return redirect('note_book_user:login')
            else:
                messages.error(request,"Password did not match")
                return redirect('note_book_user:signup')
            


            


    return render(request,"signup.html")

def logout(request):
    auth.logout(request)
    return redirect('note_book_user:login')

@login_required
def dashboard(request):

    
    all_notes = NoteBooks.objects.filter(user = User.objects.get(username = request.user.username)).order_by('-date')
    title = "Dashboard"
    print(all_notes)
    
    #forming request
    if request.method == "POST":

        if request.POST.get('logout_btn'):
           
            auth.logout(request)
            return redirect('note_book_user:login')
        
        if request.POST.get('submit_note'):

            noteTitle = request.POST.get('noteTitle')
            noteContent = request.POST.get('noteContent')
            image = request.FILES.get('image')


            if Data_Manpulation.save_notebook_data(request,noteTitle,noteContent,image):
                messages.success(request,"Notes added")     
            else:
                messages.error(request,"Failed")
            return redirect('note_book_user:dashboard')
        
        if request.POST.get('delete_note'):

            note_id = int(request.POST.get('note_id'))
            
            if Data_Manpulation.delete_note(note_id):
                messages.success(request,"Note Deleted")     
            else:
                messages.error(request,"Failed")
            return redirect('note_book_user:dashboard')

    print(settings.MEDIA_URL)
    context = {
        'all_notes':all_notes,
        'title':title,
        'media_url':settings.MEDIA_URL,
    }            


    return render(request, "dashboard.html",context)

