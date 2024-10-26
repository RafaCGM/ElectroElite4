from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class AcessForm(forms.Form):
    username = forms.CharField(
        label = 'Usuário'
    )
    password = forms.CharField(
        label = "Senha",
        widget = forms.PasswordInput() 
    )

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name' : 'Primeiro nome',
            'last_name': 'Último nome',
            'username': 'Nome de Usuário',
            'email': 'E-mail',
            'password': 'Senha'
        }

        help_texts = {
            'password': 'Utilize uma senha com caracteres, números e símbolos especiais'   
        }

        error_messages = {
            'username': {
                'required': 'Este campo não pode ser vazio.'
            },
            'password': {
                'required': 'Senha inválida.'
            }
        }

        widgets = {
            'email' : forms.TextInput(attrs={
                'placeholder' : 'exemplo@gmail.com',
                'required' : 'true'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder' : 'Digite sua senha'
            })
        }

    def clean_email(self):
        data = self.cleaned_data.get('email')

        if not '@' in data:
            raise ValidationError(
                'O E-mail deve apresentar um @',
                code='invalid'
            )
        
        return data

    def clean(self):
        cleaned_data = super().clean()

        pass1 = cleaned_data.get("password")
        pass2 = cleaned_data.get("password2")

        if pass1 != pass2:
            raise ValidationError(
                {'password' : "Ambas as senhas devem ser iguais!"}
            )

    email = forms.CharField(
        required = True,
        max_length = 150,
        help_text = (
            'Digite um e-mail válido'
        )
    )

    password2 = forms.CharField(
        required=True,
        label='Repita sua senha',
        widget=forms.PasswordInput(attrs={
                'placeholder' : 'Digite sua senha',
            }
        )
    )
