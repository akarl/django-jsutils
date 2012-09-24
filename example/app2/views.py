from django.http import HttpResponse


def home(request):
    return HttpResponse('app2.views.home')


def more(request, more_name):
    return HttpResponse('app2.views.more %s' % more_name)


def other(request, other_id):
    return HttpResponse('app2.views.other %s' % str(other_id))
