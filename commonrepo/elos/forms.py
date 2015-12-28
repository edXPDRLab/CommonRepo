# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.forms import ModelForm, ModelChoiceField
from django.shortcuts import get_object_or_404
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

from commonrepo.users.models import User as User

from .models import ELO

class ELOForm(ModelForm):
    class Meta:
        model = ELO
        fields = ['name', 'author', 'original_type']

    def __init__(self, *args, **kwargs):
        super(ELOForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))

class ELOForkForm(ModelForm):
    class Meta:
        model = ELO
        fields = ['name', 'author', 'original_type', 'init_file', 'version', 'parent_elo', 'parent_elo_uuid', 'parent_elo_version']

    def __init__(self, pk=None, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(ELOForkForm, self).__init__(*args, **kwargs)
        elo_original = get_object_or_404(ELO, id=pk)
        self.fields["name"].initial = elo_original.name + " (Fork from author " + elo_original.author.username + ")"
        self.fields["name"].widget.attrs['readonly'] = True
        self.fields["author"].queryset = User.objects.filter(username=self.request_user)
        self.fields["author"].empty_label = None
        self.fields["author"].widget.attrs['readonly'] = True
        self.fields["original_type"].initial = elo_original.original_type
        self.fields["original_type"].widget.attrs['readonly'] = True
        self.fields["init_file"].initial = elo_original.init_file
        self.fields["init_file"].widget.attrs['readonly'] = True        
        self.fields["version"].initial = 1
        self.fields["version"].widget.attrs['readonly'] = True
        self.fields["parent_elo"].queryset = ELO.objects.filter(id=pk)
        self.fields["parent_elo"].empty_label = None
        self.fields["parent_elo"].widget.attrs['readonly'] = True
        self.fields["parent_elo_uuid"].initial = elo_original.uuid
        self.fields["parent_elo_uuid"].widget.attrs['readonly'] = True
        self.fields["parent_elo_version"].initial = elo_original.version
        self.fields["parent_elo_version"].widget.attrs['readonly'] = True
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))

class ELOUpdateForm(ModelForm):
    class Meta:
        model = ELO
        fields = ['name', 'original_type', 'is_public', 'metadata']

    def __init__(self, pk=None, *args, **kwargs):
        super(ELOUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url 'elos:elos-mylist' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
        ))
