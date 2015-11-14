# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Max, Count
import random

from hackathon.users.models import User
from .models import Submission
from .forms import SubmissionForm


@login_required
def submissions_list(request):
	current_user = request.user

    # Handle file upload
	if request.method == 'POST':
		form = SubmissionForm(request.POST, request.FILES)
		if form.is_valid():
			fi = request.FILES['submissionfile']
			newdoc = Submission(submissionfile=request.FILES['submissionfile'], user=current_user)
			newdoc.save()

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

	teams = Submission.objects.exclude(auc_public__isnull=True).values('user').annotate(auc=Max('auc_public'), last_update=Max('created_at'), number=Count('submissionfile')).order_by('-auc')
	for team in teams:
		team['user'] = User.objects.get(pk=team['user'])
		team['user'].name

	return render_to_response(
		'submissions/leaderboard.html',
		{'teams': teams},
		context_instance=RequestContext(request)
	)
