from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # (r'^LFY/', include('LFY.foo.urls')),

    (r'^admin/', include(admin.site.urls)),
)
