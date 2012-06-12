#!/usr/bin/python
# -*- encoding: utf-8 -*-
import subprocess
import os

def execute_shell(command):
  subprocess.call(command, shell=True)

def kill_celery():
  values = subprocess.Popen(['ps', '-ef'], stdout=subprocess.PIPE).communicate()[0]
  for value in values.split('\n'):
    if value.endswith('python manage.py celeryd -v 2 -B -s celery -E -l INFO'):
      job_id =  value.split('   ')[1]
      execute_shell('kill -9 ' + str(job_id))
      print "kill:"+job_id
  


def kill_celery():
	#sudo kill  `ps -ef | grep -i 'projeto_django/manage.py celeryd' | grep -v grep | awk '{print $2}'`
	execute_shell('sudo kill  `ps -ef | grep -i \'projeto_django/manage.py celeryd\' | grep -v grep | awk \'{print $2}\'`')
#kill_celery()
#kill_celery()

kill_celery()
