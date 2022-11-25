from django.urls import path ,include
from rest_framework import routers
#from . import UserViewSet
from . import views
 #router=routers.DefaultRouter()
#router.register('api/users',LeadViewSet)
urlpatterns = [
    path("get-user-list/",views.get_user_list, name="get-user-list"),
    path("signup/",views.signup,name="signup"),
    path("get-user-by-num/<str:pk>/",views.get_user_by_num,name="get-user-by-num"),
    path("get-details/",views.get_details,name="get-details"),
    path("form/",views.form,name="form"),
]
