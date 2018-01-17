"""giftideas URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

from app.views import CadeauxView, CadeauDetailsView, CadeauUpdate, \
        IndexView, LoginView, RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'login', LoginView.as_view(), name="login"),
    url(r'register', RegisterView.as_view(), name="register"),
    url(r'logout', auth_views.logout, {'next_page': '/'}, name='logout')
]
urlpatterns += i18n_patterns(
    url(r'^$', IndexView.as_view(), name="index"),
    url(_(r'gifts/update/(?P<pk>\d+)'),
        CadeauUpdate.as_view(), name='cadeau-update'),
    url(_(r'gifts/(?P<pk>\d+)'),
        CadeauDetailsView.as_view(), name='cadeau-detail'),
    url(_(r'gifts'), CadeauxView.as_view(), name="cadeaux-list"),
)
