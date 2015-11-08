# -*- coding: utf-8 -*-
from django import forms


class SubmissionForm(forms.Form):
    submissionfile = forms.FileField(
        	label='Select a file',
        	help_text='max. 42 megabytes'
    )