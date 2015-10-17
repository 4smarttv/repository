import urllib,urllib2,re,sys,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,xbmcvfs,string
#from t0mm0.common.net import Net as net
#from t0mm0.common.addon import Addon
#import settings
import json
import shutil
import zipfile

#Setup Plugin
SetupPlugin = xbmcaddon.Addon(id='script.Setup')
Setuphome = SetupPlugin.getAddonInfo('path')
Setupdatapath = xbmc.translatePath(SetupPlugin.getAddonInfo('profile'))
#autoUpdate Plugin
autoUpdatePlugin = xbmcaddon.Addon(id='script.autoUpdate')
autoUpdateHome = autoUpdatePlugin.getAddonInfo('path')
autoUpdatedatapath = xbmc.translatePath(autoUpdatePlugin.getAddonInfo('profile'))
# src and des of autoUpdate plugin
src_setting_xml= os.path.join(autoUpdateHome,'settings.xml')
des_settings_xml = os.path.join(autoUpdatedatapath,'settings.xml')

# This is home storage for userdata startup backup for A2 -X2 
storage_dir = xbmc.translatePath(os.path.join('special://home/storage',''))
home_dir = xbmc.translatePath("special://home") #This is root directory of xbmc or Kodi
# This is userdata startup backup for older X1 - R6-R7
A1_userdata_dir = '/storage/emulated/0/Android/data/org.xbmc.xbmc/userdata'
A1_storage_location = '/storage/emulated/0/Android/data/org.xbmc.xbmc'


# src and des of Setup
home_Setup_xml= os.path.join(Setuphome,'settings.xml')
datapath_Setup_xml = os.path.join(Setupdatapath,'settings.xml')
if os.path.exists(autoUpdatedatapath)==False:
  os.mkdir(autoUpdatedatapath)
  #copy setting.xml file here
  xbmc.log(msg='script.autoUpdate des_settings_xml,%s'%(des_settings_xml), level=xbmc.LOGDEBUG)
  xbmc.log(msg='script.autoUpdate src_setting_xml,%s'%(src_setting_xml), level=xbmc.LOGDEBUG)
  shutil.copyfile(src_setting_xml,des_settings_xml)
  xbmc.sleep(5000)
  xbmc.executebuiltin('Notification(Setup, Created file for autoUpdatedatapath,5000)')
#else: # start fresh tvbox by reset file
#  shutil.copyfile(src_setting_xml,des_settings_xml)
if not autoUpdatePlugin.getSetting('Machine_id') or autoUpdatePlugin.getSetting('Machine_id')=="":
  shutil.copyfile(src_setting_xml,des_settings_xml)
  xbmc.executebuiltin('Notification(Setup, Created file for autoUpdatedatapath,5000)')
  xbmc.sleep(5000)
#src_setting_xml = home+"\resource\setting.xml"
xbmc.log(msg='autoUpdateHome,%s'%(autoUpdateHome), level=xbmc.LOGDEBUG)
xbmc.log(msg='autoUpdatedatapath:,%s'%(autoUpdatedatapath), level=xbmc.LOGDEBUG)
xbmc.log(msg='Setuphome:,%s'%(Setuphome), level=xbmc.LOGDEBUG)
xbmc.log(msg='Setupdatapath: ,%s'%(Setupdatapath), level=xbmc.LOGDEBUG)
# path for file auth
AuthPathTxt='http://4SmartTVBox.com/Auth/dat.txt'  #?
# path for demo DB for downgrade
remote_K_demo_db='http://4SmartTVBox.com/U_NoKaraoke_1/XKaraokeDB/MyVideos93.txt'
remote_K_full_db='http://4SmartTVBox.com/U_Karaoke_3/XKaraokeDB/MyVideos93.txt'
remote_K_HardDrive_db='http://4SmartTVBox.com/U_HardDrive_9/XKaraokeDB/MyVideos93.txt'
DBUpdatetxt='http://4SmartTVBox.com/U_NoKaraoke_1/XKaraokeDB/update.txt'
# location of DB
# 3 information for update database
db_database_dir = os.path.join(xbmc.translatePath("special://database"), 'MyVideos93.db')
db_storage_dir = os.path.join(xbmc.translatePath("special://home/storage/userdata/Database"), 'MyVideos93.db')



