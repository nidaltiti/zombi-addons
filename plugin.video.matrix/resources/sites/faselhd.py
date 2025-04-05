# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/

import re
import base64
	
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
import xbmcgui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.comaddon import progress, VSlog, isMatrix, siteManager, addon
from resources.lib.parser import cParser
from bs4 import BeautifulSoup
ADDON = addon()
icons = ADDON.getSetting('defaultIcons')

SITE_IDENTIFIER = 'faselhd'
SITE_NAME = 'Faselhd'
SITE_DESC = 'arabic vod'
sHost = base64.b64decode(siteManager().getUrlMain2(SITE_IDENTIFIER)).decode("utf-8")
 
URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

MOVIE_EN = (URL_MAIN + '/movies', 'showMovies')
MOVIE_HI = (URL_MAIN + '/hindi', 'showMovies')
MOVIE_ASIAN = (URL_MAIN + '/asian-movies', 'showMovies')
KID_MOVIES = (URL_MAIN + '/dubbed-movies', 'showMovies')
SERIE_EN = (URL_MAIN + '/series', 'showSeries')
REPLAYTV_NEWS = (URL_MAIN + '/tvshows', 'showSeries')
ANIM_MOVIES = (URL_MAIN + '/anime-movies', 'showMovies')
SERIE_ASIA = ('https://www.faselhd.co/asian-series', 'showSeries')
ANIM_NEWS = (URL_MAIN + '/anime', 'showAnimes')
DOC_NEWS = (URL_MAIN + '/movies-cats/documentary', 'showMovies')
DOC_SERIES = (URL_MAIN + '/series_genres/documentary', 'showSeries')
MOVIE_TOP = (URL_MAIN + '/movies_top_votes', 'showMovies')
MOVIE_POP = (URL_MAIN + '/movies_top_views', 'showMovies')
MOVIE_PACK = (URL_MAIN , 'showPack')

URL_SEARCH = (URL_MAIN + '/?s=', 'showSeries')
URL_SEARCH_MOVIES = (URL_MAIN + '/?s=%D9%81%D9%8A%D9%84%D9%85+', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '/?s=%D9%85%D8%B3%D9%84%D8%B3%D9%84+', 'showSeries')
FUNCTION_SEARCH = 'showMovies'
 
