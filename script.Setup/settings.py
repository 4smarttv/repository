import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import os


ADDON = xbmcaddon.Addon(id='script.playkaraoke')
DATA_PATH = os.path.join(xbmc.translatePath('special://profile/data/scriptkaraoke'), '')

def addon():
    return ADDON

def setView():
    if ADDON.getSetting('auto-view') == 'true':
        return True
    else:
        return False

        
        
