from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from . forms import ProfileUserCreationForm, ProfileUserChangeForm
from . models import Profile

# class ProfileUserAdmin(UserAdmin):
#     add_form = ProfileUserCreationForm
#     form = ProfileUserChangeForm
#     model = Profile
#     list_display = ['first_name','last_name', 'bio', 'location', 'phone', 'birth_date',]

# admin.site.register(Profile, ProfileUserAdmin)
# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name','last_name')