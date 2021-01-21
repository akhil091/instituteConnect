from . import views
from django import forms
from .models import subcategory_choices,  project


class FilterForm(forms.Form):
    selectedcategpryt = forms.ModelChoiceField(queryset=project.objects.all().order_by('subcategory'), required=False, label='', empty_label="Show All")