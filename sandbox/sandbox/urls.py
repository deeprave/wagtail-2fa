import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from wagtail import VERSION as WAGTAIL_VERSION
from wagtail.admin import urls as wagtailadmin_urls

if WAGTAIL_VERSION >= (3, 0):
    # noinspection PyUnresolvedReferences
    from wagtail import urls as wagtail_urls
else:
    # noinspection PyUnresolvedReferences
    from wagtail.core import urls as wagtail_urls

from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
