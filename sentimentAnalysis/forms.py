from django import forms

class SelectFlight(forms.Form):

	choices = [("0","Country"),
			("1","Tweet"),
			("2","User")]
	searchOptions = forms.ChoiceField(choices)