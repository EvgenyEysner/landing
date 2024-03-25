from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import FormContact


class IndexView(TemplateView, FormView):
    template_name = "app/index.html"
    form_class = FormContact
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        if self.request.POST.get("form_type") == "form_1":
            self.object = form.save(commit=False)
            self.object.save()

        elif self.request.POST.get("form_type") == "form_2":
            self.object = form.save(commit=False)
            self.object.save()

        return super().form_valid(form)


class ReviewView(TemplateView, FormView):
    template_name = "app/review.html"
    form_class = FormContact
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        if self.request.POST.get("form_type") == "form_1":
            self.object = form.save(commit=False)
            self.object.save()

        elif self.request.POST.get("form_type") == "form_2":
            self.object = form.save(commit=False)
            self.object.save()

        return super().form_valid(form)

def ajax_add_review(request):
    ...