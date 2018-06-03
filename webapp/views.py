from django.shortcuts import render
from .form import NameForm
from .models import Restuarant
from random import randint

def add(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            restuarant = form.save(commit=False)
            restuarant.author = request.user
            restuarant.save()
            nameList = Restuarant.objects.all()
            return render(request, 'list.html', { 'isShowingInput': True, 'nameList': nameList })
    else: 
        form = NameForm()
    return render(request, 'add.html', { 'isShowingInput': True, 'form': form })

def mainpage(request):  
    return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True, 'result': 'วันนี้กินไหน' })

def random(request):
    nameQuerySet = Restuarant.objects.all()    
    randNum = randint(0, nameQuerySet.count()-1)
    nameList = list(nameQuerySet)
    result = nameList[randNum]
    return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': False, 'result': result })

def listpage(request):
    nameQuerySet = Restuarant.objects.all()
    return render(request, 'list.html', { 'isShowingInput': True, 'nameList': nameQuerySet })

def delete(request, pk):
    try:
        restuarant = Restuarant.objects.get(id=pk).delete()
    except Restuarant.DoesNotExist:
        print('not existed')
    nameQuerySet = Restuarant.objects.all()
    return render(request, 'list.html', { 'isShowingInput': True, 'nameList': nameQuerySet })