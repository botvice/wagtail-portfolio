from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

from wagtail.admin import widgets
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

class ProjectsListingPage(Page):
    parent_page_types = ["home.HomePage"]
    sub_title = models.CharField(
        default="Sub Title",
        max_length=100,
        blank=False,
        help_text='Smaller heading under the main title page. Max 100 words.'
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['projects'] = ProjectsPage.objects.live().public()
        return context

    content_panels = Page.content_panels + [
        FieldPanel("sub_title"),
    ]

class ProjectsPage(Page):
    parent_page_types = ["projects.ProjectsListingPage"]
    summary = models.TextField(
        blank=False,
        max_length=500,
        help_text='Give a brief summary of the project. Additional details may be included in this page further down if necessary.'
    )

    languages_used = models.TextField(
        blank=False,
        max_length=100,
        help_text='List all the languages used seperating by comma and connecting the last language with an "and"'
    )

    project_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='Insert an image to be used for the project. It will be cropped to 570px by 370px',
        related_name="+",
    )

    date_started = models.DateField()

    date_widget = widgets.AdminDateInput(
        attrs = {
            'placeholder': 'dd-mm-yyyy'
        }
    )

    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("text", blocks.TextBlock()),
        ("image", blocks.ImageBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("summary"),
            FieldPanel("languages_used"),
            ImageChooserPanel("project_image"),
            FieldPanel("date_started", widget=date_widget),
        ], heading="standard details"),
        StreamFieldPanel("body"),
    ]
