import datetime
import os
import base64
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile


fss_share = FileSystemStorage(location=settings.SHARE_DATA)


def save_image(filename, datainbase64):
        imgdata = base64.b64decode(datainbase64)
        return fss_share.save(filename, ContentFile(imgdata))


def generate_img_path(instance, filename):
    print('generate_video_path')
    a = filename.split('.')
    ext = a[-1] if len(a) > 1 else 'mp4'
    today = datetime.date.today()
    path = os.path.join(settings.VIDEO_ASSETS_PATH, today.isoformat(), '%s.%s' % (instance.id, ext))
    instance.path = os.path.join(settings.SHARE_DATA, path)
    return instance.path
