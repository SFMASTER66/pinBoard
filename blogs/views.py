from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse

from .models import Post, Comment
from shared.models import *
from django.contrib import auth
from django.shortcuts import render,render_to_response
from django.template import RequestContext

from .forms import *

# Create your views here.
def index(request):
    latest_post_list = sorted(Post.objects.all(), key=lambda p: p.score)
    # latest_post_list = Post.objects.all()
    context = {
        'latest_post_list': latest_post_list,
    }

    return render(request, 'blogs/index.html', context=context)

def create_post(request):
    if (request.method == 'POST'):
        pass
    return render(request, 'blogs/add_post.html', {'form': AddPostForm()})

class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-create_time')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/detail.html'


class ResultsView(generic.DetailView):
    model = Post
    template_name = 'blogs/results.html'

class PostView(generic.DetailView):
    model = Post
    template_name = 'blogs/post.html'

class CommentView(generic.ListView):
    template_name = 'blogs/comment.html'
    context_object_name = 'comment_list'

    # dispatch is called when the class instance loads
    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk', "-1")
        return super(generic.ListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """Return the comments of the certain post ordered by score."""
        return sorted(Comment.objects.filter(parent=self.pk), key=lambda c: c.score)

class LoginView(generic.DetailView):
    model = Post
    template_name = 'blogs/login.html'

class RegisterView(generic.DetailView):
    model = Post
    template_name = 'blogs/register.html'

def vote(request, content_id):
    if (request.method == 'POST'):
        user_id = request.POST.get('user_id', None)
        value = request.POST.get('value', 1)
        return HttpResponse(str(Vote.vote(content_id, user_id, value)))

def login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']


            #userinfo = User.objects.get(username=username)  #get all info of user

            #current_user = request.user admin user
            #print(userinfo.email)


            user = User.objects.filter(username__exact = username,password__exact = password)
            print(user)
            if user:
                response = HttpResponseRedirect('/blogs/')
                response.set_cookie('username',username,3600)
                return response

                #request.session['username'] = user
                #request.session.set_expiry(600)
                #return render(request, '/blogs/',{
                #'welcome':"欢迎你"})
            else:
                error = 'Username is not right or password is not right!'
                return render(request,'blogs/login.html', {'form': LoginForm(), 'error': error})

    #return render(request, 'blogs/login.html', locals())

    login_form = LoginForm()
    return render(request, 'blogs/login.html', {'form': login_form, 'message': ''})


def register(request):
    if (request.method == 'POST'):
        register_form = RegisterForm(request.POST)
        # message = "Please check the information"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            repassword = register_form.cleaned_data['repassword']

            if password != repassword:
                password_message = 'password does not match!'
                return render(request, 'blogs/register.html', {'form': RegisterForm(), 'password_message': password_message})

            same_name_user = User.objects.filter(username=username)
            if same_name_user:
                user_name_message = 'Username already exists!'
                return render(request, 'blogs/register.html', {'form': RegisterForm(), 'user_name_message': user_name_message})
            same_email_user = User.objects.filter(email=email)
            if same_email_user:
                email_message = 'Email already exists!'
                return render(request, 'blogs/register.html', {'form': RegisterForm(), 'email_message': email_message})

            new_user = User.objects.create()
            new_user.username = username
            new_user.email = email
            new_user.password = password
            new_user.save()

            # message = 'Registered Successfully!'

            # return redirect('/login/')
            return render_to_response("blogs/login.html")
        else:
            message = 'Invalid input!'
            return render_to_response("blogs/login.html")


    register_form = RegisterForm()
    return render(request, 'blogs/register.html', {'form': register_form, 'message': ''})

def post(request):
    return render(request, 'blogs/post.html', locals())

def comment(request):
    return render(request, 'blogs/comment.html', locals())



