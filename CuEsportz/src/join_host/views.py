from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def join(request):
    return render(request, 'join.html', {})

@csrf_exempt
def host(request):
    return render(request, 'host.html', {})

@csrf_exempt
def wallet(request):
    return render(request, 'wallet.html', {})

@csrf_exempt
def hostsData(request):
    if request.method == 'POST':
        name = request.POST['tournament_name']
        maps = request.POST['map']
        team = request.POST['team']
        perspective = request.POST['perspective']
        number = request.POST['number']
        rank = request.POST['no_of_rank']
        amount = request.POST['amount']

        print(name)
        print(maps)
        print(team)
        print(perspective)
        print(number)
        print(rank)
        print(amount)

    return HttpResponse("failed")