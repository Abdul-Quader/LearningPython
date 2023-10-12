import subprocess
# command = ["dir","/B"]
command = "$env:SHELL"
# command = "Get-Process -Name powershell"
sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rt=sp.wait()
out, err = sp.communicate()
print(out)
print(err)