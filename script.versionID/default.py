import xbmcplugin , xbmcgui , xbmcaddon , xbmc , os
#from t0mm0.common.net import Net as net
#from t0mm0.common.addon import Addon
#import settings
import json
import shutil
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = xbmcaddon . Addon ( id = 'script.versionID' )
oo = o0OO00 . getAddonInfo ( 'path' )
i1iII1IiiIiI1 = xbmc . translatePath ( o0OO00 . getAddonInfo ( 'profile' ) )
if 40 - 40: ooOoO0O00 * IIiIiII11i
if 51 - 51: oOo0O0Ooo * I1ii11iIi11i
I1IiI = xbmcaddon . Addon ( id = 'script.autoUpdate' )
o0OOO = I1IiI . getAddonInfo ( 'path' )
iIiiiI = xbmc . translatePath ( I1IiI . getAddonInfo ( 'profile' ) )
if 23 - 23: iii1II11ii * i11iII1iiI + iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
if 68 - 68: o00ooo0 / Oo00O0
ooO0oooOoO0 = str ( I1IiI . getSetting ( 'Version_id' ) )
if 21 - 21: IiIii1Ii1IIi / O0Oooo00 . oo00 * I1ii11iIi11i
xbmc . log ( msg = 'script.versionID software_version_id:,%s' % ( ooO0oooOoO0 ) , level = xbmc . LOGDEBUG )
o0000o0o0000o = str ( I1IiI . getSetting ( 'Machine_id' ) )
o0o0Oo0oooo0 = str ( I1IiI . getSetting ( 'AddOns_id' ) )
oO0O0o0o0 = str ( I1IiI . getSetting ( 'GDrive_id' ) )
i1iIIII = str ( I1IiI . getSetting ( 'KaraokeDB_id' ) )
I1 = str ( I1IiI . getSetting ( 'Userdata_id' ) )
O0OoOoo00o = xbmcgui . Dialog ( )
O0OoOoo00o . ok ( "Software Version: %s" % ( ooO0oooOoO0 ) , 'Machine ID: %s' % ( o0000o0o0000o ) , 'AddOns ID: %s' % ( o0o0Oo0oooo0 ) + ', GDrive ID: %s' % ( oO0O0o0o0 ) + ', KaraokeDB ID: %s' % ( i1iIIII ) + ', Userdata ID: %s' % ( I1 ) , 'Please, press OK' )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