def OpenURL(url):   # get remote data file
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
def DowngradeKaraokeDB():
    import downloader
    dp = xbmcgui.DialogProgress()
    dp.create("Downgrade Karaoke Data","",'Building Data, Please Wait', ' ')
    downloader.download(remote_K_demo_db, db_storage_dir,dp)# update database in storage
    downloader.download(remote_K_demo_db, db_database_dir,dp)# update in database
def UpgradeKaraokeDB():
    import downloader
    dp = xbmcgui.DialogProgress()
    dp.create("Update Karaoke Data","",'Building Data, Please Wait', ' ')
    downloader.download(remote_K_full_db, db_storage_dir,dp)# update database in storage
    downloader.download(remote_K_full_db, db_database_dir,dp)# update in database
def UpgradeKaraokeDBToHardDrive():
    import downloader
    dp = xbmcgui.DialogProgress()
    dp.create("Update Hard Drive Karaoke Data","",'Building Data, Please Wait', ' ')
    downloader.download(remote_K_HardDrive_db, db_storage_dir,dp)# update database in storage
    downloader.download(remote_K_HardDrive_db, db_database_dir,dp)# update in database
#just for hardDrive
remote_Addons = ''

remote_userdata = ''
def pathForHardDrive(id):
  if id == 9 or id == 10:
    remote_Addons = 'http://4SmartTVBox.com/U_HardDrive_9/XAddOns/UpdateAddons_HD.zip'
    remote_userdata = 'http://4SmartTVBox.com/U_HardDrive_9/XUserdata/UpdateUserdata_HD.zip'
  elif id == 13:
    remote_Addons = 'http://4SmartTVBox.com/U_Other_13/XAddOns/UpdateAddons_HD.zip'
    remote_userdata = 'http://4SmartTVBox.com/U_Other_13/XUserdata/UpdateUserdata_HD.zip'
     

def UpdateHardDriveAddons():
    import downloader
    dp = xbmcgui.DialogProgress()
    dp.create("Update Addons for Hard Drive","",'Downloading, Please Wait', ' ')
    if not os.path.exists(storage_dir):
      os.makedirs(storage_dir)
    Addons_storage_Zip = os.path.join(xbmc.translatePath("special://home/storage"), 'UpdateAddons_HD.zip')
    downloader.download(remote_Addons, Addons_storage_Zip,dp)
    dlog = xbmcgui.Dialog()
    dlog.notification("Update Addons","Done DownLoad, Installing")
    z=zipfile.ZipFile(Addons_storage_Zip,"r")
    #zl=z.namelist()
    #deleteDir(addons_dir)   #delete most of addons , will delete all user addons too, potential problem
    z.extractall(home_dir) #extract to homedir, overwrite addons if there are
    z.close()
    dlog.notification("Update Addons","Install Finished!")
#just for hardDrive    
def UpdateHardDriveUserdata():
    import downloader
    #deleteDir(userdata_storage_dir)   #don't need to delete dir latter just overwrite so can only update one file as guisetting.xml
    dp = xbmcgui.DialogProgress()
    dp.create("Update Userdata for Hard Drive","",'Downloading, Please Wait!', ' ')
    if not os.path.exists(storage_dir):
      os.makedirs(storage_dir)
    userdata_storage_Zip = os.path.join(xbmc.translatePath("special://home/storage"), 'UpdateUserdata_HD.zip')
    downloader.download(remote_userdata, userdata_storage_Zip,dp)
    dlog = xbmcgui.Dialog()
    dlog.notification("Update Userdata","Done DownLoad, Installing")
    z=zipfile.ZipFile(userdata_storage_Zip,"r")
    #zl=z.namelist()
    #make the update for A1-X1 and older
    if os.path.exists(A1_userdata_dir):
      z.extractall(A1_storage_location)
    else:
      #z.extractall(storage_dir)
      #for Kodi extract to home directory
      z.extractall(home_dir)
    z.close()
    #xbmc.sleep(10000)

