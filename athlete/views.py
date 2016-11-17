from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import Athlete, TrainingLevel

# Create your views here.


# Gives us a list view
class IndexView(generic.ListView):
    template_name = 'athlete/index.html'

    # Returns all athletes to object_list
    def get_queryset(self):
        return Athlete.objects.all()


# Detail view based on the Athlete model
class AthleteInfoView(generic.DetailView):
    model = Athlete
    template_name = 'athlete/athlete.html'


# Creates a form that we can view to add athletes
class AddAthlete(generic.CreateView):
    model = Athlete
    fields = ['first_name', 'last_name', 'date_of_birth', 'club', 'picture']


# Creates a form that we can edit an existing athlete
class UpdateAthlete(generic.UpdateView):
    model = Athlete
    fields = ['first_name', 'last_name', 'date_of_birth', 'club', 'picture']


# Deletes the specific athlete and returns to the index page
class DeleteAthlete(generic.DeleteView):
    model = Athlete
    success_url = reverse_lazy('athlete:index')


# Creates a form that we can view to add Trainings
class AddTraining(generic.CreateView):
    model = TrainingLevel
    fields = ['level_name', 'number_of_sublevels']
