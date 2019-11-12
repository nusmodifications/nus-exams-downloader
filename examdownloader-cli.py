import subprocess
import sys
import getpass
import examdownloader
import argparse

# Insert configuration here
username = ""       # NUSNET ID i.e. "E0123456"
password = ""       # NUSNET password
destination = ""    # target destination i.e. "." (current directory)


def startDownload(module, username, destination, password):

    ed = examdownloader.examdownloader('CLI')

    def updateStatus(msg, type='normal'):
        print msg

    def downloadCallback(status, lastfile='', numFiles=0):
        if status:
            updateStatus(str(numFiles) + ' papers downloaded successfully!', 'success')
            subprocess.call(['open', '-R', lastfile])
        else:
            updateStatus('Paper not released by Department', 'error')

    ed.getContents(module, username, password, destination, downloadCallback, updateStatus)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Downloads exam papers from UCL automatically")
    parser.add_argument('-u', '--user', help="NUSNET ID", type=str)
    parser.add_argument('-d', '--dest', help="Path to store files", type=str)
    parser.add_argument('-m', '--module', help="Module of which to download exam papers", type=str)
    args = vars(parser.parse_args())

    module = args.get("module")
    if not username:
        username = args.get("user")
    if not username:
        username = raw_input('Enter NUSNET ID: ')

    if not password:
        password = getpass.getpass('Enter password for {}: '.format(username))

    if not module:
        module = raw_input("Enter module to download exams for: ")

    if not destination:
        destination = args.get("dest")
    if not destination:
        destination = raw_input('Enter location to store exams in: ')

    startDownload(module, username, destination, password)
