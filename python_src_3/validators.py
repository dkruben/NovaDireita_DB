# -*- coding: utf-8 -*-
import re
import wx

from constants import select_options
from utils import convert_hex_to_rgb


class BaseValidator(wx.Validator):
    def __init__(self):
        super(BaseValidator, self).__init__()

    def Validate(self, text_ctrl):
        value = text_ctrl.GetValue()
        if not self.is_valid(value):
            if self.field_name:
                wx.MessageBox(f"Por favor, insira um(a) {self.field_name.lower()} válido(a).", "Erro de Validação", wx.OK | wx.ICON_ERROR)
            else:
                wx.MessageBox("Por favor, insira um valor válido.", "Erro de Validação", wx.OK | wx.ICON_ERROR)
            text_ctrl.SetBackgroundColour(wx.Colour(convert_hex_to_rgb('#FFC8C8')))
            text_ctrl.SetFocus()
            return False
        else:
            text_ctrl.SetBackgroundColour(wx.NullColour)
        return True

    def is_valid(self, value):
        raise NotImplementedError("Subclasses devem implementar o método is_valid.")


class ZipValidator(BaseValidator):
    field_name = "Código Postal"
    
    def is_valid(self, value):
        return bool(re.match(r'\d{4}-\d{3}', value))


class CityDistrictParishValidator(BaseValidator):
    field_name = "Cidade e/ou Distrito e/ou Freguesia"
    
    def is_valid(self, value):
        trimmed_value = value.strip()
        if not trimmed_value:
            return False
        
        valid_options = list(select_options.keys())
        valid_options += [parish for city in select_options.values() for parish in city]
        valid_options += [city for district in select_options.values() for city in district]
        valid_options += [district for district in select_options.values()]
        
        return trimmed_value in valid_options


class EmailValidator(BaseValidator):
    field_name = "Email"

    def is_valid(self, value):
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value))


class PhoneValidator(BaseValidator):
    field_name = "Telefone"

    def is_valid(self, value):
        return bool(re.match(r'^\+\d{3}-\d{9}$', value))


class BiCcValidator(BaseValidator):
    field_name = "BI/CC"

    def is_valid(self, value):
        return bool(re.match(r'^\d{8} \d [A-Z]{2}\d', value))


class NifValidator(BaseValidator):
    field_name = "NIF"

    def is_valid(self, value):
        return bool(re.match(r'^\d{9}$', value))
