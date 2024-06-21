from django.forms import BooleanField, ModelForm

from mailing_interface_app.models import ClientService, Message, SendingMailSet, SendTry


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ClientServiceForm(StyleFormMixin, ModelForm):
    class Meta:
        model = ClientService
        exclude = ('owner',)


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        exclude = ('slug', 'user')


class SendingMailSetForm(StyleFormMixin, ModelForm):
    class Meta:
        model = SendingMailSet
        exclude = ('sending_status', 'next_sending_time', 'owner')


class SendingMailSetModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = SendingMailSet
        fields = ('is_active',)


class SendTryForm(StyleFormMixin, ModelForm):
    class Meta:
        model = SendTry
        exclude = ('status', 'last_sending_date', 'server_response',)
