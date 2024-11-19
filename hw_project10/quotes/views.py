from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Quote, Author
from .forms import QuoteForm, AuthorForm


def main(request):
    quotes = Quote.objects.all()
    return render(request, 'main.html', {"quotes": quotes})


def author_details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    return render(request, 'author_details.html', {"author": author})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.author = Author.objects.get(pk=form.cleaned_data['author_id'])
            tags = form.cleaned_data['tags'].split(',')
            new_quote.tags = [x.strip(' ') for x in tags]
            new_quote.save()

            return redirect(to='quotes:main')
        else:
            return render(request, 'add_quote.html')

    authors = Author.objects.all()

    return render(request, 'add_quote.html', {"authors": authors, 'form': QuoteForm()})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.save()

            return redirect(to='quotes:main')
        else:
            return render(request, 'add_author.html')

    return render(request, 'add_author.html', {'form': AuthorForm()})
