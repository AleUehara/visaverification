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
  

kill_celery()
kill_celery()
