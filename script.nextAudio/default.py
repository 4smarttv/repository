import xbmcplugin , xbmcgui , xbmcaddon , xbmc , os
import json
import shutil
if 64 - 64: i11iIiiIii
#Setup Plugin
OO0o = xbmcaddon . Addon ( id = 'script.nextAudio' )
Oo0Ooo = OO0o . getAddonInfo ( 'path' )
O0O0OO0O0O0 = xbmc . translatePath ( OO0o . getAddonInfo ( 'profile' ) )
iiiii = xbmc . translatePath ( os . path . join ( O0O0OO0O0O0 , 'settings.xml' ) )
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
iI1 = xbmc . translatePath ( os . path . join ( 'special://home/storage/userdata' , 'guisettings.xml' ) )
i1I11i = os . path . join ( Oo0Ooo , 'settings.xml' )
OoOoOO00 = os . path . join ( O0O0OO0O0O0 , 'settings.xml' )
if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
if 73 - 73: OOooOOo / ii11ii1ii
if os . path . exists ( O0O0OO0O0O0 ) == False :
 os . mkdir ( O0O0OO0O0O0 )
 if 94 - 94: OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo
 shutil . copyfile ( i1I11i , OoOoOO00 )
O0oOO0o0 = 'Vietnamese'
i1ii1iIII = 'English'
xbmc . executebuiltin ( 'Action(audionextlanguage)' )
if 59 - 59: II1i * o00ooo0 / o00 * Oo0oO0ooo
def o0oOoO00o ( filename , old_string , new_string ) :
 i1 = open ( filename ) . read ( )
 if old_string in i1 :
  if 64 - 64: oo % O0Oooo00
  if 87 - 87: OOOo0 / o00ooo0 . OOooOOo * oOooOoO0Oo0O - Oo0oO0ooo * O0Oooo00
  xbmc . executebuiltin ( 'SetGUILanguage(English)' )
  i1 = i1 . replace ( old_string , new_string )
  O0 = open ( filename , 'w' )
  O0 . write ( i1 )
  O0 . flush ( )
  O0 . close ( )
 elif new_string in i1 :
  if 34 - 34: Oo0oO0ooo % Oo % ii11i % Oo0oO0ooo * o00 / ii11ii1ii
  if 31 - 31: i11iIiiIii / Ooo00oOo00o / O0Oooo00 * o0000oOoOoO0o / I1IiI
  xbmc . executebuiltin ( 'SetGUILanguage(Vietnamese)' )
  i1 = i1 . replace ( new_string , old_string )
  O0 = open ( filename , 'w' )
  O0 . write ( i1 )
  O0 . flush ( )
  O0 . close ( )
o0oOoO00o ( iiiii , O0oOO0o0 , i1ii1iIII )
if 99 - 99: ii11i * oOooOoO0Oo0O * Oo * ii11i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
