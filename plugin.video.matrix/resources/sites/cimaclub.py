# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/

import re
import socket
import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.parse as paseurl
from urllib.parse import urlparse, parse_qs
import  xbmcgui
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.comaddon import VSlog, siteManager, addon
from resources.lib.parser import cParser

ADDON = addon()
icons = ADDON.getSetting('defaultIcons')

SITE_IDENTIFIER = 'cimaclub'
SITE_NAME = 'Cimaclub'
SITE_DESC = 'arabic vod'
 
URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

oParser = cParser()
 
oRequestHandler = cRequestHandler(URL_MAIN)
sHtmlContent = oRequestHandler.request()
    # (.+?) ([^<]+)

sPattern = '<a href="([^<]+)" class="logo">'
aResult = oParser.parse(sHtmlContent, sPattern)
    
if (aResult[0]):
    URL_MAIN = aResult[1][0]
    VSlog(URL_MAIN) 
	
MOVIE_FAM = (URL_MAIN + '/getposts?genre=%D8%B9%D8%A7%D8%A6%D9%84%D9%8A&category=1', 'showMovies')
MOVIE_TOP = (URL_MAIN + '/getposts?type=one&data=rating', 'showMovies')
MOVIE_EN = (URL_MAIN + "/category/افلام-اجنبي/", 'showMovies')
MOVIE_AR = (URL_MAIN + '/category/افلام-عربي/', 'showMovies')
MOVIE_TURK = (URL_MAIN +'/category/أفلام2/افلام-تركى-2/', 'showMovies')
MOVIE_HI = (URL_MAIN + '/category/افلام-هندي/', 'showMovies')
MOVIE_ASIAN = (URL_MAIN + '/category/%D8%A7%D9%81%D9%84%D8%A7%D9%85-%D8%A7%D8%B3%D9%8A%D9%88%D9%8A%D8%A9', 'showMovies')
KID_MOVIES = (URL_MAIN + '/category/افلام-كرتون-2/', 'showMovies')
MOVIE_MOVIE = (True, 'load')
RAMADAN_SERIES = (URL_MAIN + '/category/مسلسلات-3/مسلسلات-رمضان-2024/', 'showSerie')


