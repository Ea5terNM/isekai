from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .models import  item ,blog , ContactMesssage
from app_general.forms import FavoriteitemForm
from django.contrib.auth.decorators import login_required

from users.models import UserFavoriteitem
from django.urls import reverse

def Home (request) :
    all_blogs = blog.objects.order_by('-addtime') [:3]
    context = {'blogs':all_blogs}
    return render (request,'app_general/Home.html',context)  

def About(request):
    return render(request,'app_general/About.html') 


def products (request):
    
    all_items = item.objects.order_by('addtime')
    form = FavoriteitemForm
    context = {'items' :all_items ,"form" : form}
    return render (request,'app_general/products.html', context)


def product (request,item_id):
    one_item = None
    try:
        one_item = item.objects.get(id=item_id)
    except:
        print('หาไม่เจอ')
    form = FavoriteitemForm
    context = {'item' :one_item ,"form" : form}
    return render (request,'app_general/product.html',context)


def Blogs (request):
    all_blogs = blog.objects.order_by('addtime')
    context = {'blogs':all_blogs}
    return render (request,'app_general/blogs.html',context)



def Blog (request,blog_id):
    one_blog = None
    try:
        one_blog = blog.objects.get(id=blog_id)
    except:
        print('หาไม่เจอ')
    context = {'blog':one_blog}
    return render(request,'app_general/blog.html',context) 


def Contact (request):
   

    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detial = data.get('detial')
        print(data, title, detial)

        if title =='' or email == '':
            context['status'] = 'alert'
            return render(request, 'app_general/Contact.html',context)

        # แก้ปัญหาในการสร้างและบันทึกอ็อบเจ็กต์ ContactMesssage
        new_message = ContactMesssage(title=title, email=email, detial=detial)
        new_message.save()
        context['status'] = 'success'
    return render (request,'app_general/Contact.html')



@login_required
def favorite_item(request: HttpRequest, item_id):
    if request.method == "POST":
        form = FavoriteitemForm(request.POST)
        if form.is_valid():
            obj, is_created = UserFavoriteitem.objects.update_or_create(
                user=request.user,
                item=item(id=item_id),
                defaults={"like": form.cleaned_data.get("like")},
            )
            print("Create favorite" if is_created else "Update favorite")

    return HttpResponseRedirect(reverse("Product", args=[item_id]))



@login_required
def unfavorite_item(request: HttpRequest, item_id):
    if request.method == "POST":
        request.user.favorite_item_set.remove(item(id=item_id))
    return HttpResponseRedirect(reverse("dashboard"))
# Create your views here.
