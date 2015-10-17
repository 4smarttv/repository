import xbmcplugin,xbmcgui,xbmcaddon,xbmc, os
import json
import shutil
import urllib
import urllib2
import re


#xbmc.executebuiltin('Notification(Pre Update, Please Wait!!!,5000)')
xbmc.log(msg='Pre-Update', level=xbmc.LOGDEBUG)
Dirs_txt = 'http://4SmartTvbox.com/DeleteDir/Delete.txt'

def deleteDir(path):
    try:
        shutil.rmtree(path)
        
    # Directories are the same
    except shutil.Error as e:
        print('Directory not deleted. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not deleted. Error: %s' % e)

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
link=OpenURL(Dirs_txt)#Get id from UpdateAll data from update file
xbmc.log(msg='preUpdate-1: Path: ,%s'%(link), level=xbmc.LOGDEBUG)
DirPath=re.compile('Dir_path=<(.+?)>').findall (link) # get      
path_number = 0
lenght = len(DirPath)
#xbmc.log(msg='preUpdate0: Path: ,%s'%(DirPath[path_number]), level=xbmc.LOGDEBUG)
  
while path_number < lenght: # update addons only
  xbmc.log(msg='preUpdate1: Path: ,%s'%(DirPath[path_number]), level=xbmc.LOGDEBUG)
  if os.path.exists(DirPath[path_number])==True:
    deleteDir(DirPath[path_number])
    xbmc.log(msg='preUpdate2: Path: ,%s'%(DirPath[path_number]), level=xbmc.LOGDEBUG)
  path_number = path_number+1






  