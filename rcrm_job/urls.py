from django.contrib.auth.decorators import login_required
from django.urls import path

from rcrm_job.views import JobListView, JobDetailView, JobCreateView, JobEditView, JobDeleteView

app_name = 'Jobs'


urlpatterns = [
    path('', login_required(JobListView.as_view()), name='Job'),
    path('add/', login_required(JobCreateView.as_view()), name='Job_Create'),
    path('<int:pk>/', login_required(JobDetailView.as_view()), name='Job_Detail'),
    path('<int:pk>/edit/', login_required(JobEditView.as_view()), name='Job_Edit'),
    path('<int:pk>/delete/', login_required(JobDeleteView.as_view()), name='Job_Delete'),
]