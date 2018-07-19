from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PageSerializer, VersionSerializer
from pages.models import Page, Version


class PagesCount(APIView):
    """Returns the number of pages."""

    def get(self, request):
        pages = Page.objects.all().count()
        return Response({'page_count': pages})


class PageVersionList(generics.ListAPIView):
    """Returns the list of versions of the selected page."""
    serializer_class = VersionSerializer

    def get_queryset(self):
        return Version.objects.filter(current_page=Page.objects.get(pk=self.kwargs['pk']))


class PageVersionDetail(generics.RetrieveAPIView):
    """Returns a description of the version of the selected page."""
    serializer_class = VersionSerializer

    def get_object(self):
        return Version.objects.filter(current_page=Page.objects.get(pk=self.kwargs['pk'])).get(version=self.kwargs['version'])


class PageCurrentVersion(generics.RetrieveAPIView):
    """Returns the current version of the selected page."""
    serializer_class = VersionSerializer

    def get_object(self):
        return Page.objects.get(pk=self.kwargs['pk']).current_version


class PageUpdate(generics.RetrieveUpdateAPIView):
    """Updates the selected page."""
    serializer_class = VersionSerializer

    def get_object(self):
        """Get the current version of the selected page."""
        return Page.objects.get(pk=self.kwargs['pk']).current_version

    def put(self, request, *args, **kwargs):
        """This method creates a copy of the version by resetting the primary key. 
        After saving, the old copy remains, and the new one is assigned to the page being updated.
        """
        instance = self.get_object()
        page = instance.current_page
        instance.pk = None
        instance.save()
        page.current_version = instance
        page.save()
        return self.update(request, *args, **kwargs)


class ChangePageVersion(APIView):
    """"This view change page version"""

    def get(self, request, pk, version):
        """Having received the current page and the required version by number, 
        we replace the current version of the page.
        """
        page = Page.objects.get(pk=pk)
        version = Version.objects.filter(current_page = page).get(version=version)
        page.current_version = version
        page.save()
        return Response({'page': page.pk, 'version': version.version})
