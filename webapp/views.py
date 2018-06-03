from django.shortcuts import render
from .form import NameForm

def add(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            restuarant = form.save(commit=False)
            restuarant.author = request.user
            restuarant.save()
            return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True })
    else: 
        form = NameForm()
    return render(request, 'add.html', { 'isShowingInput': True, 'form': form })

def random(request):
    return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True })

def listpage(request):
    return render(request, 'list.html', { 'isShowingInput': True })