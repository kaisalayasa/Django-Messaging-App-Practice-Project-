from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,UserListing,UserMessages


class RegistrationForm(UserCreationForm):
    class Meta:
        model= CustomUser
        fields=['username','email','password1','password2','status','bio','profile_pic']
        widgets={
            'status': forms.Select(attrs={'class':'form-control'})
            }

class TextForm(forms.ModelForm):
    class Meta:
        model = UserMessages
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Enter your message here...',
                'class': 'form-control',
            })
        }

class ListingForm(forms.ModelForm):
    class Meta:
        model = UserListing
        fields = ['text', 'ride_type']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'write your listing details',
                'class': 'form-control',
            }),
            'ride_type': forms.Select(attrs={'class': 'form-control'}),
        }

class EditMessage(forms.ModelForm):
    class Meta:
        model= UserMessages
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control'
            })}
        
class UpdateProflieForm(forms.ModelForm):
    class Meta:
            model = CustomUser
            fields= ['profile_pic','username','bio','status']
            widgets={
            'status': forms.Select(attrs={'class':'form-control'})
            }
        