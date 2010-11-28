from Foundation import *
from AppKit import *
import objc

class DashboardController (NSViewController):
		
    def show(self):
		self.window = NSWindow.alloc().init()
		self.DashboardViewController = NSViewController.alloc().initWithNibName_bundle_("Dashboard", None)
		self.dashboardView = self.DashboardViewController.view()
    show = classmethod(show)
	
    def resetSubviews(self):
		for i in range(1, len(self.dashboardView.subviews())):
			self.dashboardView.subviews().removeObjectAtIndex_(i)

    @objc.IBAction
    def audio_(self, sender):
		self.resetSubviews()
		self.AudioViewController = NSViewController.alloc().initWithNibName_bundle_("Audio", None)
		self.audioView = self.AudioViewController.view()
		self.dashboardView.addSubview_(self.audioView)
		
    @objc.IBAction
    def chat_(self, sender):
		self.resetSubviews()
		self.ChatViewController = NSViewController.alloc().initWithNibName_bundle_("Chat", None)
		self.chatView = self.ChatViewController.view()
		self.dashboardView.addSubview_(self.chatView)
				
    @objc.IBAction
    def link_(self, sender):
		self.resetSubviews()
		self.LinkViewController = NSViewController.alloc().initWithNibName_bundle_("Link", None)
		self.linkView = self.LinkViewController.view()
		self.dashboardView.addSubview_(self.linkView)
				
    @objc.IBAction
    def logout_(self, sender):
		NSApp().terminate_(self)
		
    @objc.IBAction
    def photo_(self, sender):
		self.resetSubviews()
		self.PhotoViewController = NSViewController.alloc().initWithNibName_bundle_("Photo", None)
		self.photoView = self.PhotoViewController.view()
		self.dashboardView.addSubview_(self.photoView)
		
    @objc.IBAction
    def quote_(self, sender):
		self.resetSubviews()
		self.QuoteViewController = NSViewController.alloc().initWithNibName_bundle_("Quote", None)
		self.quoteView = self.QuoteViewController.view()
		self.dashboardView.addSubview_(self.quoteView)
				
    @objc.IBAction
    def text_(self, sender):
		self.resetSubviews()
		self.TextViewController = NSViewController.alloc().initWithNibName_bundle_("Text", None)
		self.textView = self.TextViewController.view()
		self.dashboardView.addSubview_(self.textView)

    @objc.IBAction
    def video_(self, sender):
		self.resetSubviews()
		self.VideoViewController = NSViewController.alloc().initWithNibName_bundle_("Video", None)
		self.videoView = self.VideoViewController.view()
		self.dashboardView.addSubview_(self.videoView)