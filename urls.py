from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template, redirect_to
import basic.blog.urls
import basic.events.urls
import basic.people.urls
import basic.media.urls.photos

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# register basic app admins
from basic.blog.admin import *
from basic.events.admin import *
from basic.people.admin import *
import st_james.views

# if none of the URLs are found, this setting appends a slash and tries again.
APPEND_SLASH = True

# urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'st_james_site.views.home', name='home'),
    # url(r'^st_james_site/', include('st_james_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # enable basic apps
    url(r'^blog/', include(basic.blog.urls)),
    url(r'^events/$', st_james.views.event_list),
    url(r'^events/', include(basic.events.urls)),
    url(r'^people/', include(basic.people.urls)),
    url(r'^media/', include(basic.media.urls.photos)),
    # enable comments
    (r'^comments/', include('django.contrib.comments.urls')),
    # template urls
    url(r'^$', st_james.views.home),
    url(r'^contact/$', st_james.views.contact),
    url(r'^about/$', direct_to_template, {'template': 'about.html'}),
    # if nothing else, redirect home
    # (r'^', redirect_to, {'url':'home/'}), # TODO replace with a 404
)
