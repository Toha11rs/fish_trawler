from django.shortcuts import get_object_or_404, redirect, render
from fish import models
from base.forms import NavigationForm,TrawlerForm
from django.db.models import Sum

def main(request):
    all_catch = models.navigation.objects.aggregate(total=Sum('catch'))['total']

    navigation = models.navigation.objects.all()
    trawler= models.trawler.objects.all()

    context = {
        "navigation": navigation,
        'trawler':trawler,
        'all_catch':all_catch,
    }

    return render(request,'base/main.html',context)


def create_navigations(request):
    form = NavigationForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        print("неправильная форма")
    
    context = {'form': form}
    return render(request, 'base/add_navigation.html', context)


def delete_navigations(request, id):
    navigation = models.navigation.objects.get(id=id)
    navigation.delete()
    return redirect('main')
  

def edit_navigations(request, pk):
    
    transaction = get_object_or_404(models.navigation, pk=pk)
    
    if request.method == 'POST':
        form = NavigationForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = NavigationForm(instance=transaction)
    
    return render(request, 'base/edit_navigation.html', {'form': form})


def add_trawler(request):
    form = TrawlerForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        print("неправильная форма")
    
    context = {'form': form}
    return render(request, 'base/add_trawler.html', context)