
# coding: utf-8

from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.hosters.hoster import iHoster
from resources.lib.comaddon import VSlog
#import jsunpack
from resources.lib.packer import cPacker
import re
import xbmcgui


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'peytonepre', 'Peytonepre')

    def _getMediaLinkForGuest(self):
        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        api_call = ''

        oParser = cParser()
        
        sPattern = '(\s*eval\s*\(\s*function\(p,a,c,k,e(?:.|\s)+?)<\/script>'
        aResult = re.findall(sPattern,sHtmlContent,re.DOTALL)
    #    xbmcgui.Dialog().ok("hi", "Success" if aResult else "Failed")
      #  xbmcgui.Dialog().ok("hi2", str(aResult))

        if aResult :
           # xbmcgui.Dialog().ok("hi3", str(aResult[0]))
            sHtmlContent = cPacker().unpack(aResult[0])
       #     xbmcgui.Dialog().ok("hls", str(sHtmlContent))
          
        
        sPattern = r'https://[^\s"]+\.m3u8[^\s"]*'
        aResult = re.findall(sPattern,sHtmlContent)
      #  aResult = oParser.parse(sHtmlContent, sPattern)
      #  xbmcgui.Dialog().ok("link", str(aResult[0]))

        if aResult:
            api_call = aResult[0]

        if api_call:
            return True, api_call

        return False, False
