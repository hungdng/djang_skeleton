# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path
import datetime
import random
import string

DEFAULT_CHAR_STRING = string.ascii_lowercase + string.digits


def generate_random_string(chars=DEFAULT_CHAR_STRING, size=6):
    return ''.join(random.choice(chars) for _ in range(size))


def rename_file_with_date_time(obj):
    image_name_str, image_extension = os.path.splitext(obj.name)
    image_extension = image_extension.lower()

    filename_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
    image_name_str = image_name_str + '_' + filename_datetime

    return image_name_str + image_extension
