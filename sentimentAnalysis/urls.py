from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
 #   url(r'^$', views.index, name='index'),
    
    
    url(r'^$', views.firstForm),
    url(r'^tweet/$', views.getTweetByTweetName),
    
    #url(r'^displayFlights?$', views.displayFlights),
  # 	url(r'^searchbycountry/$', views.searchByCountry),
   #	url(r'^country/(?P<country>[0-9]{4})/$', views.searchByCountry),
   

    url(r'^searchbytweet/$', views.searchByTweet),
    
    url(r'^admin/', admin.site.urls),
       
]