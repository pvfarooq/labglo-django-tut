from django.shortcuts import render

from books.models import Book


# Create your views here.
def home(request):
    context = {
        # "books": Book.objects.all(),
        "books": Book.objects.prefetch_related("tags").all(),
    }
    return render(request, "home.html", context)


"""
account = Account.objects.select_related("user").all()
for i in account:
    print(i.user.username)

"""
