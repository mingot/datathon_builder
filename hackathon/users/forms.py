from django import forms


class SignupForm(forms.Form):
    TEAMS = (
        ('RugBcn', 'RugBcn'),
        ('EducatedLobsters', 'EducatedLobsters'),
        ('Low riders', 'Low riders'),
        ('Erasmus heroes', 'Erasmus heroes'),
        ('DeepYellow', 'DeepYellow'),
        ('Blua Tigro', 'Blua Tigro'),
        ('Alpha', 'Alpha'),
        ('Omega', 'Omega'),
        ('Race Against the Machine', 'Race Against the Machine'),
        ('Equipo A', 'Equipo A'),
        ('BASELINE', 'BASELINE'),
    )
    team = forms.ChoiceField(choices=TEAMS, required=True, label='Team')

    def signup(self, request, user):
        user.team = self.cleaned_data['team']
        user.save()




