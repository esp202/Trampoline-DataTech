from django import forms
from .models import Athlete, TrainingLevel, SubLevels, Skills


# Creates forms based on model of Athlete
class AthleteForm(forms.ModelForm):

    class Meta:
        model = Athlete
        fields = ['first_name', 'last_name', 'date_of_birth', 'club', 'picture']


# Creates forms based on model of TrainingLevel
class TrainingForm(forms.ModelForm):

    class Meta:
        model = TrainingLevel
        fields = ['level_name', 'number_of_sublevels', ]


# Creates forms based on model of Sublevels
class SubLevelForm(forms.ModelForm):

    class Meta:
        model = SubLevels
        fields = ['sub_level_name', 'number_of_skills', ]


# Creates forms based on model of Skills
class SkillForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = ['skill_name', ]
