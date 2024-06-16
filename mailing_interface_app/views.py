from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing_interface_app.forms import ClientServiceForm, MessageForm, SendingMailSetForm, SendTryForm
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
    success_url = reverse_lazy('mailing_interface_app:base')
    form_class = MessageForm


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing_interface_app:base')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing_interface_app:base')


class MessageListView(ListView):
    model = Message


class SendingMailSetCreateView(CreateView):
    model = SendingMailSet
    success_url = reverse_lazy('mailing_interface_app:base')
    form_class = SendingMailSetForm


class SendingMailSetDetailView(DetailView):
    model = SendingMailSet


class SendingMailSetUpdateView(UpdateView):
    model = SendingMailSet
    form_class = SendingMailSetForm
    success_url = reverse_lazy('mailing_interface_app:base')


class SendingMailSetDeleteView(DeleteView):
    model = SendingMailSet
    success_url = reverse_lazy('mailing_interface_app:base')


class SendingMailSetListView(ListView):
    model = SendingMailSet


class SendTryListView(ListView):
    model = SendTry


class SendTryDetailView(DetailView):
    model = SendTry


class SendTryCreateView(CreateView):
    model = SendTry
    success_url = reverse_lazy('mailing_interface_app:base')
    form_class = SendTryForm


class SendTryUpdateView(UpdateView):
    model = SendTry
    form_class = SendTryForm
    success_url = reverse_lazy('mailing_interface_app:base')


class SendTryDeleteView(DeleteView):
    model = SendTry
    success_url = reverse_lazy('mailing_interface_app:base')
