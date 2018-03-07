from django.shortcuts import render

# Create your views here.

from .models import Student, Kafedra, StudentInstance, Institut

def index(request):
    """
  
    """
   
    num_students=Student.objects.all().count()
    num_instances=StudentInstance.objects.all().count()
    
    num_instances_available=StudentInstance.objects.filter(status__exact='a').count()
    num_kafedras=Kafedra.objects.count()  

     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    return render(
        request,
        'index.html',
      context={'num_students':num_students,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_kafedras':num_kafedras,
            'num_visits':num_visits}, # num_visits appended
    )

from django.views import generic

class StudentListView(generic.ListView):
    model = Student
    paginate_by = 2
class StudentDetailView(generic.DetailView):
    model = Student