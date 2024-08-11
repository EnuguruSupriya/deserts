from django.urls import path
from icecreams import views
urlpatterns=[
    path('info/<int:cost>/<int:no>',views.func,name="ice"),
]