machineIdNumber = 1

link=OpenURL(AuthPathTxt)
xbmc.log(msg='script.autoUpdate src_setting_xml,%s'%(link), level=xbmc.LOGDEBUG)
keyboard = xbmc.Keyboard( '', 'Enter User Name:', False )
keyboard.doModal()
if ( keyboard.isConfirmed() ):
  userName = keyboard.getText()
  match1=re.compile('UserName=<(.+?)>').findall (link) # get the id of update version  
  if userName == match1[0]:
    xbmc.log('Username is right')
    keyboard = xbmc.Keyboard( '', 'Enter Password:', True )
    keyboard.doModal()
    if(keyboard.isConfirmed()):
      passWord = keyboard.getText()
      match2=re.compile('Password=<(.+?)>').findall (link) # get the id of update version  
      if passWord == match2[0]:
        keyboard = xbmc.Keyboard( '1', 'Enter TVbox Model Number:', False )
        keyboard.doModal()
        if(keyboard.isConfirmed()):
          machineIdNumber = int(keyboard.getText())
          autoUpdatePlugin.setSetting('Machine_id',str(machineIdNumber))
          #Copy userdata setting.xml back to home setting.xml to make the final setting of the box in rom
          shutil.copyfile(des_settings_xml, src_setting_xml)
          xbmc.executebuiltin('Notification(Setup, Created file for autoUpdatedatapath,5000)')
          filesize = int(os.path.getsize(db_database_dir))
          demosize = int(autoUpdatePlugin.getSetting('DB_demo_size'))
          if machineIdNumber==1 or machineIdNumber==2:
            xbmc.log('Machine id 1 or 2')
            if (filesize > demosize): # downgrade the database
              xbmc.executebuiltin('Notification(Setup, Downgrade DB now,7000)')
              DowngradeKaraokeDB() # down grade to Demo DB
          elif machineIdNumber==9 or machineIdNumber==10 or machineIdNumber == 13: #add id 13 for M8 harddrive karaoke
          #Add this change to UpdateAddons_1.zip of Id=12 dir 
            # change database to hard drive
            #UpgradeKaraokeDBToHardDrive()
            # already set id number to 9 or 10 call autoUpdate script to update need file and database for hardrive
            # 1) karaokesearch, 2) playkaraoke, 3) userdata include database playlist
            
            #xbmc.executebuiltin('runscript(script.autoUpdate)')
            #pathForHardDrive(machineIdNumber)
            if machineIdNumber == 9 or machineIdNumber == 10:
              remote_Addons = 'http://4SmartTVBox.com/U_HardDrive_9/XAddOns/UpdateAddons_HD.zip'
              remote_userdata = 'http://4SmartTVBox.com/U_HardDrive_9/XUserdata/UpdateUserdata_HD.zip'
            elif machineIdNumber == 13:
              remote_Addons = 'http://4SmartTVBox.com/U_Other_13/XAddOns/UpdateAddons_HD.zip'
              remote_userdata = 'http://4SmartTVBox.com/U_Other_13/XUserdata/UpdateUserdata_HD.zip'
            UpdateHardDriveAddons()
            UpdateHardDriveUserdata() 
          else:
            xbmc.log('Machine id 3 and up')
            if (demosize > filesize): # updrade database
              xbmc.executebuiltin('Notification(Setup, Upgrade DB now,7000)')
              UpgradeKaraokeDB() # down grade to Demo DB
        else: xbmc.executebuiltin('Notification(Setup, The box is at it original setting,5000)')
      else: xbmc.executebuiltin('Notification(Setup, The Password is not match,5000)')
    else: xbmc.executebuiltin('Notification(Setup, No Password is Enter,5000)')
  else: xbmc.executebuiltin('Notification(Setup, No User Name as Entered,5000)')
xbmc.executebuiltin('Notification(Setup, Done Setting!!!,5000)')
  