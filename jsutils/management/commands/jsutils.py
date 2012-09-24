from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):

        url_conf = __import__(settings.ROOT_URLCONF)

        show_urls(url_conf.urls.urlpatterns)


def show_urls(urllist, namespace=None):

    for entry in urllist:
        if hasattr(entry, 'name'):
            name = entry.name
            print('%s:%s' % (namespace, name))

        if hasattr(entry, 'url_patterns'):
            if hasattr(entry, 'namespace'):
                namespace = entry.namespace

            show_urls(entry.url_patterns, namespace)

