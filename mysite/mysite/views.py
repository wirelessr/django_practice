import datetime

from django.template.loader import get_template
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail, get_connection

from mysite.forms import ContactForm

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render({'current_date' : now})
    return HttpResponse(html)

def shortcut_time(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
#    try:
#        offset = int(offset)
#    except ValueError:
#        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be  %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={
            'subject': 'I love your site!'}
            )

    return render(request, 'contact_form.html', {'form': form})
