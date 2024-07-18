# -*- coding: utf-8 -*-
from fpdf import FPDF


class PrintPdf(FPDF):
    def header(self):
        self.image('logos/nova_direita.png', 10, 8, 33)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Lista de Militantes', 0, 1, 'C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')
    
    def chapter_title(self, name):
        self.set_font('Arial', '', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, name, 0, 1, 'L', True)
        self.ln(4)
    
    def chapter_body(self, body):
        with open(body, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('Times', '', 12)
        self.multi_cell(0, 10, txt)
        self.ln()
    
    def print_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)
