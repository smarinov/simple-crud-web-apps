from django.shortcuts import render, redirect

from pets.forms import CommentForm, PetForm
from pets.models import Like, Pet, Comment


# Create your views here.
def list_pets(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }

    return render(request, 'pet_list.html', context)


def show_pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
        }
        return render(request, 'pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.save()
            return redirect('pet details', pk)
        else:
            context = {
                'pet': pet,
                'form': form,
            }
            return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect('pet details', pk)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = PetForm(instance=pet)
        context = {
            'form': form,
            'pet': pet,
        }
        return render(request, 'pet_edit.html', context)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', pet.pk)
        else:
            context = {
                'form': form,
                'pet': pet,
            }
            return render(request, 'pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
        }
        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')


def create_pet(request):
    if request.method == 'GET':
        form = PetForm()
        context = {
            'form': form,
        }
        return render(request, 'pet_create.html', context)
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list pets')
        else:
            return render(request, 'pet_create.html', {'form': form})