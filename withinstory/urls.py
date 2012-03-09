from tastypie.api import Api
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
from withinstory.api.resources import StoryResource, UserProfileResource
from withinstory.app import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

api_v1 = Api(api_name='v1')
api_v1.register(StoryResource())
api_v1.register(UserProfileResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'withinstory.views.home', name='home'),
    # url(r'^withinstory/', include('withinstory.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', views.register),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^$', direct_to_template, {'template': 'index.html'}),
    url(r'^getapikey/$', views.get_api_key),
    
    # API entry point. Should be in the end.
    url(r'^api/', include(api_v1.urls)),
)
