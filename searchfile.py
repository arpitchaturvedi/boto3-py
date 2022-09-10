from this import d
from paramiko import HostKeys
import os
import datetime
currentdate= datetime.datetime.now()
# for dirname, dirpath, filename in os.walk("/var/www/html"):
#     print(dirname)
#     print(filename)
#     print(dirpath)
max_age=10
for dirpath,dirname,filename in os.walk("/ansible"):
    for file in filename:
        comp_path = os.path.join(dirpath,file)
        file_stat=os.stat(comp_path)
        #print(file_stat)
        file_ctime=file_stat.st_ctime        
        filecreation_date= datetime.datetime.fromtimestamp(file_ctime)
        #print(filecreation_date)

        diff_in_days=currentdate - filecreation_date
        print(diff_in_days)