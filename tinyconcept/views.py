from framework.viewsupport import template_response_view
from models import Idea
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

def store_idea_content(request, idea=None):
	if not idea:
		idea = Idea.new_with_post(request)
	else:
		idea.update_with_post(request)
	idea.full_clean()
	idea.save()

@template_response_view()
def ideas_list(request):
	"""
	operations on the whole list of ideas.
	GET - returns a list of all objects
	POST - creates a new idea object
	"""
	if 'POST' == request.method:
		store_idea_content(request)
		return HttpResponseRedirect("/")
	
	ideas = Idea.objects.all()
	print ideas
	return locals()

@template_response_view()
def idea_detail(request, name):
	"""
	GET - return a detail view of a single idea
	PUT - store an updated version of a single idea
	DELETE - delete a single idea
	"""
	idea = get_object_or_404(Idea, name=name)
	if 'PUT' == request.method:
		store_idea_content(request, idea)
		return HttpResponseRedirect("/")
	elif 'DELETE' == request.method:
		idea.delete()
		return HttpResponseRedirect("/")
	return locals()
	
@template_response_view('tinyconcept.idea_form')
def idea_form_new(request):
	"""
	GET - returns an empty form for a new idea
	POST - calls POST ideas_list
	"""
	if 'POST' == request.method:
		return ideas_list(request)

@template_response_view('tinyconcept.idea_form')
def idea_form_update(request, name):
	"""
	GET  - return a form, filled with the data from an existing 
	       empty instance for editing.
	POST - validate input and redirect to PUT /{name} to 
	       update the instance if valid.
	"""
	if 'POST' == request.method:
		# seems like django loads the POST content lazily
		request.POST = request.POST
		request.method = 'PUT'
		return idea_detail(request, name)
	idea = get_object_or_404(Idea, name=name)
	return locals()

@template_response_view()
def idea_form_delete(request, name):
	"""
	GET  - return a confirmation form, asking the user if he really
	       wants to delete the entity
	POST - redirect to DELETE /animal/{name} to delete the instance
	"""
	if 'POST' == request.method:
		request.method = 'DELETE'
		return idea_detail(request, name)
	idea = get_object_or_404(Idea, name=name)
	return locals()
