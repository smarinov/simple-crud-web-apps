from django.urls import path

from pets.views import list_pets, show_pet_details, like_pet, edit_pet, delete_pet, create_pet

urlpatterns = [
    path('', list_pets, name='list pets'),
    path('details/<int:pk>/', show_pet_details, name='pet details'),
    path('like/<int:pk>/', like_pet, name='like pet'),
    path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
    path('create/', create_pet, name='create pet'),
]
