from django.db import models
from datetime import datetime
import re

class Idea(models.Model):
	name = models.CharField(max_length=64, unique=True)
	title = models.CharField(max_length=64)
	text = models.TextField(max_length=2048, blank=True)
	last_modified = models.DateTimeField()
	
	@classmethod
	def new_with_data(cls, title, text):
		if not title:
			title = re.sub("\s+", " ", text)
			if len(title) > 64:
				title = "%s ..." % title[:60]
		
		name = re.sub("\s+", "_", re.sub("[^\w\s]", "", title.lower()))
		i = 0
		while Idea.objects.filter(name=name):
			i = i + 1
			name = "%s__%s" % (name[:-5], i)
		newidea = Idea()
		newidea.name = name
		newidea.title = title
		newidea.text = text
		newidea.update_last_modified()
		return newidea
	
	@classmethod
	def new_with_post(cls, request):
		return Idea.new_with_data(request.POST['title'], 
								  request.POST['text'])
		
	def update_last_modified(self):
		self.last_modified = datetime.now()
		
	def validate():
		pass
		
	def update_with_post(self, request):
		self.name = request.POST['name']
		self.title = request.POST['title']
		self.text = request.POST['text']
		self.update_last_modified()
		self.full_clean()
