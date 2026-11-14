from fpdf import FPDF


def main():
    name = input("Name: ").strip()
    make_pdf(name)


def make_pdf(name):
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()

    
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")


    img_w = 190
    img_x = (pdf.w - img_w) / 2
    img_y = 70
    pdf.image("shirtificate.png", x=img_x, y=img_y, w=img_w)


    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(img_y + 55)
    pdf.cell(0, 20, name, align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
