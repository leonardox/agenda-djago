# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
	data = models.DateField()
	hora = models.TimeField()
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
	usuario = models.ForeignKey(User)
	participantes = models.ManyToManyField(User, related_name="item_participantes")
	
	def __unicode__(self):
		return u"%s - %s %s" % (self.titulo, self.data, self.hora)

def envia_email(**kwargs):
	try:
		item = kwargs['instance']
	except KeyError:
		return
	print item
	for participante in item.participantes.all():
		if not participante.email:
			continue
		dados = (item.titulo, item.data.strftime("%d/%m/%Y"),
			item.hora, item.descricao)
			
		participante.email_user(
			subject= "[Evento] %s dia %s as %s" % (dados[0], dados[1], dados[2]),
			message= "Evento: %s\nDia: %s\nHora: %s\n\n\n\n %s" % 
				(dados[0], dados[1], dados[2], dados[3])
			)
				
models.signals.post_save.connect(envia_email, sender=Item,
	dispatch_uid="agenda.models.Item")
