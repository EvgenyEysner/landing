import json

from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import FormContact, FormReview
from .models import Rating


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


class ReviewView(TemplateView):
    template_name = "app/review.html"

    def post(self, request, *args, **kwargs):
        response_data = {}
        if request.method == "POST":
            team = request.POST.get("team")
            text = request.POST.get("text")
            star = request.POST.get("star")


            rating = Rating.objects.create(team=team, review=text, star=1)
            print("PRINT", request.POST)
        #     response_data["result"] = "Create post successful!"
        #     response_data["id"] = rating.pk
        #     response_data["review"] = rating.review
        #     response_data["team"] = rating.team
        #     response_data["star"] = rating.star
        #
        #     return HttpResponse(
        #         json.dumps(response_data), content_type="application/json"
        #     )
        # else:
        #     return HttpResponse(
        #         json.dumps({"nothing to see": "this isn't happening"}),
        #         content_type="application/json",
        #     )
