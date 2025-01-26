from django.shortcuts import render,redirect
from .models import UserMessages,Room,CustomUser
from .forms import RegistrationForm,TextForm,UserListing,EditMessage,UpdateProflieForm,ListingForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import UserMessagesSerializer,CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserMessagesViewSet(viewsets.ModelViewSet):
    queryset =UserMessages.objects.all()
    serializer_class = UserMessagesSerializer
# Create your views here.

def registerPage(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(data=request.POST,files=request.FILES)  
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('home')

    context = {'form': form}
    return render(request, 'Base/register.html', context)

def loginPage(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
            

    context = {'form': form} 
    return render(request, 'Base/login.html', context)


def homePage(request):
    rooms = Room.objects.all()
    
    listings= UserListing.objects.all()
    
            
    context = {'rooms': rooms,'ListingForm':ListingForm,'listings':listings}
    return render(request,'Base/home.html',context)
@login_required
def listingCreation(request):
    form= ListingForm()
    if request.method=="POST":
        form= ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user     
            listing.save()
            return redirect('home')
    context = {'form':form,}
    return render(request,'Base/listingForm.html',context)
@login_required
def roomPage(request,pk):
    rooms = Room.objects.all()
    chat = UserMessages.objects.filter(room=pk)
    form = TextForm()
    room = Room.objects.get(id=pk)
    editForm = None
    editID = None

    if request.method == "POST":
        if "edit_message" in request.POST:
            editID = request.POST.get("message_id")
            message_instance = UserMessages.objects.get(id=editID)
            editForm = EditMessage(request.POST, instance=message_instance)
            if editForm.is_valid():
                editForm.save()
                editForm = None 
                editID = None
        elif "send_message" in request.POST:
            new_message_form = TextForm(request.POST)
            if new_message_form.is_valid():
                new_message = new_message_form.save(commit=False)
                new_message.room = room
                new_message.user = request.user
                new_message.save()

    context = {'rooms': rooms,'chat': chat,'form': form,'room': room,'editForm': editForm,'editID': editID,}
    return render(request, 'Base/room.html', context)

@login_required
def signout(request):
    logout(request)
    return redirect('home')
@login_required
def deleteMessage(request,pk):
    userText= UserMessages.objects.get(id=pk)
    if request.user== userText.user:
        room_id= userText.room.id
        userText.delete()
        return redirect('room',pk=room_id)
    

@login_required
def updateProfile(request):
    updateForm= UpdateProflieForm(instance=request.user)

    if request.method=='POST':
        updateForm=UpdateProflieForm(request.POST,instance=request.user)
        if updateForm.is_valid():
            updateForm.save()
    context={'updateForm':updateForm,}
    
    return render(request,'Base/userprofile.html',context)
    