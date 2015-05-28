from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "agenda.views.lista"),
    url(r'^adiciona/$', "agenda.views.adiciona"),
    url(r'^item/(?P<nr_item>\d+)/$', "agenda.views.item"),
    url(r'^remove/(?P<nr_item>\d+)/$', "agenda.views.remove"),
    url(r'^login/', "django.contrib.auth.views.login", {
		"template_name": "login.html"}),
	url(r'^logout/', "django.contrib.auth.views.logout_then_login" , {
		"login_url": "/login/"}),
    
    
    # Examples:
    # url(r'^$', 'gerente.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
