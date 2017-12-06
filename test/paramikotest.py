import paramiko
import uuid

# # based on username and password
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect("10.0.0.3",1212,"oldboy","123456")
# stin,stout,stderr = ssh.exec_command("df -h")
# for item in stderr:
#     print(item)
# for item in stout:
#     print(item)
# ssh.close()



# # based on public key
# pravite = paramiko.RSAKey.from_private_key_file("D:/New folder/id_rsa")
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname="10.0.0.3",port=1212,username="oldboy",pkey=pravite)
# stin,stout,stderr = ssh.exec_command("df -h")
# for item in stderr:
#     print(item)
# for item in stout:
#     print(item)
# ssh.close()


# file transfer based on user and password
ssh = paramiko.Transport(('10.0.0.3',1212))
ssh.connect(username='oldboy',password='123456')
sftp = paramiko.SFTPClient.from_transport(ssh)
sftp.put('D:/New folder/oldboy.txt','/tmp/from_windows')
ssh.close()
