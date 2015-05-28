from django.contrib import admin
from agenda.models import Item

class ItemAdmin(admin.ModelAdmin):
	fields = ("titulo", "data", "hora", "descricao", "participantes")
	list_display = ("titulo", "data", "hora")
	
	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()
	
	def queryset(self, request):
		qs = super(ItemAdmin, self).queryset(request)
		return qs.filter(usuario = request.user)
	
admin.site.register(Item, ItemAdmin)

# Register your models here.
