from django.http import HttpResponse

def index(request):
    return HttpResponse("Shapes index. supsup.")


#def home(request):
# return render(path to home template...")