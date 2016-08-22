# coding: utf-8

import logging
import os
import time

from apscheduler.schedulers.background import BackgroundScheduler

from task import TaskDiskCheck, TaskMemCheck

class Schedule(object):
    def __init__(self):
       self.scheduler = BackgroundScheduler()
       self.scheduler.add_job(TaskMemCheck('all', 'memory_check').task_execute, 'interval', seconds=3)
       self.scheduler.add_job(TaskDiskCheck('all', 'disk_check').task_execute, 'interval', seconds=5)
       self.scheduler.print_jobs()

    def start(self):
       self.scheduler.start()

    def shutdown(self):
    	self.scheduler.shutdown()


if __name__ == '__main__':
	logging.basicConfig()
	Schedule().start()
	try:
		while True:
			time.sleep(2)
	except (KeyboardInterrupt, SystemExit):
		Schedule().shutdown()

