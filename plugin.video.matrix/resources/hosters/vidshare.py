

from resources.lib.handler.requestHandler import cRequestHandler
from resources.hosters.hoster import iHoster
from resources.lib.parser import cParser
from resources.lib.packer import cPacker
from resources.lib.comaddon import VSlog
from resources.lib import random_ua
import xbmcgui
import requests
import re

UA = random_ua.get_pc_ua()

class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'vidshare', 'Vidshare')

    def _getMediaLinkForGuest(self, autoPlay = False):
        VSlog(self._url)

        oParser = cParser()
        sReferer = self._url 
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Referer": "https://example.com",
    "x-requested-with": "XMLHttpRequest",
    "accept": "*/*"
}
        response = requests.get(self._url , headers=headers)
        content = response.text
        sHtmlContent=content
        pattern = r'file:"(https?://.+?)"'
        aResult = re.findall(pattern, content)
     #   xbmcgui.Dialog().ok("",str (aResult[0]))
        if aResult[0]:
             api_call= aResult[0]
             pass
        
             
             pass

        '''''

        oRequest = cRequestHandler(self._url)
        
        sHtmlContent = oRequest.request()
        xbmcgui.Dialog().ok("",str (sHtmlContent))
        oRequest.enableCache(False)
        sHtmlContent = oRequest.request()
       
        sPattern = '(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>'
        aResult = oParser.parse(sHtmlContent,sPattern)
        if (aResult[0] == True):
            sHtmlContent = cPacker().unpack(aResult[1][0])
            sPattern = 'file:"(.+?)",label:".+?"}'
            aResult = oParser.parse(sHtmlContent,sPattern)
           
        if (aResult[0] == True):
                api_call = aResult[1][0] 

        sPattern = 'file:"(.+?)"}'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0] == True):
            api_call = aResult[1][0] +'|User-Agent=' + UA + '&Referer=' + sReferer
            '''
                
        if (api_call):
            return True, api_call
					
        return False, False