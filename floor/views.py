from django.shortcuts import render, HttpResponse


def home(request):
    import datetime

    context = {
        "title": "Homeeeeeee",
    }

    context["date"] = datetime.date.today()
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
