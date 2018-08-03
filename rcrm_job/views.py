from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView


from rcrm_account.utils import AccountControlViewMixin, AccountControlViewMixinTwo, \
    AccountControlViewMixinSix, AccountControlViewMixinFive,\
    UserAccountControlViewMixin
from rcrm_job.forms import JobForm
from rcrm_job.models import Job

from openpyxl import Workbook
from tablib import Dataset


# Create your views here.


# --------------------------------- Job ---------------------------------

class JobListView(UserAccountControlViewMixin, TemplateView):
    """
    Jobs are listed with this view.
    """
    template_name = 'job/pages/job_list.html'

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        queryset = Job.objects.filter(is_deleted=False, account=self.request.user.account)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) |
                                       Q(description__icontains=q) |
                                       Q(city__icontains=q) |
                                       Q(office__icontains=q)
                                       )
        context['jobs'] = queryset.distinct()
        context['all_jobs'] = Job.objects.filter(is_deleted=False, account=self.request.user.account)
        return context


class JobDetailView(AccountControlViewMixin, TemplateView):
    """
    Job detail information can be seen with this view.
    """
    template_name = 'job/pages/job_detail.html'

    def dispatch(self, request, pk, *args, **kwargs):
        try:
            self.job = Job.objects.get(is_deleted=False, id=pk)
        except Job.DoesNotExist:
            raise Http404()

        if self.job.account != request.user.account:
            raise Http404()

        return super(JobDetailView, self).dispatch(request, pk, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)

        context.update({
            'job': self.job
        })

        return context


class JobCreateView(UserAccountControlViewMixin, CreateView):
    """
    A job can be created using this view.
    """
    model = Job
    form_class = JobForm
    template_name = 'job/forms/job_create.html'
    success_url = reverse_lazy('Jobs:Job')

    def form_valid(self, form):
        job = form.save(commit=False)
        job.account = self.request.user.account
        job.save()
        messages.success(self.request, _('Created successfully, thank you.'))

        return super(JobCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Please correct the errors and try again.'))

        return super(JobCreateView, self).form_invalid(form)


class JobEditView(AccountControlViewMixinTwo, UpdateView):
    """
    An job can be edited using this view.
    """
    model = Job
    form_class = JobForm
    template_name = 'job/forms/job_edit.html'

    def dispatch(self, request, pk, *args, **kwargs):
        try:
            self.job = Job.objects.get(is_deleted=False, id=pk)
        except Job.DoesNotExist:
            raise Http404()

        if self.job.account != request.user.account:
            raise Http404()

        return super(JobEditView, self).dispatch(request, pk, *args, **kwargs)

    def get_success_url(self):
        id = self.kwargs['pk']
        job = get_object_or_404(Job, id=id)

        return reverse('Jobs:Job_Detail', args=[job.id])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Saved successfully, thank you.'))

        return super(JobEditView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Please correct the errors and try again.'))

        return super(JobEditView, self).form_invalid(form)


class JobDeleteView(AccountControlViewMixinTwo, UpdateView):
    """
    A job can be deleted using this view.
    """
    model = Job
    fields = []
    template_name = 'job/forms/job_delete.html'

    def get_success_url(self):
        return reverse_lazy('Jobs:Job')

    def form_valid(self, form):
        form_delete = form.save(commit=False)
        form_delete.is_active = False
        form_delete.is_deleted = True
        form_delete.save()
        messages.success(self.request, _('Deleted successfully, thank you.'))
        return super(JobDeleteView, self).form_valid(form=form)
