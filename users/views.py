from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.contrib.auth.models import User 


from django.urls import reverse_lazy
from .models import Social
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from .forms import(
	 UserRegisterForm,
	 UserUpdateForm,
	 ProfileUpdateForm,
	 BiographyForm,
	 AccessCodeForm
 )
from django.apps import apps
Post = apps.get_model('blog', 'Post')

def register(request):
	if request.method == 'POST':
		form1 = UserRegisterForm(request.POST)
		form2 = AccessCodeForm(request.POST)
		if form2.is_valid() and form1.is_valid():
			accesscode = form2.cleaned_data.get('accesscode')
			if accesscode == 'WRITETODAY':
				form1.save()
				username = form1.cleaned_data.get('username')
				messages.success(request, f'Your account has been created! Login in pls!')
				return redirect('login')
			else:
				messages.warning(request,f'WRONG ACCESS CODE')
	else:
		form1 = UserRegisterForm()
		form2 = AccessCodeForm()
		
	context = {
		'form1': form1,
		'form2': form2
		
	}
	return render(request, 'users/register.html', context)

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
								  request.FILES, 
								  instance=request.user.profile)
		b_form = BiographyForm(request.POST, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid() and b_form.is_valid():
			u_form.save()
			p_form.save()
			b_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('editprofile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
		b_form = BiographyForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form,
		'b_form': b_form
	}

	return render(request, 'users/editprofile.html', context)


class ProfileListView(ListView):
	model = Post
	template_name = 'users/profile.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		user = self.request.user
		return Post.objects.filter(author=user).order_by('-date_posted')


class CreateSocial(LoginRequiredMixin, CreateView):
	model = Social
	fields = ['title', 'link']
	success_url = reverse_lazy('editprofile')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateSocial, self).form_valid(form)

