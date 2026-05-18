from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import segno
import time

# TODO: artistic qr, file output naming, image resolution options

def get_source():
    source = source_link.get()
    file_output = file_output_name.get()
    output_type = select_output_type.get()
    if activate_artistic.get():
        scale_value = int(scale_slider.get())
        generate_artistic_qr(source, file_output, output_type, bg_name, scale_value)
    else:
        generate_qr(source, file_output, output_type)

def generate_qr(source, file_output, output_type):
    qrcode = segno.make(str(source), micro=False)
    print("created qrcode var")
    qrcode.save(str(file_output) + str(output_type), scale=10)
    print(f"saved img as {file_output}{output_type}")
    if file_output == "program_preview":
        preview_img = ImageTk.PhotoImage(Image.open(f"program_preview{output_type}"))
        print("created preview_img var")
        print(preview_img)
        global preview
        print("created preview global var")
        preview = Label(root, image=preview_img)
        preview.image = preview_img
        print("created preview label")
        print(preview)
        preview.pack()
        print("packed preview")
    else:
        messagebox.showinfo("Complete", "QR Code has been generated.")

def generate_artistic_qr(source, file_output, output_type, bg_name, scale_value):
    qrcode = segno.make(str(source), micro=False)
    qrcode.to_artistic(background=bg_name, target=str(file_output+output_type), scale=scale_value)
    if file_output == "program_preview":
        preview_img = ImageTk.PhotoImage(Image.open(f"program_preview{output_type}"))
        global preview
        preview = Label(root, image=preview_img)
        preview.image = preview_img
        preview.pack()
    else:
        messagebox.showinfo("Complete", "QR Code has been generated.")

def import_background():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.webp"), ("All files", "*.*")])
    if file_path:
        global bg_name
        bg_name = file_path

def toggle_artistic():
    if activate_artistic.get():
        submit.pack_forget()
        preview_button.pack_forget()
        label_title_artistic.pack()
        label_background.pack()
        import_background_button.pack()
        scale_slider.pack()
        submit.pack()
        preview_button.pack()
    else:
        label_title_artistic.pack_forget()
        label_background.pack_forget()
        import_background_button.pack_forget()
        scale_slider.pack_forget()

def preview_qr():
    preview.pack_forget()
    source = source_link.get()
    output_type = select_output_type.get()
    if activate_artistic.get():
        scale_value = int(scale_slider.get())
        generate_artistic_qr(source, "program_preview", output_type, bg_name, scale_value)
    else:
        generate_qr(source, "program_preview", output_type)
    
root = Tk(className='Simple QR Code Generator')
#root.geometry("700x500")
#root.resizable(False, False)
title = Label(root, text="Simple QR Code Generator")
title.pack()

label_source_type = Label(root, text="Select Source Type")
select_source_type = ttk.Combobox(
    root,
    values=["URL", "Plain Text"],
    state="readonly"
)
label_source_type.pack()
select_source_type.pack()
label_source_link = Label(root, text="Source: ")
label_source_link.pack()
source_link = Entry(root)
label_file_output_name = Label(root, text="File Output Name: ")
activate_artistic = IntVar()
activate_artistic_button = Checkbutton(root, text="Artistic QR", variable=activate_artistic, command=toggle_artistic)
label_title_artistic = Label(root, text="-- Artistic QR --")
label_background = Label(root, text="Background: ")
import_background_button = Button(root, text="Import File", command=import_background)
file_output_name = Entry(root)
label_output_type = Label(root, text="Select Output Type")
select_output_type = ttk.Combobox(
    root,
    values=[".png", ".gif"],
    state="readonly"
)
scale_slider = Scale(root, from_=0, to=10, orient="horizontal")
submit = Button(root, text="Generate", command=get_source)
preview_button = Button(root, text="Preview", command=preview_qr)
preview = Label(root, text="YOUr iMaGe WiLl BE ShoWeD HeRE")
label_source_link.pack()
source_link.pack()
label_file_output_name.pack()
file_output_name.pack()
label_output_type.pack()
select_output_type.pack()
activate_artistic_button.pack()
submit.pack()
preview_button.pack()
preview.pack()

root.mainloop()
