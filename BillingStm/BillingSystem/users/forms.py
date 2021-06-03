from django import forms
from .models import Employee, EmpLogin


class AddEmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {"username":forms.TextInput(attrs=({"class":"form-control"})),
                   "password":forms.PasswordInput(attrs=({"class":"form-control"})),
                   "first_name":forms.TextInput(attrs=({"class":"form-control"})),
                   "last_name":forms.TextInput(attrs=({"class":"form-control"}))}
        labels = {"first_name":"First Name","last_name":"Last Name"}


class EmpLoginForm(forms.ModelForm):
    class Meta:
        model = EmpLogin
        fields = "__all__"
        widgets = {"username": forms.TextInput(attrs=({"class": "form-control"})),
                   "password": forms.PasswordInput(attrs=({"class": "form-control"})),
                   "login_time": forms.DateTimeInput(attrs=({"class": "form-control"})),
                   "logout_time": forms.DateTimeInput(attrs=({"class": "form-control"}))}
        # labels = {"first_name": "First Name", "last_name": "Last Name"}



