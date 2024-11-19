from django.forms import ModelForm, CharField, TextInput, IntegerField, Textarea
from .models import Quote, Author


class QuoteForm(ModelForm):
    quote = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    tags = CharField(min_length=3, max_length=150, required=True, widget=TextInput())
    author_id = IntegerField(required=True)

    class Meta:
        model = Quote
        fields = ['quote', 'author_id', 'tags']


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=150, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=12, required=True, widget=TextInput())
    born_location = CharField(min_length=3, max_length=150, required=True, widget=TextInput())
    description = CharField(min_length=3, max_length=500, required=True, widget=Textarea())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
