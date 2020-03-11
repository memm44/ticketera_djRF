from django.urls import path
from rest_framework.authtoken import views  # para devolver el token del usuario
from .views import ListIssues, DetailIssue, AsignIssue, \
    ListResponsible, DetailResponsible, UserCreate, LoginView, ResponsibleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/issuers', ResponsibleViewSet, basename='issuers')
urlpatterns = [
    path('issues', ListIssues.as_view(), name='issues-list'),
    path('issue/<int:pk>/', DetailIssue.as_view(), name='issue'),
    path('issues/asign', AsignIssue.as_view(), name="asign_issue"),
    path('issuers', ListResponsible.as_view(), name="responsibles"),
    path('issuers/<str:pk>/', DetailResponsible.as_view(), name='issue'),
    path('users/create', UserCreate.as_view(), name="users"),
    path('v2/users/login/', LoginView.as_view(), name='login'),  # funcion que devuelve manualmente el token
    path('v2/users/login_drf/', views.obtain_auth_token, name='login_drf'),  # la misma anterior pero nativa de drf
]
urlpatterns += router.urls
