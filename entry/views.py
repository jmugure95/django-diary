from django.shortcuts import render,redirect
from .models import Entry
from .forms import EntryForm

# Create your views here.
def home_view(request):
	entries = Entry.objects.all().order_by('-date')
	return render(request,'entry/index.html',{'entries':entries})

def entry_view(request):
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('entry:home')
	else:
		form = EntryForm()
	return render(request,'entry/entry.html',{'form':form})
    
