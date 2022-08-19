from django import forms

class DataForm(forms.Form):
    choose_file_csv_or_JSON=forms.FileField()