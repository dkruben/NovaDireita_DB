# -*- coding: utf-8 -*-
import os
import wx
from reportlab.lib.units import inch

from constants import select_options


current_dir = os.path.dirname(os.path.abspath(__file__))


def convert_hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    h_len = len(hex_color)
    return tuple(int(hex_color[i:i + h_len // 3], 16) for i in range(0, h_len, h_len // 3))
    

def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 10)
    page_number_text = "%d" % doc.page
    canvas.drawCentredString(0.75 * inch, 0.75 * inch, page_number_text)
    canvas.restoreState()


def create_district_city_parish_selection(parent):
    district_choices = list(select_options.keys())
    city_choices = list(select_options.get(district_choices[0], {}).keys()) if district_choices else []
    parish_choices = select_options.get(district_choices[0], {}).get(city_choices[0], []) if city_choices else []

    district_combo = wx.ComboBox(parent, choices=district_choices, style=wx.CB_READONLY)
    city_combo = wx.ComboBox(parent, choices=city_choices, style=wx.CB_READONLY)
    parish_combo = wx.ComboBox(parent, choices=parish_choices, style=wx.CB_READONLY)

    def on_district_select(event):
        selected_district = district_combo.GetValue()
        city_combo.Clear()
        city_choices = list(select_options.get(selected_district, {}).keys())
        city_combo.AppendItems(city_choices)
        city_combo.SetValue('')  # Clear city selection
        parish_combo.Clear()
        parish_combo.SetValue('')  # Clear parish selection

    def on_city_select(event):
        selected_district = district_combo.GetValue()
        selected_city = city_combo.GetValue()
        parish_combo.Clear()
        parish_choices = select_options.get(selected_district, {}).get(selected_city, [])
        parish_combo.AppendItems(parish_choices)
        parish_combo.SetValue('')  # Clear parish selection

    district_combo.Bind(wx.EVT_COMBOBOX, on_district_select)
    city_combo.Bind(wx.EVT_COMBOBOX, on_city_select)

    return district_combo, city_combo, parish_combo
