import xbmcplugin , xbmcgui , xbmcaddon , xbmc , os
import json
import shutil
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
#playKaraoke Plugin
o0OO00 = xbmcaddon . Addon ( id = 'script.playkaraoke' )
oo = o0OO00 . getAddonInfo ( 'path' )
i1iII1IiiIiI1 = xbmc . translatePath ( o0OO00 . getAddonInfo ( 'profile' ) )
iIiiiI1IiI1I1 = os . path . join ( oo , 'settings.xml' )
o0OoOoOO00 = os . path . join ( i1iII1IiiIiI1 , 'settings.xml' )
if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
o0OOO = xbmcaddon . Addon ( id = 'script.autoUpdate' )
if 13 - 13: ooOo + Ooo0O
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
O0oOO0o0 = xbmcgui . Dialog ( )
O0oOO0o0 . notification ( "Loading Songs, Please Wait!!!" , "Infor contact Authorized Dealer, or Call 1-800-558-9456" , xbmcgui . NOTIFICATION_INFO , 10000 )
i1ii1iIII = int ( o0OOO . getSetting ( 'Machine_id' ) )
if 59 - 59: II1i * o00ooo0 / o00 * Oo0oO0ooo
def o0oOoO00o ( path ) :
 import random
 i1ii1iIII = int ( o0OOO . getSetting ( 'Machine_id' ) )
 if i1ii1iIII == 1 or i1ii1iIII == 2 :
  if 43 - 43: o00O0oo . IiII
  IIii11I1 = 1
 else :
  IIii11I1 = random . randint ( 1 , 95 )
 oo0 = path + str ( IIii11I1 ) + '.m3u'
 if 80 - 80: i1IIi * iIii1I11I1II1 / o00ooo0 % IiII + o00 . o00ooo0
 xbmc . log ( msg = 'Karaoke: _queue_play_video: Adverize Path,%s' % ( oo0 ) , level = xbmc . LOGDEBUG )
 return oo0
 if 98 - 98: i11iIiiIii * Oo % II1i * II1i * OOOo0
 if 79 - 79: o00ooo0
class oOo0oooo00o ( xbmc . Player ) :
 if 65 - 65: Ooo0O * iIii1I11I1II1 * Oo0oO0ooo
 def __init__ ( self ) :
  xbmc . Player . __init__ ( self )
  xbmc . log ( msg = 'XBMC Playback Init' , level = xbmc . LOGDEBUG )
  if 18 - 18: iIii1I11I1II1 / ooOoO0o + IiII / Ooo00oOo00o - OOOo0 - ooOoO0o
 def onPlayBackStarted ( self ) :
  if 1 - 1: ooOoO0o - I1Ii111 % O0 + Oo - II1i / ooOoO0o
  xbmc . log ( msg = 'XBMC Playback Started' , level = xbmc . LOGDEBUG )
  if xbmc . Player ( ) . isPlayingVideo ( ) :
   iIiiI1 = xbmc . Player ( ) . getPlayingFile ( )
   xbmc . log ( msg = 'onPlayBackStarted: playing File: ,%s' % ( iIiiI1 ) , level = xbmc . LOGDEBUG )
   OoOooOOOO = 'http://www.4SmartTVBox.com/Video/adv'
   if OoOooOOOO in iIiiI1 :
    xbmc . executebuiltin ( 'Notification(Loading Next Song, Please Wait!!!,5000)' )
    xbmc . Player ( ) . playnext ( )
    if 45 - 45: o00 + o00O0oo
 def onPlayBackEnded ( self ) :
  if 17 - 17: Ooo0O
  xbmc . log ( msg = 'XBMC Playback Ended' , level = xbmc . LOGDEBUG )
  o00ooooO0oO = oOoOo00oOo . getposition ( )
  if o00ooooO0oO == - 1 :
   xbmc . abortRequested = True
  else :
   xbmc . executebuiltin ( 'Notification(Loading Next Song, Please Wait!!!,5000)' )
 def onPlayBackStopped ( self ) :
  if 96 - 96: i1IIi . ooOo * I1Ii111 % Oo0oO0ooo
  xbmc . abortRequested = True
  xbmc . log ( msg = 'XBMC Playback Stopped' , level = xbmc . LOGDEBUG )
  if 60 - 60: IiII * Ooo0O % Ooo0O % ooOoO0o * OOOo0 + i1IIi
