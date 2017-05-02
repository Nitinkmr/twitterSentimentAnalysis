from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
 #   url(r'^$', views.index, name='index'),
    
    
    url(r'^$', views.firstForm),
    url(r'^tweet/$', views.getTweetByTweetName),
    url(r'^userName/$', views.getTweetByUserName),
    
    url(r'^searchbycountry/$', views.country_dropDown),
   	url(r'^country/(?P<country>[0-9]{4})/$', views.searchByCountry),
   	
   	url(r'^countryvisualisations/$', views.countryVisual),
    url(r'^searchbytweet/$', views.searchByTweet),
    
    url(r'^visualisations/$', views.visualisations),
    


    url(r'^searchbyuser/$', views.searchByUserName),
    url(r'^admin/', admin.site.urls),
       
]
