import sys
import examdownloader

module = 'CS1010S'
username = 'A0012345X'
password = 'awesomepassword'
destination = './'

def startDownload(args):
    global module, username, password, destination
    if len(args) > 0:
        module = args[0]
        username = args[1]
        password = args[2]
        destination = args[3]
    ed = examdownloader.examdownloader('CLI')

    def downloadCallback(status):
        print('Success!' if status else 'Failed...')

    ed.getContents(module, username, password, destination, downloadCallback)

if __name__ == '__main__':
    startDownload(sys.argv[1:])
