from django.shortcuts import render

def add(request):
    print(request.path_info[1:])
    return render(request, 'add.html', { 'isShowingInput': True })

def random(request):
    return render(request, 'random.html', { 'isShowingInput': False, 'firstRandom': True })
