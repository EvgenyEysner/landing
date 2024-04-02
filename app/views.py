# import requests
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import FormContact
from .models import Rating


class IndexView(TemplateView, FormView):
    template_name = "app/index.html"
    form_class = FormContact
    success_url = reverse_lazy("home")

    # ToDo add to index.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Rating.objects.all()
        return context

    def form_valid(self, form):
        if self.request.POST.get("form_type") == "form_1":
            self.object = form.save(commit=False)
            self.object.save()

        elif self.request.POST.get("form_type") == "form_2":
            self.object = form.save(commit=False)
            self.object.save()
        return super().form_valid(form)


class ReviewView(TemplateView):
    template_name = "app/review.html"
    success_url = reverse_lazy("home")

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            team = request.POST.get("team")
            text = request.POST.get("review")
            star = request.POST.get("star")
            username = request.POST.get("username")
            print(username)
            ip = request.META.get("REMOTE_ADDR")

            # response = requests.get(url=f"http://ip-api.com/json/{ip}").json()

            # data = {
            #     "country": response.get("country"),
            #     "region": response.get("regionName"),
            #     "city": response.get("city"),
            # }

            # address = Address.objects.create(
            #     country=data.get("country", 0),
            #     region=data.get("region", 0),
            #     city=data.get("city", 0),
            # )
            Rating.objects.create(team=team, review=text, star=star, username=username)
        return redirect(self.success_url)
