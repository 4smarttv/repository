import os, sys
import xbmc, xbmcaddon

__addon__        = xbmcaddon.Addon()
__addonid__      = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__language__     = __addon__.getLocalizedString
__cwd__          = __addon__.getAddonInfo('path').decode("utf-8")
__resource__   = xbmc.translatePath( os.path.join( __cwd__, 'resources', 'lib' ).encode("utf-8") ).decode("utf-8")

sys.path.append(__resource__)



if ( __name__ == "__main__" ):
    keyboard = xbmc.Keyboard( '', __language__(32101), False )
    keyboard.doModal()
    if ( keyboard.isConfirmed() ):
        searchstring = keyboard.getText()
        if searchstring.isdigit():
            if len(searchstring)==4 or len(searchstring)==5:
                import gui
                ui = gui.GUI( "script-karaokesearch-main.xml", __cwd__, "Default", searchstring=searchstring )
                ui.doModal()
                del ui
                sys.modules.clear()
            else: xbmc.executebuiltin('Notification(Karaoke Search,Enter a 4 or 5 digit numbers,5000,/plugin.video.live.streams.icon.png)') 
        else:
            if len(searchstring)>=5:
                import gui
                ui = gui.GUI( "script-karaokesearch-main.xml", __cwd__, "Default", searchstring=searchstring )
                ui.doModal()
                del ui
                sys.modules.clear()
            else:  xbmc.executebuiltin('Notification(Karaoke Search,Enter String 5 char or longer,5000,/plugin.video.live.streams.icon.png)') 
         