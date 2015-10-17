import xbmcplugin,xbmcgui,xbmcaddon,xbmc, os
import shutil


#Setup Plugin ChangePW 
chagePWPlugin = xbmcaddon.Addon(id='plugin.video.4SmartChangePW')
chagePWHome = chagePWPlugin.getAddonInfo('path')
chagePWDatapath = xbmc.translatePath(chagePWPlugin.getAddonInfo('profile'))

#Setup Plugin for CheckPW
PWCheckPlugin = xbmcaddon.Addon(id='script.PWCheck')
PWCheckhome = PWCheckPlugin.getAddonInfo('path')
PWCheckdatapath = xbmc.translatePath(PWCheckPlugin.getAddonInfo('profile'))


# src and des of Setup
home_PWCheck_xml= os.path.join(PWCheckhome,'settings.xml')
datapath_PWCheck_xml = os.path.join(PWCheckdatapath,'settings.xml')
if os.path.exists(PWCheckdatapath)==False:
  os.mkdir(PWCheckdatapath)
  #copy setting.xml file here
  xbmc.log(msg='script.autoUpdate des_settings_xml,%s'%(home_PWCheck_xml), level=xbmc.LOGDEBUG)
  xbmc.log(msg='script.autoUpdate src_setting_xml,%s'%(datapath_PWCheck_xml), level=xbmc.LOGDEBUG)
  shutil.copyfile(home_PWCheck_xml,datapath_PWCheck_xml)
  xbmc.sleep(5000)
  xbmc.executebuiltin('Notification(Setup, Created file for datapath_PWCheck_xml,5000)')
#org_PW = int(PWCheckPlugin.getSetting('PW'))
#xbmc.log(msg='Original PW: ,%s'%(org_PW), level=xbmc.LOGDEBUG)

keyboard = xbmc.Keyboard( '', '                            Enter New Password in Number:', False )
keyboard.doModal()
if ( keyboard.isConfirmed() ):
  entered_PW = str(keyboard.getText())
  xbmc.log(msg='Entered PW: ,%s'%(entered_PW), level=xbmc.LOGDEBUG)
  if entered_PW == '':
    xbmc.executebuiltin('Notification(Setup, Password empty, it is Not Change!!!,10000)')
  else:
    PWCheckPlugin.setSetting('PW',str(entered_PW))
    xbmc.executebuiltin('Notification(Setup, Password is Changed!!!,5000)')
else:
  xbmc.executebuiltin('Notification(Setup, Password is Not Change!!!,10000)')

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
    pass
elif mode==1:
  item = xbmcgui.ListItem(path=url)
  xbmc.log(msg='executebuiltin: url: ,%s'%(url), level=xbmc.LOGDEBUG)
  xbmc.executebuiltin(url)
xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.4SmartHousePlugin/?category=XXX)')

xbmcplugin.endOfDirectory(int(sysarg))