from django.shortcuts import render, get_object_or_404
from .form import RestuarantForm
from .models import Restuarant
from random import randint

def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RestuarantForm(request.POST)
            if form.is_valid():
                restuarant = form.save(commit=False)
                restuarant.save()
                restuarants = Restuarant.objects.all()
                return render(request, 'list.html', { 'isShowingInput': True, 'restuarants': restuarants })
        else: 
            form = RestuarantForm()
        return render(request, 'add.html', { 'isShowingInput': True, 'form': form, 'isShowingEdit': False })
    else:
        return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True, 'result': 'วันนี้กินไหน' })

def mainpage(request):  
    return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True, 'result': 'วันนี้กินไหน' })

def random(request):
    restuarantQuerySet = Restuarant.objects.all()    
    randNum = randint(0, restuarantQuerySet.count()-1)
    restuarantList = list(restuarantQuerySet)
    result = restuarantList[randNum]
    return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': False, 'result': result })

def listpage(request):
    restuarants = Restuarant.objects.all()
    return render(request, 'list.html', { 'isShowingInput': True, 'restuarants': restuarants })

def delete(request, pk):
    if request.user.is_authenticated:
        try:
            restuarant = Restuarant.objects.get(id=pk).delete()
        except Restuarant.DoesNotExist:
            print('not existed')
        restuarants = Restuarant.objects.all()
        return render(request, 'list.html', { 'isShowingInput': True, 'restuarants': restuarants })
    else:
        return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True, 'result': 'วันนี้กินไหน' })

def edit(request, pk):
    if request.user.is_authenticated:
        restuarant = get_object_or_404(Restuarant, pk=pk)
        if request.method == "POST":
            restuarantForm = RestuarantForm(request.POST, instance=restuarant)
            restuarant = restuarantForm.save(commit=False)
            restuarant.save()
            restuarants = Restuarant.objects.all()
            return render(request, 'list.html', { 'isShowingInput': True, 'restuarants': restuarants })
        else:
            restuarantForm = RestuarantForm(instance=restuarant)
        return render(request, 'add.html', { 'isShowingInput': True, 'form': restuarantForm, 'isShowingEdit': True })
    else:
        return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True, 'result': 'วันนี้กินไหน' })