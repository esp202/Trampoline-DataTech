from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

# Structure of Club in the database.
class Club(models.Model):
    club_name = models.CharField(max_length=100)

    # Shows club name instead of model object
    def __str__(self):
        return self.club_name


# Structure of Athlete in the database
class Athlete(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    club = models.ForeignKey(Club)  # Possibly add on_delete=modles.CASCADE
    picture = models.FileField()

    # Takes us to the athleteinfo page for the specific athlete we just created
    def get_absoulute_url(self):
        return reverse('athlete:athleteinfo', kwargs={'pk': self.pk})

    # Shows Athlete first & last name instead of Athlete object
    def __str__(self):
        return self.first_name + ' ' + self.last_name


# Structure of Training Level in the database
class TrainingLevel(models.Model):
    level_name = models.CharField(max_length=10)
    number_of_sublevels = models.IntegerField()


class SubLevels(models.Model):
    training_level = models.ForeignKey(TrainingLevel)
    sub_level_name = models.CharField(max_length=20)
    number_of_skills = models.IntegerField()


class Skills(models.Model):
    sub_level = models.ForeignKey(SubLevels)
    skill_name = models.CharField(max_length=100)
    skill_complete = models.BooleanField(default=False)
