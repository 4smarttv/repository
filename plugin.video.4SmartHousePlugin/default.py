import sys
import xbmcgui
import urllib
import urllib2
import xbmcaddon,xbmcplugin,xbmcgui, xbmc, os
import re


addon = xbmcaddon.Addon()
addonID = addon.getAddonInfo('id')
addonname = addon.getAddonInfo('name')
mysettings = xbmcaddon.Addon(id='plugin.video.4SmartHousePlugin')
# add in for addons path
addonsPath=xbmc.translatePath("special://addons")

#MoviHD


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]

        return param

def addLink(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    #liz.setInfo( type="Video", infoLabels={ "Title": name})
    #liz.setProperty('mimetype', 'video/x-msvideo')
    #liz.setProperty("IsPlayable","true")
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz, isFolder=False)
    Selected_skin = xbmc.getSkinDir()
    if Selected_skin == 'skin.4xeebo':
      xbmc.executebuiltin('Container.SetViewMode(51)')
    return ok

def OpenURL(url):   # get remote data file 
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    try:
      response = urllib2.urlopen(req)
    except:
      link = ''
      xbmc.executebuiltin('activatewindow(home)')
      return link  
    link=response.read()
    response.close()
    return link

pluginUrl = str(sys.argv[0])
pluginHandle = int(sys.argv[1])
pluginQuery = str(sys.argv[2])
xbmc.log(msg='pluginUrl: ,%s'%(pluginUrl), level=xbmc.LOGDEBUG)
xbmc.log(msg='pluginHandle: ,%s'%str(pluginHandle), level=xbmc.LOGDEBUG)
xbmc.log(msg='pluginQuery: ,%s'%(pluginQuery), level=xbmc.LOGDEBUG)
    
#params=get_params()
url=None
category=None
mode=None
category = pluginQuery[10:] 
xbmc.log(msg='category: ,%s'%(category), level=xbmc.LOGDEBUG)
#try:
#        category=urllib.unquote_plus(params["category"])
#except:
#        pass
#xbmc.log(msg='Category: ,%s'%(category), level=xbmc.LOGDEBUG)
Addon_LinkTxt = 'http://4SmartTvbox.com/CurrentAddOns/'+category+'.txt'
def getPlugin():
  xbmc.log(msg='Name Addon_LinkTxt: ,%s'%(Addon_LinkTxt), level=xbmc.LOGDEBUG)
  if category:
    xbmc.log(msg='Name category: ,%s'%(category), level=xbmc.LOGDEBUG)
    xbmc.log(msg='Name OpenURL(Addon_LinkTxt): ,%s'%(Addon_LinkTxt), level=xbmc.LOGDEBUG)
    link=OpenURL(Addon_LinkTxt)#Get id from UpdateAll data from update file
    addonsName=re.compile('AddOns_name=<(.+?)>').findall (link) # get      
    addons_number = 0
    lenght = len(addonsName)
    while addons_number < lenght: # update addons only
      addonsPath = addonsName[addons_number] 
      searchString = addonsName[addons_number]
      if '-' in searchString:
        addonsIndex = searchString.index('-')
        Name = searchString[:addonsIndex]
        xbmc.log(msg='Name searchString: ,%s'%(Name), level=xbmc.LOGDEBUG) 
      else:
        Name = str(addonsName[addons_number])
      NameDisplay = Name[13:]
      #image = '/storage/emulated/0/Android/data/org.xbmc.xbmc/files/.xbmc/addons/'+str(addonsPath)+'/icon.png'
      #image = addonsPath+str(addonsPath)+'/icon.png'
      addonsNamePath = os.path.join(xbmc.translatePath("special://home/addons"), searchString)
      xbmc.log(msg='addonsNamePath: ,%s'%(addonsNamePath), level=xbmc.LOGDEBUG)
      if os.path.exists(addonsNamePath)==True:
        image = addonsNamePath + '/icon.png'
        addLink(NameDisplay,'RunAddon('+Name+')',1,image)
        xbmc.log(msg='Path exist: ,%s'%(Name), level=xbmc.LOGDEBUG)
      else:
        #image = 'http://4Smarttvbox.com/Channel_Images4/click_Install.png'
        image = 'http://4Smarttvbox.com/Plugin_Image/'+Name+'.png'
        #urlPlugin='ActivateWindow(10025,&quot;plugin://plugin.video.viettv24free/&quot;,return)'
        #urlPlugin='ActivateWindow(10025,plugin://plugin.video.viettv24free/)'
        urlPlugin='ActivateWindow(10025,plugin://'+Name+'/)'
        xbmc.log(msg='Path DO NOT exist urlPlugin: ,%s'%(urlPlugin), level=xbmc.LOGDEBUG)
        addLink(NameDisplay,urlPlugin,2,image)
        
      xbmc.log(msg='executebuiltin: Name: ,%s'%(Name), level=xbmc.LOGDEBUG)
      addons_number = addons_number + 1
  else:
    xbmc.executebuiltin('activatewindow(home)')
    

params=get_params()
url=None
category=None
mode=None
iconimage=None
edit=None
inum=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        category=urllib.unquote_plus(params["category"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

sysarg=str(sys.argv[1])

if mode==None or url==None or len(url)<1:
  getPlugin()
elif mode==1:
  #item = xbmcgui.ListItem(path=url)
  xbmc.log(msg='executebuiltin1: url: ,%s'%(url), level=xbmc.LOGDEBUG)
  xbmc.executebuiltin(url)
elif mode==2:
  xbmc.log(msg='executebuiltin2: url: ,%s'%(url), level=xbmc.LOGDEBUG)
  xbmc.executebuiltin(url)



xbmcplugin.endOfDirectory(int(sysarg))
