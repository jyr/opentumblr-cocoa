from Foundation import *
from AppKit import *
import objc
class DashboardController (NSWindowController):
    def init(self):
		return self.initWithWindowNibName_('Dashboard')

    def show(self):
		w = DashboardController.alloc().init()
		w.showWindow_(self)
		w.retain()
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
		
    @objc.IBAction
    def video_(self, sender):
		print ""
