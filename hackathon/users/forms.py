from django import forms


class SignupForm(forms.Form):
    TEAMS = (
        ('The G-Priors', 'The G-Priors'),
        ('TeamUNO', 'TeamUNO'),
        ('Pretty fly for a wifi', 'Pretty fly for a wifi'),
        ('Multimetro', 'Multimetro'),
        ('Hacaguays', 'Hacaguays'),
        ('Bcn R users group', 'Bcn R users group'),
        ('Alpha', 'Alpha'),
        ('Red Jaguars', 'Red Jaguars'),
        ('Silver Snakes', 'Silver Snakes'),
        ('Green Monkeys', 'Green Monkeys'),
        ('BASELINE', 'BASELINE'),
    )
    team = forms.ChoiceField(choices=TEAMS, required=True, label='Team')

    def signup(self, request, user):
        user.team = self.cleaned_data['team']
        user.save()