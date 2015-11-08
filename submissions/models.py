from django.db import models
from hackathon.users.models import User


class Submission(models.Model):

	submissionfile = models.FileField(upload_to='documents/')
	auc = models.FloatField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)  # 'hackathon.users.models.User'

	def __unicode__(self):
		return u'%s submission' % self.user.first_name

