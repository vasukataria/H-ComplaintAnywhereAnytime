from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views

# urlpatterns = [path("",views.front, name='front'),
#                 path('signUp/', views.signUp, name='signUp'),
#                 path('login/',views.login, name='login'),
#                 path('logout/',views.logout,name='logout'),
#                 path('complaints/',views.list, name='complaints'),
#                 path('Electricity/',views.Electricity, name='Electricity'),
#                 path('Plumber/',views.Plumber, name='plumber'),
#                 path('Air_conditioner/',views.Air_conditioner, name='Air_conditioner'),
#                 path('Room_cleaning/',views.Room_cleaning, name='Room_cleaning'),
#                 path('Carpanter/', views.Carpanter, name='Carpanter'),
# ]

url_patterns = [
    re_path('^$', views.front, name='front'),
    re_path(r'^signUp/$', views.signUp, name='signUp'),
    re_path(r'^home/$', views.Home.as_view(), name='home'),
    re_path(r'^complaints/$', views.ComplaintListCreateView.as_view(), name='complaint-list'),
    re_path(r'^complaints/new/$', views.NewComplaint.as_view(), name='new-complaint'),
    re_path(r'^complaints/(?P<pk>\d+)/$', views.ComplaintsDetailView.as_view(), name='complaint-detail'),
    re_path(r'^complaints/(?P<pk>\d+)/resolve$', views.ResolveComplaint.as_view(), name='resolve-complaint'),
    re_path(r'^feedback/$', TemplateView.as_view(template_name='feedback.html'), name='feedback'),
    re_path(r'^aboutus/$', TemplateView.as_view(template_name='about-us.html'), name='about-us'),
]

"""
/complaints/new
POST /complaints/

/complaints/{id}/edit
PUT /complaints/{id}

GET /complaints/
GET /complaints/{id}

DELETE /complaints/{id}
"""
