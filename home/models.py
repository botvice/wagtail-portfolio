from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

class HomePage(Page):

    sub_heading = models.CharField(
        max_length=140, 
        blank=True, 
        help_text='Subheading text under the banner title',
    )

    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='The banner background image',
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("sub_heading"),
            ImageChooserPanel("banner_background_image"),
        ], heading="homepage banner"),
        #StreamFieldPanel("body"),
    ]