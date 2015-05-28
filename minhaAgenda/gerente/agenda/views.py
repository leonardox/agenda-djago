# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from models import Item
from django.template import RequestContext
from forms import FormItem
from django.contrib.auth.decorators import login_required

@login_required
def lista(request):
	lista_itens = Item.objects.filter(usuario=request.user)
	return render_to_response("lista.html", {'lista_itens': lista_itens })

@login_required
def adiciona(request):
	if request.method == "POST":
		form = FormItem(request.POST, request.FILES)
		if form.is_valid():
			item = form.save(commit=False)
			item.usuario = request.user
			item.save()
			form.save_m2m()
			return render_to_response("salvo.html", {})
	else:
		form = FormItem()
	return render_to_response("adiciona.html", {'form': form}, 
		context_instance= RequestContext(request))
		
@login_required
def item(request, nr_item):
	item = get_object_or_404(Item, pk = nr_item, usuario = request.user)
	if request.method == "POST":
		form = FormItem(request.POST, request.FILES, instance = item)
		if form.is_valid():
			item = form.save(commit=False)
			item.usuario = request.user
			item.save()
			form.save_m2m()
			return render_to_response("salvo.html", {})
	else:
		form = FormItem(instance=item)
	return render_to_response("item.html", {'form': form},
		context_instance = RequestContext(request))

@login_required		
def remove(request, nr_item):
	item = get_object_or_404(Item, pk=nr_item, usuario = request.user)
	if request.method == "POST":
		item.delete()
		return render_to_response("removido.html", {})
	return render_to_response("remove.html", {'item': item},
		context_instance = RequestContext(request))
