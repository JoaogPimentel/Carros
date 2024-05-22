from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from  cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    def get_queryset(self):#para busca
        cars= super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars =cars.filter(model__icontains =search)
        return cars
class CarDetailView(DetailView):
    model= Car
    template_name ='car_detail.html'
@method_decorator(login_required(login_url='login'),name= 'dispatch')#para impedir que pessoas que não estejam logadas possam fazer alterações/ caso não esteja logado vai levar para a login page
class NewCreateCarView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='login'),name='dispatch')
class CarUpdateView(UpdateView):
    model=Car
    form_class=CarModelForm
    template_name = 'car_update.html'
    def get_success_url(self): #função para retornar para a pagina detail do carro que foi alterado
        return  reverse_lazy('car_detail',kwargs={'pk':self.object.pk})
@method_decorator(login_required(login_url='login'),name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url ='/cars/'
