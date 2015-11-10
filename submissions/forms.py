# -*- coding: utf-8 -*-
from django import forms


NUM_LINES = 100


class SubmissionForm(forms.Form):
    submissionfile = forms.FileField(
        	label='Select a file',
        	help_text='max. 42 megabytes'
    )

    def clean(self):
		# try:
		# 	print self.cleaned_data['submissionfile']
		# 	ff = open(self.cleaned_data['submissionfile'])
		# except:
		# 	raise forms.ValidationError('File could not be opened')

		# num_lines = sum(1 for line in ff)
		# if num_lines!=NUM_LINES:
		# 	raise forms.ValidationError('File must have %s number of lines' % str(NUM_LINES))

		return self.cleaned_data