from django.shortcuts import render, redirect
from app.forms import StudentForm
from app.models import Student




def home(request):
	context = {}
	context['title'] = 'CRUD APP || Home'
	template_name = 'index.html'
	students = Student.objects.all()
	context['students'] = students

	return render(request, template_name, context)

def create(request):
	context = {}
	template_name = 'index.html'
	form = StudentForm()
	context['form'] = form
	context['show_edit_window'] = True
	students = Student.objects.all()
	context['students'] = students

	return render(request, template_name, context)

def hide(request):
	context = {}
	template_name = 'index.html'
	context['show_edit_window'] = False
	students = Student.objects.all()
	context['students'] = students
	context['show_update_window'] = False
	
	return render(request, template_name, context)

def save(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/home')
			except:
				pass
	return redirect('/create')

def update(request, id):
	context = {}
	template_name = 'index.html'
	request.session['id'] = id
	student = Student.objects.get(id = id)
	form = StudentForm(instance=student)
	context['form'] = form
	context['show_update_window'] = True
	students = Student.objects.all()
	context['students'] = students

	return render(request, template_name, context)

def save_update(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			student = Student.objects.get(id = request.session['id'])
			form = StudentForm(request.POST, instance=student)
			try:
				form.save()
				del request.session['id']
				return redirect('/home')
			except:
				pass
	return redirect('/update')




def delete(request, id):
	student = Student.objects.get(id = id)
	student.delete()
	return redirect('/home')


def reload(request):
	return redirect('/home')

#END
