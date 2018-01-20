from django.contrib import admin
from .models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'auc_public', 'auc_private')

admin.site.register(Submission, SubmissionAdmin)
