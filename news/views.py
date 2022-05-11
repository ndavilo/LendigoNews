from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post, Comment
from .forms import PostForm, EditForm, AddCommentForm, EditCommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
import requests
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

def GetNumberCode():
	url = "https://hacker-news.firebaseio.com/v0/topstories.json"
	payload = "{}"
	response = requests.request("GET", url, data=payload)
	number_code_list=response.text.replace('[','').replace(']','').split(',')

	return number_code_list[:10]

def MissingNumberCode(secondlist):# compared with the database
	Missing_list =[]
	for i in range(len(secondlist)):
		if Post.objects.filter(code=int(secondlist[i])).exists():
			pass
		else:
			Missing_list.append(secondlist[i])

	return Missing_list


def GetNewsAPI(number_code_list, s1="title"):
	requested_list =[]

	for num in number_code_list:
		s2=str(num)
		url = f'https://hacker-news.firebaseio.com/v0/item/{s2}/{s1}.json?print=pretty'
		payload = "{}"
		response = requests.request("GET", url, data=payload)
		requested=((response.text).replace('\n','')).replace('"','')
		requested_list.append(requested)

	return requested_list


class HomeView(View):
	def get(self, request, *args, **kwargs):
		secondlist=GetNumberCode()
		number_code_list=MissingNumberCode(secondlist)

		code_list=GetNewsAPI(number_code_list, "id")
		title_list=GetNewsAPI(number_code_list, "title")
		author_list=GetNewsAPI(number_code_list, "by")
		url_list=GetNewsAPI(number_code_list, "url")
		for i in range(len(code_list)):
			if Post.objects.filter(code=int(code_list[i])).exists():
				pass
			else:
				new_post = Post(
					code		= code_list[i],
					title 		= title_list[i],
					by 			= author_list[i],
					urls 		= url_list[i]
						)
				new_post.save()

		post_list = Post.objects.all().order_by('-id')
		paginator = Paginator(post_list, 25) # Show 25 contacts per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request, 'home.html', {'page_obj': page_obj})


class SearchResultsView(ListView):
	model = Post
	template_name = "search_results.html"

	def get_queryset(self):  
		query = self.request.GET.get("q")
		object_list = Post.objects.filter(
			Q(title__icontains=query) | Q(body__icontains=query)#search through titles and post bodies
			)
		return object_list

class LatestNewsView(ListView):
	model = Post
	template_name = "latest_news.html"

	def get_queryset(self):  
		object_list = Post.objects.all().order_by('-id')[:25]# Show 25 new news
		return object_list

class ADetailView(DetailView):
	model 			= Post
	template_name 	= 'details.html'

	def get_context_data(self, *args, **kwargs):
		context 				= super(ADetailView, self).get_context_data(*args, **kwargs)
		stuff 					= get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes				= stuff.total_likes()

		liked					= False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked				= True

		context["liked"]		= liked
		context["total_likes"]	= total_likes

		return context


class AddPostView(CreateView):
	model 			= Post
	form_class		= PostForm
	template_name	= 'add_post.html'
	success_url 	= reverse_lazy('home')

class AddCommentView(CreateView):
	model 			= Comment
	form_class		= AddCommentForm
	template_name	= 'add_comment.html'
	success_url 	= reverse_lazy('home')

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

class UpdatePostView(UpdateView):
	model 			= Post
	template_name	= 'add_post.html'
	form_class		= EditForm
	success_url 	= reverse_lazy('home')

class DeletePostView(DeleteView):
	model 			= Post
	template_name	= 'delete_post.html'
	success_url 	= reverse_lazy('home')


class UpdateCommentView(UpdateView):
    model 			= Comment
    template_name	= 'update_comment.html'
    form_class		= EditCommentForm
    success_url 	= reverse_lazy('home')

class DeleteCommentView(DeleteView):
    model 			= Comment
    template_name	= 'delete_comment.html'
    success_url 	= reverse_lazy('home')


def LikeView(request, pk):
	post 			= get_object_or_404(Post, id = request.POST.get('post_id'))
	liked			= False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked			= False

	else:
		post.likes.add(request.user)
		liked		= True

	return HttpResponseRedirect(reverse('home'))

def AboutView(request):
	return render(request, 'about.html')



