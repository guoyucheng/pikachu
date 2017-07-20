from django.conf.urls import include, url
from django.contrib import admin
from plateform import views as plateform_views
from account import views as account_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'pikachu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^platform/get_platforms/', plateform_views.get_platforms),
    url(r'^platform/get_lives/', plateform_views.get_lives),
    url(r'^account/login/', account_views.login),
    url(r'^account/logout/', account_views.logout),
    url(r'^platform/get_live/', plateform_views.get_live),
]
