from django.urls import path, re_path

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
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),

    # GET /complaints/ - Get all complaints
    # POST /complaints/ - Create new complaint
    re_path(r'^complaints/$', views.ComplaintListCreateView.as_view(), name='complaint-list'),

    # Form to create new complaint
    re_path(r'^complaints/new/$', views.NewComplaint.as_view(), name='new-complaint'),

    # GET /complaints/{id} - Get single complaint
    # PUT /complaints/{id} - Update single complaint
    # DELETE /complaints/{id} - Delete single complaint
    re_path(r'^complaints/(?P<pk>\d+)/$', views.ComplaintsDetailView.as_view(), name='complaint-detail')
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
