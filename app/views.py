import random

from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import FormContact
# from .helpers.get_user_geo import get_address
from .models import Rating, InstallationTeam, Address


class IndexView(TemplateView, FormView):
    template_name = "app/index.html"
    form_class = FormContact
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = list(Rating.objects.all())
        context["reviews"] = random.sample(reviews, 5)
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

    def get(self, request, *args, **kwargs):
        team_id = self.kwargs.get("team_id")
        try:
            team = InstallationTeam.objects.get(id=team_id)
        except InstallationTeam.DoesNotExist:
            raise Http404("Installation Team not found")
        return render(request, self.template_name, {"team": team})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            team_id = self.kwargs.get("team_id")
            text = request.POST.get("review")
            star = request.POST.get("star")
            username = request.POST.get("username")

            # ip = request.META.get("REMOTE_ADDR")

            # data = get_address(ip)

            # address = Address.objects.create(
            #     country=data.get("country", 0),
            #     region=data.get("region", 0),
            #     city=data.get("city", 0),
            # )
            Rating.objects.create(
                team_id=team_id,
                review=text,
                star=star,
                username=username,
                # address=address,
            )
        return redirect(self.success_url)
