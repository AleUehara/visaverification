#!/usr/bin/python
# -*- encoding: utf-8 -*-
#import os

#os.system("manage.py celeryd -v 2 -B -s celery -E -l INFO")

import subprocess
subprocess.Popen("python manage.py celeryd -v 2 -B -s celery -E -l INFO", shell=True)

