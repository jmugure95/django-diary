from django.forms import ModelForm
from .models import Entry


class EntryForm(ModelForm):
	class Meta:
		model = Entry
		fields = ('name','story',)

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':'Entry Title'})
		self.fields['story'].widget.attrs.update({'class':'form-control','placeholder':'Enter your Thoughts...'})