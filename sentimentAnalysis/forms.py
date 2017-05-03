from django import forms
from countries import get_countries

class SelectFlight(forms.Form):

	choices = [("0","Country"),
			("1","Tweet")]
	searchOptions = forms.ChoiceField(choices)


class NameForm(forms.Form):

	country_list = get_countries()
	coun = []
	for cc in country_list:
		coun.append((cc['name'],cc['name']))
	coun.sort(key=lambda tup: tup[0])
	print coun
	# countries_drop_down = forms.ChoiceField(choices = [(country['name'],country['name']) for country in country_list])
	locations = forms.ChoiceField(choices = [(country[0],country[1]) for country in coun])
	#trending_issues = []