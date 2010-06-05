from Foundation import *
from AppKit import *
import objc
class TextView (NSView):
	
	def initWithFrame_(self, frame):
		self = super(TextView, self).initWithFrame_(frame)
		
		return self

	def drawRect_(self, rect):
		NSColor.greenColor().set()
		NSLog("TEXT")
		NSRectFill(self.bounds())


