# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

import pyuac
from tkcalendar import DateEntry

from constants import district_options
from loggin_setup import logger
from terms_and_conditions import text_rgpd
from users import Users

logger.info('=============================')


def format_cep(cep):
    if len(cep) == 4:
        return f"{cep}-"


class Application:
    def __init__(self, master=None):
        logger.info(f"A iniciar a aplicação 'Nova Direita'")
        self.user = Users()
        self.lbl_font = ('Cambria', '12', 'bold')
        self.txt_font = ('times new roman', '11')
        self.radio = StringVar()
        # Militante
        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()
        # Procurar
        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2['pady'] = 5
        self.container2.pack()
        # Nome
        self.container3 = Frame(master)
        self.container3['padx'] = 20
        self.container3['pady'] = 5
        self.container3.pack()
        # Endereço
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 5
        self.container4.pack()
        # Cidade
        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5['pady'] = 5
        self.container5.pack()
        # Distrito
        self.container6 = Frame(master)
        self.container6['padx'] = 20
        self.container6['pady'] = 5
        self.container6.pack()
        # Cód. Postal
        self.container7 = Frame(master)
        self.container7['padx'] = 20
        self.container7['pady'] = 5
        self.container7.pack()
        # Telefone
        self.container8 = Frame(master)
        self.container8['padx'] = 20
        self.container8['pady'] = 5
        self.container8.pack()
        # NIF
        self.container9 = Frame(master)
        self.container9['padx'] = 20
        self.container9['pady'] = 5
        self.container9.pack()
        # BI/CC
        self.container10 = Frame(master)
        self.container10['padx'] = 20
        self.container10['pady'] = 5
        self.container10.pack()
        # Calendário
        self.container11 = Frame(master)
        self.container11['padx'] = 20
        self.container11['pady'] = 5
        self.container11.pack()
        # E-mail
        self.container12 = Frame(master)
        self.container12['padx'] = 20
        self.container12['pady'] = 5
        self.container12.pack()
        # RGPD
        self.btn_open_second_window = Button(master, text='Termos e Condições', font=self.lbl_font, width=16, bg='purple', fg='white')
        self.btn_open_second_window['padx'] = 20
        self.btn_open_second_window['pady'] = 5
        self.btn_open_second_window['command'] = self.openSecondWindow
        self.btn_open_second_window.pack()
        # Disponível
        self.container13 = Frame(master)
        self.container13['padx'] = 20
        self.container13['pady'] = 5
        self.container13.pack()
        # Inserir
        self.container14 = Frame(master)
        self.container14['pady'] = 15
        self.container14.pack()
        # Alterar
        self.container15 = Frame(master)
        self.container15['pady'] = 15
        self.container15.pack()
        # Excluir
        self.container16 = Frame(master)
        self.container16['pady'] = 15
        self.container16.pack()
        # Sair
        self.title = Label(self.container1, text='Gestão de Militantes:')
        self.title['font'] = self.lbl_font
        self.title.pack()
        # Militante
        self.lbl_idUser = Label(self.container2, text='Militante:', font=self.lbl_font, width=10)
        self.lbl_idUser.pack(side=LEFT)
        self.txt_idUser = Entry(self.container2)
        self.txt_idUser['width'] = 14
        self.txt_idUser['font'] = self.txt_font
        self.txt_idUser.pack(side=LEFT)
        # Procurar
        self.btn_search = Button(self.container2, text='Procurar', font=self.lbl_font, width=10)
        self.btn_search['command'] = self.search_militant
        self.btn_search.pack(side=RIGHT)
        # Nome
        self.lbl_name = Label(self.container3, text='Nome:', font=self.lbl_font, width=10)
        self.lbl_name.pack(side=LEFT)
        self.txt_name = Entry(self.container3)
        self.txt_name['width'] = 125
        self.txt_name['font'] = self.txt_font
        self.txt_name.pack(side=LEFT)
        # Endereço
        self.lbl_address = Label(self.container4, text='Endereço:', font=self.lbl_font, width=10)
        self.lbl_address.pack(side=LEFT)
        self.txt_address = Entry(self.container4)
        self.txt_address['width'] = 125
        self.txt_address['font'] = self.txt_font
        self.txt_address.pack(side=LEFT)
        # Cidade
        self.lbl_city = Label(self.container5, text='Cidade:', font=self.lbl_font, width=10)
        self.lbl_city.pack(side=LEFT)
        self.txt_city = Entry(self.container5)
        self.txt_city['width'] = 125
        self.txt_city['font'] = self.txt_font
        self.txt_city.pack(side=LEFT)
        # Distrito
        self.lbl_district = Label(self.container6, text='Distrito:', font=self.lbl_font, width=10)
        self.lbl_district.pack(side=LEFT)
        self.selected_district = StringVar()
        self.selected_district.set(district_options[10])
        self.dropdown_district = OptionMenu(self.container6, self.selected_district, *district_options)
        self.dropdown_district.pack(side=LEFT)
        # Cód. Postal
        self.lbl_cep = Label(self.container7, text='Cód. Postal:', font=self.lbl_font, width=10)
        self.lbl_cep.pack(side=LEFT)
        self.txt_cep = Entry(self.container7)
        self.txt_cep['width'] = 125
        self.txt_cep['font'] = self.txt_font
        self.txt_cep.pack(side=LEFT)
        # Add validation to format CEP
        validate_cep = self.container7.register(format_cep)
        self.txt_cep.config(validate="key", validatecommand=(validate_cep, "%P"))
        # Telefone
        self.lbl_phone = Label(self.container8, text='Telefone:', font=self.lbl_font, width=10)
        self.lbl_phone.pack(side=LEFT)
        self.txt_phone = Entry(self.container8)
        self.txt_phone['width'] = 125
        self.txt_phone['font'] = self.txt_font
        self.txt_phone.pack(side=LEFT)
        # NIF
        self.lbl_nif = Label(self.container9, text='NIF:', font=self.lbl_font, width=10)
        self.lbl_nif.pack(side=LEFT)
        self.txt_nif = Entry(self.container9)
        self.txt_nif['width'] = 125
        self.txt_nif['font'] = self.txt_font
        self.txt_nif.pack(side=LEFT)
        # BI/CC
        self.lbl_cc = Label(self.container10, text='BI/CC:', font=self.lbl_font, width=10)
        self.lbl_cc.pack(side=LEFT)
        self.txt_cc = Entry(self.container10)
        self.txt_cc['width'] = 125
        self.txt_cc['font'] = self.txt_font
        self.txt_cc.pack(side=LEFT)
        # Calendar
        self.lbl_calendar = Label(self.container11, text='Data de Nascimento:', font=self.lbl_font)
        self.lbl_calendar.pack(side=LEFT, padx=10, pady=5)
        frame_calendar = Frame(self.container11)
        frame_calendar.pack(side=LEFT)
        self.entry_calendar = DateEntry(frame_calendar, width=12, font=self.txt_font, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.entry_calendar.pack(side=LEFT)
        # E-mail
        self.lbl_email = Label(self.container12, text='E-mail:', font=self.lbl_font, width=10)
        self.lbl_email.pack(side=LEFT)
        self.txt_email = Entry(self.container12)
        self.txt_email['width'] = 125
        self.txt_email['font'] = self.txt_font
        self.txt_email.pack()
        # Disponível
        self.lbl_available = Label(self.container13, text='Aceito os termos acima?', font=self.lbl_font, width=30)
        self.lbl_available.pack(side=LEFT)
        self.box_available_1 = Radiobutton(self.container13, text='Sim', font=self.txt_font, variable=self.radio, value='Sim')
        self.box_available_1.pack(side=LEFT)
        self.box_available_2 = Radiobutton(self.container13, text='Não', font=self.txt_font, variable=self.radio, value='Não')
        self.box_available_2.pack(side=LEFT)
        # Inserir
        self.bnt_insert = Button(self.container14, text='Inserir', font=self.lbl_font, width=12, bg='green', fg='white')
        self.bnt_insert['command'] = self.insert_militant
        self.bnt_insert.pack(side=LEFT)
        # Alterar
        self.bnt_change = Button(self.container14, text='Alterar', font=self.lbl_font, width=12, bg='orange', fg='white')
        self.bnt_change['command'] = self.change_militant
        self.bnt_change.pack(side=LEFT)
        # Excluir
        self.bnt_delete = Button(self.container14, text='Excluir', font=self.lbl_font, width=12, bg='red', fg='white')
        self.bnt_delete['command'] = self.exclude_militant
        self.bnt_delete.pack(side=LEFT)
        # Exportar Sheets
        self.bnt_export = Button(self.container15, text='Exportar Exel', font=self.lbl_font, width=12, bg='blue', fg='white')
        self.bnt_export['command'] = self.export_sheets
        self.bnt_export.pack(side=LEFT)
        # Exportar PDF
        self.bnt_export_pdf = Button(self.container15, text='Exportar PDF', font=self.lbl_font, width=12, bg='pink', fg='white')
        self.bnt_export_pdf['command'] = self.export_pdf
        self.bnt_export_pdf.pack(side=LEFT)
        # Sair
        self.bnt_exit = Button(self.container15, text='Sair', font=self.lbl_font, width=12, bg='gray', fg='white')
        self.bnt_exit['command'] = root.destroy
        self.bnt_exit.pack(side=LEFT)
        # Mensagem
        self.lbl_msg = Label(self.container16, text='', fg='blue')
        self.lbl_msg['font'] = ('Verdana', '9', 'bold')
        self.lbl_msg.pack()
    
    def openSecondWindow(self):
        second_window = Toplevel()
        second_window.title("Termos e Condições")
        second_window.geometry("600x500")
        second_window.iconbitmap('logo.ico')
        second_window.transient(root)
        second_window.focus_force()
        second_window.grab_set()
        text_area = scrolledtext.ScrolledText(second_window, wrap=WORD, font=self.txt_font)
        text_area.insert(END, text_rgpd)
        text_area.configure(state='disabled')
        text_area.pack(fill=BOTH, expand=True, padx=10, pady=10)
        close_button = Button(second_window, text='Fechar', command=second_window.destroy, width=12, bg='red', fg='black')
        close_button.pack(pady=10)
        second_window.update_idletasks()
        width = second_window.winfo_width()
        height = second_window.winfo_height()
        x = (second_window.winfo_screenwidth() // 2) - (width // 2)
        y = (second_window.winfo_screenheight() // 2) - (height // 2)
        second_window.geometry(f'{width}x{height}+{x}+{y}')
        second_window.bind('<Escape>', lambda event: second_window.destroy())
    
    def insert_militant(self):
        logger.info(f"Attempting to insert militant: {self.txt_name.get()}")
        self.user.name = self.txt_name.get()
        self.user.address = self.txt_address.get()
        self.user.city = self.txt_city.get()
        self.user.district = self.selected_district.get()
        self.user.cep = self.txt_cep.get()
        self.user.phone = self.txt_phone.get()
        self.user.nif = self.txt_nif.get()
        self.user.cc = self.txt_cc.get()
        self.user.calendar_date = self.entry_calendar.get_date()
        self.user.email = self.txt_email.get()
        self.user.available = self.radio.get()
        # Verificar se o campo 'nome' está preenchido
        if not self.user.name:
            self.lbl_msg['text'] = 'Campo "Nome" é obrigatório.'
            return
        # Verificar se o campo 'Morada' está preenchido
        if not self.user.address:
            self.lbl_msg['text'] = 'Campo "Morada" é obrigatório.'
            return
        # Verificar se o campo 'Cidade' está preenchido
        if not self.user.city:
            self.lbl_msg['text'] = 'Campo "Cidade" é obrigatório.'
            return
        # Verificar se o campo 'Distrito' está preenchido
        if not self.user.district:
            self.lbl_msg['text'] = 'Campo "Distrito" é obrigatório.'
            return
        # Verificar se o campo 'Código Postal' está preenchido
        if not self.user.cep:
            self.lbl_msg['text'] = 'Campo "Código Postal" é obrigatório.'
            return
        # Validate phone number
        if not self.user.phone.isdigit() or len(self.user.phone) != 9:
            self.lbl_msg['text'] = 'O número de telefone deve conter 9 dígitos.'
            return
        # Validate NIF
        if not self.user.nif.isdigit() or len(self.user.nif) != 9:
            self.lbl_msg['text'] = 'O NIF deve conter 9 dígitos.'
            return
        # Validate CC
        if not self.user.cc.isdigit() or len(self.user.cc) != 8:
            self.lbl_msg['text'] = 'O número do Cartão de Cidadão deve conter 8 dígitos.'
            return
        # Verificar se o campo 'Data de Nascimento' está preenchido
        if not self.user.calendar_date:
            self.lbl_msg['text'] = 'Campo "Data de Nascimento" é obrigatório.'
            return
        # Verificar se o campo 'Email' está preenchido
        if not self.user.email:
            self.lbl_msg['text'] = 'Campo "Email" é obrigatório.'
            return
        # Verificar se o campo 'Termos' está preenchido
        if not (self.openSecondWindow and self.user.available):
            self.lbl_msg['text'] = 'Você precisa de aceitar os termos e condições para continuar.'
            return
        # Limpar os campos após a operação
        self.txt_idUser.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_address.delete(0, END)
        self.txt_city.delete(0, END)
        self.user.district = self.selected_district.get()
        self.txt_cep.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_nif.delete(0, END)
        self.txt_cc.delete(0, END)
        self.entry_calendar.delete(0, END)
        self.txt_email.delete(0, END)
        self.radio.get()
        self.lbl_msg['text'] = self.user.insert_militant()
        self.clear_fields()
        logger.debug(f"Militant data: {self.user.__dict__}")
        result = self.user.insert_militant()
        logger.info(f"Insert militant result: {result}")
    
    def change_militant(self):
        logger.info(f"Attempting to update militant: {self.txt_name.get()}")
        self.user.idUser = self.txt_idUser.get()
        self.user.name = self.txt_name.get()
        self.user.address = self.txt_address.get()
        self.user.city = self.txt_city.get()
        self.user.district = self.selected_district.get()
        self.user.cep = self.txt_cep.get()
        self.user.phone = self.txt_phone.get()
        self.user.nif = self.txt_nif.get()
        self.user.cc = self.txt_cc.get()
        self.user.calendar_date = self.entry_calendar.get_date()
        self.user.email = self.txt_email.get()
        self.user.available = self.radio.get()
        #
        self.txt_idUser.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_address.delete(0, END)
        self.txt_city.delete(0, END)
        self.selected_district.set(self.user.district)
        self.txt_cep.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_nif.delete(0, END)
        self.txt_cc.delete(0, END)
        self.entry_calendar.delete(0, END)
        self.txt_email.delete(0, END)
        self.radio.get()
        self.lbl_msg['text'] = self.user.update_militant()
        self.clear_fields()
        logger.debug(f"Dados do Militante atualizados: {self.user.__dict__}")
        result = self.user.update_militant()
        logger.info(f"Resultado da atualização do Militante: {result}")
    
    def exclude_militant(self):
        logger.info(f"A tentar excluir o Militante: {self.txt_idUser.get()}")
        self.user.idUser = self.txt_idUser.get()
        self.txt_idUser.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_address.delete(0, END)
        self.txt_city.delete(0, END)
        self.selected_district.set(self.user.district)
        self.txt_cep.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_nif.delete(0, END)
        self.txt_cc.delete(0, END)
        self.entry_calendar.delete(0, END)
        self.txt_email.delete(0, END)
        self.lbl_msg['text'] = self.user.delete_militant()
        self.clear_fields()
        result = self.user.delete_militant()
        logger.info(f"Militante excluído: {result}")
    
    def export_sheets(self):
        self.lbl_msg['text'] = self.user.create_sheet()
    
    def export_pdf(self):
        self.lbl_msg['text'] = self.user.generate_pdf()
    
    def search_militant(self):
        logger.info(f"Procurar o Militante: {self.txt_idUser.get()}")
        userId = self.user.idUser
        idUser = self.txt_idUser.get()
        self.txt_idUser.delete(0, END)
        self.txt_idUser.insert(INSERT, userId)
        self.txt_name.delete(0, END)
        self.txt_name.insert(INSERT, self.user.name)
        self.txt_address.delete(0, END)
        self.txt_address.insert(INSERT, self.user.address)
        self.txt_city.delete(0, END)
        self.txt_city.insert(INSERT, self.user.city)
        self.selected_district.set(self.user.district)
        self.txt_cep.delete(0, END)
        self.txt_cep.insert(INSERT, self.user.cep)
        self.txt_phone.delete(0, END)
        self.txt_phone.insert(INSERT, self.user.phone)
        self.txt_nif.delete(0, END)
        self.txt_nif.insert(INSERT, self.user.nif)
        self.txt_cc.delete(0, END)
        self.txt_cc.insert(INSERT, self.user.cc)
        self.entry_calendar.delete(0, END)
        self.entry_calendar.set_date(self.user.calendar_date)
        self.txt_email.delete(0, END)
        self.txt_email.insert(INSERT, self.user.email)
        self.radio.set(self.user.available)
        self.lbl_msg['text'] = self.user.select_militant(idUser)
        self.fill_fields()
        result = self.user.select_militant(idUser)
        logger.info(f"Resultado da procura do Militante: {result}")
    
    def clear_fields(self):
        self.txt_idUser.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_address.delete(0, END)
        self.txt_city.delete(0, END)
        self.selected_district.set(self.user.district)
        self.txt_cep.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_nif.delete(0, END)
        self.txt_cc.delete(0, END)
        self.entry_calendar.delete(0, END)
        self.txt_email.delete(0, END)
    
    def fill_fields(self):
        self.txt_idUser.delete(0, END)
        self.txt_idUser.insert(INSERT, self.user.idUser)
        self.txt_name.delete(0, END)
        self.txt_name.insert(INSERT, self.user.name)


if __name__ == '__main__':
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        root = tk.Tk()
        root.withdraw()
        app = Application(root)
        root.title('Nova Direita - Gestão de Militantes')
        root.geometry('800x700')
        root.iconbitmap('logo.ico')
        root.deiconify()
        root.mainloop()
