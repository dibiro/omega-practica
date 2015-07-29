from django.conf.urls import patterns, include, url
from universidad.views import VistaPrincipal
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'Sistema.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', VistaPrincipal.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^unerg/', include('universidad.urls')),
)
