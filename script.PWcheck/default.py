import xbmcplugin , xbmcgui , xbmcaddon , xbmc , os
import shutil
if 64 - 64: i11iIiiIii
#Setup Plugin
OO0o = xbmcaddon . Addon ( id = 'script.PWCheck' )
Oo0Ooo = OO0o . getAddonInfo ( 'path' )
O0O0OO0O0O0 = xbmc . translatePath ( OO0o . getAddonInfo ( 'profile' ) )
if 5 - 5: iiI / ii1I
if 61 - 61: iII111iiiii11 % I1IiiI
if 27 - 27: iIiiiI1IiI1I1 * IIiIiII11i * IiIIi1I1Iiii - Ooo00oOo00o
I1IiI = os . path . join ( Oo0Ooo , 'settings.xml' )
o0OOO = os . path . join ( O0O0OO0O0O0 , 'settings.xml' )
if os . path . exists ( O0O0OO0O0O0 ) == False :
 os . mkdir ( O0O0OO0O0O0 )
 if 13 - 13: ooOo + Oo
 xbmc . log ( msg = 'script.autoUpdate des_settings_xml,%s' % ( I1IiI ) , level = xbmc . LOGDEBUG )
 xbmc . log ( msg = 'script.autoUpdate src_setting_xml,%s' % ( o0OOO ) , level = xbmc . LOGDEBUG )
 shutil . copyfile ( I1IiI , o0OOO )
 xbmc . sleep ( 5000 )
 xbmc . executebuiltin ( 'Notification(Setup, Created file for datapath_PWCheck_xml,5000)' )
o0O = int ( OO0o . getSetting ( 'PW' ) )
xbmc . log ( msg = 'Original PW: ,%s' % ( o0O ) , level = xbmc . LOGDEBUG )
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
O0oOO0o0 = xbmc . Keyboard ( '' , '                            Enter Password in Number:' , False )
O0oOO0o0 . doModal ( )
if ( O0oOO0o0 . isConfirmed ( ) ) :
 i1ii1iIII = int ( O0oOO0o0 . getText ( ) )
 xbmc . log ( msg = 'Entered PW: ,%s' % ( i1ii1iIII ) , level = xbmc . LOGDEBUG )
 if i1ii1iIII == o0O :
  xbmc . log ( 'PW is right' )
  xbmc . executebuiltin ( 'ActivateWindow(10025,plugin://plugin.video.4SmartHousePlugin/?category=XXX)' )
 else : xbmc . executebuiltin ( 'Notification(Sorry, Wrong password,5000)' )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
