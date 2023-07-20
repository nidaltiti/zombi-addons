﻿# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/

import re
	
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress,VSlog, siteManager, dialog, addon
from resources.lib.util import cUtil, Unquote, urlEncode, Quote
from resources.lib.Styling import getFunc, getThumb, getGenreIcon
from bs4 import BeautifulSoup
import requests
try:  # Python 2
    import urllib2
    from urllib2 import URLError as UrlError

except ImportError:  # Python 3
    import urllib.request as urllib2
    from urllib.error import URLError as UrlError

ADDON = addon()
icons = ADDON.getSetting('defaultIcons')

SITE_IDENTIFIER = 'asia2tv'
SITE_NAME = 'Asia2TV'
SITE_DESC = 'Asian Movies and TV Shows'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

WhiteList = ('افلام','مسلسلات','برامج','اطفال','رمضان','انمي','كرتون','كارتون','دراما', 'الدراما')
def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Search Movies', icons + '/Search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearchSeries', 'Search Series', icons + '/Search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearchAll', 'Search All', icons + '/Search.png', oOutputParameterHandler)
    
    showSiteCats()
    
    oGui.setEndOfDirectory()

def showSiteCats():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    
    oRequestHandler = cRequestHandler(URL_MAIN)
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
    oRequestHandler.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    oRequestHandler.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
    oRequestHandler.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
    sHtmlContent = oRequestHandler.request()
    
    soup = BeautifulSoup(sHtmlContent, "html.parser")
    MenuSoup = soup.find("header").find("nav",{"id":"site-navigation"}).ul
    
   #VSlog(MenuSoup)
    MenuItems = MenuSoup.findAll("li")
    
    for item in MenuItems:
        mItems=(item.a.text.replace("الدراما ال","مسلسلات ").replace("الدراما","المسلسلات"), item.a['href'])
        oOutputParameterHandler.addParameter('siteUrl',  mItems[1]) 
        oGui.addDir(SITE_IDENTIFIER, getFunc(mItems[0]), mItems[0], getThumb(mItems[0]), oOutputParameterHandler)
    oGui.setEndOfDirectory()
 
def showSearchAll():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/?s='+sSearchText
        showSeriesSearch(sUrl)
        oGui.setEndOfDirectory()
        return  
 
def showSearch():
    oGui = cGui() 
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/?s='+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return
 
def showSearchSeries():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/?s='+sSearchText
        showSeries(sUrl)
        oGui.setEndOfDirectory()
        return  
		
def showMovies(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
    
   #VSlog(sUrl)
    
    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    oRequestHandler.addHeaderEntry('Referer', URL_MAIN)
    sHtmlContent = oRequestHandler.request()
    
    soup = BeautifulSoup(sHtmlContent, "html.parser")
    GridSoup = soup.find("main",{"class":"container"})
    GridItems = GridSoup.findAll("div",{"class":"postmovie"})

   #VSlog(GridSoup)
    oOutputParameterHandler = cOutputParameterHandler()
    for item in GridItems:
       #VSlog(item)
        siteUrl = item.find("div",{"class":"postmovie-photo"}).a['href']
        sTitle = item.find("div",{"class":"postmovie-photo"}).a['title'].replace("فيلم","").replace("مترجم ","").replace("مترجم","").replace("مدبلج ","").replace("مدبلج","").strip()
        sYear = item.find("div",{"class":"post-date"}).text.strip()
        
        try:
            sThumb = item.find("div",{"class":"postmovie-photo"}).div.img['src']
        except:
            sThumb = ''
        sThumb = re.sub(r'-\d*x\d*.','.', sThumb)
        
        if sThumb.startswith('//'):
            sThumb = 'https:' + sThumb
           
        sDesc = ''
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('siteUrl',  siteUrl) 
        oOutputParameterHandler.addParameter('sThumb', sThumb)
        oOutputParameterHandler.addParameter('sYear',sYear)
        
        oGui.addMovie(SITE_IDENTIFIER, 'showHostersM' , sTitle, sYear, sThumb, sDesc, oOutputParameterHandler)
    
    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent)
        oOutputParameterHandler = cOutputParameterHandler()
        if sNextPage:
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()

