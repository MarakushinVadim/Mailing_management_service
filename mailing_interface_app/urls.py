from django.urls import path
from django.views.decorators.cache import cache_page

from mailing_interface_app.views import ClientServiceListView, ClientServiceDeleteView, ClientServiceUpdateView, \
    ClientServiceDetailView, ClientServiceCreateView, MessageCreateView, MessageDetailView, MessageUpdateView, \
    MessageDeleteView, MessageListView, SendingMailSetListView, SendingMailSetDetailView, SendingMailSetCreateView, \
    SendingMailSetUpdateView, SendingMailSetDeleteView, SendTryListView, SendTryDetailView, SendTryCreateView, \
    SendTryUpdateView, SendTryDeleteView, BaseView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('mailing_interface_app/client_service_list/', ClientServiceListView.as_view(), name='client_service_list'),
    path('mailing_interface_app/client_service_detail/<int:pk>/', ClientServiceDetailView.as_view(),
         name='client_service_detail'),
    path('mailing_interface_app/client_service_create/', ClientServiceCreateView.as_view(),
         name='client_service_create'),
    path('mailing_interface_app/client_service_update/<int:pk>/', ClientServiceUpdateView.as_view(),
         name='client_service_update'),
    path('mailing_interface_app/client_service_delete/<int:pk>/', ClientServiceDeleteView.as_view(),
         name='client_service_delete'),

    path('mailing_interface_app/message_create/', MessageCreateView.as_view(), name='message_create'),
    path('mailing_interface_app/message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('mailing_interface_app/message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('mailing_interface_app/message_delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('mailing_interface_app/message_list/', MessageListView.as_view(), name='message_list'),

    path('mailing_interface_app/sending_mail_set_list/', SendingMailSetListView.as_view(),
         name='sending_mail_set_list'),
    path('mailing_interface_app/sending_mail_set_detail/<int:pk>/', SendingMailSetDetailView.as_view(),
         name='sending_mail_set_detail'),
    path('mailing_interface_app/sending_mail_set_create/', SendingMailSetCreateView.as_view(),
         name='sending_mail_set_create'),
    path('mailing_interface_app/sending_mail_set_update/<int:pk>/', SendingMailSetUpdateView.as_view(),
         name='sending_mail_set_update'),
    path('mailing_interface_app/sending_mail_set_delete/<int:pk>/', SendingMailSetDeleteView.as_view(),
         name='sending_mail_set_delete'),

    path('mailing_interface_app/send_try_list/', SendTryListView.as_view(), name='send_try_list'),
    path('mailing_interface_app/send_try_detail/<int:pk>/', SendTryDetailView.as_view(), name='send_try_detail'),
    path('mailing_interface_app/send_try_create/', SendTryCreateView.as_view(), name='send_try_create'),
    path('mailing_interface_app/send_try_update/<int:pk>/', SendTryUpdateView.as_view(), name='send_try_update'),
    path('mailing_interface_app/send_try_delete/<int:pk>/', SendTryDeleteView.as_view(), name='send_try_delete'),
]
