# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import time,traceback
import re
import sys, os
import csv
import pprint
import optparse


from django.core.management.base import BaseCommand
from django.conf import settings

from django.utils.text import slugify

from filmfestival.models import Film

import boto

def copy_object(src_bucket_name,
                src_key_name,
                dst_bucket_name,
                dst_key_name,
                metadata=None,
                preserve_acl=True):
    """
    Copy an existing object to another location.

    src_bucket_name   Bucket containing the existing object.
    src_key_name      Name of the existing object.
    dst_bucket_name   Bucket to which the object is being copied.
    dst_key_name      The name of the new object.
    metadata          A dict containing new metadata that you want
                      to associate with this object.  If this is None
                      the metadata of the original object will be
                      copied to the new object.
    preserve_acl      If True, the ACL from the original object
                      will be copied to the new object.  If False
                      the new object will have the default ACL.
    """
    s3 = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    bucket = s3.lookup(src_bucket_name)

    # Lookup the existing object in S3
    key = bucket.lookup(src_key_name)

    # Copy the key back on to itself, with new metadata
    return key.copy(dst_bucket_name, dst_key_name,
                    metadata=metadata, preserve_acl=preserve_acl)





class Command(BaseCommand):
    help = '''Generate a `admin.py` file for the given app (models)'''

    def handle(self, *args, **kwargs):
        print time.ctime(), args, kwargs
        s3 = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        src_bucket_name =  'org.mykonosbiennale.2015'
        src_bucket = s3.get_bucket('com.mykonosbiennale.static')
        for key in src_bucket.list():
            if key.key.startswith('trailers/'):
                name = os.path.basename(key.key)
                name, ext = os.path.splitext(name)
                #key =  copy_object(src_bucket_name, key.key, 'com.mykonosbiennale.static', 'trailers/'+slugify(name)+ext)
                key =  copy_object('com.mykonosbiennale.static', key.key, 'com.mykonosbiennale.static', 'trailers/'+slugify(name)+ext)
                key.set_acl('public-read')
                print 'http://s3.amazonaws.com/com.mykonosbiennale.static/' + key.key