# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/

import re
import xbmcgui
import base64
import requests
from urllib.parse import unquote
from requests.compat import urlparse
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.comaddon import VSlog, siteManager, addon
from resources.lib.parser import cParser
from bs4 import BeautifulSoup

ADDON = addon()
icons = ADDON.getSetting('defaultIcons')

from resources.lib.multihost import cVidsrcto, cVidsrcnet
SITE_IDENTIFIER = 'cimau'
SITE_NAME = 'Cima4u'
SITE_DESC = 'arabic vod'
 
URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)


RAMADAN_SERIES = (URL_MAIN + '/search/label/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA%20%D8%B1%D9%85%D8%B6%D8%A7%D9%86%202024', 'showSeries')
MOVIE_EN = (URL_MAIN + 'category/all-content-5/movies-5/افلام-اجنبي-3/', 'showMovies')
MOVIE_AR = (URL_MAIN + '/category/all-content-5/movies-5/افلام-عربى-4/', 'showMovies')
MOVIE_HI = (URL_MAIN + '/category/all-content-5/movies-5/افلام-هندى-4/', 'showMovies')
MOVIE_TUK = (URL_MAIN + '/category/all-content-5/movies-5/افلام-تركى-4/', 'showMovies')
KID_MOVIES = (URL_MAIN + '/category/all-content-5/movies-5/افلام-كرتون-4/', 'showMovies')
MOVIE_NETFLIX = (URL_MAIN + '/category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%a7%d8%ac%d9%86%d8%a8%d9%8a-movies7-english/netflix-movie/', 'showMovies')

SERIE_TR = (URL_MAIN + '/category/all-content-5/مسلسلات-7/مسلسلات-تركية-4/', 'showSeries')
SERIE_EN = (URL_MAIN + 'category/all-content-5/مسلسلات-7/مسلسلات-اجنبي-4/', 'showSeries')
SERIE_AR = (URL_MAIN + '/category/all-content-5/مسلسلات-7/مسلسلات-عربية-4/', 'showSeries')
SERIE_ASIA = (URL_MAIN + '/category/all-content-5/مسلسلات-7/مسلسلات-اسيوية-4/', 'showSeries')
SERIE_HEND = (URL_MAIN + '/category/all-content-5/مسلسلات-7/مسلسلات-هندية-4/', 'showSeries')
SERIE_LATIN = (URL_MAIN + '/category/مسلسلات-7series/latino-mexico/', 'showSeries')
SERIE_RAMADAN = (URL_MAIN + '/category/مسلسلات-رمضان-2024-4/', 'showSeries')
SPORT_WWE = (URL_MAIN + '/category/all-content-5/مسلسلات-7/مصارعة-حرة-4/', 'showSeries')
SERIE_ANIME = (URL_MAIN + '/category/all-content-5/مسلسلات-7/مسلسلات-كرتون-4/', 'showSeries')
REPLAYTV_PLAY = (URL_MAIN + '/category/series/%d8%a8%d8%b1%d8%a7%d9%85%d8%ac-%d8%aa%d9%84%d9%8a%d9%81%d8%b2%d9%8a%d9%88%d9%86%d9%8a%d8%a9-tv1-shows/', 'showSeries')
SERIE_NETFLIX = (URL_MAIN + '/category/series/series-netflix/', 'showSeries')

MOVIE_PACK = (URL_MAIN , '/category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%a7%d8%ac%d9%86%d8%a8%d9%8a-movies7-english/full-pack/')
URL_SEARCH = (URL_MAIN + '/?s=', 'showMovies')
URL_SEARCH_MOVIES = (URL_MAIN + '?s=', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '?s=', 'showSeries')
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
    
  #  oOutputParameterHandler.addParameter('siteUrl', MOVIE_NETFLIX[0])
   # oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام Netflix', icons + '/MoviesEnglish.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام عربية', icons + '/Arabic.png', oOutputParameterHandler)
 
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TUK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام تركي', icons + '/Asian.png', oOutputParameterHandler)
    
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', icons + '/Hindi.png', oOutputParameterHandler)
 
    oOutputParameterHandler.addParameter('siteUrl', KID_MOVIES[0])

    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام انمي', icons + '/Anime.png', oOutputParameterHandler)
 


    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام انمي', icons + '/Anime.png', oOutputParameterHandler)
    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أجنبية', icons + '/TVShowsEnglish.png', oOutputParameterHandler)
    
  #  oOutputParameterHandler.addParameter('siteUrl', SERIE_NETFLIX[0])
 #   oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات Netflix', icons + '/TVShowsEnglish.png', oOutputParameterHandler)

    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كرتون', icons + '/Cartoon.png', oOutputParameterHandler) 

