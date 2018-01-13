# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Max, Count
from config.settings.common import ROOT_DIR
import requests

from hackathon.users.models import User
from .models import Submission
from .aux_math import auc, precision, log_loss
from .forms import SubmissionForm


def read_file(input_file):
	real_public = []
	real_private = []
	i = 0
	for r in input_file:
		if i==0 or r=='':
			i+=1
			continue
		result = float(r)
		real_private.append(result)
		if i % 3 == 0:  # Private (33%)
			real_public.append(result)
		i+=1
	return real_private, real_public

### Import test set results to compute AUC
# import requests
# from aux_math import auc
## if you see this and you are a participant, 
## be conscient of the importance in the ethics for professional development
results_file = requests.get('https://s3.amazonaws.com/bcndatathonpollution/solution.csv').text.split('\n')
real_private, real_public = read_file(results_file)

# predicted_file = open('/Users/mingot/Projectes/BCNAnalytics/datathon_pollution/sample_random.csv','r')
# predicted_private, predicted_public = read_file(predicted_file)
# auc_public = auc(real_public, predicted_public)


@login_required
def submissions_list(request):
	current_user = request.user

	# Handle file upload
	if request.method == 'POST':
		form = SubmissionForm(request.POST, request.FILES)
		if form.is_valid():

			input_file = request.FILES['submissionfile']

			try:
				predicted_private, predicted_public = read_file(input_file)
			except Exception as e:
				print 'Error', e

			auc_public = log_loss(real_public, predicted_public)
			auc_private = log_loss(real_private, predicted_private)
			newdoc = Submission(submissionfile=request.FILES['submissionfile'], user=current_user, 
				auc_public=auc_public, auc_private=auc_private)
			newdoc.save()
			# except Exception as e:
			# 	print 'Error', e
				
			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('list'))
	else:
		form = SubmissionForm()  # A empty, unbound form

    # Load documents for the list page
	documents = Submission.objects.filter(user=current_user).order_by('-created_at')
	
    # Render list page with the documents and the form
	return render_to_response(
		'submissions/list.html',
		{'submissions': documents, 'form': form},
		context_instance=RequestContext(request)
	)


def leaderboard(request):

	teams = Submission.objects.exclude(auc_public__isnull=True).values('user').annotate(auc=Max('auc_public'), last_update=Max('created_at'), number=Count('submissionfile')).order_by('auc')
	for team in teams:
		team['user'] = User.objects.get(pk=team['user'])
		team['user'].name

	return render_to_response(
		'submissions/leaderboard.html',
		{'teams': teams},
		context_instance=RequestContext(request)
	)


def leaderboard_final(request):

	teams = Submission.objects.filter(auc_private__isnull=False).order_by('auc_private')

	return render_to_response(
		'submissions/leaderboard_final.html',
		{'teams': teams},
		context_instance=RequestContext(request)
	)
