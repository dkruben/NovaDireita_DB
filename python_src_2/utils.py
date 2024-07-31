# -*- coding: utf-8 -*-
import os
import wx
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle

from constants import select_options

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))


def convert_hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    h_len = len(hex_color)
    return tuple(int(hex_color[i:i + h_len // 3], 16) for i in range(0, h_len, h_len // 3))
    
    
def calculate_militant_per_page(page_size, pxl):
    available_height = page_size[1] - 2 * pxl
    militant_height = 2.5 * pxl
    return int(available_height / militant_height)
    

def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 10)
    page_number_text = "%d" % doc.page
    canvas.drawCentredString(0.75 * inch, 0.75 * inch, page_number_text)
    canvas.restoreState()


def create_militant_table(row):
    data = [
        ["Militante:", row[0]],
        ["Nome Completo:", row[1]],
        ["Morada:", row[2]],
        ["Freguesia:", row[3]],
        ["Distrito:", row[4]],
        ["Cidade:", row[5]],
        ["Frguesia:", row[6]],
        ["Código Postal:", row[7]],
        ["Telefone:", row[8]],
        ['BI/CC', row[9]],
        ['NIF', row[10]],
        ["Email:", row[11]],
        ["Data de Nascimento:", row[12]],
        ["Aceita os Termos:", row[13]]
    ]
    table = Table(data, colWidths=[100, 300])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.darkblue),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.royalblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ]))
    return table


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
