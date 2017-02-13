from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post, Page, BlogTitle

# Create your tests here.
class PostTests(TestCase):
    def test_create_post(self):
        test_text = "bananas"
        user = User.objects.create_user(username='USERNAME', password='PASSWORD')
        p = Post.objects.create(author=user, title="Test", text=test_text)
        p.publish()
        client = Client()
        response = self.client.get("/")
        print("\n"+str(response.content)+"\n")
        self.assertContains(response, test_text)

class PageTests(TestCase):
    def test_create_page(self):
        user = User.objects.create_user(username='USERNAME', password='PASSWORD')
        p = Page.objects.create(author=user, title="Test Page", text="No one will see this")
        p.publish()
        client = Client()
        response = self.client.get("/")
        #print("\n"+str(response.content)+"\n")
        self.assertContains(response, "Test Page")

class BlogTitleTests(TestCase):
    def test_new_title(self):
        t = BlogTitle.objects.create(text="Test Title")
        t.save()
        client = Client()
        response = self.client.get("/")
        #print("\n"+str(response.content)+"\n")
        self.assertContains(response, "Test Title")