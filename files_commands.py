from subprocess import Popen, PIPE
import os
def get_files():
  list = Popen(('ls','files_created'), stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,list)

def remove_all_files():
  execute = 'find /home/filesystem_user -type f -maxdepth 1 -not -name ".*" -exec rm {} \;'  	
  process = Popen(execute, universal_newlines=True, stdout=PIPE, stderr=PIPE, shell=True).communicate()
  return True

def get_files_recent():
  list = Popen(('ls','files_created','-t'), stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,list)
