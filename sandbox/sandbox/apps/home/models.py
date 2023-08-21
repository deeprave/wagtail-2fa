from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    # noinspection PyUnresolvedReferences
    from wagtail.models import Page
else:
    # noinspection PyUnresolvedReferences
    from wagtail.core.models import Page


class HomePage(Page):
    pass
