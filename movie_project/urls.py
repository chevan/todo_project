from django.conf.urls import include, url
from django.contrib import admin
from TodoLib import urls


urlpatterns = [


    url(r'^admin/', include(admin.site.urls)),
     url(r'^todolib/', include('TodoLib.urls', namespace='todo')),
    	 


]