SERIE_AR= (URL_MAIN + '/category/مسلسلات-عربي/', 'showSerie')
SERIE_LATIN = (URL_MAIN + '/category/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA-%D8%A8%D8%B1%D8%A7%D8%B2%D9%8A%D9%84%D9%8A%D8%A9', 'showSerie')
SERIE_DUBBED = (URL_MAIN + 'category/مسلسلات-مدبلجة/', 'showSerie')
SERIE_ASIA = (URL_MAIN + '/category/مسلسلات-اسيوية/', 'showSerie')
SERIE_TR = (URL_MAIN + '/category/مسلسلات-تركية/', 'showSerie')
SERIE_EN = (URL_MAIN + '/category/مسلسلات-اجنبي/', 'showSerie')
SERIE_GENRES = (True, 'showGenres')
ANIM_NEWS = (URL_MAIN + '/category/مسلسلات-انمي/', 'showSerie')
DOC_NEWS = (URL_MAIN + '/category/%D8%A7%D9%81%D9%84%D8%A7%D9%85-%D9%88%D8%AB%D8%A7%D8%A6%D9%82%D9%8A%D8%A9', 'showMovies')
DOC_SERIES = (URL_MAIN + '/category/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA-%D9%88%D8%AB%D8%A7%D8%A6%D9%82%D9%8A%D8%A9', 'showSerie')
SPORT_NEWS = (URL_MAIN + '/category/%D8%A7%D9%84%D9%85%D8%B5%D8%A7%D8%B1%D8%B9%D9%87-wwe', 'showMovies')
URL_SEARCH = (URL_MAIN + '/search?s=', 'showMovies')
URL_SEARCH_MOVIES = (URL_MAIN + '/?s=', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '/?s=', 'showSerie')
URL_SEARCH_MISC = (URL_MAIN + '/search?s=', 'showSerie')
FUNCTION_SEARCH = 'showMovies'

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' 
def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'SEARCH_MOVIES', icons + '/Search.png', oOutputParameterHandler)
	
    oGui.addDir(SITE_IDENTIFIER, 'showSeriesSearch', 'SEARCH_SERIES', icons + '/Search.png', oOutputParameterHandler)

  #  oGui.addDir(SITE_IDENTIFIER, 'showSearchAll', 'Search All', icons + '/Search.png', oOutputParameterHandler)
    
    oOutputParameterHandler.addParameter('siteUrl', RAMADAN_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات رمضان', icons + '/Ramadan.png', oOutputParameterHandler)
    
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أجنبية', icons + '/MoviesEnglish.png', oOutputParameterHandler)
   
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام عربية', icons + '/Arabic.png', oOutputParameterHandler)
 
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ASIAN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أسيوية', icons + '/Asian.png', oOutputParameterHandler)
   
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TURK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام تركية', icons + '/Turkish.png', oOutputParameterHandler)
    
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', icons + '/Hindi.png', oOutputParameterHandler)
   
    oOutputParameterHandler.addParameter('siteUrl', KID_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كرتون', icons + '/Cartoon.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSerie', 'مسلسلات أجنبية', icons + '/TVShowsEnglish.png', oOutputParameterHandler)
    oOutputParameterHandler.addParameter('siteUrl', SERIE_AR[0])
  #  oOutputParameterHandler.addParameter('siteUrl', 'https://www.cima-club.cc:2096/category/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA-%D8%B9%D8%B1%D8%A8%D9%8A%D8%A93')
    oGui.addDir(SITE_IDENTIFIER, 'showSerie', 'مسلسلات عربية', icons + '/Arabic.png', oOutputParameterHandler)
   
    oOutputParameterHandler.addParameter('siteUrl', SERIE_ASIA[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSerie', 'مسلسلات أسيوية', icons + '/Asian.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSerie', 'مسلسلات تركية', icons + '/Turkish.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', ANIM_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSerie', 'مسلسلات إنمي', icons + '/Anime.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', DOC_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام وثائقية', icons + '/Documentary.png', oOutputParameterHandler)
    
    oOutputParameterHandler.addParameter('siteUrl', DOC_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSerie', 'مسلسلات وثائقية', icons + '/Documentary.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SPORT_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'مصارعة', icons + '/WWE.png', oOutputParameterHandler)
    
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.cima-club.cc:2096/category/%D9%85%D8%B3%D8%B1%D8%AD%D9%8A%D8%A7%D8%AA-%D9%88%D8%B9%D8%B1%D9%88%D8%B6-%D8%AA%D9%84%D9%81%D8%B2%D9%8A%D9%88%D9%86%D9%8A%D9%87')
    oGui.addDir(SITE_IDENTIFIER, 'showSerie', 'عروض تلفزيونيه',icons + '/Programs.png', oOutputParameterHandler) 
    
    oGui.setEndOfDirectory()
 
def showSearchAll():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = ' https://cimaclubs.online/' + '?s='+sSearchText
        showSerie(sUrl)
        oGui.setEndOfDirectory()
        return  
 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        word_arabic(sSearchText,"فيلم")
       # search_url=' https://cimaclubs.online/'
        sUrl = URL_MAIN + '/?s='+sSearchText 
        xbmcgui.Dialog().ok("",sUrl)
        showMovies(sUrl)
    #    sreach(sUrl,"فيلم",True)
        oGui.setEndOfDirectory()
        return
 
def showSeriesSearch():
    oGui = cGui()
  
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        word_arabic(sSearchText,"مسلسل") 
        search_url=' https://cimaclubs.online/'
        sUrl = URL_MAIN+ '/?s='+sSearchText
        showSerie(sUrl)
     #   sreach(sUrl,"مسلسل",True)
        oGui.setEndOfDirectory()
        return
		
def showGenres():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
 
    liste = []
    liste.append( ["korean series","http://cimaclub.com/category/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA-%D9%83%D9%88%D8%B1%D9%8A%D8%A9/"] )
    liste.append( ["مسلسلات-رمضان-2016","http://cimaclub.com/category/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA-%D8%B9%D8%B1%D8%A8%D9%8A/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA-%D8%B1%D9%85%D8%B6%D8%A7%D9%86-2016/"] )
	            
    for sTitle,sUrl in liste:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showSerie', sTitle, icons + '/Genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()   
def Search_movie_marix(sSearch):
    surl=sSearch.replace(URL_MAIN,"https://cimaclubs.online")+"&types=افلام"
    sreach(surl,"فيلم",False)

def Search_Series_marix(sSearch):
    Result=  paramter(sSearch,'s')
    word_arabic(Result,"مسلسل")
    surl=sSearch.replace(URL_MAIN,"https://cimaclubs.online")+"&types=مسلسلات"
     
    sreach(surl,"مسلسل",False)

 #   # xbmcgui.Dialog().ok("",surl)
def paramter(url,para):
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)

    # Extract the 's' and 'types' parameters, fallback to None if not present
    parameter_search = params.get(para, [None])[0]
    return parameter_search

    pass
def word_arabic(sSearch,mov):  

  oGui = cGui()
  if re.search(r'[\u0600-\u06FF]', sSearch):
       if(mov=="فيلم"):
        siteUrl=f'https://cimaclub.watch/فيلم-{sSearch}'+"/see/"
   #     # xbmcgui.Dialog().ok("aResult",siteUrl)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',siteUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sSearch)
        oGui.addMovie(SITE_IDENTIFIER, 'showServers', sSearch, '', "", "", oOutputParameterHandler)
       else:
      
#       sSearch = "your_series_name"  # Replace this with the actual search string
        siteUrl = f"https://cimaclub.watch/مسلسل-{sSearch}-حلقة-1/".replace(" ","-")

# Check if the first URL is valid
   #    if check_url_Series(siteUrl):
   #     # xbmcgui.Dialog().ok("aResult",siteUrl)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',siteUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sSearch)
     #  oOutputParameterHandler.addParameter('sThumb', sSearch)
        oGui.addTV(SITE_IDENTIFIER, 'seasones', sSearch, '', "", '', oOutputParameterHandler)
     #  else:
       siteUrl=f'https://cimaclub.watch/مسلسل-{sSearch}-موسم-1-حلقة-1/'.replace(" ","-")
      #    if check_url_Series(siteUrl):
       # xbmcgui.Dialog().ok("aResult",siteUrl)
       oOutputParameterHandler = cOutputParameterHandler()
       oOutputParameterHandler.addParameter('siteUrl',siteUrl)
       oOutputParameterHandler.addParameter('sMovieTitle', sSearch)
     #  oOutputParameterHandler.addParameter('sThumb', sSearch)
       oGui.addTV(SITE_IDENTIFIER, 'seasones', sSearch, '', "", '', oOutputParameterHandler)
         
      #pass
    #https://cimaclub.watch/فيلم-وقت-إضافي-2024/
def check_url_Series(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            
            return False
    except requests.exceptions.RequestException as e:
       
        return False
   
def showMovies(sSearch=''):
    oGui = cGui()

    if sSearch:
        sUrl = sSearch
     #   xbmcgui.Dialog().ok("", sUrl)
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = r'<div class="Small--Box">\s*<a href="([^"]+)"[^>]*?>.*?<img src="([^"]+)"[^>]*?>.*?<h2>(.*?)</h2>'
    aResult = re.findall(sPattern, sHtmlContent, re.DOTALL)

    oParser = cParser()

    if aResult:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult:
            sTitle = aEntry[2]
            sTitle = sTitle.replace("مشاهدة", "").replace("مشاهده", "").replace("مترجم", "").replace("فيلم", "").replace("اون لاين", "").replace("اونلاين", "").replace("برنامج", "").replace("بجودة", "").replace("WEB-DL", "").replace("BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace("HD-CAM", "").replace("DVDRip", "").replace("BluRay", "").replace("1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("4K", "").replace("BDRip", "").replace("HDCAM", "").replace("HDTC", "").replace("HDTV", "").replace("HD", "").replace("720", "").replace("HDCam", "").replace("Full HD", "").replace("1080", "").replace("HC", "").replace("Web-dl", "").replace("مدبلج للعربية", "مدبلج").replace("انيمي", "")
            sThumb = aEntry[1].replace('(', '').replace(')', '')
            siteUrl = aEntry[0].replace('/film/', '/watch/').replace('/post/', '/watch/')
            siteUrl = siteUrl + "watch/"

            sDesc = ''
            sYear = ''
            m = re.search(r'([1-2][0-9]{3})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear, '')

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle.strip())
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addMovie(SITE_IDENTIFIER, 'showServers', sTitle.strip(), '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()

def sreach(sUrl,search,flag=False ):
    oGui = cGui()
    # Initialize the input and request handlers
    oInputParameterHandler = cInputParameterHandler()
    oRequestHandler = cRequestHandler(sUrl)
    match = re.search(r'/page/(\d+)/', sUrl)
    next_page = int(match.group(1)) if match else 1
  #  next_page = oInputParameterHandler.getValue("next_page")
   
    sreachSurl=sUrl
    
  #  new_page=sUrl.replace("/?s","/page/*newpage/?s")
    
   # # xbmcgui.Dialog().ok("new_page``", new_page)
  #  # xbmcgui.Dialog().ok("Block Post",sUrl )
    

    # Make a request to get the HTML content
    sHtmlContent = oRequestHandler.request()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(sHtmlContent, 'html.parser')

    # Find the div with class "block-post"
    html = soup.find_all('div', class_='col-xs-6th col-sm-6th col-md-6th col-lg-6th')
    sPattern = r'<a href="([^"]*)" title="([^"]*)">\s*<div class="poster"><img[^>]*data-img="([^"]*)"'


   
    # Check if the div was found and display its content
    if html:
       for aEntry in html:
         div_content = str(aEntry)
            
            # Use re.search to find the title in the <a> tag
         match = re.search(sPattern, div_content)
         url=match[1]
         encoded_string=url
         decoded_string = urllib.parse.unquote(encoded_string)
         oOutputParameterHandler = cOutputParameterHandler() 
          #https://cimaclub.watch/فيلم-#f-مترجم/
          #https://cimaclubs.online/movies/فيلم-long-gone-heroes-2024-مترجم-اون-لاين/
         if search=="فيلم":
          
          if  search in  decoded_string:
       
           sUrl="https://cimaclub.watch/فيلم-#f-مترجم/"
         
           namefile=decoded_string.replace("https://cimaclubs.online/movies/فيلم-","" ).replace("-مترجم-اون-لاين/","").replace("HD","").replace("مشاهدة","").replace("كامل","")
           sUrl=sUrl.replace("#f",namefile)+"see/"
           

           sTitle = match[2].replace("فيلم","").replace("لاين", "").replace("مترجم","").replace("اون","").replace("HD","").replace("مشاهدة","").replace("كامل","").replace("(", "").replace(")", "").replace(" ", "-")
           if re.search(r'[\u0600-\u06FF]', sTitle):
            sUrl = f'https://cimaclub.watch/فيلم-{sTitle}/see/'
        #    # xbmcgui.Dialog().ok("",sUrl)
      #      pass
          else:   
             sUrl=f"https://cimaclub.watch/فيلم-{sTitle}-مترجم/".replace(" ", "-")+"see/"
           

          sThumb = match[3]
          oOutputParameterHandler.addParameter('siteUrl',sUrl)
          oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
          oOutputParameterHandler.addParameter('sThumb', sThumb)
          oGui.addMovie(SITE_IDENTIFIER, 'showServers', sTitle, '', sThumb, "", oOutputParameterHandler)
      #    # xbmcgui.Dialog().ok("url", sUrl)
         #https://cimaclubs.online/page/2/?s=den&types=%D8%A7%D9%81%D9%84%D8%A7%D9%85&types=%D8%A7%D9%81%D9%84%D8%A7%D9%85
         #https://cimaclubs.online/?s=den&types=%D8%A7%D9%81%D9%84%D8%A7%D9%85

         elif search=="مسلسل":
             
              if  search in  decoded_string:
            #   decoded_string=re.sub("-\d+-","",decoded_string)
            #   # xbmcgui.Dialog().ok("url", decoded_string)
               sUrl="https://cimaclub.watch/مسلسل-#f-موسم-1-حلقة-1/"
               namefile = decoded_string.replace("https://cimaclubs.online/series/مسلسل-", "").replace("-مترجم", " ") .replace("-الموسم","") .replace("/","").replace("HD","")            
               namefile = re.sub(r'-\d+-', '', namefile)
               namefile = re.sub(r'-\d+', '', namefile)
               namefile = namefile.replace(" ", "")
            #   # xbmcgui.Dialog().ok("namefile", namefile)
               sUrl=sUrl.replace("#f",namefile)
             #  # xbmcgui.Dialog().ok("namefile", namefile)
            #   # xbmcgui.Dialog().ok("namefile", sUrl)

               sTitle =namefile.replace("-","  ")

               sThumb = match[3]
               oOutputParameterHandler.addParameter('siteUrl',sUrl)
               oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
               oOutputParameterHandler.addParameter('sThumb', sThumb)
               oGui.addTV(SITE_IDENTIFIER, 'seasones', sTitle, '', sThumb, '', oOutputParameterHandler)
            
            
            
              pass
    else:
   #     # xbmcgui.Dialog().ok("Block Post", "No div found")
        pass
   
  #  next_page = next_page + 1

   # # xbmcgui.Dialog().ok("message", next_page)
  #  new_page = new_page.replace("*newpage", str(next_page)) 

   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sreachSurl)
    oOutputParameterHandler.addParameter('next_page', next_page+1)
    
    ##;types=افلام
    oGui.addDir(SITE_IDENTIFIER, 'next_pages', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
    if flag :
     oGui.setEndOfDirectory()
        
#\\\\\\\\\\\\

def next_pages():
     oGui = cGui()
     oInputParameterHandler = cInputParameterHandler()
    
    
    
     sUrl = oInputParameterHandler.getValue('siteUrl')
     next_page= oInputParameterHandler.getValue('next_page')
     parsed_url =paseurl.urlparse(sUrl)
     
     params = paseurl.parse_qs(parsed_url.query)

     prameter_sreach=params.get('s', [None])[0]
     prameter_type=params.get('types', [None])[0]
     ## xbmcgui.Dialog().ok("prameter_sreach", f'{next_page}')
     #types=افلام#038;types=افلام
     sreachSurl = f'https://cimaclubs.online/page/{next_page}/?s={prameter_sreach} &types= 038#{prameter_type};types={prameter_type}'
  
     if  prameter_type == 'افلام':

      sreach(sreachSurl,"فيلم",True)
     else :
      sreach(sreachSurl,"مسلسل",True)


     pass
def showSerie(sSearch = ''):
   # # xbmcgui.Dialog().ok("","hi")
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
   
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   #     # xbmcgui.Dialog().ok("",sUrl)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
 
     # (.+?) ([^<]+) .+?
  #  sPattern = '<div class="content-box">.+?<a href="(.+?)" title="(.+?)" class="fullClick"></a>.+?<img src="(.+?)" alt=.+?<span class="episode-block"><span>الحلقة </span><span>(.+?)</span>'
    sPattern = r'<div class="Small--Box">\s*<a href="([^"]+)"[^>]*?>.*?<img src="([^"]+)"[^>]*?>.*?<h2>(.*?)</h2>'

    titles= []
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()  
       
      #  nub = "123456789"
        for aEntry in aResult[1]:
 
            sTitle = aEntry[2].replace("مشاهدة","").replace("مشاهده","").replace("مسلسل","").replace("انيمي","").replace("انمي","").replace("انمى","").replace("مترجمة","").replace("برنامج","").replace("مترجم","").replace("مترجمة","").replace("فيلم","").replace("اون لاين","").replace("WEB-DL","").replace("BRRip","").replace("720p","").replace("HD-TC","").replace("HDRip","").replace("HD-CAM","").replace("DVDRip","").replace("BluRay","").replace("1080p","").replace("WEBRip","").replace("WEB-dl","").replace("مترجم ","").replace("مدبلج للعربية","مدبلج").replace("مشاهدة وتحميل","").replace("اون لاين","").replace("انيمي","").replace("كامل","") . replace("موسم ","") . replace("حلقة","").replace(" والاخيرة","").replace("والأخيرة","")
            sTitle=  re.sub("[0-9]", "", sTitle)
     #       # xbmcgui.Dialog().ok("",sTitle)
        #    siteUrl = aEntry[0].replace("/episode/","/watch/").replace("/post/","/watch/")
            siteUrl = aEntry[0]
          
            sThumb = aEntry[1].replace("(","").replace(")","")
            sDesc = ''
            sDisplayTitle = sTitle.replace("الموسم العاشر","S10").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الاول","S1").replace("الموسم الثانى","S2").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الموسم","S").replace("S ","S").split('الحلقة')[0].replace("الاخيرة","").replace("مترجم","").replace(" الحادي عشر","11").replace(" الثاني عشر","12").replace(" الثالث عشر","13").replace(" الرابع عشر","14").replace(" الخامس عشر","15").replace(" السادس عشر","16").replace(" السابع عشر","17").replace(" الثامن عشر","18").replace(" التاسع عشر","19").replace(" العشرون","20").replace(" الحادي و العشرون","21").replace(" الثاني و العشرون","22").replace(" الثالث و العشرون","23").replace(" الرابع والعشرون","24").replace(" الخامس و العشرون","25").replace(" السادس والعشرون","26").replace(" السابع والعشرون","27").replace(" الثامن والعشرون","28").replace(" التاسع والعشرون","29").replace(" الثلاثون","30").replace(" الحادي و الثلاثون","31").replace(" الثاني والثلاثون","32").replace(" الاول","1").replace(" الثاني","2").replace(" الثانى","2").replace(" الثالث","3").replace(" الرابع","4").replace(" الخامس","5").replace(" السادس","6").replace(" السابع","7").replace(" الثامن","8").replace(" التاسع","9").replace(" العاشر","10").replace("ال","")
       
            if "E" not in sDisplayTitle:
              
                sDisplayTitle=sDisplayTitle
                if sDisplayTitle  not in titles:
                   #  # xbmcgui.Dialog().ok("",sDisplayTitle)
                     titles.append(sDisplayTitle)

                     oOutputParameterHandler = cOutputParameterHandler()
                     oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                 
                     oOutputParameterHandler.addParameter('sMovieTitle', sDisplayTitle)
                     oOutputParameterHandler.addParameter('sThumb', sThumb)
			
                     oGui.addTV(SITE_IDENTIFIER, 'seasones', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)
            
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSerie', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
 
     # (.+?) ([^<]+) .+?
    
    sPattern = '<div class="content-box">.+?<a href="([^<]+)" data-src="([^<]+)" class="image"></a>.+?<h3>([^<]+)</h3></a>'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
	
	
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()  
        # xbmcgui.Dialog().ok("",  str(aResult[0]))
        for aEntry in aResult[1]:
 
            if "الحلقة" in aEntry[2]:
                continue
 
            if "فيلم" in aEntry[2]:
                continue
 
            sTitle = aEntry[2].replace("مشاهدة","").replace("مشاهده","").replace("مسلسل","").replace("انمي","").replace("انمى","").replace("مترجمة","").replace("برنامج","").replace("مترجم","").replace("مترجمة","").replace("فيلم","").replace("اون لاين","").replace("WEB-DL","").replace("BRRip","").replace("720p","").replace("HD-TC","").replace("HDRip","").replace("HD-CAM","").replace("DVDRip","").replace("BluRay","").replace("1080p","").replace("WEBRip","").replace("WEB-dl","").replace("مترجم ","").replace("مشاهدة وتحميل","").replace("اون لاين","").replace("كامل","").replace("انيمي","") 
            siteUrl = aEntry[0].replace("/episode/","/watch/").replace("/post/","/watch/")
            sThumb = aEntry[1].replace("(","").replace(")","")
            sDesc = ''
            sDisplayTitle = sTitle.replace("الموسم العاشر","S10").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الاول","S1").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الموسم","S").replace("موسم","S").replace("S ","S").split('الحلقة')[0]


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sDisplayTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
			
            if 'season' in siteUrl:
                oGui.addTV(SITE_IDENTIFIER, 'showEpisodes1', sDisplayTitle, '', sThumb, '', oOutputParameterHandler)
            else:
                oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sDisplayTitle, '', sThumb, '', oOutputParameterHandler)

 
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSerie', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
 
    if not sSearch:
        oGui.setEndOfDirectory()
def seasones():		
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
   # xbmcgui.Dialog().ok("",sUrl)
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    pattern = r'<section[^>]*class="allseasonss"[^>]*>(.*?)</section>'
    ul_content = re.search(pattern, sHtmlContent, re.DOTALL)
   # xbmcgui.Dialog().ok("xx",str( (ul_content.group(1))))
  #  sPattern =r'<a href="(https://cimaclub.org/[^"]+)">([^<]+)</a>'
    sPattern = r'<div class="Small--Box">.*?<a href="(.*?)".*?<div class="epnum"><span>الموسم</span>\s*(\d+)</div>.*?<div class="Poster">\s*<img[^>]*data-src="(.*?)"'


 
    oParser = cParser()
    aResult = re.findall(sPattern,  ul_content.group(1), re.DOTALL)
   # xbmcgui.Dialog().ok("x1",str( bool(aResult)))
    for aEntry in aResult:
     sUrl, season, sThumb = aEntry
  #   xbmcgui.Dialog().ok("sThumb",str(sThumb))
    # sThumb="https://snworksceo.imgix.net/bdh/3cfb9f33-e632-458b-ab23-bd8e755ec767.sized-1000x1000.jpg"
   
    #    "img_class": aEntry[2],
    
     oOutputParameterHandler = cOutputParameterHandler()
     oOutputParameterHandler.addParameter('siteUrl', sUrl)
     oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
     oOutputParameterHandler.addParameter('sThumb', sThumb)
   # oOutputParameterHandler.addParameter("season",f"{index+1}")
    oGui.addEpisode(SITE_IDENTIFIER, 'showEpisodes' '', sMovieTitle +season,'', sThumb,'', oOutputParameterHandler)
#    xbmcgui.Dialog().ok("ul_content",str( bool(aResult)))
   
    
    # في حال عدم وجود مواسم متعددة
    

    # oGui.setEndOfDirectory()  # يمكنك فك هذا السطر إذا كان مطلوبًا

        
    oGui.setEndOfDirectory()
    pass
#end
def showEpisodes():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    season = oInputParameterHandler.getValue('season')
    
    str_season="موسم"
    Ns = f"-{season}-"
  #  xbmcgui.Dialog().ok("",str_season+Ns)
    is_mach=str_season+Ns
    sMovie_Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
 # ([^<]+) .+?
    pattern =r'<section class="allepcont getMoreByScroll">(.*?)</section>'
    section_content = re.search(pattern, sHtmlContent, re.DOTALL)
   # xbmcgui.Dialog().ok("aResult",str(bool (section_content)))
    sPattern = r'<a href="(?P<url>[^"]+)"[^>]*>.*?<img src="(?P<img>[^"]+)"[^>]*>.*?<span>الحلقة</span>\s*(?P<episode>\d+)'

    oParser = cParser()
    aResult = re.findall(sPattern,  section_content.group(1), re.DOTALL)
   
	
#	aResult = re.findall(sPattern, sHtmlContent, re.DOTALL)
    if aResult:
     oOutputParameterHandler = cOutputParameterHandler()  
     if  not season :
      for aEntry in aResult:
            
            sUrl=aEntry[0]+"watch/"
            sMovieTitle = f"   {sMovie_Title}  [COLOR red] EP {str(aEntry[2])} [/COLOR] "
          #  sMovieTitle.replace("مشاهدة","").replace("مشاهده","").replace("مسلسل","").replace("انمي","").replace("انمى","").replace("مترجمة","").replace("برنامج","").replace("مترجم","").replace("مترجمة","").replace("فيلم","").replace("اون لاين","").replace("WEB-DL","").replace("BRRip","").replace("720p","").replace("HD-TC","").replace("HDRip","").replace("HD-CAM","").replace("DVDRip","").replace("BluRay","").replace("1080p","").replace("WEBRip","").replace("WEB-dl","").replace("مترجم ","").replace("مشاهدة وتحميل","").replace("اون لاين","").replace("كامل","").replace("انيمي","")
    #        # xbmcgui.Dialog().ok("",aEntry[0])
            oOutputParameterHandler.addParameter('siteUrl',sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle' ,sMovieTitle )
            encoded_string= sUrl
            decoded_string = urllib.parse.unquote(encoded_string)
         #   if "موسم" in sUrl:
         #   # xbmcgui.Dialog().ok("",decoded_string)
            oGui.addEpisode(SITE_IDENTIFIER, 'showServers',f" {sMovieTitle} ", '', sThumb, "", oOutputParameterHandler)



      pass
     else:
      for aEntry in aResult:
            
            sUrl=aEntry[0]+"see/"
            encoded_string= sUrl
            decoded_string = urllib.parse.unquote(encoded_string)
         
            if is_mach in decoded_string: 

           
              sMovieTitle=aEntry[1]
    #        # xbmcgui.Dialog().ok("",aEntry[0])
              oOutputParameterHandler.addParameter('siteUrl',sUrl)
              oOutputParameterHandler.addParameter('sMovieTitle', f"S{Ns.replace('-', '')}{sMovie_Title.replace('الحلقة', 'Ep')} {sMovieTitle}")

          
         #   if "موسم" in sUrl:
         #   # xbmcgui.Dialog().ok("",decoded_string)
              oGui.addEpisode(SITE_IDENTIFIER, 'showServers',f"[COLOR red](S{Ns.replace('-', '')})[/COLOR] {sMovie_Title} {sMovieTitle.replace('الحلقة', 'Ep')}", '', sThumb, '', oOutputParameterHandler)
     oGui.setEndOfDirectory()
     pass
    
          
    
        # عرض الرابط والعنوان باستخدام # xbmcgui.Dialog
       # # xbmcgui.Dialog().ok(title, link
    else:
        pass
      # xbmcgui.Dialog().ok("worring", "no")
    #worried
    # '''
    if aResult:
      
        oOutputParameterHandler = cOutputParameterHandler()  
        for aEntry in aResult:
      #      # xbmcgui.Dialog().ok("",aEntry[0])
 
            siteUrl = aEntry[0].replace("/episode/","/watch/").replace("/post/","/watch/")
            if 'season' in siteUrl:
                sTitle = sMovieTitle+" S"+aEntry[2]
            else:
                sTitle = sMovieTitle+" E"+aEntry[2]
            sThumb = sThumb
            sDesc = ""
			


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
			
            if 'season' in siteUrl:
                oGui.addSeason(SITE_IDENTIFIER, 'showEpisodes1', sMovieTitle+" S"+aEntry[2], '', sThumb, '', oOutputParameterHandler)
            else:
                oGui.addEpisode(SITE_IDENTIFIER, 'showServers', sMovieTitle.replace(" موسم "," S")+" E"+aEntry[2], '', sThumb, '', oOutputParameterHandler)
        
 
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showEpisodes', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
	#'''''wix
def showEpisodes1():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
 # ([^<]+) .+?

    sPattern = '<a href="([^<]+)" class="col-6 col-s-4 col-m-3 col-l-1 button-block"><h3>([^<]+)<span>([^<]+)</span></h3></a>'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
	
	
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()  
        for aEntry in aResult[1]:
 
            if 'season' in aEntry[0]:
                continue
 
            sTitle = ""
            siteUrl = aEntry[0].replace("/episode/","/watch/").replace("/post/","/watch/")
            sThumb = sThumb
            sDesc = ""
			

            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle+" E"+aEntry[2])
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addEpisode(SITE_IDENTIFIER, 'showServers', sMovieTitle+" E"+aEntry[2], '', sThumb, '', oOutputParameterHandler)
       
 
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showEpisodes', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
	
def showSeries():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
 
    sPattern = 'id="WatchBTn" href="([^<]+)" class'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
	
	
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()  
        for aEntry in aResult[1]:
 
            sTitle = sMovieTitle
            siteUrl = aEntry
			

            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', aEntry[1])
            oOutputParameterHandler.addParameter('sThumb', sThumb)
			
            if 'seasons' in sUrl:
                oGui.addSeason(SITE_IDENTIFIER, 'showSeries', aEntry[1], '', sThumb, '', oOutputParameterHandler)
            else:
                oGui.addEpisode(SITE_IDENTIFIER, 'showServers', aEntry[1], '', sThumb, '', oOutputParameterHandler)
        
 
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', icons + '/Next.png', oOutputParameterHandler)
       
        oGui.setEndOfDirectory()
 
def __checkForNextPage(sHtmlContent):
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern =r'<a class="page-numbers" href="([^"]+)"[^>]*>\d+</a>'
	
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
 
    if aResult[0]:
       
        parsed_url = urlparse(sUrl)
       # # xbmcgui.Dialog().ok("",  sUrl )

# Extract query parameters
        query_params = parse_qs(parsed_url.query)

# Get the 'page' parameter value
        page_value = query_params.get('page', [None])[0]

# Check if page_value is not None before trying to use replace
        if page_value:
          page_value =  int(page_value.replace('/', ''))
          returnRul = sUrl.replace(f"?page={page_value}/", f"?page={page_value + 1}/")
      #    # xbmcgui.Dialog().ok("",  returnRul )

        else:
         page_value = "Page parameter not found"
         returnRul=f"{sUrl}?page=2/ "
   #     # xbmcgui.Dialog().ok("",  returnRul )
        return returnRul

    return False
  
def showServers():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
  #  xbmcgui.Dialog().ok("address",sUrl )

    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
 
    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
    oRequestHandler.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    oRequestHandler.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
    oRequestHandler.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
    sHtmlContent = oRequestHandler.request()

   
    oParser = cParser()
    
    #Recuperation infos

    sPattern =r'<i\s+class="([^"]*fa-youtube[^"]*)"></i>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if aResult and len(aResult[1]) > 0:
        spost = aResult[1][0]
  #      # xbmcgui.Dialog().ok("Success", "Post ID found: " + spost)
    # (.+?) ([^<]+) .+?

    sPattern =r'data-watch="(https?://[^\s]+)"'

    aResult = re.findall(sPattern, sHtmlContent)

# Check if we found matches
    if aResult and len(aResult) > 0:
     spost = aResult[0]  # First match
  #   # xbmcgui.Dialog().ok("Success", "Post ID found: " + spost)
    else:
        pass
     # xbmcgui.Dialog().ok("Error", "No match found")

# Loop through the results (if any)
    for aEntry in aResult:
  #   # xbmcgui.Dialog().ok("aEntry loop", aEntry)
  #   # xbmcgui.Dialog().ok("aEntry loop: " + aEntry)
            
#

     sId = URL_MAIN + '/ajaxCenter?_action=getserver&_post_id='+spost
     siteUrl = sId+'&serverid='+aEntry[0]
     ## xbmcgui.Dialog().ok("siteUrl :", siteUrl)
			
     oRequestHandler = cRequestHandler(siteUrl)
     oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
     oRequestHandler.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
     oRequestHandler.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
     oRequestHandler.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
     sData = oRequestHandler.request()
     sPattern = r'>([^<]+)<'
     oParser = cParser()
    # aResult = re.findall(sData, sPattern)
 #   sPattern = r'>([^<]+)<' 
 #   aResult = re.findall(sPattern, sData,re.DOTALL)

   # if aResult:
  #   # xbmcgui.Dialog().ok("Parsed Data", str(aResult))
 #    pass
  #  else:
#     # xbmcgui.Dialog().ok("No Data Found", "No matches for the pattern.")
#     pass
	
    if aResult:
              
               for aEntry in aResult:
                   ## xbmcgui.Dialog().ok("aEntry ", str(aEntry))
        
                   url = str(aEntry).strip()
                 #  # xbmcgui.Dialog().ok("url", url)
                   sTitle = " "
                   sThumb = sThumb
                   if 'govid' in url:
                      url = url.replace("play","down").replace("embed-","")
                   if url.startswith('//'):
                      url = 'http:' + url
								            
                   sHosterUrl = url
                   if 'nowvid' in sHosterUrl:
                       sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
                   if 'kvid' in sHosterUrl:
                       sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
                   if 'userload' in sHosterUrl:
                       sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
                   if 'mystream' in sHosterUrl:
                       sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN  
                   if 'telvod' in sHosterUrl:
                       sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN 
						   
                   oHoster = cHosterGui().checkHoster(sHosterUrl)
                   if oHoster:
                      sDisplayTitle = sMovieTitle
                      oHoster.setDisplayName(sDisplayTitle)
                      oHoster.setFileName(sMovieTitle)
                      cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
       	
    sPattern = 'rel="nofollow" href="(.+?)" class'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

	
    if aResult[0]:
        for aEntry in aResult[1]:
            
            url = str(aEntry)
            sTitle = sMovieTitle
            if url.startswith('//'):
               url = 'http:' + url
				
					
            
            sHosterUrl = url 
            if 'nowvid' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'userload' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'moshahda' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN   
            if 'darkveed' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN 
            if 'telvod' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN  
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
               sDisplayTitle = sTitle
               oHoster.setDisplayName(sDisplayTitle)
               oHoster.setFileName(sMovieTitle)
               cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

     
    oGui.setEndOfDirectory()	
   

  
def showServers1():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
 #   # xbmcgui.Dialog().ok("addrees",sUrl )
 
    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
    oRequestHandler.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    oRequestHandler.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
    oRequestHandler.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
    sHtmlContent = oRequestHandler.request()

   
    oParser = cParser()
    
    #Recuperation infos

    sPattern = '&_post_id=([^<]+)",'
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0]):
        spost = aResult[1][0]
    # (.+?) ([^<]+) .+?

    sPattern = 'data-embedd="(.+?)">(.+?)<'
    aResult = oParser.parse(sHtmlContent, sPattern)

   
    if aResult[0]:
        for aEntry in aResult[1]:


            sId = URL_MAIN + '/ajaxCenter?_action=getserver&_post_id='+spost
            siteUrl = sId+'&serverid='+aEntry[0]
			
            oRequestHandler = cRequestHandler(siteUrl)
            oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
            oRequestHandler.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
            oRequestHandler.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
            oRequestHandler.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
            sData = oRequestHandler.request()
   
            sPattern = '([^<]+)'
            oParser = cParser()
            aResult = oParser.parse(sData, sPattern)
	
            if aResult[0]:
               for aEntry in aResult[1]:
        
                   url = str(aEntry)
                   sTitle = " "
                   sThumb = sThumb
                   if 'govid' in url:
                      url = url.replace("play","down").replace("embed-","")
                   if url.startswith('//'):
                      url = 'http:' + url
								            
                   sHosterUrl = url
                   if 'nowvid' in sHosterUrl:
                       sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
                   if 'kvid' in sHosterUrl:
                       sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
                   if 'userload' in sHosterUrl:
                       sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
                   if 'mystream' in sHosterUrl:
                       sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN  
                   if 'telvod' in sHosterUrl:
                       sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN 
						   
                   oHoster = cHosterGui().checkHoster(sHosterUrl)
                   if oHoster:
                      sDisplayTitle = sMovieTitle
                      oHoster.setDisplayName(sDisplayTitle)
                      oHoster.setFileName(sMovieTitle)
                      cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
       	
    sPattern = 'rel="nofollow" href="(.+?)" class'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

	
    if aResult[0]:
        for aEntry in aResult[1]:
            
            url = str(aEntry)
            sTitle = sMovieTitle
            if url.startswith('//'):
               url = 'http:' + url
				
					
            
            sHosterUrl = url 
            if 'nowvid' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'userload' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'moshahda' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN   
            if 'darkveed' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN 
            if 'telvod' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN  
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
               sDisplayTitle = sTitle
               oHoster.setDisplayName(sDisplayTitle)
               oHoster.setFileName(sMovieTitle)
               cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

     
    oGui.setEndOfDirectory()	
def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')



    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
    oRequestHandler.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    oRequestHandler.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
    oRequestHandler.addHeaderEntry('Accept-Language', 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3')
    sHtmlContent = oRequestHandler.request()

    sPattern = '([^<]+)'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0]:
        for aEntry in aResult[1]:
        
            url = str(aEntry)
            sTitle = " "
            if 'govid' in url:
               url = url.replace("play","down").replace("embed-","")
            if url.startswith('//'):
               url = 'http:' + url
				
					
            
            sHosterUrl = url
            if 'nowvid' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN 
            if 'telvod' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN 
            if 'userload' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'moshahda' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN   
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
               sDisplayTitle = sMovieTitle+sTitle
               oHoster.setDisplayName(sDisplayTitle)
               oHoster.setFileName(sMovieTitle)
               cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
				
		
                
    oGui.setEndOfDirectory()