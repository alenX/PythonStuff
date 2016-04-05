import os,os.path
import re
log_path = 'D:\SProgram'
re_pre = '^apache-tomcat-(\w+)'
# for root,dirs,dd in os.walk(log_path):
#     for d in dirs:
#         print(d)
tomcat_dir = []
for i in os.listdir(log_path):
    if re.match(re_pre,i) is not None:
        tomcat_dir.append(i)
for i in tomcat_dir:
    logs = log_path+'\\'+i+'\\logs'
    for root,dirs,files in os.walk(logs,topdown=False):
        for f in files:
            if os.path.getsize(os.path.join(root,f))==0 or True:
                try:
                    os.remove(os.path.join(root,f))
                except PermissionError:
                    print('文件'+os.path.join(root,f)+'正在被使用!')
