from django.conf.urls import url
from . import views

app_name = 'ivc'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^$', views.logout, name='logout'),
    url(r'^cabinet/$', views.cabinet, name='cabinet'),
    url(r'^newapp/$', views.newapp, name='newapp'),


    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'lab/(?P<pk>[0-9]+)/$', views.LabUpdate.as_view(), name='lab-update'),
    url(r'lab/(?P<pk>[0-9]+)/delete/$', views.LabDelete.as_view(), name='lab-delete'),

]