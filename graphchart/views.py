from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import json

from graphchart.models import Reading


def index(request):
    latest_reading_list = Reading.objects.order_by('-reading_time')[:5]
    context = {'latest_reading_list' : latest_reading_list}
    return render(request, 'graphchart/index.html', context)

# class IndexView(generic.ListView):
#     template_name = 'graphchart/index.html'
#     context_object_name = 'latest_reading_list'
    
#     def get_queryset(self):
#         return Reading.objects.filter(reading_time__lte=timezone.now()).order_by('-reading_time')[:5]
