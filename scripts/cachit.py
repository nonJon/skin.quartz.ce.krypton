import xbmcaddon
import xbmcgui
import time
import os
import subprocess
import sys

use_shell = False
if sys.platform == "win32":
	use_shell = True

loc = xbmc.translatePath("special://skin//scripts//texturecache.py")

rc = xbmcgui.Dialog().yesno('Texture Cache Maintenance', 'This may take awhile to run.', '', 'Sure you want to continue?')

if not rc: sys.exit(0)
 
dialog = xbmcgui.DialogProgress()
dialog.create('Texture Cache Maintenance', ("Initiating"))

p = subprocess.Popen(['python', loc, 'c'], bufsize=1, shell=use_shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

while True:
	line = p.stdout.readline()
	if line != b'':
		dialog.update(0, ("processing..."), "", (line))
	else:
		break
	if dialog.iscanceled():
		break

streamdata = p.communicate()[0]
rc = p.returncode		
p.stdout.close()
time.sleep(4)

if (not rc) and dialog.iscanceled(): 
	xbmcgui.Dialog().ok('Luke', "You switched off your targeting computer.", "", "What's wrong?")
elif not rc:
	xbmcgui.Dialog().ok('Success', 'TCM completed processing without any errors.')
else:
	xbmcgui.Dialog().ok('Ooops!', 'TCM was not able to do its thing.', '', 'Please ensure the KODI webserver is running with default settings.')