from django import forms
from countries import get_countries

class SelectFlight(forms.Form):

	choices = [("0","Country"),
			("1","Tweet"),
			("2","User")]
	searchOptions = forms.ChoiceField(choices)


class NameForm(forms.Form):

	country_list = get_countries()
	countries_drop_down = forms.ChoiceField(choices = [(country['name'],country['name']) for country in country_list])
	#trending_issues = []