from reportlab.pdfgen import canvas 

my_canvas=canvas.Canvas("hello.pdf")
my_canvas.drawString(100,750,"Hello to the pdf example!!")
my_canvas.save()

