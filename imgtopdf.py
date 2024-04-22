import re
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_image_paths(folder_name, start, end):
    pattern = re.compile(r'^([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|1[0-9]{2}|2[0-6][0-9]|276|100[1-9]|10[1-9][0-9]|101[0-1])\.jpg$')
    return [folder_name + str(i) + '.jpg' for i in range(start, end+1) if pattern.match(str(i) + '.jpg')]

def jpg_to_pdf(image_paths, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    for image_path in image_paths:
        img = Image.open(image_path)
        img_width, img_height = img.size

        # Calculate aspect ratio to maintain the original image proportions
        aspect_ratio = img_width / img_height
        if aspect_ratio > 1:
            img_width = width
            img_height = width / aspect_ratio
        else:
            img_height = height
            img_width = height * aspect_ratio

        c.setPageSize((img_width, img_height))
        c.drawImage(image_path, 0, 0, width=img_width, height=img_height)
        c.showPage()

    c.save()

# Define the folder name where images are stored
folder_name = "8086/"

# Generate image paths
image_paths = generate_image_paths(folder_name, 1001, 1011) + generate_image_paths(folder_name, 1, 276)

# Output PDF path
pdf_path = "8086.pdf"

# Convert images to PDF
jpg_to_pdf(image_paths, pdf_path)
