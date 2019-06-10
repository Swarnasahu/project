from django import forms
class RegistrationForm(forms.Form):
    firstname=forms.CharField(
        label="Enter first name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'firstname'
            }
        )
    )
    lastname=forms.CharField(
        label="Enter last name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'lastname',

            }
        )
    )
    username=forms.CharField(
        label="Enter user name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username',
            }
        )
    )
    email=forms.EmailField(
        label="Enter your emailid",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'emailid',
            }
        )
    )
    number=forms.IntegerField(
        label="Enter your number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile number'
            }
        )
    )
    password1=forms.CharField(
        label="Enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'your password'
            }

        )
    )
    password2 = forms.CharField(
        label="Enter your confirm password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your confirm password'
            }

        )
    )
class LoginForm(forms.Form):
    username=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Username'
            }
        )

    )
    password1=forms.CharField(
        label="Enter your password",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'password1'
            }
        )
    )