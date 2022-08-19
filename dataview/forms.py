from django import forms

class DataTable(forms.Form):
    option1 = (
        ('m', "Monthly"),
        ('y', "Yearly")
    )
    option2 = (
        ('p', 'Pie Chart'),
        ('b', 'Bar Chart')
    )
    choice1 = forms.ChoiceField(label="Select Month or Year", choices=option1)
    choice2 = forms.ChoiceField(label="Select Chart Type", choices=option2)
