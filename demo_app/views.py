from django.http import JsonResponse

from demo import settings
from demo_app.models import BlogPost
from django.shortcuts import render


def add_blog_post(request):
	# Check user is logged in
	if not request.user.is_authenticated:
		return JsonResponse({}, status=403)
	# Validate our request
	if 'title' not in request.POST or 'content' not in request.POST:
		return JsonResponse({}, status=400)
	# Create Blog Post
	new_blog_post = BlogPost.objects.create(
						title=request.POST['title'],
						content=request.POST['content'],
						user=request.user)
	# Return a RESTful response
	return JsonResponse({
		'id': new_blog_post.id,
		'title': new_blog_post.title,
		'content': new_blog_post.content,
		}, status=201)


def remove_blog_post(request, post_id):
	# Find objects with the given id
	blog_post = BlogPost.objects.filter(id=post_id)
	# Check the object(s) exists
	if not blog_post.exists():
		return JsonResponse({}, status=404)
	# Delete the object(s)
	blog_post.delete()
	return JsonResponse({}, status=204)


def list_blog_posts(request):
	# Get all BlogPost Objects
	blog_posts = BlogPost.objects.all()
	# Use List Comprehension to build JSON response
	return JsonResponse({
			'posts': [{
				'id': post.id,
				'title': post.title,
				'content': post.content,
				'username': post.user.username,
			} for post in blog_posts],
		}, status=200)


def add_form(request):
	return render(request, 'add_form.html')


# Create your views here.


def index(request):
	context = {
		'some_text': "This Is Some Random Text",
	}
	return render(request, 'example.html', context=context)


def delete(request):
	return render(request, 'delete_form.html')


def block(request):
	return render(request, 'block.html')
