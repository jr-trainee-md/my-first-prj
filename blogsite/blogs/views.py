from django.shortcuts import render

from rest_framework import generics

from .models import Posts, User

from rest_framework import serializers

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.contrib.auth.forms import UserCreationForm

from django import forms

from django.views.generic import CreateView

from django.urls import reverse_lazy

from rest_framework.exceptions import ValidationError

class PostsSerializer(serializers.ModelSerializer):
	usr         = serializers.ReadOnlyField(source = 'usr.username')
	usr_id      = serializers.ReadOnlyField(source = 'usr.id')

	class Meta:
		model = Posts
		fields = ['title', 'time_create', 'content', 'id', 'usr', 'usr_id']

class PostsAPIView(generics.ListCreateAPIView):
	queryset = Posts.objects.all()
	serializer_class = PostsSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(usr = self.request.user)

class PostsUpdDel(generics.RetrieveUpdateDestroyAPIView):
	queryset = Posts.objects.all()
	serializer_class = PostsSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	def put(self, request, *args, **kwargs):
		post = Posts.objects.filter(pk=kwargs['pk'], usr = self.request.user)
		if post.exists():
			return self.update(request, *args, **kwargs)
		else:
			raise ValidationError("No post with this id or you haven't permissions")

	def delete(self, request, *args, **kwargs):
		post = Posts.objects.filter(pk=kwargs['pk'], usr = self.request.user)
		if post.exists():
			return self.destroy(request, *args, **kwargs)
		else:
			raise ValidationError("No post with this id or you haven't permissions")



class Mixin:
	def get_user_context(self, **kwargs):
		return kwargs
		
class RegisterUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username','email', 'password1','password2')
		widget = {
			'username' : forms.TextInput(attrs={'class': 'form-input'}),
			'email'    : forms.TextInput(attrs={'class': 'form-input'}),
			'password1': forms.TextInput(attrs={'class': 'form-input'}),
			'password2': forms.TextInput(attrs={'class': 'form-input'}),
		}
			
class RegisterUser(Mixin, CreateView):
	form_class = RegisterUserForm
	template_name = 'blogs/register.html'
	success_url = reverse_lazy('home')

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Регистрация')
		return dict(list(context.items()) + list(c_def.items()))