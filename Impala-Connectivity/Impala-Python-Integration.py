# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:49:31 2019

@author: CON031
"""

#!pip install ibis
#!pip install ibis-framework[impala]
#!pip install ibis-framework
#!pip install ibis-framework[kerberos]
#!pip install pyhive
#!pip install sasl
#!wget https://www.lfd.uci.edu/~gohlke/pythonlibs/#sasl
#!pip install sasl-0.2.1-cp36-cp36m-win_amd64.whl
#!pip install sql
#!pip install ipython-sql
#!conda install -c conda-forge ipython-sql=0.3.6
#!pip install config


#import ibis as ibis
import pandas as pd
from impala.dbapi import connect
#import os

#hdfs = ibis.hdfs_connect(host=os.environ['192.168.101.41'], port=50070)
#client = ibis.impala.api.connect(host='192.168.101.41', port=21050)
#hdfs = ibis.hdfs_connect(host='192.168.101.41', port=50070)


#import hive from pyhive
#from pyhive import hive

#establish the connection to the db
#conn = hive.Connection(host='192.168.101.41', port='21050', auth='CUSTOM', database='employee', username='hue', password='hue')

#prepare the cursor for the queries
#cursor = conn.cursor()

#execute a query
#cursor.execute("SHOW TABLES")

#navigate and display the results 
#for table in cursor.fetchall():
#   print(table)

conn = connect(host='192.168.101.41', port=21050)

cur = conn.cursor()

cur.execute('select * from employee.employee_details limit 2')

results = cur.fetchall()

print(results)

#cur = conn.cursor()

#cur.execute('select * from employee.employee_details')

#from impala.util import as_pandas
#df = as_pandas(cur)

#df.head()


#cur = conn.cursor()
#cur.execute('select name, salary from employee.employee_details')
#df = as_pandas(cur)

#import matplotlib
#%matplotlib inline

#matplotlib.style.use('ggplot')

#df.plot()

