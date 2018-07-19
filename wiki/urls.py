from django.conf.urls import include, url
from django.contrib import admin

from pages import views as page_views

urlpatterns = [
    url(r'^$', page_views.HomePage.as_view(), name='home'),
    url(r'^create/$', page_views.PageCreate.as_view(), name='create'),
    url(r'^page/(?P<pk>\d+)/$', page_views.PageDetail.as_view(), name='page-detail'),
    url(r'^page/(?P<pk>\d+)/update/', page_views.PageUpdate.as_view(), name='page-update'),
    url(r'^page/(?P<pk>\d+)/versions/$', page_views.VersionsPageList.as_view(), name='display-versions'),
    url(r'^page/(?P<pk>\d+)/versions/(?P<version>\d+)/$', page_views.ChangePageVersion.as_view(), name='change-version'),
    url(r'^api/', include('pages.api.urls')),
    url(r'^admin/', admin.site.urls),
]
