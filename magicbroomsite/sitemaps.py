from django.contrib import sitemaps

from magicbroomsite.models import QuotationRequests
# from magicbroom.urls import urlpatterns
from django.urls import reverse

# class TodoSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.5
#
#     def items(self):
#         return QuotationRequests.objects.all()
class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    # protocol = 'https'

    def items(self):
        return ['home', 'terms_of_service', 'request_quotation', 'privacy_policy']

    def location(self, item):
        return reverse(item)
