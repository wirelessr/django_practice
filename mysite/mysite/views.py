from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    import datetime
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
