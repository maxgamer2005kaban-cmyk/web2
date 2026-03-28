from django import forms

# Простая форма, аналогичная той, что на скриншотах, но подходящая по смыслу
class PlayerForm(forms.Form):
    name = forms.CharField(label='Имя игрока', max_length=100)
    age = forms.IntegerField(label='Возраст')
