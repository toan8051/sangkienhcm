from django.views.generic import TemplateView
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Donvivttp, Sangkien
from django.urls import reverse, reverse_lazy
from .forms import SangkienForm
#from django.core.cache import cache


class DonvivttpListView(ListView):
    model = Donvivttp
    context_object_name = 'donvivttp'   # your own name for the list as a template variable
    #queryset = Department.objects.filter(name__icontains='TTVT')[:20] # Get 5 books containing the title war
    template_name = "sangkien/donvivttp_list.html"

class SangkienListView(ListView):
    model = Sangkien
    template_name = "sangkien/sangkien_list.html"

    def get_object(self, queryset=None):
        return Sangkien.objects.get(id=self.kwargs["list_id"])

    def get_queryset(self):
        donvivttp_id = self.kwargs['list_id']
        return Sangkien.objects.filter(donvivttp_id=donvivttp_id)

    def get_context_data(self):
        context = super().get_context_data()
        context["donvivttp"] = Donvivttp.objects.get(id=self.kwargs["list_id"])
        return context    

class SangkienUpdate(UpdateView):
    model = Sangkien
    # template_name = 'sangkien/sangkien_form.html'
    form_class = SangkienForm

    def get_context_data(self):
        context = super(SangkienUpdate, self).get_context_data()
        context["donvivttp"] = self.object.donvivttp
        context["title"] = "Sửa thông tin sáng kiến"
        return context

    def get_success_url(self):
        #cache.clear()
        return reverse("sangkienlist", args=[self.object.donvivttp_id])        

class SangkienCreate(CreateView):
    model = Sangkien
    form_class = SangkienForm


    def get_initial(self):
        initial_data = super(SangkienCreate, self).get_initial()
        donvivttp = Donvivttp.objects.get(id=self.kwargs["list_id"])
        #print(donvivttp)
        initial_data["donvivttp"] = donvivttp
        #form.fields['created_by'].initial = request.user.username.title
        initial_data.update({'created_by': self.request.user.id,})

        return initial_data

    def get_context_data(self):
        context = super(SangkienCreate, self).get_context_data()
        donvivttp = Donvivttp.objects.get(id=self.kwargs["list_id"])

        #print(donvivttp)
        context["donvivttp"] = donvivttp
        
        context["title"] = "Đăng ký mới sáng kiến"
        return context

    def get_success_url(self):
        #cache.clear()
        return reverse("sangkienlist", args=[self.object.donvivttp_id])     


class SangkienDelete(DeleteView):
    model = Sangkien

    def get_success_url(self):
        #cache.clear()
        return reverse_lazy("sangkienlist", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["donvivttp"] = self.object.donvivttp
        return context