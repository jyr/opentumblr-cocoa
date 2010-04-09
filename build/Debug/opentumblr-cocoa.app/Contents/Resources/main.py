#
#  main.py
#  opentumblr-cocoa
#
#  Created by Jair Gaxiola on 08/04/10.
#  Copyright __MyCompanyName__ 2010. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import opentumblr_cocoaAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
