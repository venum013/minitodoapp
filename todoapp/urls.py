from django.urls import path
from .views import Page,New,SignUpView
urlpatterns = [
    path('',Page.as_view(),name='Page'),
    path('delete/<int:todo_id>',New.as_view(),name='delete'),
    path('accounts/signup/',SignUpView.as_view(),name='signup')
]
