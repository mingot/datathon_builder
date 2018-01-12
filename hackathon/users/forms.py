from django import forms


class SignupForm(forms.Form):
    TEAMS = (
        ('Archimedes', 'Archimedes'),
        ('Newton', 'Newton'),
        ('Euclid', 'Euclid'),
        ('Gauss', 'Gauss'),
        ('Descartes', 'Descartes'),
        ('Euler', 'Euler'),
        ('Fermat', 'Fermat'),
        ('Turing', 'Turing'),
        ('Pascal', 'Pascal'),
        ('Hilbert', 'Hilbert'),
        ('BASELINE', 'BASELINE'),
    )
    team = forms.ChoiceField(choices=TEAMS, required=True, label='Team')

    def signup(self, request, user):
        user.team = self.cleaned_data['team']
        user.save()




