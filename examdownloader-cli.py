import subprocess
import sys
import examdownloader

module = 'CS1010S'
username = 'A0012345'
destination = './'

def startDownload(args):

    global module, username
    password = ''

    if len(args) > 0:
        module = args[0]
        username = args[1]

    print('Enter password for ' + username + ': ')
    password = raw_input()
    ed = examdownloader.examdownloader('CLI')


    def updateStatus(msg, type='normal'):
        print msg

    def downloadCallback(status, lastfile=''):
        print('Success!' if status else 'Failed...')
        subprocess.call(['open', '-R', lastfile])

    ed.getContents(module, username, password, destination, downloadCallback, updateStatus)

if __name__ == '__main__':
    startDownload(sys.argv[1:])
