# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/
#############################################################
# Yonn1981 https://github.com/Yonn1981/Repo
#############################################################
# big thx to Rgysoft for this code
# From this url https://gitlab.com/Rgysoft/iptv-host-e2iplayer/-/blob/master/IPTVPlayer/tsiplayer/host_faselhd.py
#############################################################
	
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.comaddon import VSlog, siteManager, addon
from resources.lib.parser import cParser
from bs4 import BeautifulSoup
import requests
import xbmcgui
import re
import base64

ADDON = addon()
icons = ADDON.getSetting('defaultIcons')

SITE_IDENTIFIER = 'cimanow'
SITE_NAME = 'Cimanow'
SITE_DESC = 'arabic vod'

UA = 'ipad'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)


MOVIE_EN = (URL_MAIN + '/category/افلام-اجنبية/', 'showMovies')
MOVIE_AR = (URL_MAIN + '/category/%D8%A7%D9%81%D9%84%D8%A7%D9%85-%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9/', 'showMovies')

MOVIE_HI = (URL_MAIN + '/category/%d8%a7%d9%84%d8%a7%d9%81%d9%84%d8%a7%d9%85/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d9%87%d9%86%d8%af%d9%8a%d8%a9/', 'showMovies')

MOVIE_TURK = (URL_MAIN + '/category/%d8%a7%d9%84%d8%a7%d9%81%d9%84%d8%a7%d9%85/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%aa%d8%b1%d9%83%d9%8a%d8%a9/', 'showMovies')
KID_MOVIES = (URL_MAIN + '/category/افلام-انيميشن/', 'showMovies')
SERIE_TR = (URL_MAIN + '/category/%d8%a7%d9%84%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%aa%d8%b1%d9%83%d9%8a%d8%a9/', 'showSeries')

RAMADAN_SERIES = (URL_MAIN + '/category/رمضان-2024/', 'showSeries')
SERIE_EN = (URL_MAIN + '/category/%d8%a7%d9%84%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%a7%d8%ac%d9%86%d8%a8%d9%8a%d8%a9/', 'showSeries')
SERIE_AR = (URL_MAIN + '/category/مسلسلات-عربية/', 'showSeries')
ANIM_NEWS = (URL_MAIN + '/category/مسلسلات-انيميشن/', 'showSeries')

DOC_NEWS = (URL_MAIN + '/?s=%D9%88%D8%AB%D8%A7%D8%A6%D9%82%D9%8A', 'showMovies')

REPLAYTV_NEWS = (URL_MAIN + '/category/%d8%a7%d9%84%d8%a8%d8%b1%d8%a7%d9%85%d8%ac-%d8%a7%d9%84%d8%aa%d9%84%d9%81%d8%b2%d9%8a%d9%88%d9%86%d9%8a%d8%a9/', 'showMovies')
URL_SEARCH = (URL_MAIN + '/?s=', 'showMovies')
URL_SEARCH_MOVIES = (URL_MAIN + '/?s=%D9%81%D9%8A%D9%84%D9%85+', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '/?s=%D9%85%D8%B3%D9%84%D8%B3%D9%84+', 'showSeries')
FUNCTION_SEARCH = 'showMovies'

s = requests.Session()

