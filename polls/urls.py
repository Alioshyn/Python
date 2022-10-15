from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/register/', views.RegisterFormView.as_view()),
    path('<int:pk>/login/', views.LoginFormView.as_view()),
    path('<int:pk>/logout/', views.LogoutView.as_view()),
    path('<int:pk>/password-change/', views.PasswordChangeView.as_view()),
]



