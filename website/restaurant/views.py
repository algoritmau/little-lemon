from django.shortcuts import render
from restaurant.forms import BookingForm

from .models import Category, Item


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return render(request, 'confirmation.html', {'form': form})

        else:
            print(form.errors)

    context = {'form': form}

    return render(request, 'book.html', context)


def menu(request):
    categories = Category.objects.all()
    items_by_category = {}

    for category in categories:
        items_by_category[category] = Item.objects.filter(category=category)

    context = {
        'items_by_category': items_by_category,
    }

    return render(request, 'menu.html', context)


def item(request, slug=None):
    if slug:
        item = Item.objects.get(slug=slug)
    else:
        item = None

    return render(request, 'item.html', {'item': item})
