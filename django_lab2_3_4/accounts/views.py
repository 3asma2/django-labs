from django.shortcuts import redirect
from accounts.models import Acc
from accounts.forms import AddStudentModelForm
from django.views import View

def delete_user(request, id):
    column = Acc.objects.get(id=id)
    if column:
        column.delete()
        if request.session.get('user_selected'):
            request.session.pop('user_selected')
        return redirect('home')
    else:
        return redirect('home')


def create_user(request):
    if request.method == 'POST':
        form = AddStudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            if request.session.get('user_selected'):
                request.session.pop('user_selected')
            return redirect('home')
        else:
            return redirect('home')


class UpdateUser(View):
    def get(self, request):
        pass

    def post(self, request, id):
        form = AddStudentModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            column = Acc.objects.get(id=id)
            column.name = name
            column.save()
            if request.session.get('user_selected'):
                request.session.pop('user_selected')
            return redirect('home')
        else:
            return redirect('home')


def update_user(request, id):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        column = Acc.objects.get(id=id)
        if column:
            print(column.name, "first")
            column.name = name
            print(column.name, "second")
            column.save()
            if request.session.get('user_selected'):
                request.session.pop('user_selected')
            return redirect('home')
        else:
            return redirect('home')


def search_user(request):
    if request.method == 'GET':
        name = request.GET.get('user_name')
        column = Acc.objects.filter(name=name)
        if column:
            request.session['user_selected'] = list(column).values()
            return redirect('home')
        else:
            return redirect('home')
