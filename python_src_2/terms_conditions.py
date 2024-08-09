# -*- coding: utf-8 -*-
import wx

from constants import text_rgpd, icon
from utils import convert_hex_to_rgb


class SecondWindow(wx.Frame):
    def __init__(self, parent, title):
        super(SecondWindow, self).__init__(parent, title=title, size=(500, 400))
        self.SetIcon(wx.Icon(icon))
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Add the multi-line text box
        info_label = wx.StaticText(panel, label="Termos e Condições:")
        self.info_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(400, 200))
        vbox.Add(info_label, 0, wx.ALL, 5)
        vbox.Add(self.info_text, 5, wx.EXPAND | wx.ALL, 5)
        
        # Example: populate the text box with some text
        self.info_text.SetValue(text_rgpd)
        
        # Add the exit button
        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        exit_button = wx.Button(panel, label="Sair")
        exit_button.Bind(wx.EVT_BUTTON, self.on_exit)
        hbox_buttons.Add(exit_button, 0, wx.ALL | wx.CENTER, 10)
        vbox.Add(hbox_buttons, 0, wx.ALIGN_CENTER)
        
        # Set the button colors
        exit_button.SetBackgroundColour(wx.Colour(convert_hex_to_rgb('#FF0000')))
        exit_button.SetForegroundColour(wx.Colour(convert_hex_to_rgb('#FFFFFF')))
        
        panel.SetSizer(vbox)
        self.Centre()
    
    def on_exit(self, events):
        self.Close()
