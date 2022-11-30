from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(reguest):
    if reguest.method != 'POST':
        form = UserCreationForm
    else: form = UserCreationForm(data=reguest.POST)

    if form.is_valid():
        new_user = form.save()
        login(reguest, new_user)
        return redirect('product:list')

    context = {'form': form}
    return render(reguest, 'users/register.html', context)