from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing_interface_app.forms import ClientServiceForm
from mailing_interface_app.models import ClientService, Message, SendingMailSet, SendTry


class BaseView(TemplateView):
    template_name = 'mailing_interface_app/base.html'


class ClientServiceListView(ListView):
    model = ClientService


class ClientServiceDetailView(DetailView):
    model = ClientService


class ClientServiceCreateView(CreateView):
    model = ClientService
    form_class = ClientServiceForm
    success_url = reverse_lazy('mailing_interface_app:base')


class ClientServiceUpdateView(UpdateView):
    model = ClientService
    form_class = ClientServiceForm
    success_url = reverse_lazy('mailing_interface_app:base')


class ClientServiceDeleteView(DeleteView):
    model = ClientService
    success_url = reverse_lazy('mailing_interface_app:base')


class MessageCreateView(CreateView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message


class MessageListView(ListView):
    model = Message


class SendingMailSetCreateView(CreateView):
    model = SendingMailSet


class SendingMailSetDetailView(DetailView):
    model = SendingMailSet


class SendingMailSetUpdateView(UpdateView):
    model = SendingMailSet


class SendingMailSetDeleteView(DeleteView):
    model = SendingMailSet


class SendingMailSetListView(ListView):
    model = SendingMailSet


class SendTryListView(ListView):
    model = SendTry


class SendTryDetailView(DetailView):
    model = SendTry


class SendTryCreateView(CreateView):
    model = SendTry


class SendTryUpdateView(UpdateView):
    model = SendTry


class SendTryDeleteView(DeleteView):
    model = SendTry
