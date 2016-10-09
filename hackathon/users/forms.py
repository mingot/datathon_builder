from django import forms


class SignupForm(forms.Form):
    TEAMS = (
        ('RugBcn', 'RugBcn'),
        ('EducatedLobsters', 'EducatedLobsters'),
        ('Low riders', 'Low riders'),
        ('Erasmus heroes', 'Erasmus heroes'),
        ('DeepYellow', 'DeepYellow'),
        ('Pachons', 'Pachons'),
        ('Alpha', 'Alpha'),
        ('Omega', 'Omega'),
        ('Race Against the Machine', 'Race Against the Machine'),
        ('BASELINE', 'BASELINE'),
    )
    team = forms.ChoiceField(choices=TEAMS, required=True, label='Team')

    def signup(self, request, user):
        user.team = self.cleaned_data['team']
        user.save()




