from django.conf.urls import url
from . import views

app_name = 'athlete'

urlpatterns = [
    # /athlete/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /athlete/athletePK/
    url(r'^athlete/(?P<pk>[0-9]+)/$', views.AthleteInfoView.as_view(), name='athleteinfo'),

    url(r'^athlete/add_athlete/$', views.AddAthlete.as_view(), name='add_athlete'),

    url(r'^athlete/(?P<pk>[0-9]+)/$', views.UpdateAthlete.as_view(), name='update_athlete'),

    url(r'^athlete/(?P<pk>[0-9]+)/delete_athlete/$', views.DeleteAthlete.as_view(), name='delete_athlete'),

    url(r'^add_training/$', views.AddTraining.as_view(), name='add_training'),


]