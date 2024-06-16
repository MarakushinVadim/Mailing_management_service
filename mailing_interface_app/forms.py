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
        fields = '__all__'


class MessageForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Message
        exclude = ('slug', 'user',)


class SendingMailSetForm(StyleFormMixin, ModelForm):

    class Meta:
        model = SendingMailSet
        exclude = ('first_sending_date', 'sending_time', 'sending_status',)


class SendTryForm(StyleFormMixin, ModelForm):

    class Meta:
        model = SendTry
        exclude = ('sending_status', 'last_sending_date', 'server_response',)
