import random

from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import FormContact, FormPrice
# from .helpers.get_user_geo import get_address
from .models import Rating, InstallationTeam, Address


class IndexView(TemplateView, FormView):
    template_name = "app/index.html"
    form_class = FormContact
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = list(Rating.objects.all())
        context["reviews"] = random.sample(reviews, 5) if reviews else None
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST" and request.POST.get("form_type") == "form-1":
            form = FormContact(request.POST)

            if form.is_valid():
                # Form fields passed validation
                cd = form.cleaned_data
                name = f"{cd['name']}"
                email = f"{cd['email']}"
                phone = f"{cd['phone']}"
                subject = "Eine neue Anfrage"
                message = (
                    f"Eine neue Nachricht von {name}. Tel.: {phone} \nEmail: {email} "
                    f"\nNachricht: {cd['message']}"
                )
                send_mail(
                    subject,
                    message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.RECIPIENT_ADDRESS],
                )
                return HttpResponseRedirect(self.success_url)
        else:
            form = FormContact()

        if request.method == "POST" and request.POST.get("form_type") == "form-2":
            # Form was submitted
            form = FormPrice(request.POST)
            if form.is_valid():
                # Form fields passed validation
                cd = form.cleaned_data
                print("REQUEST: ", cd)
                name = f"{cd['name']}"
                phone = f"{cd['phone']}"
                email = f"{cd['email']}"
                subject = "Eine neue Preise Anfrage"
                message = (
                    f"Eine neue Nachricht von {name}. Telefonnummer: {phone} \nEmail: {email} "
                )
                send_mail(
                    subject,
                    message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.RECIPIENT_ADDRESS],
                )
                return HttpResponseRedirect(self.success_url)
            else:
                form = FormPrice()
        return render(request, self.template_name, {"form": form})

    # def form_valid(self, form):
    #     if self.request.POST.get("form_type") == "form_1":
    #         self.object = form.save(commit=False)
    #         self.object.save()
    #
    #     elif self.request.POST.get("form_type") == "form_2":
    #         self.object = form.save(commit=False)
    #         self.object.save()
    #     return super().form_valid(form)


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
