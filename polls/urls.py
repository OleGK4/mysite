from django.urls import path
from .views import BBLoginView
from . import views
from .views import profile
from .views import BBLogoutView

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('polls/login', BBLoginView.as_view(), name='login'),
    path('polls/profile/', profile, name='profile'),
    path('polls/logout/', BBLogoutView.as_view(), name='logout'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
