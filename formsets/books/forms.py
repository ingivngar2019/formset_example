from django import forms
from django.forms import formset_factory, BaseFormSet
from .models import *
from django.forms.formsets import TOTAL_FORM_COUNT, INITIAL_FORM_COUNT,MIN_NUM_FORM_COUNT, MAX_NUM_FORM_COUNT, ORDERING_FIELD_NAME, DELETION_FIELD_NAME

class BookForm(forms.Form):

    fields = ('name','genre',)
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )

    # genre = forms.ModelChoiceField(
    #     queryset=Genre.objects.all(),
    #     required=True,
    #     label='Genre',
    #     widget=forms.Select(attrs={
    #         'placeholder': '',
    #         'class': 'form-control',
    #         'readonly': 'yes'
    #     })
    # )

    genero = forms.CharField(
        label='Genre',
        widget = forms.HiddenInput(attrs={
            'class': 'form-control',
        })
    )


BookFormset = formset_factory(BookForm, extra=1)

class BaseAddableFormSet( BaseFormSet):
    def add_form(self, **kwargs):
        # add the form
        tfc = self.total_form_count()
        self.forms.append(self._construct_form(tfc, **kwargs))
        self.forms[tfc].is_bound = False

        # make data mutable
        self.data = self.data.copy()

        # increase hidden form counts
        total_count_name = '%s-%s' % (self.management_form.prefix, TOTAL_FORM_COUNT)
        initial_count_name = '%s-%s' % (self.management_form.prefix, INITIAL_FORM_COUNT)
        self.data[total_count_name] = self.management_form.cleaned_data[TOTAL_FORM_COUNT] + 1
        self.data[initial_count_name] = self.management_form.cleaned_data[INITIAL_FORM_COUNT] + 1

    def add_fields(self, form, index):
        super(BaseAddableFormSet, self).add_fields(form, index)
        form.empty_permitted = False

AddableBookFormset = formset_factory(BookForm, formset=BaseAddableFormSet, extra=1)