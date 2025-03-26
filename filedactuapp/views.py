from django.shortcuts import render

from .models import Messages


# Create your views here.
def index(request):
    if request.method == "POST":
        message = request.POST.get("contents")
        user = request.user
        Messages.objects.create(contents=message, users=user)
    context = {"messages": Messages.objects.order_by("-created_at")}
    return render(request, "index.html", context=context)


def details(request, id):
    if request.method == "POST":
        message = request.POST.get("contents")
        user = request.user
        Messages.objects.create(
            contents=message, users=user, reponse_to=Messages.objects.get(id=id)
        )
    context = {}
    context = {
        "responses_comments": Messages.objects.filter(reponse_to_id=id),
        "message_user": Messages.objects.get(id=id),
    }
    return render(request, "details.html", context=context)
