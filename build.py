import argparse
import codecs
import os
import re
import platform
import subprocess
import shutil


__version__ = '1.0'


title_re = re.compile('^\s*\[title\]:\s*#\s*\((.*)\)\s*$')


def mkmds(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    copdirs(src, dest)
    mkmd(src, dest)


def copdirs(src, dest):
    for root, dirs, files in os.walk(src):
        if os.path.basename(root).startswith('__'):
            continue
        newdir = os.path.join(root.replace(src, dest))
        if newdir == dest:
            continue
        if not os.path.exists(newdir):
            os.mkdir(newdir)


def mkmd(src, dest):
    for root, dirs, files in os.walk(src):
        newdir = os.path.join(root.replace(src, dest))
        for filename in files:
            if filename.startswith('__') or not filename.endswith('.py'):
                continue
            name, _ = os.path.splitext(filename)
            ext = '.md'
            with codecs.open(os.path.join(root, filename), 'r', encoding='utf-8') as sourcefile:
                newfilepath = os.path.join(newdir, (name + ext))
                with codecs.open(newfilepath, 'w', encoding='utf-8') as destfile:
                    txt = sourcefile.read()
                    towrite = txt.replace('"""', '')
                    destfile.write(towrite)


def mkyml(dest, mkdocsyml):
    yml = (
        "site_name: База знаний Python\n"
        "theme: readthedocs\n"
        "docs_dir: mds\n"
        "site_dir: docs\n"
        "pages:\n"
        "    - Привет: 'index.md'\n"
    )
    for root, dirs, files in os.walk(dest):
        for filename in files:
            if not filename.endswith('.md'):
                continue
            splitted = os.path.normpath(root).split(os.path.sep)[1:]
            if splitted:
                path = os.path.join(*splitted)
                title, y = yamlpage(os.path.join(root, filename), os.path.join(path, filename))
                if title:
                    yml += '{}\n'.format(y)

    with codecs.open(mkdocsyml, 'w', encoding='utf-8') as file:
        file.write(yml)


def yamlpage(filepath, value):
    title = ''
    with open(filepath, 'r') as file:
        for i, line in enumerate(file.readlines()):
            match = title_re.match(line)
            if match:
                title = match.group(1)
            if i > 10:
                break
    return title, "    - {}: '{}'".format(title, value)


def pycharm():
    if '64bit' in platform.architecture():
        pycharm_exe = 'pycharm64.exe'
    else:
        pycharm_exe = 'pycharm.exe'

    pf_dir = ''
    if os.path.isdir('C:\Program Files (x86)\JetBrains'):
        pf_dir = 'C:\Program Files (x86)\JetBrains'

    # более приоритетный путь в сравнении с (x86)
    if os.path.isdir('C:\Program Files\JetBrains'):
        pf_dir = 'C:\Program Files\JetBrains'

    latest_pycharm = ''
    if pf_dir:
        max_ctime = 0
        for r, d, f in os.walk(pf_dir):
            for file in f:
                if file == pycharm_exe:
                    file_path = r'{}\{}'.format(r, file)
                    if os.path.getctime(file_path) > max_ctime:
                        latest_pycharm = file_path
    return latest_pycharm


def diff(path1, path2):
    pycharm_path = pycharm()
    if pycharm_path:
        diff_args = r'"{}" diff {} {}'.format(pycharm_path, path1, path2)
        subprocess.call(diff_args)


def creadate(filepath):
    if platform.system() == 'Windows':
        return os.path.getctime(filepath)
    stat = os.stat(filepath)
    try:
        return stat.st_birthtime
    except AttributeError:
        return stat.st_mtime


def delmds(dest, mkdocsyml):
    if os.path.exists(mkdocsyml):
        os.remove(mkdocsyml)
    if os.path.exists(dest):
        shutil.rmtree(dest)


if __name__ == '__main__':
    src = 'source'
    dest = 'mds'
    mkdocsyml = os.path.join('.', 'mkdocs.yml')

    parser = argparse.ArgumentParser()
    parser.add_argument('-md', action='store_true')
    parser.add_argument('-rm', action='store_true')
    args = parser.parse_args()

    if args.md:
        delmds(dest, mkdocsyml)
        mkmds(src, dest)
        mkyml(dest, mkdocsyml)

    elif args.rm:
        delmds(dest, mkdocsyml)

    else:
        subprocess.call('mkdocs build', shell=True)
        subprocess.call('mkdocs serve', shell=True)
