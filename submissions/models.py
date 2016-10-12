import os
from django.db import models
from config.settings.common import ROOT_DIR
from hackathon.users.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import datetime
import random
import requests



def tied_rank(x):
    """
    This function computes the tied rank of elements in x.
    Parameters
    ----------
    x : list of numbers, numpy array
    Returns
    -------
    score : list of numbers
            The tied rank f each element in x
    """
    sorted_x = sorted(zip(x,range(len(x))))
    r = [0 for k in x]
    cur_val = sorted_x[0][0]
    last_rank = 0
    for i in range(len(sorted_x)):
        if cur_val != sorted_x[i][0]:
            cur_val = sorted_x[i][0]
            for j in range(last_rank, i): 
                r[sorted_x[j][1]] = float(last_rank+1+i)/2.0
            last_rank = i
        if i==len(sorted_x)-1:
            for j in range(last_rank, i+1): 
                r[sorted_x[j][1]] = float(last_rank+i+2)/2.0
    return r


def auc(actual, posterior):
    """
    This function computes the AUC error metric for binary classification.
    Parameters
    ----------
    actual : list of binary numbers, numpy array
             The ground truth value
    posterior : same type as actual
                Defines a ranking on the binary numbers, from most likely to
                be positive to least likely to be positive.
    Returns
    -------
    score : double
            The mean squared error between actual and posterior
    """
    r = tied_rank(posterior)
    num_positive = len([0 for x in actual if x==1])
    num_negative = len(actual)-num_positive
    sum_positive = sum([r[i] for i in range(len(r)) if actual[i]==1])
    auc = ((sum_positive - num_positive*(num_positive+1)/2.0) /
           (num_negative*num_positive))
    return auc


def precision(real, predict):
    return sum([real[i] == predict[i] for i in range(len(real))]) * 100.0 / len(real)


def update_filename(instance, filename):
    name = instance.user.team.replace(' ','_') + '_' + instance.user.username + '_' + datetime.now().strftime('%y%m%d%H%M%S') + '_' + str(int(random.random()*1000))
    return name


class Submission(models.Model):

    submissionfile = models.FileField(upload_to=update_filename)  # 'documents/'
    auc_public = models.FloatField(null=True, blank=True)
    auc_private = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    file_error = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'%s %s %s submission: %s' % (self.created_at, str(self.auc_public), self.user.username, self.submissionfile.url)

    def compute_score(self):
        predicted_private = []
        predicted_public = []
        if self.submissionfile.url[0:4]=='http':
            # AWS S3 submission casa
            results_file = requests.get(self.submissionfile.url).text.split('\n')
            results_file.remove('')  # remove white spaces

            # quality checks
            if len(results_file) != 30000:
                self.file_error = 'Length not correct'
                self.save()
                return

            # # Check for 
            # try:
            #     x = float(results_file[0])
            # except:
            #     self.file_error = 'All values have to be floats'
            #     self.save()
            #     return

        else:
            results_file = open(str(ROOT_DIR) + '/hackathon' + self.submissionfile.url)

        i = 0
        for r in results_file:
            if r=='':
                continue
            if i%20==0:
                predicted_public.append(float(r))
            else:
                predicted_private.append(float(r))
            i+=1

        self.auc_public = auc(real_public, predicted_public)
        # self.auc_private = auc(real_private, predicted_private)
        self.save()

 
# @receiver(post_save, sender=Submission)
# def submission_done(sender, **kwargs):
# 	"""
# 		After save compute score in a new thread
# 	"""
# 	submission = kwargs['instance']
# 	if submission.auc_public is None:
# 		print 'creating thread to compute auc...'
#         submission.compute_score()
		# score_computation_thread = threading.Thread(target=submission.compute_score,args=[])
		# score_computation_thread.start()




