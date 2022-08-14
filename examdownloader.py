import http.client as httplib
import urllib
import os

class examdownloader(object):
    def __init__(self, mode):
        self.mode = mode

    def getContents(self, module, username, password, destination, downloadEndCallback, updateStatus):
        updateStatus('Connecting to NUS Library Portals...')

        conn = httplib.HTTPSConnection('libbrs.nus.edu.sg')
        page = '/infogate/loginAction.do?execution=login'
        conn.request('GET', page)

        resp = conn.getresponse()
        conn.close()
        cookie = resp.getheader('Set-Cookie')
        sessionid = cookie[:cookie.find(';')]
        cookie = sessionid

        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Cookie' : cookie
        }
        headersGet = {
            'Cookie' : cookie
        }
        params = {
            'userid': username,
            'password': password,
            'domain': 'NUSSTU',
            'key': 'blankid+RESULT+EXAM+' + module
        }
        params = urllib.parse.urlencode(params)

        conn = httplib.HTTPSConnection('libbrs.nus.edu.sg')
        conn.request('POST', page, params, headers)
        resp = conn.getresponse()
        data = str(resp.read())
        conn.close()

        if data.find("login") != -1:
            updateStatus("Wrong username/password", "error")
            return

        conn = httplib.HTTPSConnection('libbrs.nus.edu.sg')
        page = '/infogate/jsp/login/success.jsp;jsessionid='+sessionid+'?exe=ResultList'
        conn.request('GET', page, params, headersGet)
        conn.close()

        conn = httplib.HTTPSConnection('libbrs.nus.edu.sg')
        page = '/infogate/searchAction.do?execution=ResultList'
        params = 'database=EXAM&searchstring='+module+'&d='
        conn.request('POST', page, params, headers)
        resp = conn.getresponse()
        data = resp.read()
        conn.close()

        data = str(data)
        params = self.getParams(data)
        maxDocIndex = int(params['maxNo'])
        params['maxDocIndex'] = params['maxNo']
        pdfs = {}

        if maxDocIndex < 1:
            updateStatus('No papers available for this module', 'error')
            return

        for i in range(1, maxDocIndex+1):
            conn = httplib.HTTPSConnection('libbrs.nus.edu.sg')
            page = '/infogate/searchAction.do?execution=ViewSelectedResultListLong'
            params['preSelectedId'] = i
            params['exportids'] = i
            conn.request('POST', page, urllib.parse.urlencode(params), headers)
            resp = conn.getresponse()
            data = resp.read()
            conn.close()
            data = str(data)

            pdfIndex = data.find('View attached PDF file')
            if pdfIndex == -1:
                continue
            pdfIndex = data.rfind('href=', 0, pdfIndex)
            openquotes = data.find('"', pdfIndex)
            closequotes = data.find('"', openquotes+1)
            page = page[:page.rfind('/')+1] + data[openquotes+1:closequotes]

            titleIndex = data.find('title=', pdfIndex)
            if titleIndex == -1:
                continue
            openquotes = data.find('"', titleIndex)
            closequotes = data.find('"', openquotes+1)
            title = data[openquotes+1: closequotes]
            pdfs[title] = page

        counter = 0;
        for title, page in pdfs.items():
            counter += 1
            updateStatus('Downloading ' + str(counter) + ' of ' + str(len(pdfs)))

            conn = httplib.HTTPSConnection('libbrs.nus.edu.sg')
            conn.request('GET', page, None, headersGet)
            resp = conn.getresponse()
            data = resp.read()

            conn.close()

            title = title[title.find('file')+5:]
            filename = destination + '/' + title
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            try:
                f = open(filename, 'wb')
                print('Writing ' + title)
                f.write(data)
                f.close()
            except Exception as e:
                updateStatus('Invalid destination', 'error')
                return

        if 'filename' in vars():
            downloadEndCallback(True, filename, counter)
        else:
            downloadEndCallback(False)

    def getParams(self, data):
        start = data.find('databasenamesasstring')
        start = data.rfind('<', 0, start)
        end = data.find('<select', start)

        params = {
            'databasenamesasstring' : 'Examination Papers Database',
            'searchid':'-6901505210342489183',
            'f':'list',
            'b':'1',
            'p':'1',
            'd':'EXAM',
            'u':'dummy',
            'r':'',
            'l':'20',
            'n':'',
            'nn':'',
            'historyid':'1',
            'maxDocIndex':'11',
            'preSelectedId':'1,', #id
            'maxNo':'11',
            'sPage1':'1',
            'pageNo1':'1',
            'exportids':'1', #id
            'maxNo':'11',
            'sPage2':'1',
            'pageNo2':'1',
            'paraid[0]':'PGH2',
            'parashortname[0]':'FACU',
            'paravalue[0]':'',
            'paraid[1]':'PGH3',
            'parashortname[1]':'SUBJ',
            'paravalue[1]':'',
            'paraid[2]':'PGH5',
            'parashortname[2]':'CNAM',
            'paravalue[2]':''
        }

        start = data.find('name=', start, end)
        while start != -1:
            openquotes = data.find('"', start, end)
            closequotes = data.find('"', openquotes+1, end)
            name = data[openquotes+1:closequotes]
            start = data.find('value=', start, end)
            openquotes = data.find('"', start, end)
            closequotes = data.find('"', openquotes+1, end)
            value = data[openquotes+1:closequotes]
            params[name] = value
            start = data.find('name=', start, end)

        maxNo = data.find("Listing 1 to ");
        if maxNo != -1:
            maxNo = int(data[maxNo+13:maxNo+15])
        params['maxNo'] = maxNo

        return params
