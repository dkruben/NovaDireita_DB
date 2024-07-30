import re
import wx
from constants import councils_options


# Modify the Validate method in BaseValidator class to pass the value of the TextCtrl object
class BaseValidator(wx.Validator):
    def Validate(self, text_ctrl):
        value = text_ctrl.GetValue()
        if not self.is_valid(value):
            if self.field_name:
                wx.MessageBox(f"Por favor, insira um(a) {self.field_name.lower()} válido(a).", "Erro de Validação", wx.OK | wx.ICON_ERROR)
            else:
                wx.MessageBox("Por favor, insira um valor válido.", "Erro de Validação", wx.OK | wx.ICON_ERROR)
            return False
        return True


class ParishValidator(BaseValidator):
    field_name = "Freguesia"
    
    def is_valid(self, value):
        return bool(re.match(r'^[A-Za-zÀ-ÿ\s\-]', value))


class ZipValidator(BaseValidator):
    field_name = "Código Postal"
    
    def is_valid(self, value):
        return bool(re.match(r'\d{4}-\d{3}', value))


class CityDistrictValidator(BaseValidator):
    field_name = "Cidade e/ou Distrito"

    def is_valid(self, value):
        trimmed_value = value.strip()
        if not trimmed_value:
            return False
        valid_options = list(councils_options.keys()) + [city for district in councils_options.values() for city in district]
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
        return bool(re.match(r'^\d{8} \d[A-Z]{2} \d$', value))


class NifValidator(BaseValidator):
    field_name = "NIF"

    def is_valid(self, value):
        return bool(re.match(r'^\d{9}$', value))
