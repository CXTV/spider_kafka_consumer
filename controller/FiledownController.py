# -*- coding: utf-8 -*-
import redis, os, contextlib, urllib2

from Controller import Controller
from model.crawl_image_map import CrawlImageMap
import json, requests, re, logging

class FiledownController(Controller):
    def __init__(self, topic="downfile_queue"):
        super(FiledownController, self).__init__(topic, 'filedown')

    def run(self):
        for message in self.consumer:
            if message is not None:
                file = message.value
                if file is None:
                    continue

                fileinfo = file.split('_____')
                file_url = fileinfo[0]
                file_save_path = fileinfo[1]

                image_map = CrawlImageMap(img_path=file_save_path, real_path=file_url)
                with self.session_scope(self.sess) as session:
                    session.add(image_map)