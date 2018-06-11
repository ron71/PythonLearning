# This module allows us to open the default web browser of the PC and navigate to the given URL

import webbrowser

webbrowser.open("https://www.facebook.com")
# Above line atomatically opens the brwoser and leds to facebook page
help(webbrowser)

# webbrowser.open(url, new=0, autoraise=True)

# Display url using the default browser.
# If new is 0, the url is opened in the same browser window if possible.
# If new is 1, a new browser window is opened if possible.
# If new is 2, a new browser page (“tab”) is opened if possible.
# If autoraise is True, the window is raised if possible
# (note that under many window managers this will occur regardless of the setting of this variable).

# get() method
# This method is used to get the controller object of specified type of web browser
# TypeName           Class Name
# 'mozilla'           Mozilla('mozilla')
# 'firefox'           Mozilla('mozilla')
# 'netscape'          Mozilla('netscape')
# 'galeon'            Galeon('galeon')
# 'epiphany'          Galeon('epiphany')
# 'skipstone'         BackgroundBrowser('skipstone')
# 'kfmclient'         Konqueror()
# 'konqueror'         Konqueror()
# 'kfm'               Konqueror()
# 'mosaic'            BackgroundBrowser('mosaic')
# 'opera'             Opera()
# 'grail'             Grail()
# 'links'             GenericBrowser('links')
# 'elinks'            Elinks('elinks')
# 'lynx'              GenericBrowser('lynx')
# 'w3m'               GenericBrowser('w3m')
# 'windows-default'   WindowsDefault
# 'macosx'            MacOSX('default')
# 'safari'            MacOSX('safari')
# 'google-chrome'     Chrome('google-chrome')
# 'chrome'            Chrome('chrome')
# 'chromium'          Chromium('chromium')
# 'chromium-browser'  Chromium('chromium-browser')

# chrome = webbrowser.get(using= 'google-chrome')
# chrome.open_new("https://www.facebook.com")