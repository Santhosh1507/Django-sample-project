from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item

def my_app(request):
    return HttpResponse("Hello, world. You're at the polls index.") 


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to a page that displays the list of items
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

# Create your views here.
