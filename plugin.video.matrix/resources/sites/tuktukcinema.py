# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/

import re
import xbmcgui
import base64
import urllib.parse
import requests
from bs4 import BeautifulSoup
from resources.lib.multihost import cMegamax

	
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.comaddon import VSlog, siteManager, addon
from resources.lib.parser import cParser
from resources.lib import random_ua

UA = random_ua.get_ua()

ADDON = addon()
icons = ADDON.getSetting('defaultIcons')

SITE_IDENTIFIER = 'tuktukcinema'
SITE_NAME = 'Tuktukcinema'
SITE_DESC = 'arabic vod'
 
URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

oParser = cParser()
 
oRequestHandler = cRequestHandler(URL_MAIN)
sHtmlContent = oRequestHandler.request()
    # (.+?) ([^<]+)

sPattern = 'HomeURL = "(.+?)";'
aResult = oParser.parse(sHtmlContent, sPattern)
    
if (aResult[0]):
    URL_MAIN = aResult[1][0]
    VSlog(URL_MAIN)
 
MOVIE_PACK = (URL_MAIN , 'showPack')
MOVIE_EN = (URL_MAIN + 'category/movies-2/افلام-اجنبي/', 'showMovies')
MOVIE_HI = (URL_MAIN + 'category/movies-33/افلام-هندى/', 'showMovies')
MOVIE_ASIAN = (URL_MAIN + 'category/movies-33/افلام-اسيوي/', 'showMovies')
MOVIE_TURK = (URL_MAIN + 'category/movies-33/افلام-تركي/', 'showMovies')
KID_MOVIES = (URL_MAIN + 'category/anime-6/افلام-انمي/', 'showMovies')
SERIE_EN = (URL_MAIN + 'category/series-1/', 'showSeries')


SERIE_HEND = (URL_MAIN + 'category/series-9/مسلسلات-هندي/', 'showSeries')
SERIE_ASIA = (URL_MAIN + 'category/series-9/مسلسلات-أسيوي/', 'showSeries')
SERIE_TR = (URL_MAIN + 'category/series-9/مسلسلات-تركي/', 'showSeries')
ANIM_NEWS = (URL_MAIN + 'category/anime-6/انمي-مترجم/', 'showSeries')
DOC_NEWS = (URL_MAIN + 'genre/وثائقي/?filter=movies', 'showMovies')
DOC_SERIES = (URL_MAIN + 'genre/وثائقي/?filter=serie', 'showSeries')
SPORT_WWE = (URL_MAIN + '?s=wwe', 'showMovies')
URL_SEARCH = (URL_MAIN + '/search/', 'showMovies')
URL_SEARCH_MOVIES = (URL_MAIN + '/?s=%D9%81%D9%8A%D9%84%D9%85+', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '/?s=%D9%85%D8%B3%D9%84%D8%B3%D9%84+', 'showSeriesSearch')
FUNCTION_SEARCH = 'showSeries'
 
