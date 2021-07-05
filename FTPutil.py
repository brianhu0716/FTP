# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 09:35:05 2021

@author: Brian Hu
"""

import ftputil
import os
class FTPtransmit():
    def __init__(server, user, password):
        self.host = ftputil.FTPHost(server, user, password)
    def uploadFile(source, target, filename):
                    
        os.chdir(source)
        self.host.chdir(target)
        if os.path.isdir(os.curdir):
            fname = os.path.basename(os.path.curdir)
            self.host.mkdir(fname)
            self.host.chdir(self.host.join(self.host.curdir, fname))
            Upload()
        else:
            self.host.upload(source, target)
        
    def downloadFile(source, target, filename):
        def Download():
            for filename in host.listdir(host.curdir):
                if host.path.isdir(host.path.join(host.curdir, filename)):
                    os.mkdir(filename)
                    os.chdir(os.path.join(os.curdir, filename))
                    host.chdir(host.path.join(host.curdir, filename))
                    Download()
                    os.chdir('../')
                    host.chdir('../')
                else:
                    host.download(filename, filename)