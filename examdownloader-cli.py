import subprocess
import getpass
import examdownloader
import argparse

# Insert configuration here
username = ""       # NUSNET ID i.e. "E0123456"
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
    parser = argparse.ArgumentParser(description="Downloads exam papers from NUS Library Portal automatically")
    parser.add_argument('-u', '--user', help="NUSNET ID", type=str)
    parser.add_argument('-d', '--dest', help="Path to store files", type=str, default=".")
    parser.add_argument('-m', '--module', help="Module of which to download exam papers", type=str)
    args = vars(parser.parse_args())

    # If not set by user in top part of the file
    if not username:
        username = args.get("user")
    # If not set by user even in the command line arguments
    if not username:
        username = raw_input('Enter NUSNET ID: ')

    # always ask for security reasons
    password = getpass.getpass('Enter password for {}: '.format(username))

    # expected to be set newly with each call
    module = args.get("module")
    # if not set in CL arguments
    if not module:
        module = raw_input("Enter module to download exams for: ")

    # If not set by user in top part of the file
    # defaults to "." by configuration of argparse
    if not destination:
        destination = args.get("dest")

    startDownload(module, username, destination, password)
