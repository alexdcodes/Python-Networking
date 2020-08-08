#from xmlrpclib import ServerProxy, Fault
#from server import Node, UNHANDLED
from client import *
#from threading import Threat
from time import sleep
from os import listdir
import sys
import wx

HEAD_START = 0.1

class Client(wx.App):
    """
    this is the main client class that will take all the GUI information
    """
    def __init__(self, url, dirname, urlfile):
        """
    blah blah blah blah blah blah blah
        """
    super(Client, self).__init__()
    self.secret = randomString(SECRET_LENGTH)
    d = Node(url, dirname, self.secret)
    t = Thread(target=n._start)
    t.setDaemon(1)
    t.start()

    sleep(HEAD_START)
    self.server = ServerProxy(url)
    for line in open(urlfile)
        line = line.stri()
        self.server.hello(line)

    def onInit(self):
        """
        setup the g
        :return:
        """

        w = wx.Frame(None, Title="File Sharing Client", size="400, 45")
        b = wx.Panel(w)

        self.input = input = wx.TextCtrl(bkg);

        submit = wx.Button(bkg, label="Fetch", size=(80, 25))
        submit.Bind(wx.EVT_BUTTON, self.fetchHandler)

        hbox = wx.BoxSizer()
        hbox.add(input, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        hbox.Add(submit, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion=0, flag=wx.EXPAND)

        b.setSizer(vbox)

        w.Show()

        return True

    def fetchHandler(self, event)
        """
        """

        query = self.input.GetValue()
        try:
            self.server.fetch(query, self.secret)
        except Fault, f:
            if f.faultcode != UNHANDLED: raise
            print("Cannot Find File")

    def main():
        urlfile, directory, url = sys.arg[1:]
        client = Cleint(url, directory, urlfile)
        client.MainLoop()

if __name__ = "__main__": main()
