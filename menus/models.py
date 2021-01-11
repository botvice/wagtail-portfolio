from django.db import models

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from django_extensions.db.fields import AutoSlugField

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.core.models import Orderable

class MenuItem(Orderable):
    link_title = models.CharField(blank=True, max_length=25)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
    )

    panels = [
        FieldPanel("link_title"),
        PageChooserPanel("link_page"),
    ]

    page = ParentalKey("Menu", related_name="menu_items")

class Menu(ClusterableModel):

    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        InlinePanel("menu_items", label="Menu Item"),
    ]

    def __str__(self):
        return self.title