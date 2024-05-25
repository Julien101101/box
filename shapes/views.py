from django.http import HttpResponse
from .models import Shape

# def index(request):
#     return HttpResponse("Shapes index. supsup.")


#def shapes(request):
# return render(path to shapes template...")

def index(request):
    latest_question_list = Shape.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged

def detail(request, shape_id):
    return HttpResponse("You're looking at question %s." % shape_id)
