import urllib,urllib2,re,xbmcgui,xbmcaddon,xbmc,os
import zipfile
import shutil

#autoUpdate Plugin
autoUpdatePlugin = xbmcaddon.Addon(id='script.autoUpdate')
autoUpdatephome = autoUpdatePlugin.getAddonInfo('path')
autoUpdatedatapath = xbmc.translatePath(autoUpdatePlugin.getAddonInfo('profile'))

src_setting_xml= os.path.join(autoUpdatephome,'settings.xml')
des_settings_xml = os.path.join(autoUpdatedatapath,'settings.xml')

xbmc.log(msg='Auto Update started', level=xbmc.LOGDEBUG)
xbmc.log(msg='AutoUpdate datapath,%s'%(autoUpdatedatapath), level=xbmc.LOGDEBUG)
dlog = xbmcgui.Dialog()
if os.path.exists(autoUpdatedatapath)==False:
    os.mkdir(autoUpdatedatapath)
    #copy setting.xml file here
    shutil.copyfile(src_setting_xml,des_settings_xml)
    dlog.notification("Copy AutoUpdate file","Wait",xbmcgui.NOTIFICATION_INFO,10000)
    xbmc.sleep(7000)
# check to make sure the file is there and not corrupt
if not autoUpdatePlugin.getSetting('Machine_id') or autoUpdatePlugin.getSetting('Machine_id')=="":
    shutil.copyfile(src_setting_xml,des_settings_xml)
    dlog.notification("Copy AutoUpdate file","Wait",xbmcgui.NOTIFICATION_INFO,10000)
    xbmc.sleep(7000)

#get all machine updated id
   
machine_id = int(autoUpdatePlugin.getSetting('Machine_id'))

local_addons_id = int(autoUpdatePlugin.getSetting('AddOns_id'))
local_userdata_id = int(autoUpdatePlugin.getSetting('Userdata_id'))
local_karaokeDB_id = int(autoUpdatePlugin.getSetting('KaraokeDB_id'))
local_gdrive_id = int(autoUpdatePlugin.getSetting('GDrive_id'))
    
    
# 3 information for update database
db_database_dir = os.path.join(xbmc.translatePath("special://database"), 'MyVideos93.db')
db_storage_dir = os.path.join(xbmc.translatePath("special://home/storage/userdata/Database"), 'MyVideos93.db')

# 4 information for update Karaoke plugin setting
gdrive_setting_xml = os.path.join(xbmc.translatePath("special://home/userdata/addon_data/plugin.video.gdrive"), 'settings.xml')
gdrive_storage_setting_xml = os.path.join(xbmc.translatePath("special://home/storage/userdata/plugin.video.gdrive"), 'settings.xml')


#addon = Addon('plugin.video.4SmartKaraoke',sys.argv)
#from sqlite3 import dbapi2 as database
#db_dir_txt = os.path.join(xbmc.translatePath("special://database"), 'MyVideos93.txt')

home_dir = xbmc.translatePath("special://home") #This is root directory of xbmc 
# This is home storage for userdata startup backup for A2 -X2 
storage_dir = xbmc.translatePath(os.path.join('special://home/storage',''))

# This is userdata startup backup for older X1 - R6-R7
A1_userdata_dir = '/storage/emulated/0/Android/data/org.xbmc.xbmc/userdata'
A1_storage_location = '/storage/emulated/0/Android/data/org.xbmc.xbmc'

addons_dir = xbmc.translatePath("special://home/addons")

userdata_storage_dir = xbmc.translatePath(os.path.join('special://home/storage/userdata','')) 
PL_storage_m3u = os.path.join(xbmc.translatePath("special://home/userdata/playlists/video"), 'PL_Local.m3u')


def OpenURL(url):   # get remote data file
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    try:
      response = urllib2.urlopen(req)
    except:
      link = 'AddOns_id=<0>, KaraokeDB_id=<0>, GDrive_id=<0>, Userdata_id=<0>'
      return link  
    link=response.read()
    response.close()
    return link


def UpdateAddons():
    import downloader
    dp = xbmcgui.DialogProgress()
    dp.create("Update Addons: "+str(local_addons_id+1),"",'Downloading, Please Wait', ' ')
    if not os.path.exists(storage_dir):
      os.makedirs(storage_dir)
    downloader.download(remote_Addons, Addons_storage_Zip,dp)
    dlog = xbmcgui.Dialog()
    dlog.notification("Update Addons","Done DownLoad, Installing")
    z=zipfile.ZipFile(Addons_storage_Zip,"r")
    #zl=z.namelist()
    #deleteDir(addons_dir)   #delete most of addons , will delete all user addons too, potential problem
    z.extractall(home_dir) #extract to homedir, overwrite addons if there are
    z.close()
    dlog.notification("Update Addons","Install Finished!")
    
