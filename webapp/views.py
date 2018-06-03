from django.shortcuts import render, get_object_or_404
from .form import NameForm
from .models import Restuarant
from random import randint

def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NameForm(request.POST)
            if form.is_valid():
                restuarant = form.save(commit=False)
                restuarant.save()
                nameList = Restuarant.objects.all()
                return render(request, 'list.html', { 'isShowingInput': True, 'nameList': nameList })
        else: 
            form = NameForm()
        return render(request, 'add.html', { 'isShowingInput': True, 'form': form, 'isShowingEdit': False })
    else:
        return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True, 'result': 'วันนี้กินไหน' })

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
    if request.user.is_authenticated:
        try:
            restuarant = Restuarant.objects.get(id=pk).delete()
        except Restuarant.DoesNotExist:
            print('not existed')
        nameQuerySet = Restuarant.objects.all()
        return render(request, 'list.html', { 'isShowingInput': True, 'nameList': nameQuerySet })
    else:
        return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True, 'result': 'วันนี้กินไหน' })

def edit(request, pk):
    if request.user.is_authenticated:
        restuarant = get_object_or_404(Restuarant, pk=pk)
        if request.method == "POST":
            restuarantForm = NameForm(request.POST, instance=restuarant)
            restuarant = restuarantForm.save(commit=False)
            restuarant.save()
            nameList = Restuarant.objects.all()
            return render(request, 'list.html', { 'isShowingInput': True, 'nameList': nameList })
        else:
            restuarantForm = NameForm(instance=restuarant)
        return render(request, 'add.html', { 'isShowingInput': True, 'form': restuarantForm, 'isShowingEdit': True })
    else:
        return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True, 'result': 'วันนี้กินไหน' })