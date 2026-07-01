from importlib.metadata import PackageNotFoundError, version

import django

from django.utils.module_loading import autodiscover_modules

from .documents import Document  # noqa
from .indices import Index  # noqa
from .fields import *  # noqa

try:
    __version__ = version("django-elasticsearch-dsl")
except PackageNotFoundError:
    __version__ = "0.0.0"


def autodiscover():
    autodiscover_modules('documents')


