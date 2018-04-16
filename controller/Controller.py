# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from kafka import KafkaConsumer
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from model.util import db_connect, create_news_table
import settings

@contextmanager
def session_scope(session):
    sess = session()
    try:
        yield sess
        sess.commit()
    except:
        sess.rollback()
        raise
    finally:
        sess.close()

class Controller(object):
    def __init__(self, topic):
        engine = db_connect()
        create_news_table(engine)
        self.sess = sessionmaker(bind=engine)
        self.server = settings.kafka
        self.session_scope = session_scope
        self.post_sn_url = settings.post_address
        self.token = '9286168e06a110cd374caa0f67f08199'

        if topic:
            self.consumer = KafkaConsumer(topic, bootstrap_servers=self.server['host'], group_id='spider', auto_offset_reset="earliest")
