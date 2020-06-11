from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from demo_app.models import BlogPost


class BlogPostTestCase(TestCase):
    def setUp(self):
        user = User.objects.all().first()
        if user is None:
            user = User.objects.create(first_name="TESTER", email="email@email.com", password="password")
        post_id = BlogPost.objects.create(title="Test Title", content="Some test content", user=user)
        self.post_id = post_id.id

    def test_blog_post_has_user(self):
        post = BlogPost.objects.filter(id=self.post_id)
        self.assertEqual(post.exists(), True)
        post = post.first()
        self.assertIsNotNone(post.user)