def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'SEARCH MOVIES', icons + '/Search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeriesSearch', 'SEARCH SERIES', icons + '/Search.png', oOutputParameterHandler)

    
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أجنبية', icons + '/MoviesEnglish.png', oOutputParameterHandler)
 
    
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ASIAN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أسيوية', icons + '/Asian.png', oOutputParameterHandler)
    
    
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', icons + '/Hindi.png', oOutputParameterHandler)
   
    
    oOutputParameterHandler.addParameter('siteUrl', ANIM_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام إنمي', icons + '/Anime.png', oOutputParameterHandler)
    
    
    oOutputParameterHandler.addParameter('siteUrl', KID_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كرتون', icons + '/Cartoon.png', oOutputParameterHandler)

    
    oOutputParameterHandler.addParameter('siteUrl', DOC_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام وثائقية', icons + '/Documentary.png', oOutputParameterHandler) 

    
    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أجنبية', icons + '/TVShowsEnglish.png', oOutputParameterHandler)

    
    oOutputParameterHandler.addParameter('siteUrl', SERIE_ASIA[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أسيوية', icons + '/Asian.png', oOutputParameterHandler)
  
    
    oOutputParameterHandler.addParameter('siteUrl', DOC_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات وثائقية', icons + '/Documentary.png', oOutputParameterHandler) 
    
    
    oOutputParameterHandler.addParameter('siteUrl', ANIM_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showAnimes', 'مسلسلات إنمي', icons + '/Anime.png', oOutputParameterHandler)
 
    
    oOutputParameterHandler.addParameter('siteUrl', REPLAYTV_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'برامج تلفزيونية',icons + '/Programs.png', oOutputParameterHandler) 
	
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_PACK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showPack', 'أقسام الموقع', icons + '/Lists.png', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()
	
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/?s=%D9%81%D9%8A%D9%84%D9%85+'+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return
 
def showSeriesSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/?s=%D9%85%D8%B3%D9%84%D8%B3%D9%84+'+sSearchText
        showSeries(sUrl)
        oGui.setEndOfDirectory()
        return

def showPack():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    oParser = cParser()
     # (.+?) ([^<]+) .+?
    sStart = 'id="siteMenu"'
    sEnd = '</ul>'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)
    sPattern = 'href="([^<]+)">([^<]+)</a>'


    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)


    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            if '#' in aEntry[0] or 'oscar' in aEntry[0] or 'soon' in aEntry[0] or 'review' in aEntry[0]:
                continue 
            sTitle = aEntry[1]
            siteUrl = aEntry[0].split('"')[0]
            if siteUrl.startswith('/'):
                siteUrl = URL_MAIN + aEntry[0].split('"')[0]

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)

            if 'serie' in siteUrl or 'tvshow' in siteUrl or 'tvshow' in siteUrl or 'asian_top_views' in siteUrl or 'anime_top_views' in siteUrl:
                oGui.addMisc(SITE_IDENTIFIER, 'showSeries', sTitle, 'mslsl.png', '', '', oOutputParameterHandler)
            else:
                oGui.addMisc(SITE_IDENTIFIER, 'showMovies', sTitle, 'film.png', '', '', oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showPack', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
	
def showMovies(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    soup = BeautifulSoup(sHtmlContent, "html.parser")
    sHtmlContent = str(soup.find("div",{"id":"postList"}))
    #VSlog(sHtmlContent)

    sPattern = '<div class=\"postDiv\">.*\s*<a href=\"(.+?)\".*\s*.*\s*.*alt=\"(.+?)\".*data-src=\"(.+?)(\?resize|\")'
	
    matches = re.findall(sPattern,sHtmlContent)
    aResult = [True,matches]
	
    if aResult[0]:
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)
        oOutputParameterHandler = cOutputParameterHandler() 
        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
 
            
            sTitle = aEntry[1].replace("مشاهدة","").replace("مترجم","").replace("فيلم","").replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("مترجم","").replace("فيلم","").replace("والأخيرة","").replace("مدبلج للعربية","مدبلج").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","").replace("برنامج","")
            siteUrl = aEntry[0]
            s1Thumb = aEntry[2].replace("(","").replace(")","")
            sThumb = re.sub(r'-\d*x\d*.','.', s1Thumb)
            sDesc = ''
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear,'')


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
			
            oGui.addMovie(SITE_IDENTIFIER, 'showLink', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        progress_.VSclose(progress_)
 
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
 
    if not sSearch:
        oGui.setEndOfDirectory()

def showSeries(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    soup = BeautifulSoup(sHtmlContent, "html.parser")
    sHtmlContent = str(soup.find("div",{"id":"postList"}))
    #VSlog(sHtmlContent)

    sPattern = '<div class=\"postDiv\">.*\s*<a href=\"(.+?)\".*\s*.*\s*.*alt=\"(.+?)\".*data-src=\"(.+?)(\?resize|\")'
	
    matches = re.findall(sPattern,sHtmlContent)
    aResult = [True,matches]
 # ([^<]+) .+?
    #sPattern = '<div class="postDiv">.+?<a href="([^<]+)">.+?data-src="(.+?)".+?alt="(.+?)"/>'


    #oParser = cParser()
    #aResult = oParser.parse(sHtmlContent, sPattern)
	
	
    if aResult[0]:
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)
        oOutputParameterHandler = cOutputParameterHandler() 
        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
 
            
            sTitle = aEntry[1].replace("مشاهدة","").replace("مسلسل","").replace("انمى","").replace("مترجم","").replace("فيلم","").replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("مترجم","").replace("فيلم","").replace("والأخيرة","").replace("مدبلج للعربية","مدبلج").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","").replace("برنامج","")
            siteUrl = aEntry[0]
            s1Thumb = aEntry[2].replace("(","").replace(")","")
            sThumb = re.sub(r'-\d*x\d*.','.', s1Thumb)
            sDesc = ''
            sDisplayTitle2 = sTitle.split('ال')[0]
            sDisplayTitle2 = sDisplayTitle2.split('مدبلج')[0]
            sDisplayTitle = sTitle.replace("الموسم العاشر","S10").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الاول","S1").replace("الموسم الأول","S1").replace(" الثانى","2").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الحلقة "," E").replace("الموسم","S").replace("S ","S")


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sDisplayTitle2)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
			
            oGui.addTV(SITE_IDENTIFIER, 'showSeasons', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

        progress_.VSclose(progress_)
 
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
 
    if not sSearch:
        oGui.setEndOfDirectory()
		
def showAnimes(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    if isMatrix(): 
       sHtmlContent = str(sHtmlContent.encode('latin-1',errors='ignore'),'utf-8',errors='ignore')
 
    soup = BeautifulSoup(sHtmlContent, "html.parser")
    sHtmlContent = str(soup.find("div",{"id":"postList"}))
    #VSlog(sHtmlContent)

    sPattern = '<div class=\"postDiv\">.*\s*<a href=\"(.+?)\".*\s*.*\s*.*alt=\"(.+?)\".*data-src=\"(.+?)(\?resize|\")'
	
    matches = re.findall(sPattern,sHtmlContent)
    aResult = [True,matches]
    
      # # (.+?) ([^<]+) .+?
    # sPattern = '<div class="postDiv">.+?<a href="([^<]+)">.+?data-src="(.+?)".+?alt="(.+?)"/>'
    # oParser = cParser()
    # aResult = oParser.parse(sHtmlContent, sPattern)
	
	
    if aResult[0]:
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)
        oOutputParameterHandler = cOutputParameterHandler() 
        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
 
            sTitle = aEntry[1].replace("&#8217;","'").replace("مشاهدة","").replace("مترجم","").replace("فيلم","").replace("انمي","").replace("انمى","").replace("برنامج","")
            siteUrl = aEntry[0]
            sThumb = aEntry[2].replace("(","").replace(")","")
            sDesc = ""


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
			
            oGui.addTV(SITE_IDENTIFIER, 'showEpisodes1', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        progress_.VSclose(progress_)
 
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showAnimes', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
 
    if not sSearch:
        oGui.setEndOfDirectory()
  
def showSeasons():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
     # (.+?) ([^<]+) .+?
    sPattern = '<div class="seasonDiv.+?onclick="([^<]+)".+?data-src="(.+?)".+?alt="(.+?)"/>.+?<div class="title">(.+?)</div>'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0]):
        oOutputParameterHandler = cOutputParameterHandler() 
        for aEntry in aResult[1]:
            postid = aEntry[0].split("= '")[1]
            postid = postid.replace("'","")
            nume = aEntry[3].replace("موسم "," S")
            link = URL_MAIN+postid
 
            sTitle = aEntry[2]+nume           
            sTitle = sTitle.replace("مشاهدة","").replace("مسلسل","").replace("انمى","").replace("مترجم","").replace("فيلم","").replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("مترجم","").replace("فيلم","").replace("والأخيرة","").replace("مدبلج للعربية","مدبلج").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","").replace("برنامج","")
            siteUrl = link
            sThumb = aEntry[1]
            sDesc = ""
			


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('postid', postid)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addSeason(SITE_IDENTIFIER, 'showEpisodes1', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
 
    oGui.setEndOfDirectory() 
  
def showEpisodes():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    postid = oInputParameterHandler.getValue('postid')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent2 = oRequestHandler.request()
    oParser = cParser()

    sStart = '<div class="epAll" id="epAll">'
    sEnd = '<div class="postShare">'
    sHtmlContent2 = oParser.abParse(sHtmlContent2, sStart, sEnd)
    
    import requests

    postdata = {'seasonID':postid}
    link = URL_MAIN + '/series-ajax/?_action=get_season_list&_post_id='+postid
    headers = {'Host': 'www.faselhd.ac',
							'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36',
							'Referer': sUrl,
							'origin': URL_MAIN}
    s = requests.Session() 	
    r = s.post(link,data = postdata)
    sHtmlContent = r.content 
    if isMatrix(): 
       sHtmlContent = sHtmlContent.decode('utf8',errors='ignore') 
    if sHtmlContent:
       sPattern = '<a href="([^<]+)>([^<]+)</a>' 

       oParser = cParser()
       aResult = oParser.parse(sHtmlContent,sPattern)
       if aResult[0]:
                  for aEntry in aResult[1]:
                      oOutputParameterHandler = cOutputParameterHandler() 
                      if "العضوية" in aEntry[1]:
                         continue
 
                      sTitle = aEntry[1].replace("الحلقة "," E")
                      sTitle = ('%s %s') % (sMovieTitle, sTitle)
                      siteUrl = aEntry[0].replace(' class="active"', "").replace('"', "") 
                      sThumb = sThumb
                      sDesc = ""


                      oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                      oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                      oOutputParameterHandler.addParameter('sThumb', sThumb)
          
 
                      oGui.addEpisode(SITE_IDENTIFIER, 'showLink', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
      # (.+?) ([^<]+) .+?
    else :
       sPattern = '<a href="(.+?)">(.+?)</a>' 

       oParser = cParser()
       aResult = oParser.parse(sHtmlContent2,sPattern)
       if aResult[0]:
                  for aEntry in aResult[1]:
                      oOutputParameterHandler = cOutputParameterHandler() 
                      if "العضوية" in aEntry[1]:
                         continue
 
                      sTitle = aEntry[1].replace("الحلقة "," E")
                      sTitle = ('%s %s') % (sTitle, sMovieTitle)
                      siteUrl = aEntry[0].replace(' class="active"', "").replace('"', "") 
                      sThumb = sThumb
                      sDesc = ""


                      oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                      oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                      oOutputParameterHandler.addParameter('sThumb', sThumb)
          
 
                      oGui.addEpisode(SITE_IDENTIFIER, 'showLink', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
 
       
    oGui.setEndOfDirectory() 

def showEpisodes1():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    oParser = cParser()
    
    #Recuperation infos
    sNote = ''

    sPattern = '<div class="epAll"(.+?)<div class="col-xl-12 col-lg-12 col-md-12 col-sm-12">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern) 
     
    
    if (aResult[0]):
        sHtmlContent1 = aResult[1][0]
	
     # (.+?) ([^<]+) .+?
    sPattern = '<a href="([^<]+)>([^<]+)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent1, sPattern)
	
	
    if aResult[0]:  
        oOutputParameterHandler = cOutputParameterHandler()                     
        for aEntry in aResult[1]:
 
            sTitle = aEntry[1].replace("الحلقة "," E")
            sTitle = sMovieTitle+sTitle
            siteUrl = aEntry[0].replace('" class="active',"")
            sThumb = sThumb
            sDesc = sNote
			


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addEpisode(SITE_IDENTIFIER, 'showLink', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
        
 
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showEpisodes', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
	
def showLink():
    oGui = cGui()
    
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    oParser = cParser()

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sPattern = 'player_iframe.location.href = ["\']([^"\']+)["\'].+?</i>(.+?)</a>'
    aResult = oParser.parse(sHtmlContent, sPattern)	
    if aResult[0]:
   #     xbmcgui.Dialog().ok("aResult",str(aResult))
        for aEntry in aResult[1]:

         sHosterUrl = aEntry[0]
         sHoster = aEntry[1]
         sTitle = f'{sMovieTitle} ({sHoster})'
         oHoster = cHosterGui().getHoster('faselhd') 
         if oHoster:
                oHoster.setDisplayName(sTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb) 
        pass
    '''''
    
    oParser = cParser()
    
    #Recuperation infos
    sNote = ''

    sPattern = '<div class="singlePage">.+?<p>([^<]+)</p>'
    aResult = oParser.parse(sHtmlContent, sPattern)
 
    soup = BeautifulSoup(sHtmlContent, 'html.parser')
    xid=soup.find_all("div",id="singleDesc")
    xbmcgui.Dialog().ok("html",str (xid) )
    if (aResult[0]):
        sNote = aResult[1][0]
        xbmcgui.Dialog().ok("text",str(sNote))   
       
     # (.+?) ([^<]+) .+?
    sPattern = 'onclick="player_iframe.location.href = ([^<]+)"><a.+?href="javascript:;"><i.+?class="fa fa-play-circle"></i>([^<]+)</a></li>'


    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    #VSlog("Link Pattern :" +sPattern)
    #VSlog(aResult)
   
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()    
        for aEntry in aResult[1]:
 
            if "01#" not in aEntry[1]:
                continue
 
            sTitle = aEntry[1].replace("&#8217;", "'") 
            siteUrl = aEntry[0].replace("'", "") 


 

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            

 
            oGui.addLink(SITE_IDENTIFIER, 'showHosters', sTitle, sThumb, sNote, oOutputParameterHandler)

    # (.+?)

    sPattern = 'player_iframe.location.href = ["\']([^"\']+)["\'].+?</i>(.+?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    #VSlog("Link Pattern :" +sPattern)
    #VSlog(aResult)
	
    if aResult[0]:
        for aEntry in aResult[1]:
 
            if "embed.php?url=" in aEntry:
               continue
            
            url = aEntry.replace("'", "")
          
            if url.startswith('//'):
               url = 'http:' + url
            
            sHosterUrl = aEntry[0]
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            xbmcgui.Dialog().ok("n",str(sHosterUrl))  
            if oHoster:
               oHoster.setDisplayName(sMovieTitle)
               oHoster.setFileName(sMovieTitle)
               cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)'''
				

    oGui.setEndOfDirectory()       
  
def __checkForNextPage(sHtmlContent):
    sPattern = "<li class=\"page-item disabled active\"><span class=\"page-link\">(.+?)</span>"
	
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
 
    if aResult[0]:
        currentPage = aResult[1][0]
        #VSlog('currentPage : ' + currentPage)
        AllPagesPattern = '<li class=\"page-item\"><a class=\"page-link\" href=\"(.+?)\">(.+?)</a></li>'
        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, AllPagesPattern)
        #VSlog(aResult)
        if aResult[0]:
            for res in aResult[1]:
                #VSlog('PAGE : ' + str(res))
                if res[1] > currentPage or res[1] == '›':
                    return res[0]
    else:
        return aResult[0]
import xbmcgui
def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    # (.+?)
 

    sPattern = 'name="iframe" src="([^<]+)" frameborde'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

	
    if aResult[0]:
        for aEntry in aResult[1]:
            xbmcgui.Dialog().ok("host",aEntry)
            url = aEntry
            sTitle = " " 
            if url.startswith('//'):
               url = 'http:' + url
            
            sHosterUrl = url 
          
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
               sDisplayTitle = sMovieTitle+sTitle
               oHoster.setDisplayName(sDisplayTitle)
               oHoster.setFileName(sMovieTitle)
               cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
				
               
        
    sPattern = 'file: "(.+?)",type: "hls",'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

	
    if aResult[0]:
        for aEntry in aResult[1]:
            
            url = aEntry
            sTitle = " " 
            if url.startswith('//'):
               url = 'http:' + url
            
            sHosterUrl = url
            xbmcgui.Dialog().ok("",sHosterUrl)
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
               sDisplayTitle = sMovieTitle+sTitle
               oHoster.setDisplayName(sDisplayTitle)
               oHoster.setFileName(sMovieTitle)
               cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
				
               
        
    sPattern = 'file: "(.+?)",.+?"type": "hls",'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

	
    if aResult[0]:
        for aEntry in aResult[1]:
            
            url = aEntry
            sTitle = " "
            if url.startswith('//'):
               url = 'http:' + url
            
            sHosterUrl = url
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sDisplayTitle = sMovieTitle+sTitle
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
				                        
    sPattern = '<a href="(.+?)" class="download-btn" '
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

	
    if aResult[0]:
        for aEntry in aResult[1]:
            
            url = aEntry
            sTitle = " " 
            if url.startswith('//'):
               url = 'http:' + url
            
            sHosterUrl = url
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
               sDisplayTitle = sMovieTitle+sTitle
               oHoster.setDisplayName(sDisplayTitle)
               oHoster.setFileName(sMovieTitle)
               cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
				

                
    oGui.setEndOfDirectory()
    pass
# https://github.com/MatrixFlix/Dist/blob/main/repo/plugin.video.matrixflix/resources/hosters/faselhd.p
def decode_page(data):
    t_script = re.findall('var adilbo.*?;.*?\'(.*?);', data, re.S)
    t_int = re.findall('/g.....(.*?)\)', data, re.S)
    if t_script and t_int:
        script = t_script[0].replace("'",'')
        script = script.replace("+",'')
        script = script.replace("\n",'')
        sc = script.split('.')
        page = ''
        for elm in sc:
            try:
                c_elm = base64.b64decode(elm + "==").decode('utf-8')
                t_ch = re.findall(r"(\d+)", c_elm)
                if t_ch:
                    nb = int(t_ch[0]) + int(t_int[0])
                    page += chr(nb)
            except Exception:
                continue
        
        return page
    else:
        return ""