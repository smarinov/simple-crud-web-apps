from django.urls import path

from ExpensesApp.views import home, create, edit, delete, profile, edit_profile, delete_profile

urlpatterns = [
    path('', home, name='homepage'),
    path('create/', create, name='create'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit-profile'),
    path('profile/delete/', delete_profile, name='delete-profile'),
]