def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Search Movies', icons + '/Search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearchSeries', 'Search Series', icons + '/Search.png', oOutputParameterHandler)

	
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_PACK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showPack', 'أقسام الموقع', icons + '/Icon.png', oOutputParameterHandler)
	
	

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أجنبية', icons + '/MoviesEnglish.png', oOutputParameterHandler)



    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ASIAN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أسيوية', icons + '/Asian.png', oOutputParameterHandler)


    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TURK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام تركية', icons + '/Turkish.png', oOutputParameterHandler)


    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', icons + '/Hindi.png', oOutputParameterHandler)


    oOutputParameterHandler.addParameter('siteUrl', KID_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كرتون', icons + '/Cartoon.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أجنبية', icons + '/TVShowsEnglish.png', oOutputParameterHandler)




    oOutputParameterHandler.addParameter('siteUrl', SERIE_ASIA[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أسيوية', icons + '/Asian.png', oOutputParameterHandler)


    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات تركية', icons + '/Turkish.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', ANIM_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات إنمي', icons + '/Anime.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_HEND[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات هندية', icons + '/Hindi.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/?s='+sSearchText+'+%D9%81%D9%8A%D9%84%D9%85'
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return
 
def showSearchSeries():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/?s='+sSearchText+'+%D9%85%D8%B3%D9%84%D8%B3%D9%84'
        showSeries(sUrl)
        oGui.setEndOfDirectory()
        return

def showPack(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
# ([^<]+) .+? 

    sPattern = '<a href="([^<]+)">([^<]+)</a>'


    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
	
	
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sTitle = aEntry[1].replace("مشاهدة","").replace("مترجمة","").replace("مترجم","").replace("فيلم","").replace("والأخيرة","").replace("مدبلج للعربية","مدبلج").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","") 
            sThumb = aEntry[1]
            siteUrl = aEntry[0]
         
            sDesc = ''
			

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
			
            if 'sercat' in siteUrl:
                oGui.addDir(SITE_IDENTIFIER, 'showSeries', sTitle, sThumb, oOutputParameterHandler)
            else:
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, sThumb, oOutputParameterHandler)
 
        
 
    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent,sUrl)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showPack', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()
			
def showMovies(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:   
      oInputParameterHandler = cInputParameterHandler()
      sUrl = oInputParameterHandler.getValue('siteUrl')
      sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
      sThumb = oInputParameterHandler.getValue('sThumb')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    oParser = cParser()

    # (.+?) .+? ([^<]+)   
    sPattern = '<div class="Block--Item.+?href="([^<]+)" title="(.+?)">.+?src="(.+?)" alt='
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
 
            sTitle = aEntry[1].replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("مترجم","").replace("فيلم","").replace("والأخيرة","").replace("مدبلج للعربية","مدبلج").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","").replace("الموسم العاشر","S10").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الاول","S1").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الموسم","S").replace("S ","S").replace("الحلقة "," E")
            siteUrl = aEntry[0] 
         
            sThumb = aEntry[2]
            sDesc = ''
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                if 'عرض' in sTitle:
                    sTitle = sTitle.replace('عرض','')
                else:
                    sTitle = sTitle.replace(sYear,'')
            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
			
            oGui.addMovie(SITE_IDENTIFIER, "showHosters", sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        
    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent,sUrl)
        if sNextPage:
            sNextPage= sNextPage.replace(".cfd//", ".cfd/")
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
           # xbmcgui.Dialog().ok("sNextPage",sNextPage)

            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()


def showSeriesSearch(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
 # ([^<]+) .+?
    sPattern = '<div class="Block--Item.+?href="([^<]+)" title="(.+?)">.+?src="(.+?)" alt='

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
	
    itemList = []
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
 
            sTitle = aEntry[1].replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("مترجم","").replace("فيلم","").replace("والأخيرة","").replace("مدبلج للعربية","مدبلج").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","")
            sYear = ''
           
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear,'')
            siteUrl = aEntry[0]
            sThumb = aEntry[2]
            sDesc = ''
            sDisplayTitle = sTitle.replace("الموسم العاشر","S10").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الاول","S1").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الموسم","S").replace("S ","S").replace("الحلقة "," E")

            if sDisplayTitle not in itemList:
                itemList.append(sDisplayTitle)

                oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                oOutputParameterHandler.addParameter('sMovieTitle', sDisplayTitle)
                oOutputParameterHandler.addParameter('sThumb', sThumb)
                oOutputParameterHandler.addParameter('sYear', sYear)
                oOutputParameterHandler.addParameter('sDesc', sDesc)
                
                oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent,sUrl)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()
		
def showSeries(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
      oInputParameterHandler = cInputParameterHandler()
      sUrl = oInputParameterHandler.getValue('siteUrl')
      sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
      sThumb = oInputParameterHandler.getValue('sThumb')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
 # ([^<]+) .+? (.+?)
    sPattern =   r'<a href="(.*?)".*?<img src="(.*?)".*?<h3>(.*?)</h3>'
 #  sPattern =   r'<div class="MasterLoadMore allBlocks">.*?<a href="(.*?)".*?<img src="(.*?)".*?<h3>(.*?)</h3>'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
	
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
 
            sTitle = aEntry[2].replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("مترجم","").replace("فيلم","").replace("والأخيرة","").replace("مدبلج للعربية","مدبلج").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","").replace(" والأخيرة","")
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear,'')
            siteUrl = aEntry[0]
            sThumb = aEntry[1]
            sDesc = ''
            sDisplayTitle = sTitle.split('الحلقة')[0].split('الموسم')[0].replace("الموسم العاشر","S10").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الاول","S1").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الموسم","S").replace("S ","S")



            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sDisplayTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addTV(SITE_IDENTIFIER, 'showSeasons', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)


 
    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent,sUrl)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()

def showSeasons():

    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
  #  xbmcgui.Dialog().ok("aResult",str (sUrl))
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
 #   sPattern = r'(<section class="allseasonss">.*?</section>)'
    oParser = cParser()
    soup = BeautifulSoup(sHtmlContent, "html.parser")
 #   ul_content= re.search(sPattern, sHtmlContent,re.DOTALL)
    ul_content = soup.find("ul", class_="Blocks--List Centered")

    content=ul_content
