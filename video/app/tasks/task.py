# #coding=utf-8
# import os
# # from celery.app import task
# from app.libis.base_qiniu import video_qiniu
# from app.models import Video, VideoSub
#
# # @task
# def video_task(command, out_path, path_name, video_file_name, video_sub_id):
#     from app.utils.common import remove_path
#
#
#     os.system(command)
#
#     out_name = '.'.join([out_path, 'mp4'])
#     if not os.path.exists(out_name):
#         remove_path([out_name, path_name])
#         return False
#
#     url = video_qiniu.put(video_file_name, out_name)
#
#     if url:
#         try:
#             video_sub = VideoSub.objects.get(video_sub_id)
#             video_sub.url = url
#             video_sub.save()
#             return True
#         except:
#             return False
#         finally:
#             remove_path([out_name, path_name])
#     remove_path([out_name, path_name])