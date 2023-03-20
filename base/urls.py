from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blog, name="blogs"),
    path('message/', views.message, name='message'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





# from django.urls import path


# # from .views import postView, home, contact, blogHome
# from . import views

# urlpatterns = [
#     # path('', views.home, name='home'),
#     path('contact/', views.contact, name="contact"),
#     # path('blogs/', views.blogHome, name="blogHome"),
#     path('',views.PostList.as_view(), name="home"),
#     path('post-new/', views.PostCreateView.as_view(), name='new-blog'),
#     # path('<slug:slug>/',views.PostDetail.as_view(), name="post_detail"),
#     path('<slug:slug>/', views.post_detail, name="post_detail"),
#     # path('blog/<str:slug>', views.blogPost, name="blogpost"),
# ]