def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'SEARCH_MOVIES', icons + '/Search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeriesSearch', 'SEARCH_SERIES', icons + '/Search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أجنبية', icons + '/MoviesEnglish.png', oOutputParameterHandler)
   
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام عربية', icons + '/Arabic.png', oOutputParameterHandler)
 
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TURK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام تركية', icons + '/Turkish.png', oOutputParameterHandler)
    
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', icons + '/Hindi.png', oOutputParameterHandler)
   
    oOutputParameterHandler.addParameter('siteUrl', KID_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كرتون', icons + '/Anime.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أجنبية',icons + '/TVShowsEnglish.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات عربية',icons + '/Arabic.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات تركية',icons + '/Turkish.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', ANIM_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات إنمي', icons + '/Cartoon.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', DOC_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام وثائقية', icons + '/Documentary.png', oOutputParameterHandler) 

    oOutputParameterHandler.addParameter('siteUrl', REPLAYTV_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'برامج تلفزيونية',icons + '/Programs.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + 'category/رمضان/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'رمضان', icons + '/Ramadan.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '?s=%D9%81%D9%8A%D9%84%D9%85+'+sSearchText
        showMovies(sUrl)
        #VSlog(sUrl)
        oGui.setEndOfDirectory()
        return
 
def showSeriesSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '?s=%D9%85%D8%B3%D9%84%D8%B3%D9%84+'+sSearchText
        showSeries(sUrl)
        oGui.setEndOfDirectory()
        return
		
def showMovies(sSearch = ''):
    IsOpenDirectory=False
    oGui = cGui()

    # Determine the URL based on search or default value
    if sSearch:
        sUrl = sSearch
        IsOpenDirectory=False
    else:
        IsOpenDirectory=True
        # If no search term is provided, retrieve the URL from the parameter handler
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
      #  xbmcgui.Dialog().ok("Article Content", sUrl)
    # Check if sUrl is available before proceeding
    if sUrl:
        oParser = cParser()
        oRequest = cRequestHandler(sUrl)
        oRequest.addHeaderEntry('User-Agent', UA)

        # Fetch HTML content
        sHtmlContent = oRequest.request()
    #    xbmcgui.Dialog().ok("Article Content", sHtmlContent)
        soup = BeautifulSoup(sHtmlContent, "html.parser")
        articles_Content = soup.find_all("article")

# Define the regex pattern
        sPattern = r'<article aria-label="post">.*?<a href="(https?://[^"]+)">.*?<li aria-label="year">\s*(\d{4})\s*</li>.*?<li aria-label="title">\s*([^<]+)\s*<em>.*?</em>\s*</li>.*?<img[^>]+src="([^"]+)"'

# Process each article
        for article in articles_Content:
    # Display article content for debugging
      #   xbmcgui.Dialog().ok("Article", str(article))

    # Find matches within the article content
         aResult = re.findall(sPattern, str(article), re.DOTALL)
         if aResult:
          for aEntry in aResult:
            # Extract URL and title
            siteUrl = aEntry[0] + '/watching/'
            sYear = aEntry[1]
            sDesc = ''
            sThumb = str(aEntry[3].encode('latin-1'),'utf-8')
            sTitle = aEntry[2]
           


            # Clean up the title by removing unwanted words/phrases
            sTitle = (
                sTitle.replace("مشاهدة", "")
                .replace("مسلسل", "")
                .replace("مسرحية", "")
                .replace("انمي", "")
                .replace("مترجمة", "")
                .replace("مترجم", "")
                .replace("برنامج", "")
                .replace("فيلم", "")
                .replace("والأخيرة", "")
                .replace("مدبلج للعربية", "مدبلج")
                .replace("والاخيرة", "")
                .replace("كاملة", "")
                .replace("حلقات كاملة", "")
                .replace("اونلاين", "")
                .replace("مباشرة", "")
                .replace("انتاج ", "")
                .replace("جودة عالية", "")
                .replace("كامل", "")
                .replace("HD", "")
                .replace("السلسلة الوثائقية", "")
                .replace("الفيلم الوثائقي", "")
                .replace("اون لاين", "")
            )
            oOutputParameterHandler = cOutputParameterHandler()  
            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
			
            oGui.addMovie(SITE_IDENTIFIER, 'showServer', sTitle, '', sThumb, sDesc, oOutputParameterHandler)  

            pass
        # Only proceed if HTML content is retrieved
        if str (articles_Content):

            if aResult:
       
                      pass
                   
            else:
                xbmcgui.Dialog().notification("Error", "No articles found", xbmcgui.NOTIFICATION_ERROR, 3000)
        else:
            xbmcgui.Dialog().notification("Error", "Failed to retrieve page content", xbmcgui.NOTIFICATION_ERROR, 3000)
    else:
        xbmcgui.Dialog().notification("Error", "No URL provided", xbmcgui.NOTIFICATION_ERROR, 3000)
   
    sNextPage = __checkForNextPage(sHtmlContent)
    #xbmcgui.Dialog().ok("Next page",str (sNextPage) )
    if sNextPage:
     oOutputParameterHandler = cOutputParameterHandler()
     oOutputParameterHandler.addParameter('siteUrl', sNextPage)
     oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
    if  IsOpenDirectory:
     oGui.setEndOfDirectory()
   # Function ends def showMovies(sSearch = ''): 
   
def __checkForNextPage(sHtmlContent): #Check if the next page exists.
    soup=BeautifulSoup(sHtmlContent,"html.parser")
    pagination = soup.find_all("ul", {"aria-label": "pagination"})
    sPattern = r'<li class="active"><a href="(https?://[^"]+)">([^<]+)</a></li>'
   
    next_page = ""
    for page in pagination:
        page_str = str(page) 
    matches = re.findall(sPattern, page_str)
   
# Print the matches
    for match in matches:
  #   href = match[0]
     number = int (match[1])+1
     next_page=(f"{str(number)}")
     
   #  xbmcgui.Dialog().ok("next",next_page)
    sPattern =  r'<li\s*.*?><a href="(https?://[^"]+)">([^<]+)</a></li>'
    for page in pagination :
        page_str=str(page)
        matches_NextPage = re.findall(sPattern, page_str)
        for match in matches_NextPage:
           number=str (match[1])

           if str (next_page) ==   str(number) :
     #       xbmcgui.Dialog().ok("",  str(number))
            results=match[0]


            return results # Join results into a single string separated by newlines
    
    return  False
    pass
#End __checkForNextPage(sHtmlContent):

def showSeries(sSearch = ''):
    IsOpenDirectory=False
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
      IsOpenDirectory=False
    else:
          IsOpenDirectory=True
          oInputParameterHandler = cInputParameterHandler()
          sUrl = oInputParameterHandler.getValue('siteUrl')
      #  xbmcgui.Dialog().ok("Article Content", sUrl)
    # Check if sUrl is available before proceeding
    if sUrl:
        oParser = cParser()
        oRequest = cRequestHandler(sUrl)
        oRequest.addHeaderEntry('User-Agent', UA)

        # Fetch HTML content
        sHtmlContent = oRequest.request()
    #    xbmcgui.Dialog().ok("Article Content", sHtmlContent)
        soup = BeautifulSoup(sHtmlContent, "html.parser")
        articles_Content = soup.find_all("article")

# Define the regex pattern
        sPattern = r'<article aria-label="post">.*?<a href="(https?://[^"]+)">.*?<li aria-label="year">\s*(\d{4})\s*</li>.*?<li aria-label="title">\s*([^<]+)\s*<em>.*?</em>\s*</li>.*?<img[^>]+src="([^"]+)"'

# Process each article
        for article in articles_Content:
           aResult = re.findall(sPattern, str(article), re.DOTALL)
       #    xbmcgui.Dialog().ok("aResult",str(aResult))
           if aResult:
                for aEntry in aResult:
            # Extract URL and title
                 siteUrl = aEntry[0] 
                 sYear = aEntry[1]
                 sDesc = ''
                 sThumb = str(aEntry[3].encode('latin-1'),'utf-8')
                 sTitle = aEntry[2]
                 sTitle = (
                sTitle.replace("مشاهدة", "")
                .replace("مسلسل", "")
                .replace("مسرحية", "")
                .replace("انمي", "")
                .replace("مترجمة", "")
                .replace("مترجم", "")
                .replace("برنامج", "")
                .replace("فيلم", "")
                .replace("والأخيرة", "")
                .replace("مدبلج للعربية", "مدبلج")
                .replace("والاخيرة", "")
                .replace("كاملة", "")
                .replace("حلقات كاملة", "")
                .replace("اونلاين", "")
                .replace("مباشرة", "")
                .replace("انتاج ", "")
                .replace("جودة عالية", "")
                .replace("كامل", "")
                .replace("HD", "")
                .replace("السلسلة الوثائقية", "")
                .replace("الفيلم الوثائقي", "")
                .replace("اون لاين", "")
            )

           #      xbmcgui.Dialog().ok("Title",str(sTitle))
                 oOutputParameterHandler = cOutputParameterHandler()  
                 oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                 oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                 oOutputParameterHandler.addParameter('sThumb', sThumb)
                 oOutputParameterHandler.addParameter('sYear', sYear)
                 oOutputParameterHandler.addParameter('sDesc', sDesc)
                 oGui.addTV(SITE_IDENTIFIER, 'showSeasons', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                 pass # for aEntry in aResult:
        pass#  for article in articles_Content:
        sNextPage = __checkForNextPage(sHtmlContent)
    #xbmcgui.Dialog().ok("Next page",str (sNextPage) )
    if sNextPage:
     oOutputParameterHandler = cOutputParameterHandler()
     oOutputParameterHandler.addParameter('siteUrl', sNextPage)
     oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
     if IsOpenDirectory:
      oGui.setEndOfDirectory()
       # sPattern = r'<article aria-label="post">.*?<a href="(https?://[^"]+)">.*?<li aria-label="year">\s*(\d{4})\s*</li>.*?<li aria-label="title">\s*([^<]+)\s*<em>.*?</em>\s*</li>.*?<img[^>]+src="([^"]+)"'
    '''''
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
 
    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('User-Agent', UA)
    data = oRequest.request()
 
  


     # (.+?) ([^<]+) .+?

    if 'adilbo' in data:
        t_script = re.findall('<script.*?;.*?\'(.*?);', data, re.S)
        t_int = re.findall('/g.....(.*?)\)', data, re.S)
        if t_script and t_int:
            script = t_script[0].replace("'",'')
            script = script.replace("+",'')
            script = script.replace("\n",'')
            sc = script.split('.')
            page = ''
            for elm in sc:
                c_elm = base64.b64decode(elm+'==').decode()
                t_ch = re.findall('\d+', c_elm, re.S)
                if t_ch:
                    nb = int(t_ch[0])+int(t_int[0])
                    page = page + chr(nb)
            #VSlog(page)

            sPattern = '<article aria-label="post"><a href="([^<]+)">.+?<li aria-label="year">(.+?)</li>.+?<li aria-label="title">([^<]+)<em>.+?data-src="(.+?)" width'


            oParser = cParser()
            aResult = oParser.parse(page, sPattern)
	
            itemList = []
            if aResult[0]:
                oOutputParameterHandler = cOutputParameterHandler()  
                for aEntry in aResult[1]:
 
                    if "فيلم" in aEntry[2]:
                        continue
 
                    sTitle = aEntry[2]
                    sTitle = str(sTitle.encode('latin-1'),'utf-8')
                    siteUrl = aEntry[0]
                    sThumb = str(aEntry[3].encode('latin-1'),'utf-8')
                    if sThumb.startswith('//'):
                        sThumb = 'http:' + sThumb
                    sDesc = ''
                    sYear = aEntry[1]
                    
                    if sTitle not in itemList:
                        itemList.append(sTitle)

                        oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                        oOutputParameterHandler.addParameter('sThumb', sThumb)
                        oOutputParameterHandler.addParameter('sYear', sYear)
                        oOutputParameterHandler.addParameter('sDesc', sDesc)
                
                        oGui.addTV(SITE_IDENTIFIER, 'showSeasons', sTitle, '', sThumb, sDesc, oOutputParameterHandler)



                        
            #itemList = []
            # if aResult[0]:
                # total = len(aResult[1])
                # progress_ = progress().VScreate(SITE_NAME)
                # oOutputParameterHandler = cOutputParameterHandler()  
                # for aEntry in aResult[1]:
                    # progress_.VSupdate(progress_, total)
                    # if progress_.iscanceled():
                        # break
 
                    # sTitle = aEntry[1]
            
                    # sTitle =  "PAGE " + sTitle
                    # sTitle =   '[COLOR red]'+sTitle+'[/COLOR]'
                    # siteUrl = aEntry[0]
                    # sThumb = ""

                    # if sTitle not in itemList:
                        # itemList.append(sTitle)
                        # oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                        # oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                        # oOutputParameterHandler.addParameter('sThumb', sThumb)
                
                        # oGui.addDir(SITE_IDENTIFIER, 'showSeries', sTitle, '', oOutputParameterHandler)

                # progress_.VSclose(progress_)
 
    if not sSearch:
        sStart = '</section>'
        sEnd = '</ul>'
        page = oParser.abParse(page, sStart, sEnd)

        sPattern = '<li><a href="(.+?)">(.+?)</a>'
        oParser = cParser()
        aResult = oParser.parse(page, sPattern)
        
        soup = BeautifulSoup(page,"html.parser")
        CurrentPage = int(soup.find("li",{"class":"active"}).text)
        #VSlog(CurrentPage)
        
        if aResult[0]:
            oOutputParameterHandler = cOutputParameterHandler()  
            for aEntry in aResult[1]:
                
                deviation = int(aEntry[1])-CurrentPage
                if deviation==1:
                    #sTitle = aEntry[1]
            
                    sTitle =  'Next'
                    #sTitle =   '[COLOR red]'+sTitle+'[/COLOR]'
                    siteUrl = aEntry[0]
                    sThumb = icons + '/Next.png'

                    oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)
            
                    oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, sThumb, oOutputParameterHandler)
                    '''''
        
 
def showSeasons():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
 
    # (.+?) .+?  ([^<]+)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()




    oParser = cParser()
    sStart = '<section aria-label="seasons">'
    sEnd = '</section>'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)
  #  xbmcgui.Dialog().ok("showSeasons",str (sHtmlContent))
    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('User-Agent', UA)
    data = oRequest.request()
    spattern = r'<a href="([^"]+)">'

# Find all matches
    aResult = re.findall(spattern, sHtmlContent)
  #  xbmcgui.Dialog().ok("links",str (aResult))
    

  
  
  
    '''''
    

     # (.+?) ([^<]+) .+?
  

    if 'adilbo' in data:
        t_script = re.findall('<script.*?;.*?\'(.*?);', data, re.S)
        t_int = re.findall('/g.....(.*?)\)', data, re.S)
        if t_script and t_int:
            script = t_script[0].replace("'",'')
            script = script.replace("+",'')
            script = script.replace("\n",'')
            sc = script.split('.')
            page = ''
            for elm in sc:
                c_elm = base64.b64decode(elm+'==').decode()
                t_ch = re.findall('\d+', c_elm, re.S)
                if t_ch:
                    nb = int(t_ch[0])+int(t_int[0])
                    page = page + chr(nb)
            #VSlog(page)
            
            oParser = cParser()
            sStart = '<section aria-label="seasons">'
            sEnd = '<ul class="tabcontent" id="related">'
            page = oParser.abParse(page, sStart, sEnd)
            
            sPattern = '<a href="([^<]+)">([^<]+)<em>'
    
            oParser = cParser()
            aResult = oParser.parse(page, sPattern)
         '''
    if aResult:
                oOutputParameterHandler = cOutputParameterHandler()  
                for num,aEntry in enumerate (aResult):
                    snum=int(num+1)


                    sSeason =f"S{snum}"
                    sTitle = sMovieTitle+sSeason.replace("الموسم"," S").replace("S ","S")
                  #  xbmcgui.Dialog().ok("links",str (aEntry))
                    siteUrl = aEntry
                    sThumb = sThumb
                    sDesc = ""
 

                    oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)
            

 
                    oGui.addSeason(SITE_IDENTIFIER, 'showEps', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
       
    oGui.setEndOfDirectory() 
 
def showEps():
    oGui = cGui()
  
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
 #   xbmcgui.Dialog().ok("sHtmlContent",str (sUrl))
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
  #  xbmcgui.Dialog().ok("sHtmlContent",str (sHtmlContent))
    soup=BeautifulSoup(sHtmlContent,"html.parser")
    ul_eps = soup.find_all("ul", class_="tabcontent active")#<ul class="tabcontent active" id="eps">
    ul_content=str(ul_eps)
    tag_conten_il=  BeautifulSoup(ul_content,"html.parser")
    il_tags= tag_conten_il.find_all("li")
    sPattern = r'<a href="([^"]+)"[^>]*>.*?<img[^>]*src="([^"]+)"[^>]*>.*?<em>(\d+)</em>'


 
    for il_tag in  il_tags:
#     xbmcgui.Dialog().ok("sHtmlContent",str (il_tag))
      block = str(il_tag)

    # Perform regex search on the block
      aResult = re.findall(sPattern, block, re.DOTALL)

   
     
      for aEntry in aResult:  
       oOutputParameterHandler = cOutputParameterHandler()  
       siteUrl = aEntry[0]+'/watching/'
       sThumb = aEntry[1]
       sTitle = sMovieTitle+' E'+aEntry[2]
       sDesc = ""
       oOutputParameterHandler.addParameter('siteUrl', siteUrl)
       oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
       oOutputParameterHandler.addParameter('sThumb', sThumb)
      # xbmcgui.Dialog().ok("Extracted aEntry",str (siteUrl))
     
       oGui.addEpisode(SITE_IDENTIFIER, 'showServer', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
            
   
    # Display the result for each <li>
    '''''
      if aResult:
              
                oOutputParameterHandler = cOutputParameterHandler()  
                for aEntry in aResult:
                    xbmcgui.Dialog().ok("Extracted Data",str (aEntry))

 
                    sTitle = sMovieTitle+' E'+aEntry[2]
                    
                    siteUrl = aEntry[0] + 'watching/'
                    sThumb = str(aEntry[1].encode('latin-1'),'utf-8')
                    sDesc = ""

                    oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)
            

 
                    oGui.addEpisode(SITE_IDENTIFIER, 'showServer', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
   '''
    
    '''''
    oParser = cParser()
    sStart = '<section aria-label="seasons">'
    sEnd = '<ul class="tabcontent" id="related">'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)
    '''
    '''''
    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('User-Agent', UA)
    data = oRequest.request()


     # (.+?) ([^<]+) .+?

    if 'adilbo' in data:
        t_script = re.findall('<script.*?;.*?\'(.*?);', data, re.S)
        t_int = re.findall('/g.....(.*?)\)', data, re.S)
        if t_script and t_int:
            script = t_script[0].replace("'",'')
            script = script.replace("+",'')
            script = script.replace("\n",'')
            sc = script.split('.')
            page = ''
            for elm in sc:
                c_elm = base64.b64decode(elm+'==').decode()
                t_ch = re.findall('\d+', c_elm, re.S)
                if t_ch:
                    nb = int(t_ch[0])+int(t_int[0])
                    page = page + chr(nb)
            #VSlog(page)
            
            oParser = cParser()
            sStart = '<section aria-label="seasons">'
            sEnd = '<ul class="tabcontent" id="related">'
            page = oParser.abParse(page, sStart, sEnd)
            
            sPattern = '<li><a href="(.+?)"><img  src="(.+?)" alt="logo" />.+?<em>(.+?)</em>'

            oParser = cParser()
            aResult = oParser.parse(page, sPattern)
   
    

   
            if aResult[0]:
                oOutputParameterHandler = cOutputParameterHandler()  
                for aEntry in aResult[1]:

 
                    sTitle = sMovieTitle+' E'+aEntry[2]
                    
                    siteUrl = aEntry[0] + 'watching/'
                    sThumb = str(aEntry[1].encode('latin-1'),'utf-8')
                    sDesc = ""

                    oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)
            

 
                    oGui.addEpisode(SITE_IDENTIFIER, 'showServer', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
 
                       '''
       
    oGui.setEndOfDirectory() 

  
def showServer():
    import requests
      
 
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    host = URL_MAIN.split('/')[2]
    #VSlog(host)
 
    oRequestHandler = cRequestHandler(sUrl)
    cook = oRequestHandler.GetCookies()
    hdr = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36','Accept-Encoding' : 'gzip','cookie' : cook,'host' : host,'referer' : URL_MAIN}
    St=requests.Session()
    sHtmlContent = St.get(sUrl,headers=hdr)
    sHtmlContent = sHtmlContent.content.decode('utf8')  
    oParser = cParser()


    oRequest = cRequestHandler(sUrl)
    data = oRequest.request()
  #  xbmcgui.Dialog().ok("showServer",data)

    soup=BeautifulSoup(data,"html.parser") 
    html = soup.find_all("li", class_="active")
    
    # Display the result in Kodi's dialog
   # xbmcgui.Dialog().ok("showServer", str(html))
    
    # Regular expression pattern to find <li> with specific data-index and data-id
    sPattern = r'<li\b[^>]*>(.*?)</li>'
    
    # Convert html content to a string for regex search
    html_str = str(html)
    
    # Use re.findall with the correct parameter order
    aResult = re.findall(sPattern, html_str, re.DOTALL)

    
    # Display the result in Kodi's dialog
   # xbmcgui.Dialog().ok("showServer2", str(aResult[1]))
     # (.+?) ([^<]+) .+?

    if aResult:
         #   xbmcgui.Dialog().ok("selectElE", str("selectElE"))
            iframe = soup.find_all("iframe")
            iframe_str = str(iframe)

         #   xbmcgui.Dialog().ok("iframe", iframe_str)
            sPattern = r'<iframe[^>]+src="([^"]+)"'
            ifram_src = re.findall(sPattern, iframe_str, re.DOTALL)
            sHosterUrl =f' https:{str(ifram_src[0])}'
         #   xbmcgui.Dialog().ok(str(sHosterUrl))
         #   xbmcgui.Dialog().ok("src", str(   sHosterUrl ))
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            sTitle=sMovieTitle
            if oHoster:
             oHoster.setDisplayName(sTitle)
             oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb) 
            pass
            soup=BeautifulSoup(data,"html.parser") 
            html = soup.find_all("li", attrs={"aria-label": "download"})

    
    # Display the result in Kodi's dialog
           
    
    # Regular expression pattern to find <li> with specific data-index and data-id
            sPattern = r'<a href="(https?://[^"]+)"[^>]*>\s*<i[^>]*>\s*</i>\s*Filemoon\s*</a>'

    
    # Convert html content to a string for regex search
            html_str = str(html)
    
    # Use re.findall with the correct parameter order
            aResult = re.search(sPattern, html_str, re.DOTALL)
          
            if aResult :
              
                Filemoon_link=  aResult.group(1).replace("/d/","/e/")
                _requests=requests.get(Filemoon_link)
                soup=BeautifulSoup(_requests.text,"html.parser") 
                selectElE = soup.find_all("div", attrs={"class": "specific-class"})
              
                sHosterUrl =Filemoon_link
                
                oHoster = cHosterGui().checkHoster(sHosterUrl)
                sTitle=sMovieTitle
                if oHoster:
                 oHoster.setDisplayName(sTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb) 
                pass

    
    oGui.setEndOfDirectory()

#print("hi")
