import os, sys
folders = os.listdir(sys.path[0])
direcs = {}
for folder in folders:
    if folder == 'tools':
        continue
    File, ext = os.path.splitext(folder)
    if ext == '':
        for dep in os.listdir(File):
            if dep == 'BUILD.py':
                continue
            File, ext = os.path.splitext(dep)
            if ext == '.py':
                direcs[File] = sys.path[0] + '/' + folder
f = open('DEPS.BUILD','w')
for dep in direcs:
    f.write(dep + '=' + direcs[dep] + '\n')
