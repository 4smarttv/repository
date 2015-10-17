import xbmcplugin,xbmcgui,xbmcaddon,xbmc, os
import json
import shutil

#xbmc.executebuiltin('Notification(Post Update,Please Wait!!!,5000)')
xbmc.log(msg='Post-Update', level=xbmc.LOGDEBUG)
#add delete directory code here
XBMC_Viet_path = '/storage/emulated/0/Android/data/org.xbmc.xbmc/files/.xbmc/addons/repository.xbmc-viet'
#delete youtube userdata path
youtube_storage_path = '/storage/emulated/0/Android/data/org.xbmc.xbmc/files/.xbmc/storage/userdata/addon_data/plugin.video.youtube'
def deleteDir(path):
    try:
        shutil.rmtree(path)
        
    # Directories are the same
    except shutil.Error as e:
        print('Directory not deleted. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not deleted. Error: %s' % e)
if os.path.exists(XBMC_Viet_path)==True:
  deleteDir(XBMC_Viet_path)
if os.path.exists(youtube_storage_path)==True:
  deleteDir(youtube_storage_path)
  