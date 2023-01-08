from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('test/', views.test, name='test'),
    path('contact/', views.contact, name='contact'),
    # path('', views.index, name='home'),
    path('', cache_page(60)(views.HomeNews.as_view()), name='home'),
    # path('category/<int:category_id>', views.get_category, name='category'),
    path('category/<int:category_id>', views.NewsByCategory.as_view(extra_context={'title': 'some strange title'}), name='category'),
    # path('news/<int:news_id>/', views.view_news, name='view_news'),
    path('news/<int:pk>/', views.ViewNews.as_view(), name='view_news'),
    # path('news/add_news/', views.add_news, name='add_news'),
    path('news/add_news/', views.CreateNews.as_view(), name='add_news'),
]
