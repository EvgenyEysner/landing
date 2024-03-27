from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import FormContact, FormReview
from .models import Rating, Contact
from .services.customer_email import send_email


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


class ContactView(TemplateView):
    template_name = "app/contact.html"
    success_url = reverse_lazy("home/")

    def post(self, request, *args, **kwargs):
        if request.POST:
            form = FormContact(request.POST)
            if form.is_valid():
                # Form fields passed validation
                cd = form.cleaned_data
                name = f"{cd['name']}"
                email = f"{cd['email']}"
                phone = f"{cd['phone']}"
                text = f"{cd['text']}"
                send_email(name, email, phone, text)
                Contact.objects.create(name=name, email=email, phone=phone, text=text)
                return redirect(reverse_lazy("/"))
            return form

    # def form_valid(self, form):
    #     if self.request.POST:
    #         self.object = form.save(commit=False)
    #         self.object.save()
    #         return HttpResponseRedirect(self.success_url)
    #
    #     return super().form_valid(form)


class ReviewView(TemplateView, FormView):
    template_name = "app/review.html"
    form_class = FormReview
    success_url = reverse_lazy("home")

    # def post(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         form = FormReview(request.POST)
    #         print(form)
    #         if form.is_valid():
    #             return HttpResponseRedirect(self.success_url)


# def rate_image(request):
#     if request.method == "POST":
#         el_id = request.POST.get("el_id")
#         val = request.POST.get("val")
#         print(val)
#         obj = Rating.objects.get(id=el_id)
#         obj.score = val
#         obj.save()
#         return JsonResponse({"success": "true", "score": val}, safe=False)
#     return JsonResponse({"success": "false"})
