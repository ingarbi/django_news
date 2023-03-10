from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import News, Category
from .forms import NewsForm
# Create your views here.

#Pagination in function
def test(request):
    objects = ['john', 'paul', 'george', 'ringo','john2', 'paul2', 'george2', 'ringo2']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num) #if we use method .page instead of .get_page if page=5 doest exists we will get exception"no results"
    return render(request, 'news/test.html', {'page_obj': page_objects})

def test(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                'ingarbi006@elasticemail.com',
                ['ingarbi006@gmail.com'],
                fail_silently=False
            )
            if mail:
                messages.success(request, "Mail was sent successfully")
                return redirect('test')
            else:
                messages.error(request, "Mail was not sent")
        else:
            messages.error(request, "Mail was not sent")
    else:
        form = ContactForm()

    return render(request, 'news/test.html', {"form": form})

def index(request):
    news = News.objects.all()
    title = "List of news"
    context = {
        'news': news,
        'title': title
    }
    return render(request, 'news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, 'news/category.html', context=context)


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    # news_item = News.objects.get(pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})


#  ?????? ?????????? ?????????????? ???? ???????????? ?? ??????????????
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():#???????? ?????????? ???????????????? ?????????????????? ???? ???????????????????? ?????????? ???????? ????????
#             # print(form.cleaned_data)
#             # title = form.cleaned_data['title'] ???????????? ?????????? ????????????????????
#             news = News.objects.create(**form.cleaned_data)
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
