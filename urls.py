from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tinyconcept.views.ideas_list'),
    url(r'^\.new$', 'tinyconcept.views.idea_form_new'),
    url(r'^(?P<name>\w+)$', 'tinyconcept.views.idea_detail'),
    url(r'^(?P<name>\w+)\.edit$', 'tinyconcept.views.idea_form_update'),
    url(r'^(?P<name>\w+)\.delete$', 'tinyconcept.views.idea_form_delete'),
)
