from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .models import Lab, App, Employees, Subdivision, Type_App, Housing, Classroom, Status
from .forms import UserForm, AppForm

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'ivc/login_form.html', context)


def newapp(request):
    if not request.user.is_authenticated():
        return render(request, 'ivc/login_form.html')
    else:
        form = AppForm(request.POST or None)
        if form.is_valid():
            apps = form.save(commit=False)
            apps.user = request.user
            apps.save()
            return render(request, 'ivc/cabinet.html', {'app': apps})
        context = {
            "form": form,
        }
        return render(request, 'ivc/newapp.html', context)


def cabinet(request):
    if not request.user.is_authenticated():
        return render(request, 'ivc/login_form.html')
    else:
        user = request.user
        emp = get_object_or_404(Employees, username=user.username)
        sub = get_object_or_404(Subdivision, dp_id=emp.id)
        app = get_object_or_404(App, em_id=emp.id)
        tp = get_object_or_404(Type_App, id=app.tp_id)
        cr = get_object_or_404(Classroom, id=app.cr_id)
        hs = get_object_or_404(Housing, id=cr.hs_id)
        st = get_object_or_404(Status, id=app.st_id)
        return render(request, 'ivc/cabinet.html', {'user': user, 'emp': emp, 'sub': sub, 'app': app, 'tp': tp, 'hs': hs, 'cr': cr, 'st': st})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'ivc/cabinet.html')
            else:
                return render(request, 'ivc/login_form.html', {'error_message': 'Ваш аккаунт не активен'})
        else:
            return render(request, 'ivc/login_form.html', {'error_message': 'Неверно введён логин/пароль'})
    return render(request, 'ivc/login_form.html')

class IndexView(generic.ListView):
    template_name = 'ivc/index.html'
    context_object_name = 'all_labs'

    def get_queryset(self):
        return Lab.objects.all()

class DetailView(generic.DeleteView):
    model = Lab
    template_name = 'ivc/detail.html'

class LabCreate(CreateView):
    model = App
    fields = ['tp_id', 'cr_id']

class LabUpdate(UpdateView):
    model = Lab
    fields = ['title', 'zav_lab', 'type_work', 'lab_logo']

class LabDelete(DeleteView):
    model = Lab
    success_url = reverse_lazy('ivc:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'ivc/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, passsword=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('ivc:index')

        return render(request, self.template_name, {'form': form})
