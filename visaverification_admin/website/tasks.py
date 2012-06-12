from celery.task import task
from website.models import Site

import re
import urllib2

#A sample
def access_site(url):
  cartao = 4058781520152016
  html = urllib2.urlopen("%s%s&primeiroAcesso=S" % (url ,cartao) ).read()
  patt = re.compile("R\$\s\d+\,\d+")
  value = patt.findall(html)[0].replace("R$", "").replace(",", ".")
  return float(value)


@task()
def find_site():

  #SELECT to find sites
  sites = Site.objects.all()
  for site in sites:
    print "Finding site"
    value = access_site(site.url)
    if value > 200:
  	  print "High Value"
  	  print site.corporate_email
    else:
      print "Low Value"
  return True
