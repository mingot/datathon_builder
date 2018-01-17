from django import forms


class SignupForm(forms.Form):
    TEAMS = (
        ('Alpha', 'Alpha'),
        ('Big Chusta', 'Big Chusta'),
        ('Dataire', 'Dataire'),
        ('Datastrophic Team', 'Datastrophic Team'),
        ('Dirty Data', 'Dirty Data'),
        ('Dreamers', 'Dreamers'),
        ('Just Peanuts', 'Just Peanuts'),
        ('R Users Group', 'R Users Group'),
        ('R-Student', 'R-Student'),
        ('Solaris', 'Solaris'),
        ('Worthless without Coffee', 'Worthless without Coffee'),
        ('XTeamFME', 'XTeamFME'),
    )
    
    team = forms.ChoiceField(choices=TEAMS, required=True, label='Team')

    def signup(self, request, user):
        user.team = self.cleaned_data['team']
        user.save()




