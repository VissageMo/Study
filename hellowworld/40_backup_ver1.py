import os
import time

source = ['Users/mowenhao/PycharmProjects']  # 需备份文件所在地址

target_dir = 'Users/mowenhao/backup'  # 生成的备份文件存放地址

target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backuo to', target)
else:
    print('Backup FAILED')