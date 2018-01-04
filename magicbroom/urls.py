"""magicbroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from magicbroomsite.views import home_page, RequestQuotation, SuccessSubmission, TermsOfService,\
                                PrivacyPolicy


from magicbroomsite.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from magicbroomsite.views import *
# from django.contrib.sitemaps.views import sitemap
# from django.urls import path
#Add The namespace
app_name = 'magicbroomsite'

# Sitemap for dynamic, Model based data
# sitemaps = {
#     'todos': TodoSitemap()
# }
sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name="home"),
    # url(r'^requestquotation/$', request_quotation, name="request_quotation"),
    url(r'^requestquotation/$', RequestQuotation.as_view(), name="request_quotation"),
    url(r'^successquotesubmission/$', SuccessSubmission, name="success_submission"),
    url(r'^termsofservice/$', TermsOfService, name="terms_of_service"),
    url(r'^privacypolicy/$', PrivacyPolicy, name="privacy_policy"),
    # Static sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt', include('robots.urls')),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    #      name='django.contrib.sitemaps.views.sitemap'),

    # url(r'^robots.txt$', include('robots.urls')),
]
