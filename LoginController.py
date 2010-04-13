from Foundation import *
from AppKit import *
import objc

import urllib2
import tumblr
from tumblr import Api
from  DashboardController import *

class LoginController(NSWindowController):
    blog = objc.IBOutlet()
    password = objc.IBOutlet()
    user = objc.IBOutlet()
	
    def init(self):
		self.errors = {'403':'Login o password incorrectos','404':'Tumblrlog incorrecto','urlopen':'no ingreso su tumblrlog'}
		return self
		
    @objc.IBAction
    def authTumblr_(self, sender):
		self.p = self.password.stringValue()
		self.u = self.user.stringValue()
		self.b = self.blog.stringValue()
		self.api = Api(self.b, self.u, self.p)
		NSLog("Blog %s, User %s , Password  %s" % (self.b, self.u, self.p))
		#DashboardController.show()
		try:
			self.auth = self.api.auth_check()
			#print dir(self)
			self.destroy()
			DashboardController.show()
		except tumblr.TumblrAuthError:
			#self.invalid = Invalid(self)
			#self.invalid.show_()
			print self.errors['403']
		except tumblr.TumblrError(self):
			print self.errors['404']
		#except urllib2.HTTPError():
		#	print self.errors['404']
		#except urllib2.URLError:
		#	print self.errors['urlopen']

    def destroy(self):
		app = NSApplication.sharedApplication()
		appdelegate = app.delegate()
		appdelegate.w.close()
