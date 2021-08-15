import time
import os

# Checking fastest connection but not full of database
def timers(path):
    urlfix = path.split('/')[0]
    start = time.time()
    os.system("sudo timeout 7 nc -vz "+urlfix+" 80 ")
    os.system("sudo timeout 7 wget "+path)
    return (time.time()-start)

if __name__ == "__main__":
    timelist = []
    urls = ['ftp.harukasan.org/kali','kali.download/kali','ftp.jaist.ac.jp/pub/Linux/kali','kali.itsec.am/kali','mirror-1.truenetwork.ru/kali','mirror.lagoon.nc/kali','hlzmel.fsmg.org.nz/kali','wlglam.fsmg.org.nz/kali','ftp.acc.umu.se/mirror/kali.org/kali','mirror.karneval.cz/pub/linux/kali','mirror.serverion.com/kali','mirrors.dotsrc.org/kali','mirror.pyratelan.org/kali','ftp.halifax.rwth-aachen.de/kali','ftp2.nluug.nl/os/Linux/distr/kali','ftp1.nluug.nl/os/Linux/distr/kali','mirror.erickochen.nl/kali','mirror.neostrada.nl/kali','archive-4.kali.org/kali']
    urls2 = ['ftp.belnet.be/mirror/kali/kali', 'ftp.free.fr/pub/kali', 'ftp.cc.uoc.gr/mirrors/linux/kali/kali', 'kali.koyanet.lv/kali', 'mirrors.netix.net/kali', 'mirrors.ocf.berkeley.edu/kali', 'archive.linux.duke.edu/kalilinux/kali', 'mirror.cedia.org.ec/kali', 'ftp.ne.jp/Linux/packages/kali/kali', 'ftp.riken.jp/Linux/kali', 'linux3.yz.yamagata-u.ac.jp/pub/Linux/kali', 'mirror.serverius.net/kali', 'mirror.ufro.cl/kali', 'us.mirror.nsec.pt/kali']
    urls2.extend(urls)
    for url in urls2:
        temp = timers(url)
        timelist.append(temp)
        print(temp)
    temp = urls2[timelist.index(min(timelist))]
    print( temp )
    os.system("sudo rm kali.*")
    os.system("sudo rm wget-log*")
    os.system("sudo rm kali")
