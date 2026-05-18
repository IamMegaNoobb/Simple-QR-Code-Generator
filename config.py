from tkinter import *
from tkinter import ttk
from instance import *

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple QR Code Generator")
        self.geometry("700x500")
        self.resizable(False, False)

        self.title_label = Label(self, text="Simple QR Code Generator")
        self.title_label.grid(row=0, column=0, columnspan=2)

        # define columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=30)

        # frame
        self.frame_left = Frame(self)
        self.frame_left.grid(row=1, column=0, sticky="NSEW")
        self.frame_right = Frame(self)
        self.frame_right.grid(row=1, column=1, sticky="NSEW")
        # elements
        Label(self.frame_left, text="Select Source Type").pack()
        self.source_type = ttk.Combobox(
            self.frame_left,
            values=["URL", "Plain Text"],
            state="readonly"
        )

        self.source_type.pack()
        Label(self.frame_left, text="Source").pack()

        self.source = Entry(self.frame_left)
        self.source.pack()

        Label(self.frame_left, text="File output name").pack()
        self.file_output_name = Entry(self.frame_left)
        self.file_output_name.pack()

        Label(self.frame_left, text="File output type").pack()
        self.file_output_type = ttk.Combobox(
            self.frame_left,
            values=[".png", ".gif"],
            state="readonly"
        )
        self.file_output_type.pack()
        
        self.activate_artistic = IntVar()
        self.activate_artistic_button = Checkbutton(self.frame_left, text="Artisitic QR", variable=self.activate_artistic, command=toggle_artistic)
        self.activate_artistic_button.pack()

        self.label_background = Label(self.frame_left, text="Background")
        self.import_background_button = Button(self.frame_left, text="Import File", command=import_background)

        self.scale_slider = Scale(self.frame_left, from_=0, to=10, orient="horizontal")

        self.submit = Button(self.frame_left, text="Generate", command=get_source)
        self.submit.pack()

        self.preview_button = Button(self.frame_left, text="Preview", command=preview_qr)
        self.preview_button.pack()

        self.preview = Label(self.frame_right, text="Your preview will be showed here.")
        self.preview.place(relx=0.5, rely=0.5, anchor=CENTER)

def start_instance():
    global app
    app = App()
    app.mainloop()
