from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditSettingsForm, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import DetailView, CreateView, DeleteView
from news.models import Profile
from django.contrib.auth.models import User


class UserRegisterView(generic.CreateView):
	form_class 		=	SignUpForm
	template_name 	= 	'registration/register.html' 
	success_url		=	reverse_lazy('login')

class UserEditView(generic.UpdateView):
	form_class 		=	EditSettingsForm
	template_name 	= 	'registration/edit_settings.html'
	success_url		=	reverse_lazy('home')

	def get_object(self):
		return self.request.user

class Password_ChangeView(PasswordChangeView):
	
	form_class		=	PasswordChangingForm #PasswordChangeForm
	success_url		=	reverse_lazy('password_success')

def password_success(request):
	return render(request, 'registration/password_success.html', {})

class ShowProfilePageView(DetailView):
	model 			=	Profile
	template_name	=	'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		context 		= super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
		page_user		= get_object_or_404(Profile, id=self.kwargs['pk'])
		context["page_user"]	= page_user
		return context

class EditProfilePageView(generic.UpdateView):
	model 			=	Profile
	template_name	=	'registration/edit_profile_page.html'
	form_class 		=	ProfilePageForm
	#fields 			=	['Phone', 'bio', 'profile_pic']
	success_url		=	reverse_lazy('home')

class CreateProfilePageView(CreateView):
	model 			=	Profile
	form_class 		=	ProfilePageForm
	template_name	=	"registration/create_profile_page.html"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class DeleteUserView(DeleteView):
    model 			= User
    template_name	= 'registration/delete_user.html'
    success_url 	= reverse_lazy('home')

