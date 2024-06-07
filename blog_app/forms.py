from django import forms
from django.core.exceptions import ValidationError
from django.forms import CheckboxSelectMultiple

from blog_app.models import Contactus, Article


# class Contactform(forms.Form):
#     choices_years = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]
#     colors = [
#         ('red', 'RED'),
#         ('green', 'GREEN'),
#         ('blue', 'BLUE')
#     ]
#     name = forms.CharField(max_length=20)
#     email = forms.EmailField()
#     password1 = forms.IntegerField(widget=forms.PasswordInput, label='Password')
#     password2 = forms.IntegerField(widget=forms.PasswordInput, label='Password')
#     date = forms.DateField(widget=forms.SelectDateWidget(years=choices_years))
#     color_choices0 = forms.ChoiceField(choices=colors)
#     color_choices1 = forms.MultipleChoiceField(widget=CheckboxSelectMultiple, choices=colors)
#     color_choices2 = forms.ChoiceField(widget=forms.RadioSelect, choices=colors)
#
#     def clean(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("passowords are not same")
#
#     def clean_name(self):
#         name = self.cleaned_data.get("name")
#         if 'mahdi' in name:
#             raise ValidationError("this is the name of your lord you cant use this spacial name")
#         else:
#             return name
# we can use this shape of form

# or use this shape of form:

class Contactusform(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ['title', 'text', 'email'] # or '__all__'
        # we use exclude to sho what we dont whant use in our form
        # like thaht : exclude = ['password']

        # for style you can use widgets :
        #
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your title'}),
        #     'text': forms.Textarea(attrs={
        #         "style": 'border-radius: 10px;'
        #     })
        # }

        # im using this to my contactus page and te upper text was for learning
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your title'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter your text'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your email address'
            })
        }

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['author', 'slug']