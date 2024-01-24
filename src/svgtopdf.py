import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors

def create_pdf_with_grid(directory_path, output_pdf_path, images_per_row=5, rows_per_page=6):
    # Constants for layout
    page_width, page_height = A4
    margin = 2 * cm
    spacing = 0.5 * cm
    image_width = (page_width - 2 * margin - (images_per_row - 1) * spacing) / images_per_row
    image_height = (page_height - 2 * margin - (rows_per_page - 1) * spacing) / rows_per_page
    text_height = 0.7 * cm  # Height reserved for text under each image
    subtitle_height = 1 * cm  # Height reserved for folder subtitle
    font_size = 8  # Smaller font size for filenames
    subtitle_font_size = 10  # Font size for folder subtitles

    # Create a PDF canvas
    c = canvas.Canvas(output_pdf_path, pagesize=A4)

    # Initialize counters and flags
    image_counter = 0
    current_folder = None

    # Recursive directory walk
    for root, dirs, files in os.walk(directory_path):
        for svg_file in files:
            if svg_file.endswith('.svg'):
                file_path = os.path.join(root, svg_file)
                rel_path = os.path.relpath(root, directory_path)  # Relative path of the folder

                # Check if we are in a new folder
                if current_folder != rel_path:
                    current_folder = rel_path
                    if image_counter > 0:
                        c.showPage()  # Start a new page for a new folder
                        image_counter = 0  # Reset image counter

                    # Add the folder name as a subtitle
                    c.setFont("Helvetica-Bold", subtitle_font_size)
                    c.setFillColor(colors.black)
                    c.drawString(margin, page_height - margin - subtitle_height, current_folder)

                # Calculate grid position
                row = (image_counter // images_per_row) % rows_per_page + 1  # Adjust row for subtitle
                col = image_counter % images_per_row
                x = margin + col * (image_width + spacing)
                y = page_height - margin - (row + 1) * (image_height + spacing) + text_height + subtitle_height

                try:
                    # Convert SVG to a format suitable for embedding in PDF
                    drawing = svg2rlg(file_path)
                    drawing.width, drawing.height = image_width, image_height - text_height
                    renderPDF.draw(drawing, c, x, y)

                    # Add filename text below the image
                    c.setFont("Helvetica", font_size)
                    c.setFillColor(colors.black)
                    c.drawString(x, y - text_height + 3, svg_file)

                    image_counter += 1
                    if image_counter % (images_per_row * rows_per_page) == 0:
                        c.showPage()  # Add a new page when the current page is full

                except Exception as e:
                    print(f"Error processing {svg_file}: {e}")

    # Save the PDF
    c.save()

# Example usage of the function
# create_pdf_with_grid("path_to_your_svg_directory", "output.pdf")

current_directory = os.getcwd()
print(current_directory)
dr = current_directory + "\\src\\svg-files"

create_pdf_with_grid(dr, "output.pdf")



