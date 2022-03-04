from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from .models import Item

# Create your views here.
def index(request):
	items = Item.objects.order_by('checked', 'id')
	context = {'items': items}
	return render(request, 'shoppinglist/base.html', context)

def add_item(request):
	if request.method == 'POST':
		if request.POST.get('item'):
			item = Item()
			item.item = request.POST.get('item')
			item.item_info = request.POST.get('item_info')
			item.checked = False
			item.save()
			messages.add_message(request, messages.SUCCESS, item.item+' hinzugefügt.')
			return redirect('shoppinglist:index')
		else:
			messages.add_message(request, messages.ERROR, 'Fehler.')
			return redirect('shoppinglist:index')

def delete_item(request, pk):
	items = Item.objects.get(id=pk)
	items.delete()
	messages.add_message(request, messages.ERROR, 'Gelöscht.')
	return redirect('shoppinglist:index')

def check_item(request, pk):
	items = Item.objects.get(id=pk)
	items.delete()
	return redirect('shoppinglist:index')

def delete_all(request):
	items = Item.objects.all()
	items.delete()
	messages.add_message(request, messages.SUCCESS, 'Liste geleert.')
	return redirect('shoppinglist:index')

def view_item(request, pk):
	item = Item.objects.get(id=pk)
	context = {'item': item} 
	return render(request, 'shoppinglist/item_details.html', context)

def update_item(request, pk):
	if request.method == 'POST':
		item = Item.objects.get(id=pk)
		item.item = request.POST.get('item')
		item.item_info = request.POST.get('item_info')
		item.checked = True if request.POST.get('checked') == 'on' else False  
		item.save()
	return redirect('shoppinglist:index')
