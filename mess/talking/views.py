from django.shortcuts import render
from .models import ActiveUser
from .forms import UserProfileForm


def my_profile(request):
    user_profile, created = ActiveUser.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'my_profile.html', {'form': form, 'avatar': user_profile.avatar.url})