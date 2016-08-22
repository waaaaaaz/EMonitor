# coding: utf-8

import os
import datetime

from fabric.api import env, put, run

from config.hosts import HOSTS_INFO
from config.env import TARGET_DIR


class Model(object):
	
	def __init__(self, group, job_name):
		self.task_host = self._load_host_config(group)
		self.job_name = job_name

	def task_job(self):
		raise NotImplementedError

	def task_execute(self):
		for host in self.task_host:
			env.warn_only = True
			env.user = host["username"]
			env.password = host["password"]
			env.host_string = host["hostname"]
			self._check_work_dir()
			self._check_work_script(self.job_name)
			self.task_job()

	def _load_host_config(self, group):
		'''filter host by group, "all" as default'''
		hosts = []
		for host in HOSTS_INFO:
			if group in host["groups"]:
				hosts.append(host)
		return hosts

	def _check_work_dir(self):
		'''check remote script folder, if not existed , will creat'''
		result = run('ls {0}'.format(TARGET_DIR))
		if result.failed:
			run("mkdir -p {0}".format(TARGET_DIR))

	def _check_work_script(self, job_name):
		'''check current task script, if not exsited or modified, will update'''
		result = run('stat {0}/{1}.py'.format(TARGET_DIR, job_name))
		if not result.failed:
			put('./script/{0}.py'.format(job_name), TARGET_DIR)
		else:
			modify_time = run('export LC_ALL=C | stat {0}.py | head -6| tail -1'.format(job_name))
			local_script_time = os.path.getmtime('./script/{0}.py'.format(job_name))
			local_modify_time = str(datetime.datetime.fromtimestamp(local_script_time)).split('.')[0]
			if local_modify_time not in modify_time:
				put('./script/{0}.py'.format(job_name), TARGET_DIR)