OOoooooO = oOo0oooo00o ( )
oOoOo00oOo = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
if 14 - 14: ooOoO0o % O0
if oOoOo00oOo . load ( o0oOoO00o ( 'http://www.4smarttvbox.com/KaraokePL/PL_' ) ) :
 oOoOo00oOo . shuffle ( )
 xbmc . Player ( ) . play ( oOoOo00oOo )
 if 41 - 41: i1IIi + o00 + I1Ii111 - o00ooo0
elif oOoOo00oOo . load ( o0oOoO00o ( PL_local_path + 'PL_' ) ) :
 oOoOo00oOo . shuffle ( )
 xbmc . Player ( ) . play ( oOoOo00oOo )
 if 77 - 77: Ooo00oOo00o . o00ooo0 % Oo0oO0ooo
if i1ii1iIII == 1 :
 O0oOO0o0 . notification ( "Demo Karaoke 50 Songs" , "To Upgrade contact Authorized Dealer, or Call 1-800-558-9456" , xbmcgui . NOTIFICATION_INFO , 50000 )
elif i1ii1iIII == 2 :
 O0oOO0o0 . notification ( "Test Demo Karaoke 50 Songs" , "To Upgrade contact Authorized Dealer, or Call 1-800-558-9456" , xbmcgui . NOTIFICATION_INFO , 50000 )
elif i1ii1iIII == 3 :
 O0oOO0o0 . notification ( "Karaoke Full 10000 songs" , "Order at www.4SmartTvBox.com or Call 1-800-558-9456" , xbmcgui . NOTIFICATION_INFO , 50000 )
elif i1ii1iIII == 4 :
 O0oOO0o0 . notification ( "Test Karaoke 10000 Songs" , "Order at www.4SmartTvBox.com or Call 1-800-558-9456" , xbmcgui . NOTIFICATION_INFO , 50000 )
elif i1ii1iIII == 5 :
 O0oOO0o0 . notification ( "Promotion Karaoke Model" , "Order at www.4SmartTvBox.com or Call 1-800-558-9456" , xbmcgui . NOTIFICATION_INFO , 50000 )
elif i1ii1iIII == 6 :
 O0oOO0o0 . notification ( "Other Model" , "Order at www.4SmartTvBox.com or Call 1-800-558-9456" , xbmcgui . NOTIFICATION_INFO , 50000 )
elif i1ii1iIII == 7 :
 O0oOO0o0 . notification ( "Other 1 Model" , "Order at www.4SmartTvBox.com or Call 1-800-558-9456" , xbmcgui . NOTIFICATION_INFO , 50000 )
elif i1ii1iIII == 8 :
 O0oOO0o0 . notification ( "Development Model" , "Order www.4SmartTvBox.com or Call 1-800-558-9456" , xbmcgui . NOTIFICATION_INFO , 50000 )
elif i1ii1iIII == 9 or i1ii1iIII == 10 :
 O0oOO0o0 . notification ( "Hard Drive Karaoke" , " For Info Contact Authorized Dealer, or Call 1-800-558-9456" , xbmcgui . NOTIFICATION_INFO , 30000 )
else :
 O0oOO0o0 . notification ( "Extra model, check it " , "Need V2 Hard Drive plug in" , xbmcgui . NOTIFICATION_INFO , 30000 )
 if 42 - 42: IiII - i1IIi / i11iIiiIii + I1Ii111 + I1IiI
while ( not xbmc . abortRequested ) :
 xbmc . sleep ( 10000 )
xbmc . executebuiltin ( 'xbmc.activatewindow(home)' )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
