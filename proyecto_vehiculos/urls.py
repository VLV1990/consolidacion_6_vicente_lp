from django.urls import path
from.views import v_list, v_create

urlpatterns = [
    path('list', v_list),
    path('create', v_create),
]