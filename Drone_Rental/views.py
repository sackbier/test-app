from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic

from .models import Drone, Customer, Case

from .forms import DroneForm

class IndexView(generic.ListView):
    template_name = 'Drone_Rental/index.html'
    model = Case
    context_object_name = 'case_list'

class CaseDetailView(generic.DetailView):
    template_name = 'Drone_Rental/case-detail.html'
    model = Case

class DroneDetailView(generic.DetailView):
    model = Drone
    template_name = 'Drone_Rental/drone-detail.html'

class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = 'Drone_Rental/customer-detail.html'

class DroneIndex(generic.ListView):
    template_name = 'Drone_Rental/drone-index.html'
    model = Drone
    context_object_name = 'drone_list'

def edit_drone(request, current_drone):
    d = Drone.objects.get(pk=current_drone)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        form = DroneForm(request.POST, instance=d)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('drone_detail', kwargs={'pk': d.pk}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DroneForm(instance=d)

    return render(request, 'Drone_Rental/drone-edit.html', {'form': form, 'drone':d})