def showSeries(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
    
   #VSlog(sUrl)
    
    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    oRequestHandler.addHeaderEntry('Referer', URL_MAIN)
    sHtmlContent = oRequestHandler.request()
    
    soup = BeautifulSoup(sHtmlContent, "html.parser")
    GridSoup = soup.find("main",{"class":"container"})
    GridItems = GridSoup.findAll("div",{"class":"postmovie"})

   #VSlog(GridSoup)
    oOutputParameterHandler = cOutputParameterHandler()
    for item in GridItems:
       #VSlog(item)
        siteUrl = item.find("div",{"class":"postmovie-photo"}).a['href']
        sTitle = item.find("div",{"class":"postmovie-photo"}).a['title'].replace("فيلم","").replace("مترجم ","").replace("مترجم","").replace("مدبلج ","").replace("مدبلج","").strip()
        sYear = item.find("div",{"class":"post-date"}).text.strip()
        
        try:
            sThumb = item.find("div",{"class":"postmovie-photo"}).div.img['src']
        except:
            sThumb = ''
        sThumb = re.sub(r'-\d*x\d*.','.', sThumb)
        
        if sThumb.startswith('//'):
            sThumb = 'https:' + sThumb
           
        sDesc = ''
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('siteUrl',  siteUrl) 
        oOutputParameterHandler.addParameter('sThumb', sThumb)
        oOutputParameterHandler.addParameter('sYear',sYear)
        
        oGui.addMovie(SITE_IDENTIFIER, 'showEpisodes' , sTitle, sYear, sThumb, sDesc, oOutputParameterHandler)
    
    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent)
        oOutputParameterHandler = cOutputParameterHandler()
        if sNextPage:
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()

 
def showEpisodes():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
   #VSlog(sUrl)
    oInputParameterHandler = cInputParameterHandler()
    sThumb = oInputParameterHandler.getValue('sThumb')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sYear = oInputParameterHandler.getValue('sYear')
    
    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    oRequestHandler.addHeaderEntry('Referer', URL_MAIN)
    sHtmlContent = oRequestHandler.request()
    
    soup = BeautifulSoup(sHtmlContent, "html.parser")
    GridSoup = soup.find("div",{"id":"episode-list"}).find("div",{"class":"loop-episode"})
    oOutputParameterHandler = cOutputParameterHandler()
    #VSlog(GridSoup)
    sDesc = soup.find("div",{"class":"getcontent"}).p.text.encode('utf-8')
    GridLinks = GridSoup.findAll("a")
    GridLabels = GridSoup.findAll("div",{"class":"titlepisode"})
    for i in range(0,len(GridLinks)):
        #VSlog(GridLinks[i])
        sTitle = 'E' + GridLabels[i].text.split("الحلقة")[1].strip()
        siteUrl = GridLinks[i]['href']
        #.replace("الحلقة ","E").replace("الحلقة","E").replace("الحلقه ","E").replace("الحلقه","E").replace("END","").replace("والاخيرة","").replace("والأخيرة","").strip()
        
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle )
        oOutputParameterHandler.addParameter('siteUrl',  siteUrl) 
        oOutputParameterHandler.addParameter('sThumb', sThumb)
        oOutputParameterHandler.addParameter('sYear',sYear)
        oOutputParameterHandler.addParameter('sDesc',sDesc)
        oGui.addTV(SITE_IDENTIFIER, 'showHostersE' , sTitle, sYear, sThumb, sDesc, oOutputParameterHandler)
  
    oGui.setEndOfDirectory()	
    
def __checkForNextPage(sHtmlContent):
    soup = BeautifulSoup(sHtmlContent, "html.parser")
    
    try:
        PaginationSection = soup.find("nav",{"class":"navigation pagination"})
        NextPage = PaginationSection.find("a",{"class":"next page-numbers"})
        return NextPage['href']
    except:
        return False
    return False


def showHostersM():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
   #VSlog(sUrl)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    ## Watch Servers
    cook = oRequestHandler.GetCookies()
    soup = BeautifulSoup(sHtmlContent, "html.parser")
    WatchPage = soup.find("div",{"id":"episode-list"}).find("div",{"class":"loop-episode"})

    FullHostersList = []
    
    url = WatchPage.a['href']
    oRequestHandler = cRequestHandler(url)
    sHtmlContent = oRequestHandler.request()
    
    soup = BeautifulSoup(sHtmlContent, "html.parser")
   #VSlog(sHtmlContent)
    try:
        GridISoup = soup.find("ul",{"class":"server-list-menu"})
        GridItems = GridISoup.findAll("li")
        for item in GridItems:
            try:
                sHosterUrl = item['data-server']
                sHost = item.text.strip()
                sTitle = sMovieTitle
                #VSlog('sHost : ' + sHost + ' sHosterUrl : ' + sHosterUrl)
                if sHosterUrl not in FullHostersList:
                    if sHosterUrl:
                        FullHostersList.append(sHosterUrl)
                        oHoster = cHosterGui().checkHoster(sHosterUrl)
                        
                        if oHoster:
                            oHoster.setDisplayName(sTitle)
                            oHoster.setFileName(sHost)
                            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
                        else:
                           VSlog("URL ["+sHosterUrl+"] has no hoster resolver")
            except:
                oGui.addText('', 'Error - No Links Founds',icons + '/None.png')
    except:
        if 'قريباً' in sHtmlContent:
            oGui.addText('', 'Soon on Asia2TV - No Links Yet',icons + '/None.png')
        else:
            oGui.addText('', 'Error - No Links Founds',icons + '/None.png')
        
    oGui.setEndOfDirectory()

def showHostersE():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
   #VSlog(sUrl)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    ## Watch Servers
    cook = oRequestHandler.GetCookies()
    
    soup = BeautifulSoup(sHtmlContent, "html.parser")
    FullHostersList = []
   #VSlog(sHtmlContent)
    try:
        GridISoup = soup.find("ul",{"class":"server-list-menu"})
        GridItems = GridISoup.findAll("li")
        for item in GridItems:
            try:
                sHosterUrl = item['data-server']
                sHost = item.text.strip()
                sTitle = sMovieTitle
                #VSlog('sHost : ' + sHost + ' sHosterUrl : ' + sHosterUrl)
                if sHosterUrl not in FullHostersList:
                    if sHosterUrl:
                        FullHostersList.append(sHosterUrl)
                        oHoster = cHosterGui().checkHoster(sHosterUrl)
                        
                        if oHoster:
                            oHoster.setDisplayName(sTitle)
                            oHoster.setFileName(sHost)
                            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
                        else:
                           VSlog("URL ["+sHosterUrl+"] has no hoster resolver")
            except:
                oGui.addText('', 'Error - No Links Founds',icons + '/None.png')
    except:
        if 'قريباً' in sHtmlContent:
            oGui.addText('', 'Soon on Asia2TV - No Links Yet',icons + '/None.png')
        else:
            oGui.addText('', 'Error - No Links Founds',icons + '/None.png')
        
    oGui.setEndOfDirectory()