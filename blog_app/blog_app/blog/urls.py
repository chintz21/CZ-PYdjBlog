from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name="blogs"),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name="blog-detail"),
    path('blogger/<int:pk>', views.BlogListByAuthorView.as_view(), name='blog-by-author'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
]