#    xbmcgui.Dialog().ok("aResult", str(content))

  
    if content:
         
         content = ul_content.find_all("div", class_="Block--Item")
         content_str = str(content)
        # spattern = r'<div class="Block--Item">.*?<a\s+href="([^"]+)".*?<img\s+src="([^"]+)".*?<h3[^>]*>\s*(.*?)\s*</h3>.*?</div>'

    #     aResult = re.findall(spattern, content_str, re.DOTALL)
         aResult=content
     #    xbmcgui.Dialog().ok("aResult",str (aResult))
         oOutputParameterHandler = cOutputParameterHandler()
         for Entry in content:
              aEntry=[]
              aEntry.append(str(Entry.find("a").get("href")))
              aEntry.append(str(Entry.find("img").get("src")))
              aEntry.append(str(Entry.find("h3").text.strip() ))
              sTitle = aEntry[2].replace("الموسم ","S")
              sTitle = sMovieTitle+""+sTitle
              siteUrl = aEntry[0]
              sThumb = aEntry[1]
              sDesc = ""
              oOutputParameterHandler.addParameter('siteUrl',siteUrl)
              oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
              oOutputParameterHandler.addParameter('sThumb', sThumb)
              oGui.addSeason(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)


            #  a_tag = Entry.find("a") 
           ##   xbmcgui.Dialog().ok("a",str (Entry.find("a") .get("href")))

             
         
        
           #  sTitle = aEntry[2].replace("مشاهدة","").replace("مسلسل")
               

        
      #   for aEntry in aResult:
    oGui.setEndOfDirectory()         
                 

      
    


    


	

def showEpisodes():
   
    oGui = cGui()
     
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    oOutputParameterHandler = cOutputParameterHandler()
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    soup=BeautifulSoup(sHtmlContent,"html.parser")
   # rows = soup.find_all("div", class_="row")

    rows = soup.find("div", class_="row")
    aResult=rows.find_all("a")
    for aEntry  in aResult:
         
        
         siteUrl = aEntry ["href"]
      #   xbmcgui.Dialog().ok("",siteUrl)
         
         sTitle  =aEntry  ["title"]
         match = re.search(r'الحلقة\s+(\d+)', sTitle )
         sTitle = sMovieTitle+"E "+str (match.group(1))
         sThumb = ""
         sDesc = ""
         oOutputParameterHandler.addParameter('siteUrl',siteUrl)
         oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
         oOutputParameterHandler.addParameter('sThumb', sThumb)
         oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
         pass
    oGui.setEndOfDirectory()


      #   xbmcgui.Dialog().ok("row",str (match.group(1)))

# حلقة تمر عبر كل حلقة متاحة في الصفحة
    

    #
        # عرض المعلومات في نافذة الإشعارات
    
   
   
   
   
  #  oGui.setEndOfDirectory()

   

    
     # (.+?)
def __checkForNextPage(sHtmlContent,sURL):
    #VSlog(sHtmlContent)
    
    cPattern = r'<a class="next page-numbers" href="([^"]+)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, cPattern)
   
    
    if aResult[1]:
        Next_Page= f' {URL_MAIN} {str( next( iter (aResult[1])))}'
    #    xbmcgui.Dialog().ok("herf Next",Next_Page)
        Next_Page=Next_Page.replace(".cfd//", ".cfd/")
        return Next_Page.replace(".cfd//", ".cfd/").replace("/ /", "//")
    return False
