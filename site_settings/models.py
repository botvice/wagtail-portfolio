from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel

@register_setting
class SocialMediaSettings(BaseSetting):

    linkedin = models.URLField(
        blank=True,
        help_text='Enter your LinkedIn url'    
    )

    github = models.URLField(
        blank=True,
        help_text='Enter your Github url'
    )

    resume = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel("linkedin"),
        FieldPanel("github"),
        DocumentChooserPanel("resume"),
    ]

    


    