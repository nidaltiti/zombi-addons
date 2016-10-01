#-*- coding: utf-8 -*-
#
import re,os
import urllib2,urllib
import xbmc
import xbmcaddon
import base64


PathCache = xbmc.translatePath(xbmcaddon.Addon('plugin.video.smsm').getAddonInfo("profile"))
UA = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

class NoRedirection(urllib2.HTTPErrorProcessor):    
    def http_response(self, request, response):
        return response

class SucurieBypass(object):

    def __init__(self):
        self.state = False
        self.hostComplet = ''
        self.host = ''
        self.url = ''
                       
    def DeleteCookie(self,Domain):
        print 'Effacement cookies'
        file = os.path.join(PathCache,'Cookie_'+ str(Domain) +'.txt')
        os.remove(os.path.join(PathCache,file))
        
    def SaveCookie(self,Domain,data):
        Name = os.path.join(PathCache,'Cookie_'+ str(Domain) +'.txt')

        #save it
        file = open(Name,'w')
        file.write(data)

        file.close()
        
    def Readcookie(self,Domain):
        Name = os.path.join(PathCache,'Cookie_'+ str(Domain) +'.txt')
        
        try:
            file = open(Name,'r')
            data = file.read()
            file.close()
        except:
            return ''
        
        return data
          
    def DecryptCookie(self,htmlcontent):
        match = re.search("S\s*=\s*'([^']+)", htmlcontent)
        if match:
            s = base64.b64decode(match.group(1))
            s = s.replace(' ', '')
            s = re.sub('String\.fromCharCode\(([^)]+)\)', r'chr(\1)', s)
            s = re.sub('\.slice\((\d+),(\d+)\)', r'[\1:\2]', s)
            s = re.sub('\.charAt\(([^)]+)\)', r'[\1]', s)
            s = re.sub('\.substr\((\d+),(\d+)\)', r'[\1:\1+\2]', s)
            s = re.sub(';location.reload\(\);', '', s)
            s = re.sub(r'\n', '', s)
            s = re.sub(r'document\.cookie', 'cookie', s)
            try:
                cookie = ''
                #print s
                exec(s)
                match = re.match('([^=]+)=(.*)', cookie)
                if match:
                    return match.group(1) + '=' + match.group(2)
            except:
                print 'Erreur decodage sucuri'
                
        return None
        
    #Return param for head
    def GetHeadercookie(self,url):
        #urllib.quote_plus()
        Domain = re.sub(r'https*:\/\/([^/]+)(\/*.*)','\\1',url)
        cook = self.Readcookie(Domain.replace('.','_'))
        if cook == '':
            return ''
            
        return '|' + urllib.urlencode({'User-Agent':UA,'Cookie': cook })   
     
    def CheckIfActive(self,html):
        if 'sucuri_cloudproxy_js' in html:
            return True
        return False
        
        
    def SetHeader(self):
        head=[]
        head.append(('User-Agent', UA))
        head.append(('Host' , self.host))
        head.append(('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'))
        head.append(('Referer', self.url))
        head.append(('Content-Type', 'text/html; charset=utf-8'))
        head.append(('Accept-Encodinge', 'identity'))
        return head
        
    def GetHtml(self,url):
        self.hostComplet = re.sub(r'(https*:\/\/[^/]+)(\/*.*)','\\1',url)
        self.host = re.sub(r'https*:\/\/','',self.hostComplet)
        self.url = url
                  
        #on cherche des precedents cookies
        cookies = self.Readcookie(self.host.replace('.','_'))

        htmlcontent = self.htmlrequest(url,cookies)

        if not self.CheckIfActive(htmlcontent):
            # ok pas de protection
            return htmlcontent
        
        #on cherche le nouveau cookie
        cookies = self.DecryptCookie(htmlcontent)
        if not cookies:
            print 'Erreur sucuri decodage'
            return ''
            
        print 'Protection Sucuri active'
        
        #on sauve le nouveau cookie
        self.SaveCookie(self.host.replace('.','_'),cookies)
        
        #et on recommence
        htmlcontent = self.htmlrequest(url,cookies)
        
        return htmlcontent
        
    def htmlrequest(self,url,cookies = ''):
        
        opener = urllib2.build_opener(NoRedirection)
        opener.addheaders = self.SetHeader()
        
        if cookies:
            opener.addheaders.append(('Cookie', cookies))
        
        response = opener.open(url)
        htmlcontent = response.read()
        response.close()
        
        if response.info().get('Content-Encoding') == 'gzip':
            print 'contenu zippe'
            import gzip
            from StringIO import StringIO
            buf = StringIO(htmlcontent)
            f = gzip.GzipFile(fileobj=buf)
            htmlcontent = f.read()
            
        return htmlcontent
