from Treasure.models import TreasureGram
from django import forms


class TreasureForm(forms.ModelForm):
	class Meta:
		model=TreasureGram
		fields='__all__'


class TreasureCustom(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	value=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	material=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	location=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	image=forms.CharField(widget=forms.FileInput(),required=False)

	class Meta:
		model=TreasureGram
		fields='__all__'