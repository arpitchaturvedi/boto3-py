import re
logfile="/var/log/apache2/access.log.1"
logregex="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
with open(logfile) as f:
    log = f.read()
    print(log)
ip_list= re.findall(logregex,log)
print(ip_list)
