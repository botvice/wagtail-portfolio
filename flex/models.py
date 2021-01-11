from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from streams import blocks

class FlexPage(Page):

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    parent_page_types = ["home.HomePage", "flex.FlexPage"]

    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("text", blocks.TextBlock()),
        ("image", blocks.ImageBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]
