from django.urls import path
from .views import SomeProtectedView, index, UserDetailView


urlpatterns = [
    path('some-protected-view/', SomeProtectedView.as_view(), name='some_protected_view'),
    path('index/', index, name='index'),
    path('api/user-detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Other URL patterns
]
