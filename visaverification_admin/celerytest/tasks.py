from celery.task import task

@task()
def Test():
  print "This is a task"
  return True