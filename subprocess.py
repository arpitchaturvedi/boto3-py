#Python subprocess module
# sp = subprocess.Popen(command, shell=True/False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newline=True)
#subprocess.Popen() -->
#shell=True/False avoid shell=True
#python --> shell=True -->fork --> shell(syntax or semantics) \ "
#depending on shell for some output like on env_variable in this we haveto use SHELL=true, otherwise always False
import subprocess
command=["ls","-l"]
sp = subprocess.Popen(command,shell=True,)
rt=sp.wait()
out,err=sp.communicate()
print(out)
print(err)

