import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.0.0.3",1212,'oldboy','123456')
stin,stdout,sterr = ssh.exec_command("df -h")
for i in stdout:
    print(i)
ssh.close()