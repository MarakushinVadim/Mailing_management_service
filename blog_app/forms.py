from django.forms import ModelForm

from blog_app.models import Blog
from mailing_interface_app.forms import StyleFormMixin


class BlogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'avatar',]


