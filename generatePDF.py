import fpdf as pyfpdf

from fpdf import FPDF

title = 'NOTICE'

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Subject : Violation of Traffic Rules by %s' % (label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self,txt):
        # Read text file
        #with open(name, 'rb') as fh:
         #   txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(R.T.O.)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

def gPDF(name,nplate,license):
	txt = "This is to inform you that the car with the number "+ nplate + " registered under the name of " + name + " was caught violating traffic rules by our Automated program i.e. Halogen. For the same, you have to pay a fine of INR 1000/-. Please Pay the sum as soon as possible to the nearest RTO or strict actions will be taken including suspension of Driving license numbered " + license +" within 10 days from this notice."
	
	pdf = PDF()
	pdf.set_title(title)
	pdf.print_chapter(1, nplate , txt)
	pdf.output('receipt.pdf', 'F')
	
#gPDF('Rakshit','MKSISDCD')
