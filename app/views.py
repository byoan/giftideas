from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from app.forms.login import LoginForm
from app.forms.register import RegisterForm
from app.models import Produit
from django.urls import reverse_lazy
from django.views import generic


class CadeauxView(LoginRequiredMixin, ListView):
    template_name = 'cadeaux.html'

    model = Produit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CadeauDetailsView(DetailView):
    template_name = 'cadeauDetail.html'

    model = Produit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CadeauUpdate(UpdateView):
    model = Produit
    fields = ['nom', 'prix', 'detail']
    template_name = 'cadeau_update_form.html'
    success_url = reverse_lazy('cadeaux-list')


class IsLoggedView(generic.TemplateView):
    template_name = 'is_logged.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        if 'a' not in username:
            form.add_error('username',
                           'Username must have a "a"')
            return super(LoginView, self).form_invalid(form)

        if len(password) < 8:
            form.add_error('password',
                           'Min length of the password must be 8 characters')
            return super(LoginView, self).form_invalid(form)

        user = authenticate(username=username,
                            password=password)

        if user is None:
            form.add_error(None,
                           'Username or password incorrect')

        login(self.request, user)

        return super(LoginView, self).form_valid(form)

class RegisterView(generic.FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        if form.is_valid():
            # Save will use all the fields defined in the Meta class of the
            # RegisterForm form class
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(self.request, user)
            return super(RegisterView, self).form_valid(form)
