# coding: utf-8

import ast

from fabric.api import env, put, run

from model import Model
from mail import send
from config.mails import MAIL_INFO


class TaskDiskCheck(Model):

	def task_job(self):
		result = run('python /app/EMonitor/Script/disk_check.py')
		for filesystem, usage in ast.literal_eval(result).items():
			if int(usage.rstrip("%")) > 95:
				send(_mail_info())

	def _mail_info(self):
		MAIL_INFO['mail_subject'] = "Warning from {0}".format(self.__class__.__name__)
		MAIL_INFO['mail_text'] = "Host: {0}\n\rResult: {1}".format(env.host_string.split(":")[0], result)
		return MAIL_INFO



class TaskMemCheck(Model):

	def task_job(self):
		result = run('python /app/EMonitor/Script/memory_check.py')
		if int(result.split('%')[0].strip().split('.')[0]) < 5:
			send(_mail_info())
			
	def _mail_info(self):
		MAIL_INFO['mail_subject'] = "Warning from {0}".format(self.__class__.__name__)
		MAIL_INFO['mail_text'] = "Host: {0}\n\rResult: {1}".format(env.host_string.split(":")[0], result)
		return MAIL_INFO





