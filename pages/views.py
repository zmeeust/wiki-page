from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, View
from django.views.generic.edit import CreateView

from .models import Page, Version


class HomePage(ListView):
    """Display home pdge. If there are no pages, the creation page is displayed."""
    model = Page
    template_name = 'pages/index.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        if context['pages'].count() == 0:
            self.template_name = 'pages/start.html'
            context = {}
        return context


class PageDetail(DetailView):
    """Display detail information about the page."""
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'


class PageCreate(CreateView):
    """This view create new page."""
    model = Version
    fields = ['title', 'text']
    template_name = 'pages/create.html'

    def form_valid(self, form):
        """At the beginning a blank page is created, which is assigned to the new version. 
        After creating the version, it is assigned to a new page.
        """
        page = Page.objects.create()
        form.instance.current_page = page
        form.instance.save()
        page.current_version = form.instance
        page.save()
        return HttpResponseRedirect('/')


class PageUpdate(UpdateView):
    """UPdate page view"""
    fields = ['title', 'text']
    template_name = 'pages/update.html'

    def get_object(self):
        """This method returns the current version of the page, since the version is updated exactly."""
        return Page.objects.get(pk=self.kwargs['pk']).current_version

    def form_valid(self, form):
        """This method creates a copy of the version by resetting the primary key. 
        After saving, the old copy remains, and the new one is assigned to the page being updated.
        """
        form.instance.pk = None
        page = form.instance.page
        version = form.save()
        page.current_version = version
        page.save()
        return HttpResponseRedirect(page.get_absolute_url())


class VersionsPageList(ListView):
    """Display all page versions"""
    template_name = 'pages/versions.html'
    context_object_name = 'versions'

    def get_queryset(self):
        """This method returns a list of all versions of the page."""
        return Version.objects.filter(current_page=Page.objects.get(pk=self.kwargs['pk']))

    def get_context_data(self, **kwargs):
        """Redefining the context, a page object is added to the page, 
        since it is used for passing by reference when changing the current version of the page.
        """
        context = super(VersionsPageList, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(pk=self.kwargs['pk'])
        return context


class ChangePageVersion(View):
    """This view change page version"""
    
    def get(self, request, **kwargs):
        """Having received the current page and the required version by number, 
        we replace the current version of the page.
        """
        page = Page.objects.get(pk=self.kwargs['pk'])
        version = Version.objects.get(pk=self.kwargs['version'])
        page.current_version = version
        page.save()
        return HttpResponseRedirect(page.get_absolute_url())
