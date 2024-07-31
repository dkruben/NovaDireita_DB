# -*- coding: utf-8 -*-
# usr/bin/env python3
# python 3.12
import datetime
import os

import mysql.connector
import openpyxl
import wx
from reportlab.lib import colors
from reportlab.lib.pagesizes import legal
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, PageBreak, SimpleDocTemplate, Paragraph, Spacer
from wx.adv import DatePickerCtrl

from constants import icon, email_body
from database import banc
from email_sender import EmailSender
from terms_conditions import SecondWindow
from utils import create_militant_table, add_page_number, calculate_militant_per_page, create_district_city_parish_selection, current_dir
from validators import ZipValidator, EmailValidator, PhoneValidator, CityDistrictParishValidator, BiCcValidator, NifValidator

try:
    banc.connect_to_database()
except mysql.connector.Error as error:
    wx.MessageBox('Erro', f'Erro ao conectar ao banco de dados: {error}', wx.OK | wx.ICON_ERROR)


class Application(wx.Frame):
    def __init__(self, parent, title):
        super(Application, self).__init__(parent, title=title, size=(1080, 980))
        self.SetIcon(wx.Icon(icon))
        # menu variables
        self.name_text = None
        self.address_text = None
        self.parish_text = None
        self.district_combo = None
        self.city_combo = None
        self.parish_combo = None
        self.zip_text = None
        self.email_text = None
        self.phone_text = None
        self.bi_cc_text = None
        self.nif_text = None
        self.date_text = None
        self.comment_text = None
        self.terms_radio = None
        self.birthday_picker = None
        # panel
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.id_text = wx.TextCtrl(panel, style=wx.TE_READONLY)
        vbox.Add(self.id_text, 0, wx.EXPAND | wx.ALL, 5)
        # search_militant
        self.search_text = wx.TextCtrl(panel)
        vbox.Add(self.search_text, 0, wx.EXPAND | wx.ALL, 5)
        search_button = wx.Button(panel, label="Procurar Militante")
        search_button.Bind(wx.EVT_BUTTON, self.on_search)
        vbox.Add(search_button, 0, wx.ALL | wx.ALL, 5)
        self.add_input_fields(panel, vbox)
        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        # add_militant
        save_button = wx.Button(panel, label="Adicionar Dados Militante")
        save_button.Bind(wx.EVT_BUTTON, self.on_save)
        hbox_buttons.Add(save_button, 0, wx.ALL | wx.CENTER, 10)
        # update_militant
        update_button = wx.Button(panel, label="Atualizar Dados Militante")
        update_button.Bind(wx.EVT_BUTTON, self.on_update)
        hbox_buttons.Add(update_button, 0, wx.ALL | wx.CENTER, 10)
        # delete_militant
        delete_button = wx.Button(panel, label="Apagar Dados Militante")
        delete_button.Bind(wx.EVT_BUTTON, self.on_delete)
        hbox_buttons.Add(delete_button, 0, wx.ALL | wx.CENTER, 10)
        # export_pdf
        export_pdf_button = wx.Button(panel, label="Exportar para PDF")
        export_pdf_button.Bind(wx.EVT_BUTTON, self.export_all_to_pdf)
        hbox_buttons.Add(export_pdf_button, 0, wx.ALL | wx.CENTER, 10)
        # export_exel
        export_xlsx_button = wx.Button(panel, label="Exportar para Excel")
        export_xlsx_button.Bind(wx.EVT_BUTTON, self.export_all_to_xlsx)
        hbox_buttons.Add(export_xlsx_button, 0, wx.ALL | wx.CENTER, 10)
        
        vbox.Add(hbox_buttons, 0, wx.ALL | wx.CENTER, 10)
        
        panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)
    
    def add_input_fields(self, panel, vbox):
        font_label = wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, faceName="Cambria")
        font_text = wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, faceName="Times New Roman")
        # nome
        name_label = wx.StaticText(panel, label="Nome Completo:")
        name_label.SetFont(font_label)
        self.name_text = wx.TextCtrl(panel)
        vbox.Add(name_label, 0, wx.ALL, 5)
        vbox.Add(self.name_text, 0, wx.EXPAND | wx.ALL, 5)
        # morada
        address_label = wx.StaticText(panel, label="Morada:")
        address_label.SetFont(font_label)
        self.address_text = wx.TextCtrl(panel)
        self.address_text.SetHint("Formato: Rua de Cima, 123 (1º Esq.)")
        vbox.Add(address_label, 0, wx.ALL, 5)
        vbox.Add(self.address_text, 0, wx.EXPAND | wx.ALL, 5)
        # distrito
        district_label = wx.StaticText(panel, label="Distrito:")
        district_label.SetFont(font_label)
        vbox.Add(district_label, 0, wx.ALL, 5)
        self.district_combo, self.city_combo, self.parish_combo = create_district_city_parish_selection(panel)
        vbox.Add(self.district_combo, 0, wx.ALL | wx.EXPAND, 5)
        district_validator = CityDistrictParishValidator()
        self.district_combo.SetValidator(district_validator)
        # cidade
        city_label = wx.StaticText(panel, label="Cidade:")
        city_label.SetFont(font_label)
        vbox.Add(city_label, 0, wx.ALL, 5)
        vbox.Add(self.city_combo, 0, wx.ALL | wx.EXPAND, 5)
        city_validator = CityDistrictParishValidator()
        self.city_combo.SetValidator(city_validator)
        # freguesia
        parish_label = wx.StaticText(panel, label="Freguesia:")
        parish_label.SetFont(font_label)
        vbox.Add(parish_label, 0, wx.ALL, 5)
        vbox.Add(self.parish_combo, 0, wx.ALL | wx.EXPAND, 5)
        parish_validator = CityDistrictParishValidator()
        self.parish_combo.SetValidator(parish_validator)
        # cod postal
        zip_label = wx.StaticText(panel, label="Código Postal:")
        zip_label.SetFont(font_label)
        self.zip_text = wx.TextCtrl(panel, validator=ZipValidator())
        self.zip_text.SetHint("Formato: 1234-000")
        self.zip_text.SetFont(font_text)
        vbox.Add(zip_label, 0, wx.ALL, 5)
        vbox.Add(self.zip_text, 0, wx.EXPAND | wx.ALL, 5)
        # telefone
        phone_label = wx.StaticText(panel, label="Telefone:")
        phone_label.SetFont(font_label)
        self.phone_text = wx.TextCtrl(panel, validator=PhoneValidator())
        self.phone_text.SetHint("Formato: +351-900000000")
        self.phone_text.SetFont(font_text)
        vbox.Add(phone_label, 0, wx.ALL, 5)
        vbox.Add(self.phone_text, 0, wx.EXPAND | wx.ALL, 5)
        # bi/cc
        self.bi_cc_text = wx.TextCtrl(panel, validator=BiCcValidator())
        self.bi_cc_text.SetHint("Formato: 12345678 1 ZA")
        self.bi_cc_text.SetFont(font_text)
        portuguese_id_label = wx.StaticText(panel, label="BI/CC:")
        portuguese_id_label.SetFont(font_label)
        vbox.Add(portuguese_id_label, 0, wx.ALL, 5)
        vbox.Add(self.bi_cc_text, 0, wx.EXPAND | wx.ALL, 5)
        # nif
        self.nif_text = wx.TextCtrl(panel, validator=NifValidator())
        self.nif_text.SetHint("Formato: 123456789")
        self.nif_text.SetFont(font_text)
        nif_label = wx.StaticText(panel, label="NIF:")
        nif_label.SetFont(font_label)
        vbox.Add(nif_label, 0, wx.ALL, 5)
        vbox.Add(self.nif_text, 0, wx.EXPAND | wx.ALL, 5)
        # email
        email_label = wx.StaticText(panel, label="Email:")
        email_label.SetFont(font_label)
        self.email_text = wx.TextCtrl(panel, validator=EmailValidator())
        self.email_text.SetHint("Formato: example@example.net")
        self.email_text.SetFont(font_text)
        vbox.Add(email_label, 0, wx.ALL, 5)
        vbox.Add(self.email_text, 0, wx.EXPAND | wx.ALL, 5)
        # data de nascimento
        birthday_label = wx.StaticText(panel, label="Data de Nascimento:")
        birthday_label.SetFont(font_label)
        self.birthday_picker = wx.adv.DatePickerCtrl(panel, style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        vbox.Add(birthday_label, 0, wx.ALL, 5)
        vbox.Add(self.birthday_picker, 0, wx.EXPAND | wx.ALL, 5)
        # open_second_window
        open_second_window_button = wx.Button(panel, label="Termos e Condições")
        open_second_window_button.Bind(wx.EVT_BUTTON, self.on_open_second_window)
        vbox.Add(open_second_window_button, 0, wx.ALL | wx.CENTER, 10)
        # termmos e condicoes
        cbox_button = wx.BoxSizer(wx.HORIZONTAL)
        terms_label = wx.StaticText(panel, label="Aceita os termos e condições?")
        terms_label.SetFont(font_label)
        self.terms_radio = wx.RadioBox(panel, choices=["Sim", "Não"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        cbox_button.Add(terms_label, 0, wx.ALL | wx.CENTER, 5)
        cbox_button.Add(self.terms_radio, 5, wx.ALL | wx.CENTER, 5)
        vbox.Add(cbox_button, 0, wx.ALL | wx.CENTER, 5)
    
    def validate_form(self):
        fields = [
            self.name_text, self.address_text, self.parish_text,
            self.district_combo, self.city_combo, self.zip_text,
            self.phone_text, self.email_text, self.birthday_picker,
            self.bi_cc_text, self.nif_text, self.terms_radio
        ]
        
        for field in fields:
            validator = field.GetValidator()
            if validator:
                if not validator.Validate(field):
                    wx.MessageBox(f"Entrada inválida no campo {field.GetName()}", "Erro", wx.OK | wx.ICON_ERROR)
                    return False
        
        # Check if district, city, BI/CC, and NIF fields are selected/entered
        if not self.district_combo.GetValue():
            wx.MessageBox("Por favor, selecione um distrito", "Erro", wx.OK | wx.ICON_ERROR)
            return False
        if not self.city_combo.GetValue():
            wx.MessageBox("Por favor, selecione uma cidade", "Erro", wx.OK | wx.ICON_ERROR)
            return False
        if not self.parish_combo.GetValue():
            wx.MessageBox("Por favor, selecione uma freguesia", "Erro", wx.OK | wx.ICON_ERROR)
            return False
        if not self.bi_cc_text.GetValue():
            wx.MessageBox("Por favor, preencha o campo BI/CC", "Erro", wx.OK | wx.ICON_ERROR)
            return False
        if not self.nif_text.GetValue():
            wx.MessageBox("Por favor, preencha o campo NIF", "Erro", wx.OK | wx.ICON_ERROR)
            return False
        
        # Check if terms are accepted
        if self.terms_radio.GetSelection() != 0:  # 0 is "Sim"
            wx.MessageBox("Por favor, aceite os termos e condições", "Erro", wx.OK | wx.ICON_ERROR)
            return False
        
        return True
    
    @staticmethod
    def on_open_second_window(event):
        second_window = SecondWindow(None, 'Second Window')
        second_window.Show()
    
    def on_save(self, event):
        if not self.validate_form():
            return
        name = self.name_text.GetValue()
        address = self.address_text.GetValue()
        district = self.district_combo.GetValue()
        city = self.city_combo.GetValue()
        parish = self.parish_text.GetValue()
        zip_code = self.zip_text.GetValue()
        phone = self.phone_text.GetValue()
        bi_cc = self.bi_cc_text.GetValue()
        nif = self.nif_text.GetValue()
        email = self.email_text.GetValue()
        birthday = self.birthday_picker.GetValue().FormatISODate()
        terms = self.terms_radio.GetStringSelection()
        try:
            banc.cursor.execute("INSERT INTO militantes (name, address, district, city, parish, zip_code, phone, bi_cc, nif, email, birthday, agreement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, address, district, city, parish, zip_code, phone, bi_cc, nif, email, birthday, terms))
            banc.connection.commit()
            wx.MessageBox('Dados inseridos com sucesso!', 'Info', wx.OK | wx.ICON_INFORMATION)
            subject = "Inscrição Militante - Nova Direita"
            to_email = email
            message = email_body(name)
            body = message['welcome']
            EmailSender().send_email(subject, body, to_email)
            self.on_clear()
        except mysql.connector.Error as e:
            wx.MessageBox(f'Erro ao inserir dados: {e}', 'Erro', wx.OK | wx.ICON_ERROR)
            print(f'Erro ao inserir dados: {e}')
            banc.connection.rollback()
    
    def on_update(self, event):
        if not self.validate_form():
            return
        id_value = self.id_text.GetValue()
        name = self.name_text.GetValue()
        address = self.address_text.GetValue()
        district = self.district_combo.GetValue()
        city = self.city_combo.GetValue()
        parish = self.parish_text.GetValue()
        zip_code = self.zip_text.GetValue()
        phone = self.phone_text.GetValue()
        bi_cc = self.bi_cc_text.GetValue()
        nif = self.nif_text.GetValue()
        email = self.email_text.GetValue()
        birthday = self.birthday_picker.GetValue().FormatISODate()
        terms = self.terms_radio.GetStringSelection()
        
        try:
            banc.cursor.execute("UPDATE militantes SET name=%s, address=%s, district=%s, city=%s, parish=%s, zip_code=%s, phone=%s, bi_cc=%s, nif=%s, email=%s, birthday=%s, agreement=%s WHERE militant=%s", (name, address, district, city, parish, zip_code, phone, bi_cc, nif, email, birthday, terms, id_value))
            banc.connection.commit()
            wx.MessageBox('Dados atualizados com sucesso!', 'Info', wx.OK | wx.ICON_INFORMATION)
            subject = "Alteração de dados de Militante - Nova Direita"
            to_email = email
            message = email_body(name)
            body = message['update']
            EmailSender().send_email(subject, body, to_email)
            self.on_clear()
        except mysql.connector.Error as e:
            wx.MessageBox(f'Erro ao atualizar dados: {e}', 'Erro', wx.OK | wx.ICON_ERROR)
            banc.connection.rollback()
    
    def on_delete(self, event):
        id_value = self.id_text.GetValue()
        try:
            banc.cursor.execute("DELETE FROM militantes WHERE militant=%s", (id_value,))
            banc.connection.commit()
            wx.MessageBox('Dados apagados com sucesso!', 'Info', wx.OK | wx.ICON_INFORMATION)
            self.on_clear()
        except mysql.connector.Error as e:
            wx.MessageBox(f'Erro ao apagar dados: {e}', 'Erro', wx.OK | wx.ICON_ERROR)
            banc.connection.rollback()
    
    def on_search(self, event):
        search_militant = self.search_text.GetValue()
        try:
            conn = mysql.connector.connect(host=banc.host, user=banc.user, password=banc.password, database=banc.database)
            c = conn.cursor()
            c.execute("SELECT * FROM Militantes WHERE militant=%s", (search_militant,))
            result = c.fetchone()
            conn.close()
            
            if result:
                self.populate_form_with_data(result)
            else:
                wx.MessageBox("Militante não encontrado.", "Resultado da pesquisa", wx.OK | wx.ICON_ERROR)
        except mysql.connector.Error as e:
            wx.MessageBox(f"Erro ao pesquisar dados: {e}", "Erro", wx.OK | wx.ICON_ERROR)
    
    def populate_form_with_data(self, result):
        if result:
            militant, name, address, parish, district, city, zip_code, phone, bi_cc, nif, email, birthday, agreement = result
            self.id_text.SetValue(str(militant))
            self.name_text.SetValue(name)
            self.address_text.SetValue(address)
            self.parish_text.SetValue(parish)
            self.district_combo.SetStringSelection(district)
            self.city_combo.SetValue(city)
            self.zip_text.SetValue(zip_code)
            self.phone_text.SetValue(phone)
            
            # Check if bi_cc is not None before setting its value
            if bi_cc is not None:
                self.bi_cc_text.SetValue(bi_cc)
            self.nif_text.SetValue(nif)
            self.email_text.SetValue(email)
            if isinstance(birthday, datetime.date):
                birthday_str = birthday.strftime("%d-%m-%Y")
            else:
                birthday_str = birthday
            try:
                day, month, year = map(int, birthday_str.split("-"))
                self.birthday_picker.SetValue(wx.DateTime.FromDMY(day, month - 1, year))
            except (ValueError, AttributeError) as e:
                print(f"Erro ao processar a data de nascimento: {e}")
            agreement_map = {"Sim": 0, "Não": 1}
            agreement_index = agreement_map.get(agreement, -1)
            if agreement_index != -1:
                self.terms_radio.SetSelection(agreement_index)
            else:
                wx.MessageBox("Valor de concordância não reconhecido.", "Erro na seleção", wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox("Militante não encontrado.", "Resultado da pesquisa", wx.OK | wx.ICON_ERROR)
    
    def on_clear(self):
        self.id_text.SetValue("")
        self.name_text.SetValue("")
        self.address_text.SetValue("")
        self.parish_text.SetValue("")
        self.district_combo.SetValue("")
        self.city_combo.SetValue("")
        self.zip_text.SetValue("")
        self.phone_text.SetValue("")
        self.bi_cc_text.SetValue("")
        self.nif_text.SetValue("")
        self.email_text.SetValue("")
        self.birthday_picker.SetValue(wx.DateTime.Now())
        self.terms_radio.SetSelection(0)

    @staticmethod
    def export_all_to_pdf(event):
        try:
            banc.cursor.execute("SELECT * FROM militantes")
            results = banc.cursor.fetchall()
            if not results:
                wx.MessageBox('Sem dados para exportar', 'Info', wx.OK | wx.ICON_INFORMATION)
                return
            
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            export_folder = os.path.join(desktop_path, 'Listas Militantes')
            if not os.path.exists(export_folder):
                os.makedirs(export_folder)
            
            pdf_file = os.path.join(export_folder, 'militantes.pdf')
            doc = SimpleDocTemplate(pdf_file, pagesize=legal)
            
            styles = getSampleStyleSheet()
            title_style = styles['Title'].clone('CustomTitle')
            title_style.fontSize = 16
            title_style.textColor = colors.dodgerblue
            
            elements = []
            logo = os.path.join(current_dir, "..", "src_files", "logos", "nova_direita.png")
            im = Image(logo, 1.5 * inch, 1 * inch, hAlign='LEFT')
            elements.append(im)
            elements.append(Paragraph("Lista de Militantes", title_style))
            elements.append(Spacer(1, 12))
            
            militant_per_page = calculate_militant_per_page(legal, inch)
            for i, row in enumerate(results):
                if i > 0 and i % militant_per_page == 0:
                    elements.append(PageBreak())
                elements.append(create_militant_table(row))
                elements.append(Spacer(1, 12))
            
            doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
            wx.MessageBox(f'Dados exportados com sucesso para {pdf_file}', 'Info', wx.OK | wx.ICON_INFORMATION)
        
        except mysql.connector.Error as e:
            wx.MessageBox(f'Erro ao exportar dados: {e}', 'Erro', wx.OK | wx.ICON_ERROR)
    
    @staticmethod
    def export_all_to_xlsx(event):
        try:
            banc.cursor.execute("SELECT * FROM militantes")
            results = banc.cursor.fetchall()
            if not results:
                wx.MessageBox('Sem dados para exportar', 'Info', wx.OK | wx.ICON_INFORMATION)
                return
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            export_folder = os.path.join(desktop_path, 'Listas Militantes')
            if not os.path.exists(export_folder):
                os.makedirs(export_folder)
            xlsx_file = os.path.join(export_folder, 'militantes.xlsx')
            wb = openpyxl.Workbook()
            ws = wb.active
            headers = ['Militante', 'Nome Completo', 'Morada', 'Freguesia', 'Distrito', 'Cidade', 'Código Postal', 'Telefone', 'BI/CC', 'NIF', 'Email', 'Data de Nascimento', 'Aceita os Termos']
            ws.append(headers)
            for row in results:
                ws.append(row)
            wb.save(xlsx_file)
            wx.MessageBox(f'Dados exportados com sucesso para {xlsx_file}', 'Info', wx.OK | wx.ICON_INFORMATION)
        except mysql.connector.Error as e:
            wx.MessageBox(f'Erro ao exportar dados: {e}', 'Erro', wx.OK | wx.ICON_ERROR)


if __name__ == '__main__':
    app = wx.App()
    frame = Application(None, 'Nova Direita - Gestão de Militantes v1.0.0b')
    app.MainLoop()