def showHosters():
  
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sUrl = oInputParameterHandler.getValue('siteUrl')
    oRequestHandler = cRequestHandler(sUrl)
  #  xbmcgui.Dialog().ok("",str (sUrl) )
    oParser = cParser()
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<a class="watchAndDownlaod" href="([^"]+)' 
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0]):
      #   xbmcgui.Dialog().ok("aResult[1][0]",str (aResult[1][0]) )
         nUrl = aResult[1][0]
    
    oRequestHandler = cRequestHandler(nUrl)
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    oRequestHandler.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
    oRequestHandler.addHeaderEntry('Accept-Language', 'en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7')
    oRequestHandler.addHeaderEntry('Referer',nUrl.split('watch/')[0])
    sHtmlContent = oRequestHandler.request()
  #  xbmcgui.Dialog().ok("nUrl",str (nUrl.split('watch/')[0]) )
    sPattern = 'data-link="([^"]+)".+?<span>(.+?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0]):
        oOutputParameterHandler = cOutputParameterHandler()
          
     #     xbmcgui.Dialog().ok("aResult[1][0]",str (aResult[0]) )
        for aEntry in aResult[1]:  
            url = decode_string(aEntry[0])  
          #  xbmcgui.Dialog().ok("aEntry",str (url) )
            sServer = aEntry[1].replace('Govid','govid.me').replace('متعدد الجودات','tuktukmulti').replace('TukTuk Vip','megamax')
            if url.startswith('//'):
               url = f'http:{url}'
            
            sHosterUrl = url
        #    xbmcgui.Dialog().ok("data", str(sHosterUrl))
            if bool(re.search(r'mega.*max', sHosterUrl)) or bool(re.search(r'mega.*max', sServer)):
                 data =GetDataUrls(sHosterUrl)
                 if("mega"in sHosterUrl):
               
                  if data is not False:
                     for item in data:
                     #   xbmcgui.Dialog().ok("data", str(item))
                        sHosterUrl=item.get("url")
                   #     xbmcgui.Dialog().ok("data", str(sHosterUrl))
                        sQual=item.get("qual")
                        sLabel=next( iter ( item.get("label")))
                        sDisplayTitle = f'{sMovieTitle} ({sQual}) [COLOR coral]{sLabel}[/COLOR]'
                        oOutputParameterHandler.addParameter('sHosterUrl', sHosterUrl)
                        oOutputParameterHandler.addParameter('siteUrl', sUrl)
                        oOutputParameterHandler.addParameter('sQual', sQual)
                        oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
                        oOutputParameterHandler.addParameter('sThumb', sThumb)
                        oGui.addLink(SITE_IDENTIFIER, 'showLinks', sDisplayTitle, sThumb, sDisplayTitle, oOutputParameterHandler)
                        pass
                     if '?download_' in sHosterUrl:
                        continue
            if 'megamax' in sServer:
                continue 
            oHoster = cHosterGui().checkHoster(sServer)
            if oHoster:
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)   
        sPattern = '<a target="_blank" href="([^"]+)".+?class="fa fa-download"></i><span>(.+?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:           
            url = GetDataUrls(aEntry[0])
            sTitle = f'{sMovieTitle} ({aEntry[1]})' 
            if url.startswith('//'):
               url = f'http:{url}'
								
            sHosterUrl = url 
            if '?download_' in sHosterUrl or 'tuktuk' in sHosterUrl or 'megamax' in sHosterUrl:
               continue
            if 'userload' in sHosterUrl:
              sHosterUrl = f'{sHosterUrl}|Referer={URL_MAIN}'

            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
               oHoster.setDisplayName(sTitle)
               oHoster.setFileName(sMovieTitle)
               cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = '<a target="_NEW" href="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:           
            url = aEntry
            if url.startswith('//'):
               url = f'http:{url}'
								
            sHosterUrl = url 
            if '?download_' in sHosterUrl or 'tuktuk' in sHosterUrl or 'megamax' in sHosterUrl:
               continue
            if 'userload' in sHosterUrl:
              sHosterUrl = f'{sHosterUrl}|Referer={URL_MAIN}'

            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
               oHoster.setDisplayName(sMovieTitle)
               oHoster.setFileName(sMovieTitle)
               cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)               
    oGui.setEndOfDirectory()


    
   
   
    pass

def showLinks():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('sHosterUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oHoster = cHosterGui().checkHoster(sHosterUrl)
    if oHoster:
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()
    pass
def decode_string(string):
    try:
        import base64
        string1 = string.split("0REL0Y&")[0]
        string2 = string1[::-1]
        decoded_string = base64.b64decode(string2).decode('utf-8')
        return decoded_string
    
    except:
        return string


    pass

def GetDataUrls(url):
        list_link=[]
        sHosterUrl = url.replace('download', 'iframe').replace(' ', '')

        print(f"Processed URL: {sHosterUrl}")

        if 'leech' in sHosterUrl or '/e/' in sHosterUrl:
            return False

        # Initialize a session
        session = requests.Session()

        # First request to establish the session
        try:
            initial_response = session.get(sHosterUrl, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive'
            })

            if initial_response.status_code != 200:
                print(f"Error: Initial request failed with status code {initial_response.status_code}")
                return []

            # Extract version if needed
            sHtmlContent = initial_response.text
            sHtmlContent = sHtmlContent.replace('&quot;', '"')

            sVer = ''
         #   import re
            sPattern = '"version":"([^"]+)'
            matches = re.findall(sPattern, sHtmlContent)
            if matches:
                sVer = matches[0]

            # Second request with headers
            headers = {
                'Referer': sHosterUrl,
                'Sec-Fetch-Mode': 'cors',
                'X-Inertia': 'true',
                'X-Inertia-Partial-Component': 'files/mirror/video',
                'X-Inertia-Partial-Data': 'streams',
                'X-Inertia-Version': sVer,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Accept': 'application/json, text/plain, */*'
            }

            response = session.get(sHosterUrl, headers=headers)
            if response.status_code != 200:
                print(f"Error: Unable to fetch data, status code {response.status_code}")
                return []

            # Parse JSON response
            r = response.json()
            for key in r['props']['streams']['data']:
                sQual = key['label'].replace(' (source)', '')
                for sLink in key['mirrors']:
                    sHosterUrl = sLink['link']
                    sLabel = sLink['driver'].capitalize()
                    if sHosterUrl.startswith('//'):
                        sHosterUrl = 'https:' + sHosterUrl

                    list_link.append({"url" : sHosterUrl, "qual" : sQual, "label":{sLabel}})

            return list_link

        except Exception as e:
            print(f"Error: {e}")
            return []

# Example usage

