from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail

class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolve_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)

class ArticleListTest(TestCase):
    def test_articles_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_articles_list_url_resolve_articles_list_view(self):
        view = resolve('/articles/')
        self.assertEquals(view.func.view_class, ArticleList)

class ArticleCategoryListTest(TestCase):
    def test_articles_category_list_view_status_code(self):
        url = reverse('articles-category-list', args=['example-slug'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_category_list_url_resolve_articles_category_list_view(self):
        view = resolve('/articles/category/example-slug')
        self.assertEquals(view.func.view_class, ArticleCategoryList)

class ArticleDetailTest(TestCase):
    def test_article_detail_view_status_code(self):
        url = reverse('news-detail', args=['2023', '10', '24', 'example-slug'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url_resolve_article_detail_view(self):
        view = resolve('/articles/2023/10/24/example-slug')
        self.assertEquals(view.func.view_class, ArticleDetail)

# Create your tests here.
