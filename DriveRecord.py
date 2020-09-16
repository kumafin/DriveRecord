#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import picamera
import time
import sys
import datetime
from operator import itemgetter


FILEPATH = '/home/pi/Videos/' # 保存先
MOVIE_INTERVAL = 5 # 撮影時間
MAXFILE = 5
filelists = [MAXFILE] # リスト定義
now = datetime.datetime.now()
count = 0


def main():
    filename = FILEPATH + now.strftime('%Y%m%d_%H%M%S') + '.h264'
    #filename = FILEPATH + 'test.h264'
    with picamera.PiCamera() as camera:   # PiCameraクラスのインスタンス生成
        camera.hflip = True                      # 上下反転
        camera.vflip = True                      # 左右反転
        camera.resolution = (1024,768)           # 解像度 (最大2590*1944)
        camera.brightness = 70                   # 明るさ設定 デフォルト:50
        time.sleep(2)                            # カメラが落ち着く時間
        camera.start_recording(filename)         # filenameのファイル名で録画開始
        camera.wait_recording(MOVIE_INTERVAL)    # MOVIE_INTERVAL秒の録画
        camera.stop_recording()                  # 録画停止

if __name__ == '__main__':
    while(True):
        main()


#        #### ファイルがMAXFILE個以上になったら古いデータを自動削除 ####
#        for file in os.listdir(FILEPATH):  # os.listdir(path)：path内のフォルダやリストを返す
#            base, ext = os.path.splitext(file)    # os.pah.splitext(path)：pathを拡張子(ext)と拡張子以外(base)に分ける。
#            if ext == '.h264':
#                filelists.append([file, os.path.getctime(file)]) # リスト.append：リストに要素を追加 
#        print(filelists)
#        filelists.sort() 
#        # リスト.sort(key=itemgetter(インデックス), reverse=True)：インデックスはリストの何番目の要素をソートの基準にするか reverse：昇順か降順か
#
#        for i, file in enumerate(filelists):
#            if i > MAXFILE - 1:
#                os.remove(file[0])

