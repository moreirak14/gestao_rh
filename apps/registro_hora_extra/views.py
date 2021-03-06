import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View

from .models import RegistroHoraExtra
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .forms import RegistroHoraExtraForm


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    # success_url = reverse_lazy('list_hora_extra')

    def get_success_url(self):
        return reverse_lazy("update_hora_extra_base", args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy("list_hora_extra")


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):

        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs["pk"])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario

        response = json.dumps(
            {
                "mensagem": "Requisição executada",
                "horas": float(funcionario.total_horas_extra),
            }
        )

        return HttpResponse(response, content_type="application/json")
