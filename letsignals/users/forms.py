from django import forms
from . models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'



# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from . models import Profile

# class ProfileUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Profile
#         fields = '__all__'
    
# class ProfileUserChangeForm(UserChangeForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'

