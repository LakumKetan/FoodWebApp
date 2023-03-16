from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
# Create your views here.

def index(request):
    items = Item.objects.all()
    return HttpResponse(items)

def items(request):
    template = loader.get_template('food/index.html')
    items = Item.objects.all()
    context = {
        'item_list':items,
    }
    return HttpResponse(template.render(context, request))

#return render(request,'food/index.html', context)

def details(request, i_id):
    desc = Item.objects.get(pk=i_id)
    # template = loader.get_template('food/desc.html')
    context = {
        'desc':desc,
    }
    return render(request, 'food/desc.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:items')
    return render(request, 'food/item-delete.html',{'item':item})

