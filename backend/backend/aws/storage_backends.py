# pylint: disable=W0223
""" Settings for s3 storage """
import os
from django.conf import settings
from storages.utils import setting
from urllib.parse import urljoin
from storages.backends.s3boto3 import S3Boto3Storage, S3Boto3StorageFile


class StaticStorage(S3Boto3Storage):
    """ Settings for static files """
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    """ Settings for media files """
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
