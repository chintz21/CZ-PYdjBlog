from django.shortcuts import render

# Create your views here.

from blog.models import BlogAuthor, Blog, BlogComment

from django.contrib.auth.decorators import login_required

@login_required


def index(request):
    """ View function for home page of site """
    
    # Generate counts of some of the main objects.
    num_blogs = Blog.objects.all().count()
    num_authors = BlogAuthor.objects.all().count()


 #  Number of visits to this view, as counted in the session variable.
 #   num_visits = request.session.get('num_visits', 0)
 #   request.session['num_visits'] = num_visits + 1

    context = {
        'num_blogs': num_blogs,
        'num_authors': num_authors,
#        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

#from django.contrib.auth.decorators import login_required

#@login_required

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(LoginRequiredMixin ,generic.ListView):
    model=Blog

class BlogDetailView(generic.DetailView):
    """ Generic class-based view for view for a blog. """
    model = Blog

class BlogListByAuthorView(LoginRequiredMixin, generic.ListView):
    model = Blog
    paginate_by = 5
    template_name = 'blog/blog_list_by_author.html'


class BloggerListView(LoginRequiredMixin ,generic.ListView):
    "Generic class-based view for a list of bloggers."
    model = BlogAuthor
    paginate_by = 5
