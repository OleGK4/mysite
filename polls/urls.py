from django.urls import path
from . import views
from .views import BBLoginView, profile, BBLogoutView, UserUpdateView, BBPasswordChangeView, RegisterUserView, RegisterDoneView, DeleteUserView

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/', UserUpdateView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
