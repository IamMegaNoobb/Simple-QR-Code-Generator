from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import segno
import config

def get_source():
    source = config.app.source.get()
    file_output = config.app.file_output_name.get()
    output_type = config.app.file_output_type.get()
    if config.app.activate_artistic.get():
        scale_value = int(config.app.scale_slider.get())
        generate_artistic_qr(source, file_output, output_type, bg_name, scale_value)
    else:
        generate_qr(source, file_output, output_type)

# fix
def generate_qr(source, file_output, output_type):
    qrcode = segno.make(str(source), micro=False)
    qrcode.save(str(file_output) + str(output_type), scale=10)
    if file_output == "program_preview":
        preview_img = ImageTk.PhotoImage(Image.open(f"program_preview{output_type}"))
        global preview
        preview = config.app.preview
        preview = Label(config.app.frame_right, image=preview_img)
        preview.image = preview_img
        preview.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        messagebox.showinfo("Complete", "QR Code has been generated.")

# fix
def generate_artistic_qr(source, file_output, output_type, bg_name, scale_value):
    qrcode = segno.make(str(source), micro=False)
    qrcode.to_artistic(background=bg_name, target=str(file_output+output_type), scale=scale_value)
    if file_output == "program_preview":
        preview_img = ImageTk.PhotoImage(Image.open(f"program_preview{output_type}"))
        global preview
        preview = config.app.preview
        preview = Label(config.app.frame_right, image=preview_img)
        preview.image = preview_img
        preview.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        messagebox.showinfo("Complete", "QR Code has been generated.")

def import_background():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.webp"), ("All files", "*.*")])
    if file_path:
        global bg_name
        bg_name = file_path

def toggle_artistic():
    if config.app.activate_artistic.get():
        config.app.submit.pack_forget()
        config.app.preview_button.pack_forget()
        config.app.label_background.pack()
        config.app.import_background_button.pack()
        config.app.scale_slider.pack()
        config.app.submit.pack()
        config.app.preview_button.pack()
    else:
        config.app.label_background.pack_forget()
        config.app.import_background_button.pack_forget()
        config.app.scale_slider.pack_forget()

def preview_qr():
    config.app.preview.place_forget()
    source = config.app.source.get()
    output_type = config.app.file_output_type.get()
    if config.app.activate_artistic.get():
        scale_value = int(config.app.scale_slider.get())
        generate_artistic_qr(source, "program_preview", output_type, bg_name, scale_value)
    else:
        generate_qr(source, "program_preview", output_type)
