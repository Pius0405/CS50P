from fpdf import FPDF, Align


class PDF(FPDF):
    def header(self):
        #font here only applies to header as it is defined in header method
        self.set_font("Helvetica", "B", 45)
        self.cell(w = 0, h = 60, text = "CS50 Shirtificate", align = "C")


pdf = PDF()
pdf.add_page()
pdf.set_font("Helvetica", "B", 23)
pdf.set_text_color(255,255,255)
pdf.image("shirtificate.png", x = Align.C, y = 70, w = pdf.epw)
name = input("Name: ")
#alternative way to center the cell
pdf.cell(h = 235, text = f"{name} took CS50", center = True)
pdf.output("shirtificate.pdf")
