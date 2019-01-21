# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


def make_thumbnail(obj):

    THUMB_SIZE = 200, 200
    image_pil = Image.open(obj)
    image_pil.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

    thumb_name, thumb_extension = os.path.splitext(obj.name)
    thumb_extension = thumb_extension.lower()

    thumb_filename = thumb_name + '_thumb' + thumb_extension

    if thumb_extension in ['.jpg', '.jpeg']:
        FTYPE = 'JPEG'
    elif thumb_extension == '.gif':
        FTYPE = 'GIF'
    elif thumb_extension == '.png':
        FTYPE = 'PNG'
    else:
        return None    # Unrecognized file type

    # Save thumbnail to in-memory file as StringIO
    temp_thumb = BytesIO()
    image_pil.save(temp_thumb, FTYPE)
    temp_thumb.seek(0)

    response = ContentFile(temp_thumb.read())
    response.name = thumb_filename
    temp_thumb.close()

    return response
