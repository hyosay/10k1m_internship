import cv2
import os
import urllib.request
import CBImage


# 파일이 존재하는지 확인
def check_file_exists(file_path):
    return os.path.exists(file_path) and os.path.isfile(file_path)

videoLink = ""
## your cb video download link
cbVideo = "/Users/jeonhyoseong/Tagging_system/cBlock"
## image write link
outDir = "/Users/jeonhyoseong/Tagging_system/CBImageGroup"



for i in range(634):

    videoLink = cbVideo + "/CB"+ "{}".format(i).zfill(3) + ".mp4"
    if check_file_exists(videoLink):
        os.mkdir(outDir + "/number{}".format(i))
        save_path = outDir + "/number{}".format(i)
        CBImage.CBImageDownload(videoLink, save_path)
    videoLink = ""
    print("success:" + str(i))
