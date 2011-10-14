'''
Created on 28.08.2011

@author: josh
'''
from django.template.response import TemplateResponse
from django.forms.models import modelform_factory

def template_response_view(template_basename=None):  
    
    def view_decorator(view):
        pkg = view.func_globals["__package__"]
        generic_template = \
                pkg and "%s.%s" % (pkg, view.func_name) or view.func_name
        
        def view_wrapper(*args, **kwargs):
            template = template_basename or generic_template
            
            context = view(*args, **kwargs) or {}
            if not isinstance(context, dict):
                return context
            return TemplateResponse(kwargs.get('request') or args[0],
                                    "%s.html" % template,
                                    context )
        return view_wrapper
    return view_decorator

def modelform(model_class, request_data=None):
    return modelform_factory(model_class, fields=('name', 'title'))
