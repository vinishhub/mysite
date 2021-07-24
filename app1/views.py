from app1.forms import UserProfileForm
from django.shortcuts import redirect, render
from .models import UserProfile

# Create your views here.
def home(request):
    user_profiles=UserProfile.objects.all()
    form=UserProfileForm()
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('Error')
    context={
        'user_profiles':user_profiles,
        'form':form,

    }
    return render(request,'home.html',context)