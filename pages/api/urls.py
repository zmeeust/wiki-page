from django.conf.urls import url

from .views import (
    PagesCount,
    PageVersionList,
    PageVersionDetail,
    PageCurrentVersion,
    PageUpdate,
    ChangePageVersion,
    )


urlpatterns = [
    url(r'^pages/$', PagesCount.as_view()),
    url(r'^page/(?P<pk>\d+)/versions/$', PageVersionList.as_view()),
    url(r'^page/(?P<pk>\d+)/version/(?P<version>\d+)/$', PageVersionDetail.as_view()),
    url(r'^page/(?P<pk>\d+)/current-version/$', PageCurrentVersion.as_view()),
    url(r'^page/(?P<pk>\d+)/update/$', PageUpdate.as_view()),
    url(r'^page/(?P<pk>\d+)/change-version/(?P<version>\d+)/$', ChangePageVersion.as_view()),
]
