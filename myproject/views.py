from django.http import HttpResponse

def testView(request):
    return HttpResponse("Django Funcionando")