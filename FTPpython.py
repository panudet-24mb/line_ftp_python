from ftplib import FTP
from time import sleep
from line_notify import LineNotify
ACCESS_TOKEN = "your token"
notify = LineNotify(ACCESS_TOKEN)

ftp = FTP('localhost')
ftp.login('root','1234')

def changemon(dir='./'):
    ls_prev = set()

    while True:
        ls = set(ftp.nlst(dir))

        add, rem = ls-ls_prev, ls_prev-ls
        if add or rem: yield add, rem

        ls_prev = ls
        sleep(5)

for add, rem in changemon():
    print('\n'.join('+ %s' % i for i in add))
    notify.send('+ %s' % i for i in add)
    
ftp.quit()
