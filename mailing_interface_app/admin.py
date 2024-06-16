from django.contrib import admin

from mailing_interface_app.models import ClientService, SendingMailSet, Message, SendTry


@admin.register(ClientService)
class ClientServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment')
    search_fields = ('id', 'email')


@admin.register(SendingMailSet)
class SendingMailSetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'client_service', 'message', 'sending_time', 'sending_status', 'sending_period',
        'first_sending_date'
    )
    search_fields = ('id', 'name')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'letter_subject', 'slug', 'letter_body', 'user')
    search_fields = ('id', 'slug')


@admin.register(SendTry)
class SendTryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sending_mail', 'sending_status', 'last_sending_date', 'server_response', 'client_service')
    search_fields = ('id', 'sending_mail')
