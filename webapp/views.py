from django.shortcuts import render
from .form import NameForm

def add(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True })
    else: 
        form = NameForm()
    return render(request, 'add.html', { 'isShowingInput': True, 'form': form })

def random(request):
    return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True })
