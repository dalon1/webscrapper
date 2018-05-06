import urllib.request as request
import ssl

class HttpUtils(object):
    
    @staticmethod
    def getSourceCode(url):
        # Setting User Agent to avoid HTTP Error 403: Forbidden
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept-Encoding': 'identity'}
        req = request.Request(url = url, headers= headers)

        # Deactivating the SSL Certificate check
        # https://stackoverflow.com/questions/35875298/python-3-urllib-with-self-signed-certificates
        temp_ssl = ssl.create_default_context()
        temp_ssl.check_hostname = False
        temp_ssl.verify_mode = ssl.CERT_NONE
        
        try:
            resp = request.urlopen(req, context = temp_ssl)
            #resp = request.urlopen(req)
            resp_data = resp.read()
            return resp_data
        except Exception as e:
            print("HTTP Error: " + str(e)) 
    