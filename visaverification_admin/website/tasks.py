from celery.task import task

import re
import urllib2

#A sample
def access_site():
  cartao = 4058781520152016
  html = urllib2.urlopen("http://www.cbss.com.br/inst/convivencia/SaldoExtrato.jsp?numeroCartao=%s&primeiroAcesso=S" %cartao).read()
  patt = re.compile("R\$\s\d+\,\d+")
  value = patt.findall(html)[0].replace("R$", "").replace(",", ".")
  return float(value)


@task()
def find_site():

  #SELECT to find sites
  
  print "Finding site"
  value = access_site()
  if value > 200:
  	print "High Value"
  else:
    print "Low Value"
  return True
