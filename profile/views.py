from django.shortcuts import redirect, render
from .forms import messageForm
from .models import message
from django.contrib import messages



def IndexView(request):

    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid():
            form.save()
            print("hello")
            messages.success(request, "Message sent successfully.")
            return redirect('index')

    return render(request, 'index.html' )



