from .models import Documento
from django.views.generic.edit import CreateView


class DocumentoCreate(CreateView):
    model = Documento
    fields = ["descricao", "arquivo"]

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs["funcionario_id"]

        return self.form_valid(form) if form.is_valid() else self.form_invalid(form)
