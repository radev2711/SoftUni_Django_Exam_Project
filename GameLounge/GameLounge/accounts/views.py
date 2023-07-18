from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model

from .forms import CreateProfileForm, EditProfileForm
from .models import ProfileModel

User = get_user_model()


class UserRegisterView(CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context

    def get_success_url(self):
        print(self.request.POST)
        return self.request.POST.get('next', self.success_url)


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home-page')


class UserDetailsView(DetailView):
    model = ProfileModel
    template_name = 'accounts/user_details.html'


class UserEditView(UpdateView):
    model = ProfileModel
    form_class = EditProfileForm
    template_name = 'accounts/user_edit.html'

    def get_success_url(self):
        return reverse_lazy('user-details', kwargs={'pk':self.object.pk})


class UserDeleteView(DeleteView):
    model = ProfileModel
    template_name = 'accounts/user_delete.html'
    success_url = reverse_lazy('home-page')

    # def post(self, *args, pk):
    #     self.request.user.delete()

# test123@test.com