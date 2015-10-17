# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
import urllib
import urllib2
import datetime
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
from BeautifulSoup import BeautifulStoneSoup , BeautifulSoup , BeautifulSOAP
try :
 import json
except :
 import simplejson as json
import SimpleDownloader as downloader
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = xbmcaddon . Addon ( 'plugin.video.4SmartHouse' )
oo = o0OO00 . getAddonInfo ( 'version' )
i1iII1IiiIiI1 = xbmc . translatePath ( o0OO00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iIiiiI1IiI1I1 = xbmc . translatePath ( o0OO00 . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
o0OoOoOO00 = os . path . join ( i1iII1IiiIiI1 , 'favorites' )
I11i = os . path . join ( i1iII1IiiIiI1 , 'list_revision' )
O0O = os . path . join ( iIiiiI1IiI1I1 , 'icon.png' )
Oo = os . path . join ( iIiiiI1IiI1I1 , 'fanart.jpg' )
I1ii11iIi11i = os . path . join ( i1iII1IiiIiI1 , 'source_file' )
if 48 - 48: oO0o / OOooOOo / I11iIi1I / IiiIII111iI
IiII = os . path . join ( i1iII1IiiIiI1 , 'data_file.xml' )
downloader = downloader . SimpleDownloader ( )
iI1Ii11111iIi = o0OO00 . getSetting ( 'debug' )
if os . path . exists ( o0OoOoOO00 ) == True :
 i1i1II = open ( o0OoOoOO00 ) . read ( )
else : i1i1II = [ ]
if os . path . exists ( I1ii11iIi11i ) == True :
 O0oo0OO0 = open ( I1ii11iIi11i ) . read ( )
else : O0oo0OO0 = [ ]
if 6 - 6: oooO0oo0oOOOO - ooO0oo0oO0 - i111I * II1Ii1iI1i
if 12 - 12: o0oOoO00o
def i1 ( string ) :
 if iI1Ii11111iIi == 'true' :
  xbmc . log ( "[addon.live.streams-%s]: %s" % ( oo , string ) )
  if 64 - 64: ooO0Oooo00 % Ooo0
  if 89 - 89: I111i1i1111i - Ii1Ii1iiii11 % I1I1i1
def IiI1i ( url ) :
 try :
  OOo0o0 = urllib2 . Request ( url )
  O0OoOoo00o = urllib2 . urlopen ( OOo0o0 )
  iiiI11 = O0OoOoo00o . read ( )
  O0OoOoo00o . close ( )
  if 91 - 91: oOOOO / i1IIi + I1I1i1 + Ooo0
  if 17 - 17: ooO0oo0oO0
  if 64 - 64: Ooo0 % i1IIi % OoooooooOO
  if 3 - 3: I111i1i1111i + O0
  if 42 - 42: o0oOoO00o / i1IIi + i11iIiiIii - Ooo0
  return iiiI11
 except urllib2 . URLError , oo0Ooo0 :
  i1 ( 'URL: ' + url )
  if hasattr ( oo0Ooo0 , 'code' ) :
   i1 ( 'We failed with error code - %s.' % oo0Ooo0 . code )
   if 46 - 46: oOOOO % oOOOO - II1Ii1iI1i * ooO0oo0oO0 % I111i1i1111i
   if 55 - 55: oooO0oo0oOOOO % i1IIi / Ooo0 - II1Ii1iI1i - O0 / oO0o
   if 28 - 28: iIii1I11I1II1 - i1IIi
   if 70 - 70: IiiIII111iI . IiiIII111iI - IiiIII111iI / i111I * o0oOoO00o
   if 86 - 86: i11iIiiIii + Ooo0 + oOOOO * ooO0Oooo00 + ooO0oo0oO0
   if 61 - 61: IiiIII111iI / i11iIiiIii
   if 34 - 34: OoooooooOO + iIii1I11I1II1 + i11iIiiIii - i111I + i11iIiiIii
  elif hasattr ( oo0Ooo0 , 'reason' ) :
   i1 ( 'We failed to reach a server.' )
   i1 ( 'Reason: %s' % oo0Ooo0 . reason )
   if 65 - 65: oooO0oo0oOOOO
   if 6 - 6: OOooOOo / I11iIi1I % Ooo0
   if 84 - 84: i11iIiiIii . ooO0oo0oO0
   if 100 - 100: Ooo0 - Ooo0 - I1I1i1
   if 20 - 20: OoooooooOO
   if 13 - 13: i1IIi - Ooo0 % II1Ii1iI1i / iIii1I11I1II1 % I111i1i1111i
   if 97 - 97: i11iIiiIii
   if 32 - 32: I11iIi1I * O0 % II1Ii1iI1i % Ooo0 . Ii1Ii1iiii11
   if 61 - 61: oOOOO
def oOOO00o ( ) :
 if os . path . exists ( o0OoOoOO00 ) == True :
  O0O00o0OOO0 ( 'Favorites' , 'url' , 4 , os . path . join ( iIiiiI1IiI1I1 , 'resources' , 'favorite.png' ) , Oo , '' , '' , '' , '' )
 if o0OO00 . getSetting ( "browse_xml_database" ) == "true" :
  O0O00o0OOO0 ( 'XML Database' , 'http://xbmcplus.xb.funpic.de/up/data/files/' , 15 , O0O , Oo , '' , '' , '' , '' )
 if o0OO00 . getSetting ( "browse_community" ) == "true" :
  O0O00o0OOO0 ( 'Community Files' , 'community_files' , 16 , O0O , Oo , '' , '' , '' , '' )
 if os . path . exists ( I1ii11iIi11i ) == True :
  Ii1iIIIi1ii = json . loads ( open ( I1ii11iIi11i , "r" ) . read ( ) )
  if len ( Ii1iIIIi1ii ) > 1 :
   for o0oo0o0O00OO in Ii1iIIIi1ii :
    if 80 - 80: i1IIi
    if isinstance ( o0oo0o0O00OO , list ) :
     O0O00o0OOO0 ( o0oo0o0O00OO [ 0 ] . encode ( 'utf-8' ) , o0oo0o0O00OO [ 1 ] . encode ( 'utf-8' ) , 1 , O0O , Oo , '' , '' , '' , '' , 'source' )
    else :
     oOOO0o0o = O0O
     iiI1 = Oo
     i11Iiii = ''
     iI = ''
     credits = ''
     I1i1I1II = ''
     if o0oo0o0O00OO . has_key ( 'thumbnail' ) :
      oOOO0o0o = o0oo0o0O00OO [ 'thumbnail' ]
     if o0oo0o0O00OO . has_key ( 'fanart' ) :
      iiI1 = o0oo0o0O00OO [ 'fanart' ]
     if o0oo0o0O00OO . has_key ( 'description' ) :
      i11Iiii = o0oo0o0O00OO [ 'description' ]
     if o0oo0o0O00OO . has_key ( 'date' ) :
      iI = o0oo0o0O00OO [ 'date' ]
     if o0oo0o0O00OO . has_key ( 'genre' ) :
      I1i1I1II = o0oo0o0O00OO [ 'genre' ]
     if o0oo0o0O00OO . has_key ( 'credits' ) :
      credits = o0oo0o0O00OO [ 'credits' ]
     O0O00o0OOO0 ( o0oo0o0O00OO [ 'title' ] . encode ( 'utf-8' ) , o0oo0o0O00OO [ 'url' ] . encode ( 'utf-8' ) , 1 , oOOO0o0o , iiI1 , i11Iiii , I1i1I1II , iI , credits , 'source' )
     if 45 - 45: I1I1i1 . oooO0oo0oOOOO
  else :
   if isinstance ( Ii1iIIIi1ii [ 0 ] , list ) :
    oO ( Ii1iIIIi1ii [ 0 ] [ 1 ] . encode ( 'utf-8' ) , Oo )
   else :
    oO ( Ii1iIIIi1ii [ 0 ] [ 'url' ] , Ii1iIIIi1ii [ 0 ] [ 'fanart' ] )
    if 6 - 6: i111I
    if 31 - 31: Ooo0 . Ooo0 - ooO0oo0oO0 / IiiIII111iI + oOOOO * OOooOOo
def O0ooOooooO ( url = None ) :
 if url is None :
  if not o0OO00 . getSetting ( "new_file_source" ) == "" :
   o00O = o0OO00 . getSetting ( 'new_file_source' ) . decode ( 'utf-8' )
  elif not o0OO00 . getSetting ( "new_url_source" ) == "" :
   o00O = o0OO00 . getSetting ( 'new_url_source' ) . decode ( 'utf-8' )
 else :
  o00O = url
 if o00O == '' or o00O is None :
  return
 i1 ( 'Adding New Source: ' + o00O . encode ( 'utf-8' ) )
 if 69 - 69: II1Ii1iI1i % I1I1i1 - ooO0oo0oO0 + I1I1i1 - O0 % OoooooooOO
 Iii111II = None
 iiiI11 = iiii11I ( o00O )
 if 96 - 96: oO0o % Ooo0 . o0oOoO00o + OoooooooOO * II1Ii1iI1i - oooO0oo0oOOOO
 if iiiI11 . find ( 'channels_info' ) :
  Iii111II = iiiI11 . channels_info
 elif iiiI11 . find ( 'items_info' ) :
  Iii111II = iiiI11 . items_info
 if Iii111II :
  i11i1 = { }
  i11i1 [ 'url' ] = o00O
  try : i11i1 [ 'title' ] = Iii111II . title . string
  except : pass
  try : i11i1 [ 'thumbnail' ] = Iii111II . thumbnail . string
  except : pass
  try : i11i1 [ 'fanart' ] = Iii111II . fanart . string
  except : pass
  try : i11i1 [ 'genre' ] = Iii111II . genre . string
  except : pass
  try : i11i1 [ 'description' ] = Iii111II . description . string
  except : pass
  try : i11i1 [ 'date' ] = Iii111II . date . string
  except : pass
  try : i11i1 [ 'credits' ] = Iii111II . credits . string
  except : pass
 else :
  if '/' in o00O :
   IIIii1II1II = o00O . split ( '/' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '\\' in o00O :
   IIIii1II1II = o00O . split ( '\\' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '%' in IIIii1II1II :
   IIIii1II1II = urllib . unquote_plus ( IIIii1II1II )
  i1I1iI = xbmc . Keyboard ( IIIii1II1II , 'Displayed Name, Rename?' )
  i1I1iI . doModal ( )
  if ( i1I1iI . isConfirmed ( ) == False ) :
   return
  oo0OooOOo0 = i1I1iI . getText ( )
  if len ( oo0OooOOo0 ) == 0 :
   return
  i11i1 = { }
  i11i1 [ 'title' ] = oo0OooOOo0
  i11i1 [ 'url' ] = o00O
  i11i1 [ 'fanart' ] = iiI1
  if 92 - 92: I111i1i1111i . ooO0Oooo00 + ooO0oo0oO0
 if os . path . exists ( I1ii11iIi11i ) == False :
  IiII1I11i1I1I = [ ]
  IiII1I11i1I1I . append ( i11i1 )
  oO0Oo = open ( I1ii11iIi11i , "w" )
  oO0Oo . write ( json . dumps ( IiII1I11i1I1I ) )
  oO0Oo . close ( )
 else :
  Ii1iIIIi1ii = json . loads ( open ( I1ii11iIi11i , "r" ) . read ( ) )
  Ii1iIIIi1ii . append ( i11i1 )
  oO0Oo = open ( I1ii11iIi11i , "w" )
  oO0Oo . write ( json . dumps ( Ii1iIIIi1ii ) )
  oO0Oo . close ( )
 o0OO00 . setSetting ( 'new_url_source' , "" )
 o0OO00 . setSetting ( 'new_file_source' , "" )
 xbmc . executebuiltin ( "XBMC.Notification(LiveStreams,New source added.,5000," + O0O + ")" )
 if not url is None :
  if 'xbmcplus.xb.funpic.de' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=14,replace)" % sys . argv [ 0 ] )
  elif 'community-links' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=10,replace)" % sys . argv [ 0 ] )
 else : o0OO00 . openSettings ( )
 if 54 - 54: ooO0oo0oO0 - OOooOOo + OoooooooOO
 if 70 - 70: Ooo0 / ooO0Oooo00 . I111i1i1111i % I11iIi1I
def OOoOO00OOO0OO ( name ) :
 Ii1iIIIi1ii = json . loads ( open ( I1ii11iIi11i , "r" ) . read ( ) )
 for iI1I111Ii111i in range ( len ( Ii1iIIIi1ii ) ) :
  if isinstance ( Ii1iIIIi1ii [ iI1I111Ii111i ] , list ) :
   if Ii1iIIIi1ii [ iI1I111Ii111i ] [ 0 ] == name :
    del Ii1iIIIi1ii [ iI1I111Ii111i ]
    oO0Oo = open ( I1ii11iIi11i , "w" )
    oO0Oo . write ( json . dumps ( Ii1iIIIi1ii ) )
    oO0Oo . close ( )
    break
  else :
   if Ii1iIIIi1ii [ iI1I111Ii111i ] [ 'title' ] == name :
    del Ii1iIIIi1ii [ iI1I111Ii111i ]
    oO0Oo = open ( I1ii11iIi11i , "w" )
    oO0Oo . write ( json . dumps ( Ii1iIIIi1ii ) )
    oO0Oo . close ( )
    break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 7 - 7: oOOOO * IiiIII111iI % II1Ii1iI1i . Ii1Ii1iiii11
 if 45 - 45: i11iIiiIii * oO0o % iIii1I11I1II1 + i111I - Ooo0
def iIi1iIiii111 ( url , browse = False ) :
 if url is None :
  url = 'http://xbmcplus.xb.funpic.de/up/data/files/'
 iIIIi1 = BeautifulSoup ( IiI1i ( url ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 for o0oo0o0O00OO in iIIIi1 ( 'a' ) :
  iiII1i1 = o0oo0o0O00OO [ 'href' ]
  if not iiII1i1 . startswith ( '?' ) :
   o00oOO0o = o0oo0o0O00OO . string
   if o00oOO0o not in [ 'Parent Directory' , 'recycle_bin/' ] :
    if iiII1i1 . endswith ( '/' ) :
     if browse :
      O0O00o0OOO0 ( o00oOO0o , url + iiII1i1 , 15 , O0O , iiI1 , '' , '' , '' )
     else :
      O0O00o0OOO0 ( o00oOO0o , url + iiII1i1 , 14 , O0O , iiI1 , '' , '' , '' )
    elif iiII1i1 . endswith ( '.xml' ) :
     if browse :
      O0O00o0OOO0 ( o00oOO0o , url + iiII1i1 , 1 , O0O , iiI1 , '' , '' , '' , '' , 'download' )
     else :
      if os . path . exists ( I1ii11iIi11i ) == True :
       if o00oOO0o in O0oo0OO0 :
        O0O00o0OOO0 ( o00oOO0o + ' (in use)' , url + iiII1i1 , 11 , O0O , iiI1 , '' , '' , '' , '' , 'download' )
       else :
        O0O00o0OOO0 ( o00oOO0o , url + iiII1i1 , 11 , O0O , iiI1 , '' , '' , '' , '' , 'download' )
      else :
       O0O00o0OOO0 ( o00oOO0o , url + iiII1i1 , 11 , O0O , iiI1 , '' , '' , '' , '' , 'download' )
       if 80 - 80: II1Ii1iI1i + o0oOoO00o - o0oOoO00o % I111i1i1111i
       if 63 - 63: OOooOOo - i111I + O0 % ooO0Oooo00 / iIii1I11I1II1 / ooO0oo0oO0
def O0o0O00Oo0o0 ( browse = False ) :
 O00O0oOO00O00 = 'http://community-links.googlecode.com/svn/trunk/'
 iIIIi1 = BeautifulSoup ( IiI1i ( O00O0oOO00O00 ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 i1Oo00 = iIIIi1 ( 'ul' ) [ 0 ] ( 'li' ) [ 1 : ]
 for o0oo0o0O00OO in i1Oo00 :
  o00oOO0o = o0oo0o0O00OO ( 'a' ) [ 0 ] [ 'href' ]
  if browse :
   O0O00o0OOO0 ( o00oOO0o , O00O0oOO00O00 + o00oOO0o , 1 , O0O , iiI1 , '' , '' , '' , '' , 'download' )
  else :
   O0O00o0OOO0 ( o00oOO0o , O00O0oOO00O00 + o00oOO0o , 11 , O0O , iiI1 , '' , '' , '' , '' , 'download' )
   if 31 - 31: I1I1i1 . oooO0oo0oOOOO / O0
   if 89 - 89: oooO0oo0oOOOO
def iiii11I ( url ) :
 if url . startswith ( 'http://' ) :
  iiiI11 = IiI1i ( url )
  if 68 - 68: IiiIII111iI * OoooooooOO % O0 + IiiIII111iI + oOOOO
  if 4 - 4: oOOOO + O0 * o0oOoO00o
  if 55 - 55: I11iIi1I + iIii1I11I1II1 / oooO0oo0oOOOO * II1Ii1iI1i - i11iIiiIii - Ooo0
  if 25 - 25: i111I
  if 7 - 7: i1IIi / OOooOOo * I1I1i1 . Ii1Ii1iiii11 . iIii1I11I1II1
  if 13 - 13: o0oOoO00o / i11iIiiIii
  if 2 - 2: OOooOOo / O0 / ooO0oo0oO0 % oooO0oo0oOOOO % Ooo0
  if 52 - 52: ooO0oo0oO0
 else :
  if xbmcvfs . exists ( url ) :
   if url . startswith ( "smb://" ) or url . startswith ( "nfs://" ) :
    o0OO0oOO0O0 = xbmcvfs . copy ( url , os . path . join ( i1iII1IiiIiI1 , 'temp' , 'sorce_temp.txt' ) )
    if o0OO0oOO0O0 :
     iiiI11 = open ( os . path . join ( i1iII1IiiIiI1 , 'temp' , 'sorce_temp.txt' ) , "r" ) . read ( )
     xbmcvfs . delete ( os . path . join ( i1iII1IiiIiI1 , 'temp' , 'sorce_temp.txt' ) )
    else :
     i1 ( "failed to copy from smb:" )
   else :
    iiiI11 = open ( url , 'r' ) . read ( )
  else :
   i1 ( "Soup Data not found!" )
   return
 return BeautifulSOAP ( iiiI11 , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 8 - 8: II1Ii1iI1i
 if 7 - 7: ooO0oo0oO0 - OOooOOo
def oO ( url , fanart ) :
 iIIIi1 = iiii11I ( url )
 if len ( iIIIi1 ( 'channels' ) ) > 0 :
  OOo00O0 = iIIIi1 ( 'channel' )
  for ooOOOoO in OOo00O0 :
   o00oOO0o = ooOOOoO ( 'name' ) [ 0 ] . string
   o0o = ooOOOoO ( 'thumbnail' ) [ 0 ] . string
   if o0o == None :
    o0o = ''
    if 84 - 84: O0
   try :
    if not ooOOOoO ( 'fanart' ) :
     if o0OO00 . getSetting ( 'use_thumb' ) == "true" :
      OOOooOO0 = o0o
     else :
      OOOooOO0 = fanart
    else :
     OOOooOO0 = ooOOOoO ( 'fanart' ) [ 0 ] . string
    if OOOooOO0 == None :
     raise
   except :
    OOOooOO0 = fanart
    if 87 - 87: II1Ii1iI1i * i111I + o0oOoO00o / iIii1I11I1II1 / I111i1i1111i
   try :
    i11Iiii = ooOOOoO ( 'info' ) [ 0 ] . string
    if i11Iiii == None :
     raise
   except :
    i11Iiii = ''
    if 37 - 37: I111i1i1111i - oOOOO * II1Ii1iI1i % i11iIiiIii - I1I1i1
   try :
    I1i1I1II = ooOOOoO ( 'genre' ) [ 0 ] . string
    if I1i1I1II == None :
     raise
   except :
    I1i1I1II = ''
    if 83 - 83: ooO0Oooo00 / OOooOOo
   try :
    iI = ooOOOoO ( 'date' ) [ 0 ] . string
    if iI == None :
     raise
   except :
    iI = ''
    if 34 - 34: Ii1Ii1iiii11
   try :
    credits = ooOOOoO ( 'credits' ) [ 0 ] . string
    if credits == None :
     raise
   except :
    credits = ''
    if 57 - 57: II1Ii1iI1i . ooO0Oooo00 . i1IIi
   try :
    O0O00o0OOO0 ( o00oOO0o . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , o0o , OOOooOO0 , i11Iiii , I1i1I1II , iI , credits , True )
   except :
    i1 ( 'There was a problem adding directory from getData(): ' + o00oOO0o . encode ( 'utf-8' , 'ignore' ) )
 else :
  i1 ( 'No Channels: getItems' )
  i11Iii ( iIIIi1 ( 'item' ) , fanart )
  if 16 - 16: oO0o % oooO0oo0oOOOO - oO0o + Ooo0
  if 12 - 12: o0oOoO00o / o0oOoO00o + i11iIiiIii
def Ii ( name , url , fanart ) :
 iIIIi1 = iiii11I ( url )
 iii1i = iIIIi1 . find ( 'channel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 I11i1ii1 = iii1i ( 'item' )
 try :
  OOOooOO0 = iii1i ( 'fanart' ) [ 0 ] . string
  if OOOooOO0 == None :
   raise
 except :
  OOOooOO0 = fanart
 for ooOOOoO in iii1i ( 'subchannel' ) :
  name = ooOOOoO ( 'name' ) [ 0 ] . string
  try :
   o0o = ooOOOoO ( 'thumbnail' ) [ 0 ] . string
   if o0o == None :
    raise
  except :
   o0o = ''
  try :
   if not ooOOOoO ( 'fanart' ) :
    if o0OO00 . getSetting ( 'use_thumb' ) == "true" :
     OOOooOO0 = o0o
   else :
    OOOooOO0 = ooOOOoO ( 'fanart' ) [ 0 ] . string
   if OOOooOO0 == None :
    raise
  except :
   pass
  try :
   i11Iiii = ooOOOoO ( 'info' ) [ 0 ] . string
   if i11Iiii == None :
    raise
  except :
   i11Iiii = ''
   if 87 - 87: ooO0Oooo00 - iIii1I11I1II1 + OOooOOo . I111i1i1111i
  try :
   I1i1I1II = ooOOOoO ( 'genre' ) [ 0 ] . string
   if I1i1I1II == None :
    raise
  except :
   I1i1I1II = ''
   if 62 - 62: O0 * i1IIi * ooO0oo0oO0 - OOooOOo + OOooOOo
  try :
   iI = ooOOOoO ( 'date' ) [ 0 ] . string
   if iI == None :
    raise
  except :
   iI = ''
   if 34 - 34: iIii1I11I1II1 - ooO0oo0oO0
  try :
   credits = ooOOOoO ( 'credits' ) [ 0 ] . string
   if credits == None :
    raise
  except :
   credits = ''
   if 91 - 91: I111i1i1111i % i1IIi % iIii1I11I1II1
  try :
   O0O00o0OOO0 ( name . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 3 , o0o , OOOooOO0 , i11Iiii , I1i1I1II , credits , iI )
  except :
   i1 ( 'There was a problem adding directory - ' + name . encode ( 'utf-8' , 'ignore' ) )
 i11Iii ( I11i1ii1 , OOOooOO0 )
 if 20 - 20: o0oOoO00o % Ooo0 / Ooo0 + Ooo0
 if 45 - 45: II1Ii1iI1i - Ii1Ii1iiii11 - OoooooooOO - IiiIII111iI . oO0o / O0
def oo0o00O ( name , url , fanart ) :
 iIIIi1 = iiii11I ( url )
 iii1i = iIIIi1 . find ( 'subchannel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 I11i1ii1 = iii1i ( 'subitem' )
 i11Iii ( I11i1ii1 , fanart )
 if 51 - 51: Ooo0 - IiiIII111iI * I111i1i1111i
 if 66 - 66: OoooooooOO + O0
def i11Iii ( items , fanart ) :
 I1IiiI = len ( items )
 i1 ( 'Total Items: %s' % I1IiiI )
 for IIi in items :
  try :
   o00oOO0o = IIi ( 'title' ) [ 0 ] . string
   if o00oOO0o is None :
    o00oOO0o = 'unknown?'
  except :
   i1 ( 'Name Error' )
   o00oOO0o = ''
  try :
   if IIi ( 'epg' ) :
    if IIi ( 'epg' ) [ 0 ] . string > 1 :
     o00oOO0o += i1Iii1i1I ( IIi ( 'epg' ) [ 0 ] . string )
   else :
    pass
  except :
   i1 ( 'EPG Error' )
   if 91 - 91: i111I + OOooOOo . o0oOoO00o * i111I + OOooOOo * I11iIi1I
  try :
   O00O0oOO00O00 = [ ]
   for o0oo0o0O00OO in IIi ( 'link' ) :
    if not o0oo0o0O00OO . string == None :
     O00O0oOO00O00 . append ( o0oo0o0O00OO . string )
   if len ( O00O0oOO00O00 ) < 1 :
    raise
  except :
   i1 ( 'Error <link> element, Passing:' + o00oOO0o . encode ( 'utf-8' , 'ignore' ) )
   continue
   if 80 - 80: I111i1i1111i % o0oOoO00o % II1Ii1iI1i - I11iIi1I + I11iIi1I
  try :
   o0o = IIi ( 'thumbnail' ) [ 0 ] . string
   if o0o == None :
    raise
  except :
   o0o = ''
  try :
   if not IIi ( 'fanart' ) :
    if o0OO00 . getSetting ( 'use_thumb' ) == "true" :
     OOOooOO0 = o0o
    else :
     OOOooOO0 = fanart
   else :
    OOOooOO0 = IIi ( 'fanart' ) [ 0 ] . string
   if OOOooOO0 == None :
    raise
  except :
   OOOooOO0 = fanart
  try :
   i11Iiii = IIi ( 'info' ) [ 0 ] . string
   if i11Iiii == None :
    raise
  except :
   i11Iiii = ''
   if 19 - 19: oooO0oo0oOOOO * i1IIi
  try :
   I1i1I1II = IIi ( 'genre' ) [ 0 ] . string
   if I1i1I1II == None :
    raise
  except :
   I1i1I1II = ''
   if 14 - 14: I111i1i1111i
  try :
   iI = IIi ( 'date' ) [ 0 ] . string
   if iI == None :
    raise
  except :
   iI = ''
   if 11 - 11: Ii1Ii1iiii11 * OOooOOo . iIii1I11I1II1 % OoooooooOO + I111i1i1111i
  OOO = None
  if IIi ( 'regex' ) :
   try :
    OOO = { }
    for o0oo0o0O00OO in IIi ( 'regex' ) :
     OOO [ o0oo0o0O00OO ( 'name' ) [ 0 ] . string ] = { }
     OOO [ o0oo0o0O00OO ( 'name' ) [ 0 ] . string ] [ 'expre' ] = o0oo0o0O00OO ( 'expres' ) [ 0 ] . string
     OOO [ o0oo0o0O00OO ( 'name' ) [ 0 ] . string ] [ 'page' ] = o0oo0o0O00OO ( 'page' ) [ 0 ] . string
     try :
      OOO [ o0oo0o0O00OO ( 'name' ) [ 0 ] . string ] [ 'refer' ] = o0oo0o0O00OO ( 'referer' ) [ 0 ] . string
     except :
      i1 ( "Regex: -- No Referer --" )
    OOO = urllib . quote ( repr ( OOO ) )
   except :
    OOO = None
    i1 ( 'regex Error: ' + o00oOO0o . encode ( 'utf-8' , 'ignore' ) )
    if 68 - 68: oO0o + ooO0Oooo00
  try :
   if len ( O00O0oOO00O00 ) > 1 :
    I1I1I = 0
    OoOO000 = [ ]
    for o0oo0o0O00OO in O00O0oOO00O00 :
     OoOO000 . append ( o0oo0o0O00OO )
    if o0OO00 . getSetting ( 'add_playlist' ) == "false" :
     for o0oo0o0O00OO in O00O0oOO00O00 :
      I1I1I += 1
      i1Ii11i1i ( o0oo0o0O00OO , '%s) %s' % ( I1I1I , o00oOO0o . encode ( 'utf-8' , 'ignore' ) ) , o0o , OOOooOO0 , i11Iiii , I1i1I1II , iI , True , OoOO000 , OOO , I1IiiI )
    else :
     i1Ii11i1i ( '' , o00oOO0o . encode ( 'utf-8' , 'ignore' ) , o0o , OOOooOO0 , i11Iiii , I1i1I1II , iI , True , OoOO000 , OOO , I1IiiI )
   else :
    i1Ii11i1i ( O00O0oOO00O00 [ 0 ] , o00oOO0o . encode ( 'utf-8' , 'ignore' ) , o0o , OOOooOO0 , i11Iiii , I1i1I1II , iI , True , None , OOO , I1IiiI )
  except :
   i1 ( 'There was a problem adding item - ' + o00oOO0o . encode ( 'utf-8' , 'ignore' ) )
   if 91 - 91: IiiIII111iI
   if 95 - 95: OOooOOo + i11iIiiIii
def I1Ii ( regexs , url ) :
 regexs = eval ( urllib . unquote ( regexs ) )
 O0oo00o0O = { }
 i1I1I = re . compile ( '\$doregex\[([^\]]*)\]' ) . findall ( url )
 for iiI1I in i1I1I :
  if iiI1I in regexs :
   IiIiiIIiI = regexs [ iiI1I ]
   if IiIiiIIiI [ 'page' ] in O0oo00o0O :
    ooOO0OOOO0oo0 = O0oo00o0O [ IiIiiIIiI [ 'page' ] ]
   else :
    OOo0o0 = urllib2 . Request ( IiIiiIIiI [ 'page' ] )
    OOo0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
    if 'refer' in IiIiiIIiI :
     OOo0o0 . add_header ( 'Referer' , IiIiiIIiI [ 'refer' ] )
    O0OoOoo00o = urllib2 . urlopen ( OOo0o0 )
    ooOO0OOOO0oo0 = O0OoOoo00o . read ( )
    O0OoOoo00o . close ( )
    O0oo00o0O [ IiIiiIIiI [ 'page' ] ] = ooOO0OOOO0oo0
   I11iiI1i1 = re . compile ( IiIiiIIiI [ 'expre' ] ) . search ( ooOO0OOOO0oo0 )
   url = url . replace ( "$doregex[" + iiI1I + "]" , I11iiI1i1 . group ( 1 ) . strip ( ) )
 IIi = xbmcgui . ListItem ( path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIi )
 if 47 - 47: I111i1i1111i - Ooo0 . oO0o + OoooooooOO . i11iIiiIii
 if 94 - 94: ooO0oo0oO0 * Ooo0 / I11iIi1I / Ooo0
def oO0 ( ) :
 O0OO0O = [ ]
 OO = sys . argv [ 2 ]
 if len ( OO ) >= 2 :
  OoOoO = sys . argv [ 2 ]
  Ii1I1i = OoOoO . replace ( '?' , '' )
  if ( OoOoO [ len ( OoOoO ) - 1 ] == '/' ) :
   OoOoO = OoOoO [ 0 : len ( OoOoO ) - 2 ]
  OOI1iI1ii1II = Ii1I1i . split ( '&' )
  O0OO0O = { }
  for o0oo0o0O00OO in range ( len ( OOI1iI1ii1II ) ) :
   O0O0OOOOoo = { }
   O0O0OOOOoo = OOI1iI1ii1II [ o0oo0o0O00OO ] . split ( '=' )
   if ( len ( O0O0OOOOoo ) ) == 2 :
    O0OO0O [ O0O0OOOOoo [ 0 ] ] = O0O0OOOOoo [ 1 ]
 return O0OO0O
 if 74 - 74: i111I + oO0o / IiiIII111iI
 if 100 - 100: oooO0oo0oOOOO * iIii1I11I1II1
def oOo00oOoO000 ( ) :
 I11i1ii1 = json . loads ( open ( o0OoOoOO00 ) . read ( ) )
 I1IiiI = len ( I11i1ii1 )
 for o0oo0o0O00OO in I11i1ii1 :
  o00oOO0o = o0oo0o0O00OO [ 0 ]
  O00O0oOO00O00 = o0oo0o0O00OO [ 1 ]
  OOooo0oOO0O = o0oo0o0O00OO [ 2 ]
  try :
   OOOooOO0 = o0oo0o0O00OO [ 3 ]
   if OOOooOO0 == None :
    raise
  except :
   if o0OO00 . getSetting ( 'use_thumb' ) == "true" :
    OOOooOO0 = OOooo0oOO0O
   else :
    OOOooOO0 = iiI1
  try : OoOO000 = o0oo0o0O00OO [ 5 ]
  except : OoOO000 = None
  try : OOO = o0oo0o0O00OO [ 6 ]
  except : OOO = None
  if 62 - 62: OOooOOo
  try :
   if not o0oo0o0O00OO [ 4 ] == 0 :
    O0O00o0OOO0 ( o00oOO0o , O00O0oOO00O00 , o0oo0o0O00OO [ 4 ] , OOooo0oOO0O , iiI1 , '' , '' , '' , '' , 'fav' )
   else :
    i1Ii11i1i ( O00O0oOO00O00 , o00oOO0o , OOooo0oOO0O , OOOooOO0 , '' , '' , '' , 'fav' , OoOO000 , OOO , I1IiiI )
  except :
   i1Ii11i1i ( O00O0oOO00O00 , o00oOO0o , OOooo0oOO0O , OOOooOO0 , '' , '' , '' , 'fav' , OoOO000 , OOO , I1IiiI )
   if 100 - 100: Ooo0 - O0 % II1Ii1iI1i * o0oOoO00o + OOooOOo
   if 88 - 88: OoooooooOO - IiiIII111iI * O0 * OoooooooOO . OoooooooOO
def I111iI ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 oOOo0 = [ ]
 if os . path . exists ( o0OoOoOO00 ) == False :
  i1 ( 'Making Favorites File' )
  oOOo0 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  II1I1iiIII = open ( o0OoOoOO00 , "w" )
  II1I1iiIII . write ( json . dumps ( oOOo0 ) )
  II1I1iiIII . close ( )
 else :
  i1 ( 'Appending Favorites' )
  II1I1iiIII = open ( o0OoOoOO00 ) . read ( )
  iiiI11 = json . loads ( II1I1iiIII )
  iiiI11 . append ( ( name , url , iconimage , fanart , mode ) )
  oO0Oo = open ( o0OoOoOO00 , "w" )
  oO0Oo . write ( json . dumps ( iiiI11 ) )
  oO0Oo . close ( )
  if 77 - 77: oooO0oo0oOOOO - oO0o - oOOOO
  if 49 - 49: oO0o % O0 . oooO0oo0oOOOO + II1Ii1iI1i / OOooOOo
def O0oOOoOooooO ( name ) :
 iiiI11 = json . loads ( open ( o0OoOoOO00 ) . read ( ) )
 for iI1I111Ii111i in range ( len ( iiiI11 ) ) :
  if iiiI11 [ iI1I111Ii111i ] [ 0 ] == name :
   del iiiI11 [ iI1I111Ii111i ]
   oO0Oo = open ( o0OoOoOO00 , "w" )
   oO0Oo . write ( json . dumps ( iiiI11 ) )
   oO0Oo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 62 - 62: OoooooooOO * OOooOOo
 if 58 - 58: oooO0oo0oOOOO % ooO0oo0oO0
def i1OOoO ( name , list ) :
 OoOO000 = xbmc . PlayList ( 1 )
 OoOO000 . clear ( )
 IIi = 0
 for o0oo0o0O00OO in list :
  IIi += 1
  OO0O000 = xbmcgui . ListItem ( '%s) %s' % ( str ( IIi ) , name ) )
  OoOO000 . add ( o0oo0o0O00OO , OO0O000 )
 xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
 if 37 - 37: OoooooooOO - O0 - ooO0oo0oO0
 if 77 - 77: o0oOoO00o * iIii1I11I1II1
def oO00oOOoooO ( name , url ) :
 if o0OO00 . getSetting ( 'save_location' ) == "" :
  xbmc . executebuiltin ( "XBMC.Notification('LiveStreams','Choose a location to save files.',15000," + O0O + ")" )
  o0OO00 . openSettings ( )
 OoOoO = { 'url' : url , 'download_path' : o0OO00 . getSetting ( 'save_location' ) }
 downloader . download ( name , OoOoO )
 IiIi11iI = xbmcgui . Dialog ( )
 Oo0O00O000 = IiIi11iI . yesno ( 'LiveStreams' , 'Do you want to add this file as a source?' )
 if Oo0O00O000 :
  O0ooOooooO ( os . path . join ( o0OO00 . getSetting ( 'save_location' ) , name ) )
  if 3 - 3: Ooo0 * i111I % ooO0Oooo00
  if 59 - 59: II1Ii1iI1i - I111i1i1111i
def O0O00o0OOO0 ( name , url , mode , iconimage , fanart , description , genre , date , credits , showcontext = False ) :
 I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 ii1I1 = True
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 OooooOOoo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooooOOoo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date , "credits" : credits } )
 OooooOOoo0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  i1I1IiiIi1i = [ ]
  if showcontext == 'source' :
   if name in str ( O0oo0OO0 ) :
    i1I1IiiIi1i . append ( ( 'Remove from Sources' , 'XBMC.RunPlugin(%s?mode=8&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'download' :
   i1I1IiiIi1i . append ( ( 'Download' , 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'fav' :
   i1I1IiiIi1i . append ( ( 'Remove from LiveStreams Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in i1i1II :
   i1I1IiiIi1i . append ( ( 'Add to LiveStreams Favorites' , 'XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OooooOOoo0 . addContextMenuItems ( i1I1IiiIi1i )
 ii1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = OooooOOoo0 , isFolder = True )
 return ii1I1
 if 29 - 29: OOooOOo % OOooOOo
 if 94 - 94: iIii1I11I1II1 / I11iIi1I % I111i1i1111i * I111i1i1111i * oO0o
def i1Ii11i1i ( url , name , iconimage , fanart , description , genre , date , showcontext , playlist , regexs , total ) :
 ii1I1 = True
 if regexs : IIiIiI = '17'
 else : IIiIiI = '12'
 I1 = sys . argv [ 0 ] + "?"
 OOOIIiI1i1i = False
 if playlist :
  if o0OO00 . getSetting ( 'add_playlist' ) == "false" :
   I1 += "url=" + urllib . quote_plus ( url ) + "&mode=" + IIiIiI
  else :
   I1 += "mode=13&name=%s&playlist=%s" % ( urllib . quote_plus ( name ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '|' ) ) )
   OOOIIiI1i1i = True
 else :
  I1 += "url=" + urllib . quote_plus ( url ) + "&mode=" + IIiIiI
 if regexs :
  I1 += "&regexs=" + regexs
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 OooooOOoo0 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 OooooOOoo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date } )
 OooooOOoo0 . setProperty ( "Fanart_Image" , fanart )
 if not OOOIIiI1i1i :
  OooooOOoo0 . setProperty ( 'IsPlayable' , 'true' )
 if showcontext :
  i1I1IiiIi1i = [ ]
  if showcontext == 'fav' :
   i1I1IiiIi1i . append (
 ( 'Remove from LiveStreams Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) )
 )
  elif not name in i1i1II :
   O00Oo0 = (
 '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) )
 )
   if playlist :
    O00Oo0 += 'playlist=' + urllib . quote_plus ( str ( playlist ) . replace ( ',' , '|' ) )
   if regexs :
    O00Oo0 += "&regexs=" + regexs
   i1I1IiiIi1i . append ( ( 'Add to LiveStreams Favorites' , 'XBMC.RunPlugin(%s)' % O00Oo0 ) )
  OooooOOoo0 . addContextMenuItems ( i1I1IiiIi1i )
 if not playlist is None :
  if o0OO00 . getSetting ( 'add_playlist' ) == "false" :
   IiII111i1i11 = name . split ( ') ' ) [ 1 ]
   i111iIi1i1II1 = [
 ( 'Play ' + IiII111i1i11 + ' PlayList' , 'XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( IiII111i1i11 ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '|' ) ) ) )
 ]
   OooooOOoo0 . addContextMenuItems ( i111iIi1i1II1 )
 ii1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1 , listitem = OooooOOoo0 , totalItems = total )
 return ii1I1
 if 86 - 86: iIii1I11I1II1 / oooO0oo0oOOOO . oO0o
 if 19 - 19: i111I % OoooooooOO % Ii1Ii1iiii11 * ooO0oo0oO0 % O0
 if 67 - 67: OOooOOo . i1IIi
 if 27 - 27: oOOOO % OOooOOo
def i1Iii1i1I ( link ) :
 O00O0oOO00O00 = urllib . urlopen ( link )
 o0oooOO00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 iiIiii1IIIII = o0oooOO00 . split ( "Jetzt" )
 o00o = iiIiii1IIIII [ 1 ] . split ( 'programm/detail.php?const_id=' )
 II = o00o [ 1 ] . split ( '<br /><a href="/' )
 IIiiIiiI = II [ 0 ] [ 40 : len ( II [ 0 ] ) ]
 IIIIiI11I11 = o00o [ 2 ] . split ( "</a></p></div>" )
 oo00o0 = IIIIiI11I11 [ 0 ] [ 17 : len ( IIIIiI11I11 [ 0 ] ) ]
 oo00o0 = oo00o0 . encode ( 'utf-8' )
 oo00o0 = oo00o0 . encode ( 'utf-8' )
 oo00o0 = oo00o0 . encode ( 'utf-8' )
 return "  - " + oo00o0 + " - " + IIiiIiiI
 if 4 - 4: Ooo0 % II1Ii1iI1i * IiiIII111iI
 if 100 - 100: I1I1i1 * o0oOoO00o + o0oOoO00o
xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
if 54 - 54: OoooooooOO + ooO0oo0oO0 - i1IIi % i11iIiiIii
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_UNSORTED )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_DATE )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_GENRE )
except :
 pass
 if 3 - 3: ooO0oo0oO0 % ooO0oo0oO0
OoOoO = oO0 ( )
if 83 - 83: oO0o + I1I1i1
O00O0oOO00O00 = None
o00oOO0o = None
IIiIiI = None
OoOO000 = None
OOooo0oOO0O = None
iiI1 = Oo
OoOO000 = None
oO00ooooO0o = None
OOO = None
if 75 - 75: i1IIi / O0 * ooO0oo0oO0
try :
 O00O0oOO00O00 = urllib . unquote_plus ( OoOoO [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 o00oOO0o = urllib . unquote_plus ( OoOoO [ "name" ] )
except :
 pass
try :
 OOooo0oOO0O = urllib . unquote_plus ( OoOoO [ "iconimage" ] )
except :
 pass
try :
 iiI1 = urllib . unquote_plus ( OoOoO [ "fanart" ] )
except :
 pass
try :
 IIiIiI = int ( OoOoO [ "mode" ] )
except :
 pass
try :
 OoOO000 = eval ( urllib . unquote_plus ( OoOoO [ "playlist" ] ) . replace ( '|' , ',' ) )
except :
 pass
try :
 oO00ooooO0o = int ( OoOoO [ "fav_mode" ] )
except :
 pass
try :
 OOO = OoOoO [ "regexs" ]
except :
 pass
 if 29 - 29: OOooOOo % o0oOoO00o - OOooOOo / o0oOoO00o . i1IIi
i1 ( "Mode 4SmartTVBox: " + str ( IIiIiI ) )
if not O00O0oOO00O00 is None :
 i1 ( "URL: " + str ( O00O0oOO00O00 . encode ( 'utf-8' ) ) )
i1 ( "Name: " + str ( o00oOO0o ) )
if 31 - 31: I1I1i1
if IIiIiI == None :
 i1 ( "getSources" )
 oOOO00o ( )
 if 88 - 88: IiiIII111iI - oOOOO + o0oOoO00o * OOooOOo % iIii1I11I1II1 + I11iIi1I
elif IIiIiI == 1 :
 i1 ( "getData" )
 oO ( O00O0oOO00O00 , iiI1 )
 if 76 - 76: OOooOOo * I111i1i1111i % I1I1i1
elif IIiIiI == 2 :
 i1 ( "getChannelItems" )
 Ii ( o00oOO0o , O00O0oOO00O00 , iiI1 )
 if 57 - 57: iIii1I11I1II1 - i1IIi / I1I1i1 - O0 * OoooooooOO % oO0o
elif IIiIiI == 3 :
 i1 ( "getSubChannelItems" )
 oo0o00O ( o00oOO0o , O00O0oOO00O00 , iiI1 )
 if 68 - 68: OoooooooOO * ooO0Oooo00 % oooO0oo0oOOOO - Ii1Ii1iiii11
elif IIiIiI == 4 :
 i1 ( "getFavorites" )
 oOo00oOoO000 ( )
 if 34 - 34: I1I1i1 . iIii1I11I1II1 * oooO0oo0oOOOO * II1Ii1iI1i / I1I1i1 / i111I
elif IIiIiI == 5 :
 i1 ( "addFavorite" )
 try :
  o00oOO0o = o00oOO0o . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o00oOO0o = o00oOO0o . split ( '  - ' ) [ 0 ]
 except :
  pass
 I111iI ( o00oOO0o , O00O0oOO00O00 , OOooo0oOO0O , iiI1 , oO00ooooO0o )
 if 78 - 78: I11iIi1I - ooO0oo0oO0 / oooO0oo0oOOOO
elif IIiIiI == 6 :
 i1 ( "rmFavorite" )
 try :
  o00oOO0o = o00oOO0o . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o00oOO0o = o00oOO0o . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0oOOoOooooO ( o00oOO0o )
 if 10 - 10: I111i1i1111i + I11iIi1I * i111I + iIii1I11I1II1 / I1I1i1 / i111I
elif IIiIiI == 7 :
 i1 ( "addSource" )
 O0ooOooooO ( O00O0oOO00O00 )
 if 42 - 42: OOooOOo
elif IIiIiI == 8 :
 i1 ( "rmSource" )
 OOoOO00OOO0OO ( o00oOO0o )
 if 38 - 38: o0oOoO00o + oO0o % oOOOO % oooO0oo0oOOOO - Ooo0 / OoooooooOO
elif IIiIiI == 9 :
 i1 ( "download_file" )
 oO00oOOoooO ( o00oOO0o , O00O0oOO00O00 )
 if 73 - 73: ooO0oo0oO0 * O0 - i11iIiiIii
elif IIiIiI == 10 :
 i1 ( "getCommunitySources" )
 O0o0O00Oo0o0 ( )
 if 85 - 85: Ooo0 % I111i1i1111i + ooO0Oooo00 / ooO0oo0oO0 . II1Ii1iI1i + o0oOoO00o
elif IIiIiI == 11 :
 i1 ( "addSource" )
 O0ooOooooO ( O00O0oOO00O00 )
 if 62 - 62: i11iIiiIii + i11iIiiIii - ooO0oo0oO0
elif IIiIiI == 12 :
 i1 ( "setResolvedUrl" )
 IIi = xbmcgui . ListItem ( path = O00O0oOO00O00 )
 if O00O0oOO00O00 . startswith ( 'system:' ) :
  I1OooooO0oOOOO = O00O0oOO00O00 [ 7 : ]
  xbmc . log ( msg = 'executebuiltin: url: ,%s' % ( I1OooooO0oOOOO ) , level = xbmc . LOGDEBUG )
  xbmc . executebuiltin ( I1OooooO0oOOOO )
 else :
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIi )
  if 100 - 100: I111i1i1111i % o0oOoO00o
elif IIiIiI == 13 :
 i1 ( "play_playlist" )
 i1OOoO ( o00oOO0o , OoOO000 )
 if 86 - 86: I11iIi1I . O0 - OoooooooOO . IiiIII111iI + Ooo0
elif IIiIiI == 14 :
 i1 ( "get_xml_database" )
 iIi1iIiii111 ( O00O0oOO00O00 )
 if 57 - 57: ooO0oo0oO0 . i1IIi . Ii1Ii1iiii11 * i11iIiiIii + I1I1i1 . Ii1Ii1iiii11
elif IIiIiI == 15 :
 i1 ( "browse_xml_database" )
 iIi1iIiii111 ( O00O0oOO00O00 , True )
 if 57 - 57: I1I1i1
elif IIiIiI == 16 :
 i1 ( "browse_community" )
 O0o0O00Oo0o0 ( True )
 if 32 - 32: Ooo0 - I11iIi1I % OoooooooOO . I111i1i1111i / Ii1Ii1iiii11 + OOooOOo
elif IIiIiI == 17 :
 i1 ( "getRegexParsed" )
 I1Ii ( OOO , O00O0oOO00O00 )
 if 76 - 76: oOOOO
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
