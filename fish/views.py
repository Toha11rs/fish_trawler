from django.shortcuts import get_object_or_404, redirect, render
from fish import models
from base.forms import NavigationForm,TrawlerForm
from django.db.models import Sum
from django.db.models import Q


def main(request):
    all_catch = models.navigation.objects.aggregate(total=Sum('catch'))['total']

    navigation = models.navigation.objects.all()
    trawler= models.trawler.objects.all()

    search_query = request.GET.get('search')

    if search_query:
        navigation = navigation.filter(
            Q(capitan__name__icontains=search_query) |
            Q(capitan__surname__icontains=search_query) |
            Q(trawler__name__icontains=search_query) 
          
            # Q(navigation__date_navigation__icontains=search_query) 
        )


    context = {
        "navigation": navigation,
        'trawler':trawler,
        'all_catch':all_catch,
        'search_query':search_query,
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