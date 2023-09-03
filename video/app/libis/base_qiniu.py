#coding=utf-8
import time
from qiniu import Auth, put_data, put_file
from django.conf import settings

class Qiniu(object):

    def __init__(self, bucket_name, base_url):
        self.bucket_name = bucket_name
        self.base_url = base_url
        self.q = Auth(settings.QINIU_AK, settings.QINIU_SK)

    def put(self, name, path):
        token = self.q.upload_token(self.bucket_name, name)
        ret, info = put_file(token, name, path)
        mid_url = 'http://' + self.base_url
        # out_name = '_'.join([str(time.time()), ret['key']])

        if 'key' in ret:
            remote_url = '/'.join([mid_url, ret['key']])
            return remote_url
video_qiniu = Qiniu(
    bucket_name=settings.QINIU_VIDEO,
    base_url=settings.QINIU_VIDEO_URL)