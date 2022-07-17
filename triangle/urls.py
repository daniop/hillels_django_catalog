from django.urls import path

from triangle.views import PersonIndexView, get_form, person_create_form, person_update_form

app_name = 'triangle'
urlpatterns = [
    path('', get_form, name='index'),
    path('person-list/', PersonIndexView.as_view(), name='person-list'),
    path('person/', person_create_form, name='person-form'),
    path('person/<int:pk>/', person_update_form, name='person-update-form'),
]
