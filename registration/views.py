from .forms import UserCreationFormWithEmail, ProfileForm
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Profile
# Create your views here.

class SignUpView(CreateView):
	form_class = UserCreationFormWithEmail
	template_name = 'registration/signup.html'

	def get_success_url(self):
		return reverse_lazy('login') + '?register'

	def get_form(self, form_class=None):
		form = super(SignUpView, self).get_form()
		# Modificar en tiempo real
		form.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Nombre de usuario'})
		form.fields['email'].widget=forms.EmailInput(attrs={'placeholder':'Dirección email'})
		form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Contraseña'})
		form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Repite la contraseña'})
		return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
	form_class = ProfileForm
	success_url = reverse_lazy('profile')
	template_name = 'registration/profile_form.html'

	def get_object(self):
		# recuperar el objeto que se va a editar
		profile, created = Profile.objects.get_or_create(user=self.request.user)
		return profile