#    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
 #   oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أجنبية', icons + '/TVShowsEnglish.png', oOutputParameterHandler)
    
  #  oOutputParameterHandler.addParameter('siteUrl', SERIE_NETFLIX[0])
 #   oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات Netflix', icons + '/TVShowsEnglish.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات عربية', icons + '/Arabic.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_ASIA[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أسيوية', icons + '/Asian.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات تركية', icons + '/Turkish.png', oOutputParameterHandler)
 
    oOutputParameterHandler.addParameter('siteUrl', SERIE_HEND[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات هندية', icons + '/Hindi.png', oOutputParameterHandler)
 
#    oOutputParameterHandler.addParameter('siteUrl', SERIE_LATIN[0])
   # oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات لاتيني', icons + '/TVShows.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_ANIME[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات انمي', icons + '/Anime.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_RAMADAN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات رمضان', icons + '/Ramadan.png', oOutputParameterHandler)
    
    oOutputParameterHandler.addParameter('siteUrl', REPLAYTV_PLAY[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'برامج تلفزيون', icons + '/Programs.png', oOutputParameterHandler)

    
    oOutputParameterHandler.addParameter('siteUrl', SPORT_WWE[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مصارعة', icons + '/WWE.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_PACK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showPack', 'أقسام الموقع', icons + '/Icon.png', oOutputParameterHandler)
  # ## xbmcgui.Dialog().ok("site",str(URL_MAIN))

 
    oGui.setEndOfDirectory()
 
def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
  # ## xbmcgui.Dialog().ok("seach",sSearchText)
    if sSearchText:
        sUrl = URL_MAIN + '?s='+sSearchText
       # sUrl=   "https://cima4u.actor/?s=alex"
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return
 
def showSeriesSearch():
   oGui = cGui()
   sSearchText = oGui.showKeyBoard()
   if sSearchText:
       surl=URL_MAIN+'?s='+sSearchText
       showSeries(surl)
       oGui.setEndOfDirectory()
       return
   pass

def showPack():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    oParser = cParser() 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sStart = '>الرئيسية</a>'
    sEnd = '</ul>\s*</div>'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

    sPattern = '<a href="([^<]+)">([^<]+)</a>'
    aResult = oParser.parse(sHtmlContent, sPattern)	
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            if 'اخري' in aEntry[1]:
                continue 
            sTitle = aEntry[1]
            siteUrl = aEntry[0]
			
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
			
            if 'series' in siteUrl:
                oGui.addMisc(SITE_IDENTIFIER, 'showSeries', sTitle, 'mslsl.png', '', '', oOutputParameterHandler)
            else:
                oGui.addMisc(SITE_IDENTIFIER, 'showMovies', sTitle, 'film.png', '', '', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()
			
def showMovies(sSearch = ''):
  
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
     
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
      # ## xbmcgui.Dialog().ok("",sUrl)
#   ## xbmcgui.Dialog().ok("seach",sUrl)
    oParser = cParser() 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    if "?s=" in sUrl:
             aResult = []

             aResult = find_Movies_formSreach(sUrl,aResult)
             oOutputParameterHandler = cOutputParameterHandler() 
           # ## xbmcgui.Dialog().ok("Find Movies", f"Number of movies found: {len(aResult)}")
             sPattern = r'<a href="([^"]+)">.*?background-image:url\(([^)]+)\).*?<div class="BoxTitle">.*?</div>\s*([^<\n]+)\s*</div>'
             for Entry in aResult:
                 Ety=str (Entry)
                 aEntry= re.findall(sPattern,Ety,re.DOTALL)
                 siteUrl = aEntry[0][0]+"?wat=1"
                 sTitle = aEntry[0][2].replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("ومترجمه","").replace("مترجم","").replace("برنامج","").replace("فيلم","").replace("والأخيرة","").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","")
                 sTitle=str(sTitle.strip() )
              #  ## xbmcgui.Dialog().ok("aEntry", str(Ety))
                 sThumb = aEntry[0][1].replace("(","").replace(")","")
                 sDesc = ''
                 sYear = ''
                 oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                 oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                 oOutputParameterHandler.addParameter('sThumb', sThumb)
                 oOutputParameterHandler.addParameter('sYear', sYear)
                 oOutputParameterHandler.addParameter('sDesc', sDesc)
                 oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
      
             pass
    else:

   # sStart = 'class="PageContent">'
   # sEnd = '<script'
  #  sHtmlContent = re.findall(sHtmlContent, sStart, sEnd)
     soup=BeautifulSoup(sHtmlContent,"html.parser")

 #   sPattern = r'<ul\s+class="Cima4uBlocks"\s+id="post-container">(.*?)</ul>'
     Cima4uBlocks = soup.find_all("li", class_="MovieBlock")
    
   # count = len(Cima4uBlocks)
   ### xbmcgui.Dialog().ok("Cima4uBlocks",str(count))
     sPattern = r'<a\s+href="([^"]+)".*?data-image="([^"]+)".*?<h3>(.*?)</h3>'
   
 

  #  html_content = "".join(str(block) for block in Cima4uBlocks)
 #   aResult =str (Cima4uBlocks)
 #  ## xbmcgui.Dialog().ok("aResult",str(aResult))
     aResult = []
     for xEntry in Cima4uBlocks:
      xEntryStr = str(xEntry)
      aEntry = re.findall(sPattern, xEntryStr, re.DOTALL)
      if aEntry:  # Ensure there's a match
        aResult.extend(aEntry)
      oOutputParameterHandler = cOutputParameterHandler() 
     
# Display all results in one dialog
   #  ## xbmcgui.Dialog().ok("aResult", str(len(aResult)))

     for aEntry in aResult:
         
           sTitle = aEntry[2].replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("ومترجمه","").replace("مترجم","").replace("برنامج","").replace("فيلم","").replace("والأخيرة","").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","")
        
           siteUrl = aEntry[0]+"?wat=1"
          ### xbmcgui.Dialog().ok("aEntry", str(siteUrl))
           sThumb = aEntry[1].replace("(","").replace(")","")
           sDesc = ''
           sYear = ''
           oOutputParameterHandler.addParameter('siteUrl',siteUrl)
           oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
           oOutputParameterHandler.addParameter('sThumb', sThumb)
           oOutputParameterHandler.addParameter('sYear', sYear)
           oOutputParameterHandler.addParameter('sDesc', sDesc)
           oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
            
          
 

  


  
  

   
   
   

   
          #  
    '''  if aResult :
     

   
     for aEntry in aResult:

        
       
            sTitle = aEntry[2].replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("ومترجمه","").replace("مترجم","").replace("برنامج","").replace("فيلم","").replace("والأخيرة","").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","")
            siteUrl = aEntry[0]
            sThumb = aEntry[1].replace("(","").replace(")","")
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
            if "سلسلة"  in sTitle or "جميع"  in sTitle:
                oGui.addDir(SITE_IDENTIFIER, 'showTag', sTitle, '', oOutputParameterHandler)
            else:         
                oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)


    else:
        sPattern = '<li class="MovieBlock">\s*<a href="([^"]+)".+?<div.+?image:url([^<]+);">.+?class="Category">.+?</div>\s*</div>([^<]+)</div>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            oOutputParameterHandler = cOutputParameterHandler()    
            for aEntry in aResult[1]:
 
                sTitle = aEntry[2].replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("ومترجمه","").replace("مترجم","").replace("برنامج","").replace("فيلم","").replace("والأخيرة","").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","")
                siteUrl = aEntry[0]
                sThumb = aEntry[1].replace("(","").replace(")","")
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
                if "سلسلة"  in sTitle or "جميع"  in sTitle:
                    oGui.addDir(SITE_IDENTIFIER, 'showTag', sTitle, '', oOutputParameterHandler)
                else:         
                    oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    sPattern = 'page-numbers" href="([^"]+)">([^<]+)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()    
        for aEntry in aResult[1]:
 
            sTitle = aEntry[1]           
            sTitle =  "PAGE " + sTitle
            sTitle =   '[COLOR red]'+sTitle+'[/COLOR]'
            siteUrl = aEntry[0]

            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
			
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, '', oOutputParameterHandler)

 '''
    if not sSearch:
        oGui.setEndOfDirectory()

def find_Movies_formSreach(url, movie_list):
    next_url = ""
    sHtmlContent = requests.get(url)
    soup = BeautifulSoup(sHtmlContent.text, "html.parser")

    # Find all movie blocks
    Cima4uBlocks = soup.find_all("li", class_="MovieBlock")
    
    # Process each movie block
    for block in Cima4uBlocks:
        title = block.find("a").text.strip()
        if "مسلسل" not in title:  # Filter out series

      #     ## xbmcgui.Dialog().ok("Found Movie", str(title))  # Debug dialog for movie titles
            movie_list.append(block)  # Append title to the movie list

    # Handle pagination
    page_number = 1
    match = re.search(r"/page/(\d+)", url)
    if match:
        page_number = int(match.group(1))  # Convert to integer
    page_number = page_number + 1 if page_number >= 1 else 1# Increment page number

    # Find pagination links
    pages = soup.find_all("a", class_="page-numbers")
  # ## xbmcgui.Dialog().ok("Pagination Links", str(page_number))  # Debug dialog for pagination links

    for page in pages:
        furl = str(page["href"])
    #   ## xbmcgui.Dialog().ok("Page URL", furl)  # Debug dialog for each page URL

        if f"/page/{page_number}"in furl:  # Check if the URL corresponds to the next page
            next_url = furl
        #   ## xbmcgui.Dialog().notification("Next URL", next_url, xbmcgui.NOTIFICATION_INFO, 5000)
            break  # Exit loop after finding the next page

    # Recursive call for the next page if available
    if next_url:
        movie_list = find_Movies_formSreach(next_url, movie_list)

    return movie_list

    pass
def find_TvShow_formSreach(url, tvshow_list):
    next_url = ""
    sHtmlContent = requests.get(url)
    soup = BeautifulSoup(sHtmlContent.text, "html.parser")

    # Find all movie blocks
    Cima4uBlocks = soup.find_all("li", class_="MovieBlock")
    
    # Process each movie block
    for block in Cima4uBlocks:
    
     a_tag = block.find("a")
     url = a_tag['href'] if a_tag else None  # Extract href attribute if it exists

     if url:  # Ensure the URL exists
        readable_url = unquote(url)

        # Check if "مسلسل" is in the readable URL to filter series
        if "مسلسل" in readable_url:

           spattern = r"مسلسل-(.+?)-موسم-(\d+)"
           match = re.search(spattern, readable_url)
           if match:
                series_name = match.group(1).replace('-', ' ')  # استبدال الشرطات بمسافات
                season_number = match.group(2)
                pass
           elif  "حلقة" in readable_url:
               spattern = r"مسلسل-(.+?)"
               match = re.search(spattern, readable_url)
               if match:
                   series_name = match.group(1).replace('-', ' ')  # استبدال الشرط
                   season_number = ""

               
        

         
               
           
            # Clean the URL
          # cleaned_url = re.sub(r'مشاهدة-مسلسل-', '', readable_url)

# Step 2: Remove number followed by '-حلقة-' and 'والاخيرة'
         #  cleaned_url = re.sub(r'-\d+-حلقة-|والاخيرة', '', cleaned_url)

# Replace dashes with spaces and strip any leading or trailing spaces
         #  cleaned_url = cleaned_url.replace('-', ' ').strip()
           title = f" {series_name}   {season_number} "

            # Debug dialog to show the found title
          # ## xbmcgui.Dialog().ok("Found TV Show", title)

            # Add the title to the tvshow_list if not already present
           if title not in [t["title"] for t in tvshow_list]:
                copy_block=str (block)
                tvshow_list.append({"title": title, "block": str(block)})
              # Append title to the list, not the block

                # Notification for the found TV show
            #    xbmcgui.Dialog().notification("TV Show Found", title, xbmcgui.NOTIFICATION_INFO, 3000)
    # Handle pagination
    page_number = 1
    match = re.search(r"/page/(\d+)", url)
    if match:
        page_number = int(match.group(1))  # Convert to integer
    page_number = page_number + 1 if page_number >= 1 else 1# Increment page number

    # Find pagination links
    pages = soup.find_all("a", class_="page-numbers")
  # ## xbmcgui.Dialog().ok("Pagination Links", str(page_number))  # Debug dialog for pagination links

    for page in pages:
        furl = str(page["href"])
    #   ## xbmcgui.Dialog().ok("Page URL", furl)  # Debug dialog for each page URL

        if f"/page/{page_number}"in furl:  # Check if the URL corresponds to the next page
            next_url = furl
        #   ## xbmcgui.Dialog().notification("Next URL", next_url, xbmcgui.NOTIFICATION_INFO, 5000)
            break  # Exit loop after finding the next page

    # Recursive call for the next page if available
    if next_url:
        tvshow_list = find_TvShow_formSreach(next_url, tvshow_list)

    return tvshow_list

    pass
def showTag():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oParser = cParser() 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
            
    sPattern =  '<a href="([^<]+)"><div class="WatchingArea Hoverable">' 
    aResult = oParser.parse(sHtmlContent,sPattern)
    if aResult[0]:
        m3url = aResult[1][0] 
        oRequest = cRequestHandler(m3url)
        sHtmlContent = oRequest.request()

    sPattern = '<li class="MovieBlock">\s*<a href="([^"]+)".+?data-image="([^"]+)".+?class="Category">.+?</div>([^<]+)</div>'
    aResult = oParser.parse(sHtmlContent, sPattern)	
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()    
        for aEntry in aResult[1]:
 
            sTitle = aEntry[2].replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("مترجم","").replace("برنامج","").replace("فيلم","").replace("والأخيرة","").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","")
            siteUrl = aEntry[0]
            sThumb = aEntry[1].replace("(","").replace(")","")
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
            if "سلسلة"  in sTitle or "جميع"  in sTitle:
                oGui.addDir(SITE_IDENTIFIER, 'showTag', sTitle, '', oOutputParameterHandler)
            else:         
                oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)


    sPattern = '<title>([^<]+)</title>'
    aResult = oParser.parse(sHtmlContent, sPattern)    
    if (aResult[0]):
        sDisplay = aResult[1][0]

    oParser = cParser()
    sStart = 'class="SeasonsSections"'
    sEnd = 'class="WatchSectionContainer"'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

    sPattern = "href='(.+?)'>(.+?)</a>"
    aResult = oParser.parse(sHtmlContent, sPattern)	
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()    
        for aEntry in aResult[1]:
 
            sTitle = aEntry[1].replace("الجزء الأول","Part 1").replace("الجزء الاول","Part 1").replace("الجزء الثانى","Part 2").replace("الجزء الثاني","Part 2").replace("الجزء الثالث","Part 3").replace("الجزء الثالث","Part 3").replace("الجزء الرابع","Part 4").replace("الجزء الخامس","Part 5").replace("الجزء السادس","Part 6").replace("الجزء السابع","Part 7").replace("الجزء الثامن","Part 8").replace("الجزء التاسع","Part 9").replace("الجزء","Part ").replace('مترجم','').replace('ومدبلجة','مدبلجة')
            sTitle = sTitle + ' ' + sDisplay.replace('سلسلة','').replace('افلام','').replace('أفلام','').replace('مترجم','')
            siteUrl = aEntry[0]
            sThumb = sThumb
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

            oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    sPattern = 'page-numbers" href="([^"]+)">([^<]+)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)	
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sTitle = aEntry[1]            
            sTitle =  "PAGE " + sTitle
            sTitle =   '[COLOR red]'+sTitle+'[/COLOR]'
            siteUrl = aEntry[0].replace('"',"")

            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
			
            oGui.addDir(SITE_IDENTIFIER, 'showTag', sTitle, '', oOutputParameterHandler)

		
    oGui.setEndOfDirectory()       

def showSeries(sSearch = ''):
    
        
    oGui = cGui()
 #  ## xbmcgui.Dialog().ok("",sSearch)
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
       ## xbmcgui.Dialog().ok("",sUrl)
        
    if "?s=" in sUrl:
             aResult = []

             aResult = find_TvShow_formSreach(sUrl,aResult)
             oOutputParameterHandler = cOutputParameterHandler() 
            # xbmcgui.Dialog().ok("Find tvshow", f"Number of tvshow found: {len(aResult)}")
             sPattern = r'<a href="([^"]+)">.*?<div class="Thumb">.*?style="background-image:url\(([^)]+)\);".*?</div>.*?مشاهدة مسلسل ([^<]+).*?</div>'
        #     sPattern = r'<a href="([^"]+)">.*?مشاهدة مسلسل ([^<]+).*?</div>'


             for Entry in aResult:
             #   ## xbmcgui.Dialog().ok("aEntry", str(Entry["block"]))
                 Ety=Entry["block"].replace("background-image:url()","background-image:url($)")
                 aEntry = re.findall(sPattern, Ety, re.DOTALL)
                 
                 
                 if aEntry:
                  for match in aEntry:
                    try:
             #        siteUrl, sThumb ,sTitle= match 
                     siteUrl = match[0].replace('"',"")
                     sTitle = match[2].replace('"',"")
                     sThumb = match[1].replace('"',"")
                     
                         

                 #    xbmcgui.Dialog().ok("Debug sThumb", f"sThumb: '{sThumb}'")
                     pass
                    except Exception as e:
        # Log the error
                     xbmcgui.Dialog().notification("Error", f"An error occurred: {str(e)}")
                      
              #    siteUrl = aEntry[0]  # First match
              #    sThumb = aEntry[1]  # First match
               #  ## xbmcgui.Dialog().ok("aEntry", str(siteUrl))
                   # Check if sThumb is empty or just whitespace
                 
                  
            #     ## xbmcgui.Dialog().ok("aEntry", str(sTitle))
               
                 
                  sTitle = sTitle.replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("ومترجمه","").replace("مترجم","").replace("برنامج","").replace("فيلم","").replace("والأخيرة","").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","")
                  sTitle=str(sTitle.strip() )
           #       sTitle = re.sub(r'\s*موسم\s+\d+', '', sTitle)  
                 sTitle = re.sub(r'\s*حلقة\s+\d+', '', sTitle)
               
             #   ## xbmcgui.Dialog().ok("aEntry", str(siteUrl))
               #  sThumb = aEntry[0][1].replace("(","").replace(")","")
                 sDesc = ''
                 sYear = ''
                 oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                 oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                 oOutputParameterHandler.addParameter('sThumb', sThumb)
                 oOutputParameterHandler.addParameter('sYear', sYear)
                 oOutputParameterHandler.addParameter('sDesc', sDesc)
                 oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
      
             pass
    else:
   #    ## xbmcgui.Dialog().ok("sUrl",str(sUrl))

         oParser = cParser() 
         oRequestHandler = cRequestHandler(sUrl)
         sHtmlContent = oRequestHandler.request()
         soup=BeautifulSoup(sHtmlContent,"html.parser")

 #   sPattern = r'<ul\s+class="Cima4uBlocks"\s+id="post-container">(.*?)</ul>'
         Cima4uBlocks = soup.find_all("li", class_="MovieBlock")
 #  ## xbmcgui.Dialog().ok("Cima4uBlocks",str(Cima4uBlocks))
    
   # count = len(Cima4uBlocks)
   ### xbmcgui.Dialog().ok("Cima4uBlocks",str(count))
         sPattern = r'<a\s+href="([^"]+)".*?data-image="([^"]+)".*?<h3>(.*?)</h3>'
 
 #   sPattern = '<li class="MovieBlock">\s*<a href="([^"]+)".+?data-image="([^"]+)".+?class="Category">.+?</div>([^<]+)</div>'
 #   aResult = oParser.parse(sHtmlContent, sPattern)  
         aResult = re.findall(sPattern, str (Cima4uBlocks),re.DOTALL)  
         itemList = []
         numb=0
         oOutputParameterHandler = cOutputParameterHandler()
  # ## xbmcgui.Dialog().ok("aResult",str( len (aResult)))
         for aEntry in aResult:
           sTitle = (aEntry[2].replace("&#8217;","'").replace("مشاهدة","").replace("مترجمة","").replace("مسلسل","").replace("انمي","").replace("أنمي","").
                     replace("كاملة","").replace("كامل","").replace("مترجم","").replace("فيلم","").replace("برنامج","").replace("برنامج","").replace("اون لاين","").replace("WEB-DL","")
                     .replace("BRRip","").replace("720p","").replace("HD-TC","").replace("HDRip","").replace("HD-CAM","").replace("DVDRip","").replace("BluRay","").replace("1080p","")
                     .replace("WEBRip","").replace("WEB-dl","").replace("4K","").replace("All","").replace("BDRip","").replace("HDCAM","").replace("HDTC","").replace("HDTV","").replace("HD","")
                     .replace("720","").replace("HDCam","").replace("Full HD","").replace("1080","").replace("HC","").replace("Web-dl","").replace("والاخيرة",""))
           sTitle=re.sub(r"حلقة\s*\d+","",sTitle)
           str_not_space=sTitle.replace(" ", "")
           if str_not_space not in itemList:
            itemList.append(str_not_space)
            siteUrl = aEntry[0]
            sThumb = aEntry[1].replace("(","").replace(")","")
            sDesc = ""
            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
         
  
           pass
    '''''
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
 
            sTitle = aEntry[2].replace("&#8217;","'").replace("مشاهدة","").replace("مترجمة","").replace("مسلسل","").replace("انمي","").replace("أنمي","").replace("كاملة","").replace("كامل","").replace("مترجم","").replace("فيلم","").replace("برنامج","").replace("برنامج","").replace("اون لاين","").replace("WEB-DL","").replace("BRRip","").replace("720p","").replace("HD-TC","").replace("HDRip","").replace("HD-CAM","").replace("DVDRip","").replace("BluRay","").replace("1080p","").replace("WEBRip","").replace("WEB-dl","").replace("4K","").replace("All","").replace("BDRip","").replace("HDCAM","").replace("HDTC","").replace("HDTV","").replace("HD","").replace("720","").replace("HDCam","").replace("Full HD","").replace("1080","").replace("HC","").replace("Web-dl","")
            siteUrl = aEntry[0]
            sThumb = aEntry[1].replace("(","").replace(")","")
            sDesc = ""
            sDisplayTitle = sTitle.replace("الموسم العاشر","S10").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الاول","S1").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الموسم","S").replace("S ","S").replace("موسم","S").replace("S ","S").split('حلقة')[0].split('حلقه')[0]

            if sDisplayTitle not in itemList:
                itemList.append(sDisplayTitle)
                oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                oOutputParameterHandler.addParameter('sMovieTitle', sDisplayTitle)
                oOutputParameterHandler.addParameter('sThumb', sThumb)
			
                if "حفلات"  in sTitle or "جلسات"  in sTitle:
                    oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                else:         
                    oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

    else:
        sPattern = '<li class="MovieBlock">\s*<a href="([^"]+)".+?<div.+?image:url([^<]+);">.+?class="Category">.+?</div>\s*</div>([^<]+)</div>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            oOutputParameterHandler = cOutputParameterHandler()    
            for aEntry in aResult[1]:
 
                sTitle = aEntry[2].replace("&#8217;","'").replace("مشاهدة","").replace("مترجمة","").replace("مسلسل","").replace("انمي","").replace("أنمي","").replace("كاملة","").replace("كامل","").replace("مترجم","").replace("فيلم","").replace("برنامج","").replace("برنامج","").replace("اون لاين","").replace("WEB-DL","").replace("BRRip","").replace("720p","").replace("HD-TC","").replace("HDRip","").replace("HD-CAM","").replace("DVDRip","").replace("BluRay","").replace("1080p","").replace("WEBRip","").replace("WEB-dl","").replace("4K","").replace("All","").replace("BDRip","").replace("HDCAM","").replace("HDTC","").replace("HDTV","").replace("HD","").replace("720","").replace("HDCam","").replace("Full HD","").replace("1080","").replace("HC","").replace("Web-dl","")
                siteUrl = aEntry[0]
                sThumb = aEntry[1].replace("(","").replace(")","")
                sDesc = ""
                sDisplayTitle = sTitle.replace("الموسم العاشر","S10").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الاول","S1").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الموسم","S").replace("S ","S").replace("موسم","S").replace("S ","S").split('حلقة')[0].split('حلقه')[0]

                if sDisplayTitle not in itemList:
                    itemList.append(sDisplayTitle)
                    oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sDisplayTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)
			
                    if "حفلات"  in sTitle or "جلسات"  in sTitle:
                        oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                    else:         
                        oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

    sPattern = 'page-numbers" href="([^"]+)">([^<]+)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)	
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sTitle = aEntry[1]           
            sTitle =  "PAGE " + sTitle
            sTitle =   '[COLOR red]'+sTitle+'[/COLOR]'
            siteUrl = aEntry[0].replace('"',"")

            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
			
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', sTitle, '', oOutputParameterHandler)

		'''
    if not sSearch:
        oGui.setEndOfDirectory()
	
def showEpisodes():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oParser = cParser() 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    sStart = 'class="EpisodesList"'
    sEnd = '<div class'
    sHtmlContent1 = oParser.abParse(sHtmlContent, sStart, sEnd)

    sPattern = r'<ul class="insert_ep">(.*?)</ul>'
   # aResult = oParser.parse(sHtmlContent1, sPattern)  
    ul_match = re.search(sPattern, sHtmlContent,re.DOTALL)
    if ul_match:
     ul_content = ul_match.group(1)

    # Extract all href links and titles
     link_pattern = r'<a href="([^"]+)">([^<]+)</a>'
     aResult = re.findall(link_pattern, ul_content)
     #xbmcgui.Dialog().ok("aResult",f"{aResult}")
         
     if aResult:
       oOutputParameterHandler = cOutputParameterHandler()
       for aEntry in aResult:
         siteUrl = aEntry[0]+"?wat=1"
         sTitle = f'{sMovieTitle} {aEntry[1]}' 
         sTitle=re.sub(r"موسم\s*\d+","",sTitle)

         sThumb = sThumb
         sDesc = ''
         sYear = ''
         oOutputParameterHandler.addParameter('siteUrl', siteUrl)
         oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
         oOutputParameterHandler.addParameter('sThumb', sThumb)
         oOutputParameterHandler.addParameter('sYear', sYear) 
            
         oGui.addEpisode(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

         
         pass
     '''''
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()    
        for aEntry in aResult[1]:
 
            sEp = aEntry[2]
            sTitle = f'{sMovieTitle} E{sEp}'           
            siteUrl = aEntry[0]
            sThumb = sThumb
            sDesc = ''
            sYear = ''

            sDisplayTitle = sTitle.replace("الموسم العاشر","S10").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الاول","S1").replace(" الثانى","2").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الحلقة "," E").replace("حلقة "," E").replace("الموسم","S").replace("S ","S")
 
            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sDisplayTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear) 
            
            oGui.addEpisode(SITE_IDENTIFIER, 'showLinks', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showEpisodes', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    else:
        sPattern = 'itemprop="name">([^<]+)</h1>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0]):
            sTitle = aResult[1][0].replace("مشاهدة","").replace("مترجمة","").replace("مترجم","").replace("فيلم","").replace("اون لاين","").replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("مترجم","").replace("فيلم","").replace("والأخيرة","").replace("مدبلج للعربية","مدبلج").replace("والاخيرة","").replace("كاملة","").replace("حلقات كاملة","").replace("اونلاين","").replace("مباشرة","").replace("انتاج ","").replace("جودة عالية","").replace("كامل","").replace("HD","").replace("السلسلة الوثائقية","").replace("الفيلم الوثائقي","").replace("اون لاين","").replace('الحلقة ','E').replace('حلقة ','E')
            sTitle = sTitle.replace("الموسم العاشر","S10").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الأول","S1").replace("الموسم الاول","S1").replace("الموسم الثانى","S2").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الموسم","S").replace("موسم","S").replace("S ","S")

        oOutputParameterHandler = cOutputParameterHandler() 
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('sThumb', sThumb)

        oGui.addEpisode(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, '', oOutputParameterHandler)
'''''
    oGui.setEndOfDirectory()

def showLinks():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
  # ## xbmcgui.Dialog().ok("aEntry", str(sUrl))
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    soup = BeautifulSoup(sHtmlContent,"html.parser")
   # Correctly find elements using BeautifulSoup
    severs = soup.find_all("a", class_="sever_link")
    for server in severs:
        sHosterUrl=server['data-embed']
    #   ## xbmcgui.Dialog().ok("link",str ((sHosterUrl)))
      
        
        oHoster = cHosterGui().checkHoster(sHosterUrl)
        if oHoster:
            oHoster.setDisplayName( sMovieTitle)
            oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
        pass
    oGui.setEndOfDirectory()  

   


    mov_name_match = re.search(r'name="mov_name" value="(.*?)"', sHtmlContent)
    mov_url_match = re.search(r'name="mov_url" value="(.*?)"', sHtmlContent)
    submit_match = re.search(r'type="submit" value="(.*?)"', sHtmlContent)
    action_url_match = re.search(r'<form action="(.*?)"', sHtmlContent)

    if mov_name_match:
        mov_name = mov_name_match.group(1)

    if mov_url_match:
        mov_url = mov_url_match.group(1)

    if submit_match:
        submit = submit_match.group(1)

    if action_url_match:
        murl = action_url_match.group(1)

    oRequestHandler = cRequestHandler(murl)
    oRequestHandler.setRequestType(1)
    oRequestHandler.addHeaderEntry('Referer', sUrl.encode('utf-8'))
    oRequestHandler.addHeaderEntry('Origin', getHost(sUrl))
    oRequestHandler.addHeaderEntry('Accept', '*/*')
    oRequestHandler.addHeaderEntry('accept-language', 'en-US,en;q=0.9,ar;q=0.8')
    oRequestHandler.addParameters('mov_name', mov_name)
    oRequestHandler.addParameters('mov_url', mov_url)
    oRequestHandler.addParameters('submit', submit)
    sHtmlContent = oRequestHandler.request()
    

# Display a notification with the count of elements found
  
  

    sLinks = re.findall(r'sever_link="(.*?)"', sHtmlContent)
    for link in sLinks:
        sHosterUrl = link
        sDisplayTitle = sMovieTitle + get_resolution_label(link) 

        if 'userload' in sHosterUrl:
            sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
        if 'streamtape' in sHosterUrl:
            sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN  
        if 'mystream' in sHosterUrl:
            sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN 
        
        if 'mp4' in sHosterUrl:
            sHosterUrl = sHosterUrl + '|User-Agent=' + UA + '&Referer=' + sUrl
            oHoster = cHosterGui().getHoster('lien_direct')
        else:
            oHoster = cHosterGui().checkHoster(sHosterUrl)
        if oHoster:
            oHoster.setDisplayName(sDisplayTitle)
            oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
     
    oGui.setEndOfDirectory()  

def get_resolution_label(link):
    match = re.search(r"\b(?:240p|360p|480p|720p|1080p|2060p)\b", link, flags=re.IGNORECASE)
    if match:
        resolution = match.group(0).lower()
        if resolution == "2060p":
            return "4k (2060p)"
        elif resolution == "1080p":
            return "Full HD (1080p)"
        elif resolution == "720p":
            return "HD (720p)"
        elif resolution == "480p":
            return "SD (480p)"
        elif resolution == "360p":
            return "Low (360p)"
        elif resolution == "240p":
            return "Mobile (240p)"
        
    return "Unknown"

def __checkForNextPage(sHtmlContent):
    oParser = cParser()
    sPattern = '<li><a class="next page-numbers" href="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        return aResult[1][0]

    return False

def getHost(url):
    parts = url.split('//', 1)
    host = parts[0] + '//' + parts[1].split('/', 1)[0]
    return host