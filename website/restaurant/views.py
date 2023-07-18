from django.shortcuts import render
from restaurant.forms import BookingForm


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
