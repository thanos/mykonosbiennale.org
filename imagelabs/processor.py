# encoding: utf-8
import json, os
import requests
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from StringIO import StringIO
from urlparse import urlparse
from pilkit.lib import Image, ImageDraw
from pilkit.processors import (Resize, ResizeToFill, ResizeToFit, SmartCrop,
                               SmartResize, MakeOpaque)
from pilkit.utils import  (extension_to_format, format_to_extension, FileWrapper,
                          save_image, prepare_image, quiet)
from django.conf import settings
import requests
from urlparse import urlparse 
from models import ProcessedImage
    
def process(image_url,  processor = None, width=None, height=None, resolution=None, quality=100):
    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME) 
    if image_url[0] =='/': image_url = image_url[1:] 
    r = requests.get(image_url.replace('https', 'http'))
    img = Image.open(StringIO(r.content))
    processor = ResizeToFit(width, height)
    new_img = processor.process(img)
    new_file = StringIO()
    save_image(new_img, new_file, 'JPEG')
    new_k = Key(bucket)
    parts = urlparse(image_url)
    img_name = os.path.splitext(os.path.basename(parts.path))[0]
    new_k.key = 'il/{}x{}/{}.jpeg'.format(width, height, img_name)
    new_k.content_type = 'image/jpeg'
    new_k.set_contents_from_file(new_file, policy='public-read')
    new_image_url = new_k.generate_url(0, query_auth=False, force_http=True)
    processed_image,_ = ProcessedImage.objects.update_or_create(source_image = image_url, processed_image = new_image_url)
    return processed_image
    
    