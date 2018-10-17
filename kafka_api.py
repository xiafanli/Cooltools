#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import kafka
import traceback
from json import dumps
from utils import logger


class SDMSKafka(object):
    def __init__(self, broker_hosts, topic, write_sync):
        self.sync = write_sync
        self.topic = topic
        client = kafka.SimpleClient(hosts=broker_hosts)
        self.producer = kafka.SimpleProducer(client, async=(self.sync==False))

    def send(self, content):
        try:
            self.producer.send_messages(self.topic, dumps(content))

        except Exception:
            logger.error(traceback.format_exc())
            return "-1"
        return "0"
