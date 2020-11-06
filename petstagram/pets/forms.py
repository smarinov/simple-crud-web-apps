from django import forms

from pets.models import Pet, Comment


class PetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        fields = '__all__'


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control rounded-2'}))
