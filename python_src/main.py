# -*- coding: utf-8 -*-
import ctypes
import re
import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

from tkcalendar import DateEntry

from constants import district_options
from constants import icon
from terms_and_conditions import text_rgpd
from users import Users


class Application:
    def __init__(self, master=None):
        self.master = master
        self.user = Users()
        self.btn_error = None
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
        self.container3.pack(fill='x', anchor='w')
        # Endereço
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 5
        self.container4.pack(fill='x', anchor='w')
        # Cidade
        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5['pady'] = 5
        self.container5.pack(fill='x', anchor='w')
        # Distrito
        self.container6 = Frame(master)
        self.container6['padx'] = 20
        self.container6['pady'] = 5
        self.container6.pack(fill='x', anchor='w')
        # Cód. Postal
        self.container7 = Frame(master)
        self.container7['padx'] = 20
        self.container7['pady'] = 5
        self.container7.pack(fill='x', anchor='w')
        # Telefone
        self.container8 = Frame(master)
        self.container8['padx'] = 20
        self.container8['pady'] = 5
        self.container8.pack(fill='x', anchor='w')
        # NIF
        self.container9 = Frame(master)
        self.container9['padx'] = 20
        self.container9['pady'] = 5
        self.container9.pack(fill='x', anchor='w')
        # BI/CC
        self.container10 = Frame(master)
        self.container10['padx'] = 20
        self.container10['pady'] = 5
        self.container10.pack(fill='x', anchor='w')
        # BI/CC data de expiração
        self.container11 = Frame(master)
        self.container11['padx'] = 20
        self.container11['pady'] = 5
        self.container11.pack(fill='x', anchor='w')
        # Calendário
        self.container12 = Frame(master)
        self.container12['padx'] = 20
        self.container12['pady'] = 5
        self.container12.pack(fill='x', anchor='w')
        # E-mail
        self.container13 = Frame(master)
        self.container13['padx'] = 20
        self.container13['pady'] = 5
        self.container13.pack(fill='x', anchor='w')
        # RGPD
        self.btn_open_second_window = Button(master, text='Termos e Condições', font=self.lbl_font, width=16, bg='purple', fg='white')
        self.btn_open_second_window['padx'] = 20
        self.btn_open_second_window['pady'] = 5
        self.btn_open_second_window['command'] = self.openSecondWindow
        self.btn_open_second_window.pack()
        # Disponível
        self.container14 = Frame(master)
        self.container14['padx'] = 20
        self.container14['pady'] = 5
        self.container14.pack()
        # Inserir
        self.container15 = Frame(master)
        self.container15['pady'] = 15
        self.container15.pack()
        # Alterar
        self.container16 = Frame(master)
        self.container16['pady'] = 15
        self.container16.pack()
        # Excluir
        self.container17 = Frame(master)
        self.container17['pady'] = 15
        self.container17.pack()
        # Mensagem
        self.container18 = Frame(master)
        self.container18['pady'] = 15
        self.container18.pack()
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
        self.txt_name['width'] = 90
        self.txt_name['font'] = self.txt_font
        self.txt_name.pack(side=LEFT)
        # Endereço
        self.lbl_address = Label(self.container4, text='Endereço:', font=self.lbl_font, width=10)
        self.lbl_address.pack(side=LEFT)
        self.txt_address = Entry(self.container4)
        self.txt_address['width'] = 90
        self.txt_address['font'] = self.txt_font
        self.txt_address.pack(side=LEFT)
        # Cidade
        self.lbl_city = Label(self.container5, text='Cidade:', font=self.lbl_font, width=10)
        self.lbl_city.pack(side=LEFT)
        self.txt_city = Entry(self.container5)
        self.txt_city['width'] = 35
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
        self.lbl_cep = tk.Label(self.container7, text='Cód. Postal:', font=self.lbl_font, width=10)
        self.lbl_cep.pack(side=LEFT)
        self.txt_cep = Entry(self.container7)
        self.txt_cep['width'] = 20
        self.txt_cep['font'] = self.txt_font
        self.txt_cep.pack(side=LEFT)
        validate_cep = self.container7.register(self.format_cep)
        self.txt_cep.config(validate='focusout', validatecommand=(validate_cep, '%P'))
        # Telefone
        self.lbl_phone = Label(self.container8, text='Telefone:', font=self.lbl_font, width=10)
        self.lbl_phone.pack(side=LEFT)
        self.txt_phone = Entry(self.container8)
        self.txt_phone['width'] = 20
        self.txt_phone['font'] = self.txt_font
        self.txt_phone.pack(side=LEFT)
        # NIF
        self.lbl_nif = Label(self.container9, text='NIF:', font=self.lbl_font, width=10)
        self.lbl_nif.pack(side=LEFT)
        self.txt_nif = Entry(self.container9)
        self.txt_nif['width'] = 20
        self.txt_nif['font'] = self.txt_font
        self.txt_nif.pack(side=LEFT)
        # BI/CC
        self.lbl_cc = Label(self.container10, text='BI/CC:', font=self.lbl_font, width=10)
        self.lbl_cc.pack(side=LEFT)
        self.txt_cc = Entry(self.container10)
        self.txt_cc['width'] = 20
        self.txt_cc['font'] = self.txt_font
        self.txt_cc.pack(side=LEFT)
        # BI/CC data de validade
        self.lbl_cc_exp = Label(self.container11, text='Data de validade CC:', font=self.lbl_font, width=20)
        self.lbl_cc_exp.pack(side=LEFT)
        frame_cc_exp = Frame(self.container11)
        frame_cc_exp.pack(side=LEFT)
        self.entry_cc_exp = DateEntry(frame_cc_exp, width=20, font=self.txt_font, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.entry_cc_exp.pack(side=LEFT)
        # Calendário
        self.lbl_calendar = Label(self.container12, text='Data de Nascimento:', font=self.lbl_font)
        self.lbl_calendar.pack(side=LEFT)
        frame_calendar = Frame(self.container12)
        frame_calendar.pack(side=LEFT)
        self.entry_calendar = DateEntry(frame_calendar, width=20, font=self.txt_font, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.entry_calendar.pack(side=LEFT)
        # E-mail
        self.lbl_email = Label(self.container13, text='E-mail:', font=self.lbl_font, width=10)
        self.lbl_email.pack(side=LEFT)
        self.txt_email = Entry(self.container13)
        self.txt_email['width'] = 90
        self.txt_email['font'] = self.txt_font
        self.txt_email.pack(side=LEFT)
        # Disponível
        self.lbl_availability = Label(self.container14, text='Aceito os termos acima?', font=self.lbl_font, width=20)
        self.lbl_availability.pack(side=LEFT)
        self.radio_availability = StringVar()
        self.radio_availability.set('Sim')
        self.avail_yes = Radiobutton(self.container14, text='Sim', variable=self.radio_availability, value='Sim', font=self.txt_font)
        self.avail_no = Radiobutton(self.container14, text='Não', variable=self.radio_availability, value='Não', font=self.txt_font)
        self.avail_yes.pack(side=LEFT)
        self.avail_no.pack(side=LEFT)
        # Inserir
        self.bnt_insert = Button(self.container15, text='Inserir', font=self.lbl_font, width=12, bg='green', fg='white')
        self.bnt_insert['command'] = self.insert_militant
        self.bnt_insert.pack(side=LEFT)
        # Alterar
        self.bnt_change = Button(self.container15, text='Alterar', font=self.lbl_font, width=12, bg='orange', fg='white')
        self.bnt_change['command'] = self.change_militant
        self.bnt_change.pack(side=LEFT)
        # Excluir
        self.bnt_delete = Button(self.container15, text='Excluir', font=self.lbl_font, width=12, bg='red', fg='white')
        self.bnt_delete['command'] = self.exclude_militant
        self.bnt_delete.pack(side=LEFT)
        # Exportar Sheets
        self.bnt_export = Button(self.container16, text='Exportar Exel', font=self.lbl_font, width=12, bg='blue', fg='white')
        self.bnt_export['command'] = self.export_sheets
        self.bnt_export.pack(side=LEFT)
        # Exportar PDF
        self.bnt_export_pdf = Button(self.container16, text='Exportar PDF', font=self.lbl_font, width=12, bg='pink', fg='white')
        self.bnt_export_pdf['command'] = self.export_pdf
        self.bnt_export_pdf.pack(side=LEFT)
        # Sair
        self.bnt_exit = Button(self.container17, text='Sair', font=self.lbl_font, width=12, bg='gray', fg='white')
        self.bnt_exit['command'] = root.destroy
        self.bnt_exit.pack(side=LEFT)
        # Mensagem
        self.lbl_msg = Label(self.container18, text='', fg='blue')
        self.lbl_msg['font'] = ('Verdana', '9', 'bold')
        self.lbl_msg.pack()
        self.create_widgets()
    
    @staticmethod
    def format_cep(cep):
        if len(cep) == 8 and cep[:4].isdigit() and cep[4] == '-' and cep[5:].isdigit():
            return True
        return False
    
    def create_widgets(self):
        self.btn_error = Button(self.master, text="Erro gerado", command=self.generate_error)
        self.btn_error.pack()
    
    @staticmethod
    def generate_error():
        try:
            raise Exception('Ocorreu um erro')
        except Exception as err:
            messagebox.showerror('Erro', f'Ocorreu um erro: {str(err)}')
    
    def openSecondWindow(self):
        second_window = Toplevel()
        second_window.title('Termos e Condições')
        second_window.geometry('600x500')
        second_window.iconbitmap(icon)
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
        if not self.validate_fields():
            return
        self.user.name = self.txt_name.get()
        self.user.address = self.txt_address.get()
        self.user.city = self.txt_city.get()
        self.user.district = self.selected_district.get()
        self.user.cep = self.txt_cep.get()
        self.user.phone = self.txt_phone.get()
        self.user.nif = self.txt_nif.get()
        self.user.cc = self.txt_cc.get()
        self.user.cc_exp = self.entry_cc_exp.get()
        self.user.calendar_date = self.entry_calendar.get_date()
        self.user.email = self.txt_email.get()
        self.user.available = self.radio_availability.get()
        result = self.user.insert_militant()
        self.lbl_msg['text'] = result
        self.clear_fields()
        messagebox.showwarning('Inserir', f'Militante inserido com: {result}')
    
    def change_militant(self):
        if not self.validate_fields():
            return
        self.user.idUser = self.txt_idUser.get()
        self.user.name = self.txt_name.get()
        self.user.address = self.txt_address.get()
        self.user.city = self.txt_city.get()
        self.user.district = self.selected_district.get()
        self.user.cep = self.txt_cep.get()
        self.user.phone = self.txt_phone.get()
        self.user.nif = self.txt_nif.get()
        self.user.cc = self.txt_cc.get()
        self.user.cc_exp = self.entry_cc_exp.get()
        self.user.calendar_date = self.entry_calendar.get_date()
        self.user.email = self.txt_email.get()
        self.user.available = self.radio_availability.get()
        self.lbl_msg['text'] = self.user.update_militant()
        self.clear_fields()
        result = self.user.update_militant()
        messagebox.showinfo('Atualização', f'Militante atualizado: {result}')
    
    def exclude_militant(self):
        self.lbl_msg['text'] = self.user.delete_militant()
        self.clear_fields()
        result = self.user.delete_militant()
        messagebox.showinfo('Exclusão', f'Militante excluído: {result}')
    
    def export_sheets(self):
        self.lbl_msg['text'] = self.user.create_sheet()
    
    def export_pdf(self):
        self.lbl_msg['text'] = self.user.generate_pdf()
    
    def search_militant(self):
        idUser = self.txt_idUser.get()
        self.lbl_msg['text'] = self.user.select_militant(idUser)
        self.fill_fields()
        result = self.user.select_militant(idUser)
        messagebox.showinfo('Procura', f'Resultado da procura do Militante: {result}')
    
    def validate_fields(self):
        fields = {
            'Nome': self.txt_name.get(),
            'Endereço': self.txt_address.get(),
            'Cidade': self.txt_city.get(),
            'Cód. Postal': self.txt_cep.get(),
            'Telefone': self.txt_phone.get(),
            'NIF': self.txt_nif.get(),
            'BI/CC': self.txt_cc.get(),
            'Data Expiração': self.entry_cc_exp.get(),
            'Data Nascimento': self.entry_calendar.get(),
            'E-mail': self.txt_email.get(),
            'Disponível': self.radio_availability.get(),
        }

        name_regex = r'^[a-zA-Z\s]+$'
        phone_regex = r'^\d{9}$'
        nif_regex = r'^\d{9}$'
        cc_regex = r'^\d{8}$'
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
        for field, value in fields.items():
            if not value:
                messagebox.showwarning('Aviso', f'O campo \'{field}\' é obrigatório.')
                return False
            
            if field == 'Nome' and not re.match(name_regex, value):
                messagebox.showwarning('Aviso', 'O campo \'Nome\' deve conter apenas letras e espaços.')
                return False
            
            if field == 'Cód. Postal' and not self.format_cep(value):
                messagebox.showwarning('Aviso', 'Código Postal inválido. Use o formato \'xxxx-xxx\'.')
                return False
            
            if field == 'Telefone' and not re.match(phone_regex, value):
                messagebox.showwarning('Aviso', 'O campo \'Telefone\' deve conter exatamente 9 dígitos.')
                return False
            
            if field == 'NIF' and not re.match(nif_regex, value):
                messagebox.showwarning('Aviso', 'O campo \'NIF\' deve conter exatamente 9 dígitos.')
                return False
            
            if field == 'BI/CC' and not re.match(cc_regex, value):
                messagebox.showwarning('Aviso', 'O campo \'BI/CC\' deve conter exatamente 8 dígitos.')
                return False
            
            if field == 'E-mail' and not re.match(email_regex, value):
                messagebox.showwarning('Aviso', 'Endereço de e-mail inválido.')
                return False
        return True
    
    def clear_fields(self):
        self.txt_idUser.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_address.delete(0, END)
        self.txt_city.delete(0, END)
        self.user.district = self.selected_district.get()
        self.txt_cep.delete(0, END)
        self.txt_phone.delete(0, END)
        self.txt_nif.delete(0, END)
        self.txt_cc.delete(0, END)
        self.entry_cc_exp.delete(0, END)
        self.entry_calendar.delete(0, END)
        self.txt_email.delete(0, END)
    
    def fill_fields(self):
        self.txt_idUser.delete(0, END)
        self.txt_idUser.insert(0, self.user.idUser)
        self.txt_name.delete(0, END)
        self.txt_name.insert(0, self.user.name)
        self.txt_address.delete(0, END)
        self.txt_address.insert(0, self.user.address)
        self.txt_city.delete(0, END)
        self.txt_city.insert(0, self.user.city)
        self.selected_district.set(self.user.district)
        self.txt_cep.delete(0, END)
        self.txt_cep.insert(0, self.user.cep)
        self.txt_phone.delete(0, END)
        self.txt_phone.insert(0, self.user.phone)
        self.txt_nif.delete(0, END)
        self.txt_nif.insert(0, self.user.nif)
        self.txt_cc.delete(0, END)
        self.txt_cc.insert(0, self.user.cc)
        self.entry_cc_exp.delete(0, END)
        self.entry_cc_exp.insert(0, self.user.cc_exp)
        self.entry_calendar.set_date(self.user.calendar_date)
        self.txt_email.delete(0, END)
        self.txt_email.insert(0, self.user.email)
        self.radio_availability.set("Sim")


def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        print('Running with administrative privileges')
    else:
        ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, __file__, None, 1)


if __name__ == '__main__':
    run_as_admin()
    if ctypes.windll.shell32.IsUserAnAdmin():
        root = tk.Tk()
        app = Application(root)
        root.title('Nova Direita - Gestão de Militantes')
        root.geometry('800x790')
        # root.iconbitmap(icon)
        root.mainloop()
