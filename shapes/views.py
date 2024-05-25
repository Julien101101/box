from django.http import HttpResponse
from .models import Shape

# def index(request):
#     return HttpResponse("Shapes index. supsup.")


#def home(request):
# return render(path to home template...")

def index(request):
    latest_question_list = Shape.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged