"""
 Global utils
"""
import binascii
import os


from django.template.defaultfilters import slugify


def generate_unique_slug(model, field):
    """ Generate unique string """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug


def generate_token(length):
    """ generate token key """
    return binascii.hexlify(os.urandom(length)).decode()
