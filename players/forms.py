from django import forms

from .models import Player


class PlayerEditForm(forms.ModelForm):
    games_played = forms.IntegerField(
        label='Игр сыграно', min_value=0, max_value=2147483647,
    )
    wins = forms.IntegerField(
        label='Побед', min_value=0, max_value=2147483647,
    )

    class Meta:
        model = Player
        fields = ['name', 'steam_id', 'games_played', 'wins']

    def clean(self):
        cleaned_data = super().clean()
        games_played = cleaned_data.get('games_played')
        wins = cleaned_data.get('wins')

        if games_played is not None and wins is not None and wins > games_played:
            self.add_error('wins', 'Число побед не может превышать число игр.')

        return cleaned_data
