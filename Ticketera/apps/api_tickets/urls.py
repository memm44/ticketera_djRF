from django.urls import path
from django.urls import include
from .views import ListIssues, DetailIssue, AsignIssue, ListResponsible

urlpatterns = [
    path('issues', ListIssues.as_view(), name='issues-list'),
    path('issue/<int:pk>/', DetailIssue.as_view(), name='issue'),
    path('issues/asign', AsignIssue.as_view(), name="asign_issue"),
    path('issuers', ListResponsible.as_view(), name="responsibles")
]
