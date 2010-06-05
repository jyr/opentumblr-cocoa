from Foundation import *
from AppKit import *
import objc
from DashboardWindow import *
from TextView import *

class DashboardController (NSWindowController):
    def init(self):
		return self.initWithWindowNibName_('Dashboard')

    def show(self):
		w = DashboardController.alloc().init()
		w.showWindow_(self)
		w.retain()
		#print dir(w)
    show = classmethod(show)

    @objc.IBAction
    def audio_(self, sender):
		print ""

    @objc.IBAction
    def chat_(self, sender):
		print ""
		
    @objc.IBAction
    def link_(self, sender):
		print ""
		
    @objc.IBAction
    def logout_(self, sender):
		NSApp().terminate_(self)
		
    @objc.IBAction
    def photo_(self, sender):
		print ""
		
    @objc.IBAction
    def quote_(self, sender):
		print ""
		
    @objc.IBAction
    def text_(self, sender):
		print ""
		#print dir(DashboardWindow)
		#print dir(TextView)
		graphicsRect = NSMakeRect(100.0, 350.0, 450.0, 400.0)
		self.TextView = TextView.alloc().initWithFrame_(graphicsRect)
		#print dir(self.TextView)
		self.DashboardWindow = DashboardWindow.alloc().init()
		#print dir(self.DashboardWindow)
		self.DashboardWindow.setContentView_(self.TextView)
		self.DashboardWindow.display()
		#delegate = AppDelegate.alloc().init()
		#self.DashboardWindow.setDelegate_(delegate)
		#self.DashboardWindow.makeKeyAndOrderFront_(self) #abre una ventana
		#self.DashboardWindow.showWindow_(self) #abre una ventana
		#self.DashboardWindow.makeFirstResponder_(self.TextView)
		
    @objc.IBAction
    def video_(self, sender):
		print ""
