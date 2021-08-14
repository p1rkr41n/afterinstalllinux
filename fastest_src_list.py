import os
from posix import PRIO_PGRP
import re
from sys import minsize
import time

def cal_time():
    start = time.time()
    os.system("sudo apt install -y mariadb-client")
    timer =time.time() - start
    os.system("sudo apt remove -y mariadb-client")
    os.system("sudo apt -y autoremove")
    return timer
def createsrcfile(path):
    os.system("""echo "deb http://%s kali-last-snapshot main non-free contrib
deb http://%s kali-experimental main non-free contrib
deb http://%s kali-rolling main non-free contrib
deb-src http://%s kali-last-snapshot main non-free contrib
deb-src http://%s kali-experimental main non-free contrib
deb-src http://%s kali-rolling main non-free contrib"| sudo tee /etc/apt/sources.list""" % (path, path, path, path, path, path))

if __name__ == "__main__":
    # List of sources to search for srclst
    urls = ['kali.cs.nctu.edu.tw/kali','ftp.harukasan.org/kali','kali.download/kali','ftp.jaist.ac.jp/pub/Linux/kali','kali.itsec.am/kali','mirror-1.truenetwork.ru/kali','mirror.lagoon.nc/kali','hlzmel.fsmg.org.nz/kali','wlglam.fsmg.org.nz/kali','ftp.acc.umu.se/mirror/kali.org/kali','mirror.karneval.cz/pub/linux/kali','mirror.serverion.com/kali','mirrors.dotsrc.org/kali','mirror.pyratelan.org/kali','ftp.halifax.rwth-aachen.de/kali','ftp2.nluug.nl/os/Linux/distr/kali','ftp1.nluug.nl/os/Linux/distr/kali','mirror.erickochen.nl/kali','mirror.neostrada.nl/kali','archive-4.kali.org/kali','kali.download/kali']
    urls2 = ['ftp.belnet.be/mirror/kali/kali/', 'ftp.free.fr/pub/kali/', 'ftp.cc.uoc.gr/mirrors/linux/kali/kali/', 'kali.koyanet.lv/kali/', 'mirrors.netix.net/kali/', 'mirrors.ocf.berkeley.edu/kali/', 'archive.linux.duke.edu/kalilinux/kali/', 'mirror.cedia.org.ec/kali/', 'ftp.ne.jp/Linux/packages/kali/kali/', 'ftp.riken.jp/Linux/kali/', 'linux3.yz.yamagata-u.ac.jp/pub/Linux/kali/', 'mirror.serverius.net/kali/', 'mirror.ufro.cl/kali/', 'us.mirror.nsec.pt/kali/']
    #Full list of mirror names: (command to not run)
    urls.extend(urls2)
    # Run search:
    os.system("touch sources.list")
    os.system("sudo cp ./sources.list /etc/apt/sources.list")
    url = "ftp.acc.umu.se/mirror/kali.org/kali/" 
    createsrcfile(url)
    result_url= []
    for url in urls:
        result_url.append(str(cal_time())+": "+ url)
    print("=============================================================")
    # print(result_url)
    for line in result_url:
        print(line)
    minsize = str(min(result_url))
    print("This is minimum: " + minsize)
    minsize =  minsize.split(' ')
    # Set sources.list fastest
    createsrcfile(minsize[1])
