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

    def isdir(self, name):
        if not name:  # Empty name is a directory
            return True

        if self.isfile(name):
            return False

        for item in super(StaticStorage, self).listdir(name):
            if len(item):
                return True

        return False

    def isfile(self, name):
        try:
            name = self._normalize_name(self._clean_name(name))
            f = S3Boto3StorageFile(name, 'rb', self)
            if "directory" in f.obj.content_type:
                return False
            return True
        except Exception:
            return False

    def makedirs(self, name):
        name = self._normalize_name(self._clean_name(name))
        return self.bucket.meta.client.put_object(Bucket=self.bucket.name, Key=f'{name}/')

    def rmtree(self, name):
        name = self._normalize_name(self._clean_name(name))
        delete_objects = [{'Key': f"{name}/"}]

        dirlist = self.listdir(self._encode_name(name))
        for item in dirlist:
            for obj in item:
                obj_name = f"{name}/{obj}"
                if self.isdir(obj_name):
                    obj_name = f"{obj_name}/"
                delete_objects.append({'Key': obj_name})
        self.bucket.delete_objects(Delete={'Objects': delete_objects})

    def path(self, name):
        return name

    def listdir(self, name):
        directories, files = super().listdir(name)
        if '.' in files:
            files.remove('.')
        return directories, files

    def exists(self, name):
        if self.isdir(name):
            return True
        else:
            return super().exists(name)

    def get_modified_time(self, name):
        # S3 boto3 library requires that directorys have the trailing slash
        if self.isdir(name):
            name = f'{name}/'
        return super().get_modified_time(name)

    def size(self, name):
        # S3 boto3 library requires that directorys have the trailing slash
        if self.isdir(name):
            name = f'{name}/'
        return super().size(name)


class PublicMediaStorage(S3Boto3Storage):
    """ Settings for media files """
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False

    def isdir(self, name):
        if not name:  # Empty name is a directory
            return True

        if self.isfile(name):
            return False

        for item in super(PublicMediaStorage, self).listdir(name):
            if len(item):
                return True

        return False

    def isfile(self, name):
        try:
            name = self._normalize_name(self._clean_name(name))
            f = S3Boto3StorageFile(name, 'rb', self)
            if "directory" in f.obj.content_type:
                return False
            return True
        except Exception:
            return False

    def makedirs(self, name):
        name = self._normalize_name(self._clean_name(name))
        return self.bucket.meta.client.put_object(Bucket=self.bucket.name, Key=f'{name}/')

    def rmtree(self, name):
        name = self._normalize_name(self._clean_name(name))
        delete_objects = [{'Key': f"{name}/"}]

        dirlist = self.listdir(self._encode_name(name))
        for item in dirlist:
            for obj in item:
                obj_name = f"{name}/{obj}"
                if self.isdir(obj_name):
                    obj_name = f"{obj_name}/"
                delete_objects.append({'Key': obj_name})
        self.bucket.delete_objects(Delete={'Objects': delete_objects})

    def path(self, name):
        return name

    def listdir(self, name):
        directories, files = super().listdir(name)
        if '.' in files:
            files.remove('.')
        return directories, files

    def exists(self, name):
        if self.isdir(name):
            return True
        else:
            return super().exists(name)

    def get_modified_time(self, name):
        # S3 boto3 library requires that directorys have the trailing slash
        if self.isdir(name):
            name = f'{name}/'
        return super().get_modified_time(name)

    def size(self, name):
        # S3 boto3 library requires that directorys have the trailing slash
        if self.isdir(name):
            name = f'{name}/'
        return super().size(name)
