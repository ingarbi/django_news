from django import template
from django.db.models import Count, F
from django.core.cache import cache
from news.models import Category

register = template.Library()


@register.simple_tag(name="get_list_categories")
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello ', arg2='world'):
    # categories = Category.objects.all()
    # categories = Category.objects.annotate(cnt=Count('get_news')).filter(cnt__gt=0)
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.annotate(
            cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
        cache.set('categories', categories, 30)
    return {"categories": categories, 'arg1': arg1, 'arg2': arg2}
