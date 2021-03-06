from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import reverse

from jobapps import views

urlpatterns = [
    path('get_statuses', views.get_statuses, name='get_statuses'),
    path('get_jobapps', views.get_jobapps, name='get_jobapps'),
    path('update_jobapp', views.update_jobapp, name='update_jobapp'),
    path('add_jobapp', views.add_jobapp, name='add_jobapp'),
    path('delete_jobapp', views.delete_jobapp, name='delete_jobapp'),
    path('get_jobapp_detail', views.get_jobapp_detail, name='get_jobapp_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
