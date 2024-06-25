from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from blog_app.models import Blog
from mailing_interface_app.forms import (
    ClientServiceForm,
    MessageForm,
    SendingMailSetForm,
    SendTryForm,
    SendingMailSetModeratorForm,
)
from mailing_interface_app.models import ClientService, Message, SendingMailSet, SendTry
from mailing_interface_app.services import get_blogs_from_cache


class BaseView(TemplateView):
    template_name = "mailing_interface_app/home.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["sending_count"] = SendingMailSet.objects.all().count()
        context_data["active_sending_count"] = SendingMailSet.objects.filter(
            is_active=True,
        ).count()
        context_data["client_service_count"] = (
            ClientService.objects.all().distinct().count()
        )
        context_data["random_blogs"] = Blog.objects.order_by("?")[:3]
        return context_data

    def get_queryset(self):
        return get_blogs_from_cache


class ClientServiceListView(LoginRequiredMixin, ListView):
    model = ClientService

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        r_user = self.request.user
        if r_user.has_perm("mailing_interface_app.can_view_sending_mail_set"):
            return ClientService.objects.all()
        queryset = queryset.filter(owner=r_user)
        if queryset is not None:
            return queryset
        raise PermissionDenied


class ClientServiceDetailView(DetailView):
    model = ClientService


class ClientServiceCreateView(CreateView):
    model = ClientService
    form_class = ClientServiceForm
    success_url = reverse_lazy("mailing_interface_app:base")

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        form.instance.user = self.request.user

        return super().form_valid(form)


class ClientServiceUpdateView(UpdateView):
    model = ClientService
    form_class = ClientServiceForm
    success_url = reverse_lazy("mailing_interface_app:base")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return SendingMailSetForm
        raise PermissionDenied


class ClientServiceDeleteView(DeleteView):
    model = ClientService
    success_url = reverse_lazy("mailing_interface_app:base")


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    success_url = reverse_lazy("mailing_interface_app:base")
    form_class = MessageForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        form.instance.user = self.request.user

        return super().form_valid(form)


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing_interface_app:base")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return SendingMailSetForm
        raise PermissionDenied


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailing_interface_app:base")


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        r_user = self.request.user
        if r_user.has_perm("mailing_interface_app.can_view_sending_mail_set"):
            return ClientService.objects.all()
        queryset = queryset.filter(user=r_user)
        if queryset is not None:
            return queryset
        raise PermissionDenied


class SendingMailSetCreateView(LoginRequiredMixin, CreateView):
    model = SendingMailSet
    success_url = reverse_lazy("mailing_interface_app:base")
    form_class = SendingMailSetForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        form.instance.user = self.request.user

        return super().form_valid(form)


class SendingMailSetDetailView(LoginRequiredMixin, DetailView):
    model = SendingMailSet


class SendingMailSetUpdateView(LoginRequiredMixin, UpdateView):
    model = SendingMailSet
    form_class = SendingMailSetForm
    success_url = reverse_lazy("mailing_interface_app:base")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return SendingMailSetForm
        if user.has_perm("mailing_interface_app.can_edit_is_active"):
            return SendingMailSetModeratorForm
        raise PermissionDenied


class SendingMailSetDeleteView(LoginRequiredMixin, DeleteView):
    model = SendingMailSet
    success_url = reverse_lazy("mailing_interface_app:base")


class SendingMailSetListView(LoginRequiredMixin, ListView):
    model = SendingMailSet

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        r_user = self.request.user
        if r_user.has_perm("mailing_interface_app.can_view_sending_mail_set"):
            return ClientService.objects.all()
        queryset = queryset.filter(owner=r_user)
        if queryset is not None:
            return queryset
        raise PermissionDenied


class SendTryListView(ListView):
    model = SendTry


class SendTryDetailView(DetailView):
    model = SendTry


class SendTryCreateView(CreateView):
    model = SendTry
    success_url = reverse_lazy("mailing_interface_app:base")
    form_class = SendTryForm


class SendTryUpdateView(UpdateView):
    model = SendTry
    form_class = SendTryForm
    success_url = reverse_lazy("mailing_interface_app:base")


class SendTryDeleteView(DeleteView):
    model = SendTry
    success_url = reverse_lazy("mailing_interface_app:base")