def UpdateUserdata():
    import downloader
    #deleteDir(userdata_storage_dir)   #don't need to delete dir latter just overwrite so can only update one file as guisetting.xml
    dp = xbmcgui.DialogProgress()
    dp.create("Update Userdata:"+str(local_userdata_id+1),"",'Downloading, Please Wait!', ' ')
    if not os.path.exists(storage_dir):
      os.makedirs(storage_dir)
    downloader.download(remote_userdata, userdata_storage_Zip,dp)
    dlog = xbmcgui.Dialog()
    dlog.notification("Update Userdata","Done DownLoad, Installing")
    z=zipfile.ZipFile(userdata_storage_Zip,"r")
    #zl=z.namelist()
    #make the update for A1-X1 and older
    if os.path.exists(A1_userdata_dir):
      z.extractall(A1_storage_location)
    else:
      z.extractall(storage_dir)
    z.close()
    #xbmc.sleep(10000)

def UpdateKaraokeDB():
    import downloader
    dp = xbmcgui.DialogProgress()
    dp.create("Update Karaoke Data","",'Building Data, Please Wait', ' ')
    downloader.download(remote_K_db, db_storage_dir,dp)# update database in storage
    downloader.download(remote_K_db, db_database_dir,dp)# update in database

def UpdateGDriveSetting():
    import downloader
    dp = xbmcgui.DialogProgress()
    dp.create("Update Karaoke Data","",'Building Data, Please Wait', ' ')
    downloader.download(remote_K_setting, gdrive_setting_xml,dp)# update in home
    downloader.download(remote_K_setting, gdrive_storage_setting_xml,dp) #update in storage

def deleteDir(path):
    try:
        shutil.rmtree(path)
        
    # Directories are the same
    except shutil.Error as e:
        print('Directory not deleted. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not deleted. Error: %s' % e)

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)
    

#check if the MyVideos93.db file exist    
if os.path.exists(db_database_dir)==False:
    link=OpenURL(DBUpdatetxt)
    match=re.compile('KaraokeDB_id=<(.+?)>').findall (link)
    dp = xbmcgui.Dialog()
    dp.ok("Update Karaoke Data","",'Building data', 'Please Wait')
    UpdateKaraokeDB()
    autoUpdatePlugin.setSetting('KaraokeDB_id',match[0])
    
#***************************
remote_Addons = ''
Addonstxt=''

remote_userdata = ''
Userdatatxt=''

remote_K_db=''
DBUpdatetxt=''

remote_K_setting=''
GDriveSetTxt=''

webSite = 'http://4SmartTVBox.com/'
machineName = ['','U_NoKaraoke_1/','U_TestNoKaraoke_2/','U_Karaoke_3/','U_TestKaraoke_4/','U_TimeProm_5/','U_Other_6/',
               'U_Other1_7/','U_Development_8/','U_HardDrive_9/','U_Test_HardDrive_10/','U_Other_11/','U_Test_Other_12/',
               'U_Other_13/','U_Test_Other_14/']
#U_Other_11 -> for start installation of xbmc - MX2
#U_Test_Other_12 -> new installation for M8
#*******************************

def getMachineDataPath(machineId,verIdAddons,verIdUserdata):
    global remote_Addons, Addonstxt, remote_userdata, Userdatatxt, remote_K_db, DBUpdatetxt, remote_K_setting, GDriveSetTxt  
    remote_Addons = webSite+machineName[machineId]+'XAddOns/UpdateAddons_'+str(verIdAddons)+'.zip'
    Addonstxt = webSite+machineName[machineId]+'XAddOns/update.txt'
    
    remote_userdata = webSite+machineName[machineId]+'XUserdata/UpdateUserdata_'+str(verIdUserdata)+'.zip'
    Userdatatxt = webSite+machineName[machineId]+'XUserdata/update.txt'
    
    remote_K_db = webSite+machineName[machineId]+'XKaraokeDB/MyVideos93.txt'
    DBUpdatetxt = webSite+machineName[machineId]+'XKaraokeDB/update.txt'
    
    remote_K_setting = webSite+machineName[machineId]+'XKSetting/settings.xml'
    GDriveSetTxt = webSite+machineName[machineId]+'XKSetting/update.txt'
