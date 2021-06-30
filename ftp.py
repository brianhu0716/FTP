import os
from os.path import isfile, isdir, join, dirname

os.chdir('C:\\Users\\Brian Hu\\Desktop\\temp_folder')
local_path = os.getcwd()

from ftplib import FTP
ftp = FTP()
ftp.connect(host='ftp.dlptest.com', timeout=30)
ftp.login(user='dlpuser', passwd='rNrKYTX9g7z3RgJRmxWuGHbeu')
ftp_path = ftp.cwd()

def dfs(local_path, ftp_path):
    for filename in os.listdir(local_path):
        if isdir(join(local_path, filename)):
            ftp.mkd(filename)
            ftp.cwd(join(ftp_path, filename))
            local_path = join(local_path, filename)
            dfs(local_path)
            local_path = dirname(local_path)
            ftp.cwd('../')
        with open(filename, 'rb') as file:
            ftp.storbinary('STOR ' + filename, file)
dfs(local_path, ftp_path)
        
            