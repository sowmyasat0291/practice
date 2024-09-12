from django.urls import path
from .views import SomeProtectedView, index

urlpatterns = [
    path('some-protected-view/', SomeProtectedView.as_view(), name='some_protected_view'),
    path('index/', index, name='index'),

    # Other URL patterns
]