#*********************   Update skin for Koki 15.1
#xbmc.executebuiltin('Skin.SetString(CustomHomeItem_1.Label,New 4 SmartHouse)')
#xbmc.executebuiltin('Skin.SetString(CustomHomeItem_1.Icon,special://userdata/Thumbnails/IMAGES/4SmartHouse_icon.png)')
####
xbmc.executebuiltin('Skin.SetBool(AltHomeStyle,true)')
    #<setting type="bool" name="skin.4xeebo.AltHomeStyle">true</setting>
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_1.Label,4SmartHouse.com)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_1.Icon,special://userdata/Thumbnails/IMAGES/4SmartHouse_icon.png)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_2.Label,4Smart Play Karaoke)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_2.Icon,special://home/addons/script.playkaraoke/icon.png)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_3.Label,PhimVang.org)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_3.Icon,special://home/addons/plugin.video.phimvang-1.1.1/icon.png)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_4.Label,Tin Tuc)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_4.Icon,special://userdata/Thumbnails/IMAGES/tintuc_dir.jpg)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_5.Label,Phim Viet)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_5.Icon,special://userdata/Thumbnails/IMAGES/PhimViet_dir.jpg)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_6.Label,Kids Place)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_6.Icon,special://userdata/Thumbnails/IMAGES/kid1_dir.jpg)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_7.Label,Movies &amp; Music)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_7.Icon,special://userdata/Thumbnails/IMAGES/EnglishMovie_dir.jpg)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_8.Label,TV Channels)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_8.Icon,special://userdata/Thumbnails/IMAGES/TV_dir.jpg)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_9.Label,Sports)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_9.Icon,special://userdata/Thumbnails/IMAGES/Sports.jpg)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_10.Label,Asian)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_10.Icon,special://userdata/Thumbnails/IMAGES/asian_dir.jpg)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_11.Label,RADIOS)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_11.Icon,special://userdata/Thumbnails/IMAGES/Radio.jpg)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_12.Label,News  And Channels)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_12.Icon,special://userdata/Thumbnails/IMAGES/news.jpg)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_13.Label,YouTube)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_13.Icon,special://home/addons/plugin.video.youtube/icon.png)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_14.Label,IceFilms)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_14.Icon,special://home/addons/plugin.video.icefilms/icon.png)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_15.Label,Genegis)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_15.Icon,special://home/addons/plugin.video.genesis/icon.png)')
xbmc.executebuiltin('Skin.SetString(SetItem,Video_Addon)')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_1.Path,RunAddon(plugin.video.4SmartHouse))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_2.Path,RunScript(script.playkaraoke))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_3.Path,RunAddon(plugin.video.phimvang))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_4.Path,ActivateWindow(10025,plugin://plugin.video.4SmartHousePlugin/?category=tintuc))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_5.Path,ActivateWindow(10025,plugin://plugin.video.4SmartHousePlugin/?category=PhimViet))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_6.Path,ActivateWindow(10025,plugin://plugin.video.4SmartHousePlugin/?category=kid))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_7.Path,ActivateWindow(10025,plugin://plugin.video.4SmartHousePlugin/?category=Movies))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_8.Path,ActivateWindow(10025,plugin://plugin.video.4SmartHousePlugin/?category=TV))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_9.Path,ActivateWindow(10025,plugin://plugin.video.4SmartHousePlugin/?category=Sport))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_10.Path,ActivateWindow(10025,plugin://plugin.video.4SmartHousePlugin/?category=asia))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_11.Path, ActivateWindow(10025,plugin://plugin.video.4SmartHouse/?fanart=http%3a%2f%2fwww.4smarttvbox.com%2fchannel_Images%2fThoiBaoRadio.jpg;mode=2;name=Radio%20Viet%20Nam;url=http%3a%2f%2f4smarttvbox.com%2f4SmartHouse_vn5.xml))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_12.Path,RunScript(script.newAndChannels))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_13.Path,RunAddon(plugin.video.youtube))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_14.Path,RunAddon(plugin.video.icefilms))')
xbmc.executebuiltin('Skin.SetString(CustomHomeItem_15.Path,RunAddon(plugin.video.genesis))')
xbmc.executebuiltin('XBMC.ReloadSkin()')        

#************************ End Update skin for Kodi 15.1

  

while not xbmc.abortRequested:
    if not xbmc.Player().isPlayingVideo():
      dlog = xbmcgui.Dialog()
      isRestart = False
      

      dlog.notification("Checking for update, Please Wait!!!","Info contact Authorized Dealer, or Call 1-800-558-9456",xbmcgui.NOTIFICATION_INFO,10000)
      # checking for deleted file every time it start
      xbmc.executebuiltin('runscript(script.preUpdate)')
      
      getMachineDataPath(machine_id,local_addons_id+1,local_userdata_id+1)
       
                          
      #have to change MyVideos93.db to .txt, because of the download on our server
      
      PL_local_path = xbmc.translatePath("special://home/userdata/playlists/video")

      xbmc.log(msg='AutoUpdate Addonstxt:,%s'%(Addonstxt), level=xbmc.LOGDEBUG)
  
      # 1 Update All include AddOns and Userdata
      link=OpenURL(Addonstxt)#Get id from UpdateAll data from update file
      match1=re.compile('AddOns_id=<(.+?)>').findall (link) # get the id of update version  
      # 2 Update userdata only
      link=OpenURL(Userdatatxt)#Get data from update file
      match2=re.compile('Userdata_id=<(.+?)>').findall (link) # get the id of update version
      # 3 Update Karaoke Database
      link=OpenURL(DBUpdatetxt)#Get data from update file
      match3=re.compile('KaraokeDB_id=<(.+?)>').findall (link) # get the id of update version
      # 4 Update Karaoke Setting for Authentication
      link=OpenURL(GDriveSetTxt)#Get data from update file
      match4=re.compile('GDrive_id=<(.+?)>').findall (link) # get the id of update version
      
      while int(match1[0]) > local_addons_id: # update addons only
        xbmc.executebuiltin('Notification(Update Addons, Updating... Please Wait!!!,30000)')
        xbmc.executebuiltin('runscript(script.preUpdate)')
        # 1 Path for download update addons only zipfile
        Addons_storage_Zip = os.path.join(xbmc.translatePath("special://home/storage"), 'UpdateAddons_'+str(local_addons_id+1)+'.zip')
        UpdateAddons()
        autoUpdatePlugin.setSetting('AddOns_id',str(local_addons_id+1))  #set the Current version id on local
        local_addons_id = local_addons_id+1
        getMachineDataPath(machine_id,local_addons_id+1,local_userdata_id+1)
        xbmc.executebuiltin('runscript(script.postUpdate)')
        isRestart = True
      
      # need addons sepparate from userdata update and other
      while int(match2[0]) > local_userdata_id:      # Update userdata only
        xbmc.executebuiltin('Notification(Update Userdata, Updating... Please Wait!!!,30000)')
        xbmc.executebuiltin('runscript(script.preUpdate)')
        # 2 Path Update userdata only
        userdata_storage_Zip = os.path.join(xbmc.translatePath("special://home/storage"), 'UpdateUserdata_'+str(local_userdata_id+1)+'.zip')
        UpdateUserdata()     #update userdata
        autoUpdatePlugin.setSetting('Userdata_id',str(local_userdata_id+1))  #set the Current version id on local
        local_userdata_id = local_userdata_id+1
        getMachineDataPath(machine_id,local_addons_id+1,local_userdata_id+1)
        xbmc.executebuiltin('runscript(script.postUpdate)')
        isRestart = True
      
      if int(match3[0]) > local_karaokeDB_id:     # Update karaoke database
        xbmc.executebuiltin('Notification(Update Database, Updating... Please Wait!!!,30000)')
        UpdateKaraokeDB()     #update Database
        autoUpdatePlugin.setSetting('KaraokeDB_id',local_karaokeDB_id+1)  #set the Current version id on local
        local_karaokeDB_id = local_karaokeDB_id+1
        isRestart = True
          
      if int(match4[0]) > local_gdrive_id:        #update  Gdrive authenticate
        xbmc.executebuiltin('Notification(Update Karaoke Setting, Updating... Please Wait!!!,30000)')
        UpdateGDriveSetting()     #update Gdrive Setting
        autoUpdatePlugin.setSetting('GDrive_id',local_gdrive_id)  #set the Current version id on local
        local_gdrive_id = local_gdrive_id+1
        isRestart = True
      if isRestart:
        xbmc.executebuiltin('XBMC.ReloadSkin()')        
    xbmc.sleep(8640000)