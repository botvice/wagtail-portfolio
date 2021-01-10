from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleBlock(blocks.StructBlock):

    class Meta:
        template = "streams/title_block.html"
        icon = "title"
        label = "Title"
        help_text = "Text to be used as a sub header"

    text = blocks.CharBlock(
        required=False,
    )

class TextBlock(blocks.StructBlock):

    class Meta:
        template = "streams/text_block.html"
        icon = "edit"
        label = "Text Box"
        help_text = "Text to be used as regular text"

    text = blocks.RichTextBlock(
        required=False,
    )

class ImageBlock(blocks.StructBlock):

    class Meta:
        template = "streams/image_block.html"
        icon = "image"
        label = "Image"
        help_text = "Choose an image to be displayed"

    image = ImageChooserBlock()

