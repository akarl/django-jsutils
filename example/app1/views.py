from django.http import HttpResponse


def home(request):
    return HttpResponse('app1.views.home')


def more(request, more_name):
    return HttpResponse('app1.views.more %s' % more_name)


def other(request, other_id):
    return HttpResponse('app1.views.other %s' % str(other_id))
