"""
URL configuration for idfinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getstarted', views.get_started, name='get_started'),
    path('report', views.report, name='report'),
    path('retrieve', views.retrieve, name='retrieve'),

    # TESTING SUBMIT
    path('submit', views.submit_request, name='submit_request'),
    path('register', views.register, name='register'),
    # path('report_a_lost_id/<int:id>', views.report_a_lost_id, name='report_a_lost_id'),
    # path('return/<int:report_id>', views.return_id, name='return_id'),
    path('retrieval_form', views.retrieval_form, name='retrieval_form'),

    # path('reg_citizens/submit/<int:citizen_id>', views.reg_citizens, name='reg_citizens'),
    path('reg_citizens', views.reg_citizens, name='reg_citizens'),

    path('donations', views.donate, name='donate'),
    path('idno', views.contact, name='contact'),
    path('login', views.login_page, name='login'),
    path('signup', views.signup, name='signup'),  # Registration page
    path('logout', views.logout_page, name='logout'),
    path('lost/citizen/<int:id>', views.lost_book, name='lost_book'),

    path('admin/', admin.site.urls),
]
