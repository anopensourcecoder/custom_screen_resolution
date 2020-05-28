
#try:
#    from custom_screen_resolution.resolutions import  PPI, Scale, Height, Resolution
#except ModuleNotFoundError:
#    from resolutions import  PPI, Scale, Height, Resolution


from custom_screen_resolution.custom_screen_resolution import  PPI, Scale, Height, Resolution
from . import __version__

from tkinter import *
import os

class CSR_GUI:


    def __init__(self, main_form):


        #print("ResolutionsGUI init")
        font_gui = "Arial 11"
        font_menu = "Arial 13"
        font_header_title = "Arial 20"
        font_header = "Arial 15"
        font_label_input = "Arial 10"
        font_input = "Arial 16"
        width_input = 7
        font_submit = "Arial 11"
        font_result = "Arial 16"
        main_form.title("Custom Screen Resolution GUI")
        #main_form.geometry("800x600")
        main_form.minsize(800,600)
        main_form.grid_rowconfigure(0, weight=1)
        main_form.grid_columnconfigure(0, weight=1)

        #ROOT_DIR = os.path.abspath(os.curdir)+'/custom_screen_resolution/'
        ROOT_DIR = os.path.dirname(__file__)
        #print(ROOT_DIR)

        #logo = PhotoImage(logo.png')


        #root.configure()
        main_frame = Frame(main_form )
        main_frame.grid(row=0, column=0, sticky="NEW")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=0)
        main_frame.grid_columnconfigure(2, weight=1)



        # menu
        self.menu_bar = Menu(main_form)
        main_form.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(font=font_menu, label="About",command=self.about_command)
        #file_menu.add_command(font=guifont, label="Save")
        #file_menu.add_command(font=guifont, label="Settings")
        #file_menu.add_command(font=guifont, label="Import")
        #file_menu.add_command(font=guifont, label="Export")



        self.file_menu.add_separator()
        self.file_menu.add_command(font=font_menu, label="Exit",  underline=1, accelerator='Alt-X',
                              command=lambda arg1=main_form: self.quit(arg1))
        self.menu_bar.add_cascade(font=font_menu, label="Menu", menu=self.file_menu,underline=0, accelerator='Alt-m')

        self.menu_bar.bind_all("<Alt-x>", self.quit)

        # ------- Header frame -----------------
        self.gui_header_frame = Frame(main_frame, height=30)
        self.gui_header_frame.grid(row=0, column=1)

        self.logo = PhotoImage(file=ROOT_DIR + '/logo32.png')
        self.gui_header_logo = Button(self.gui_header_frame, width=32, height=32 ,
                                      text="",image=self.logo, compound = LEFT, command = self.logo_command )
        self.gui_header_logo.grid(row=0, column=0, sticky="")
        self.gui_header_title = Label(self.gui_header_frame, text="Welcome to Custom Screen Resolution!",
                                      font=font_header_title)
        self.gui_header_title.grid(row=0, column=1, sticky="W", padx=20, pady=20)

        #------------side--------------
        self.side_frame = LabelFrame(main_frame,text="Calculate Resolution base on Screen size, PPI and Aspect ratio"
                                     ,borderwidth=4, font=font_header )
        self.side_frame.grid(row=1, column=1, sticky="WNE")
        self.side_frame.configure(padx=0, pady=10)
        #self.side_frame.configure( background = '#bbaaaa')

        self.side_screen_size = StringVar()
        self.side_screen_ppi = StringVar()
        self.side_screen_ratiox = StringVar()
        self.side_screen_ratioy = StringVar()
        self.side_result = StringVar()

        self.side_label_size = Label(self.side_frame, font=font_label_input, text="Screen Size" )
        self.side_label_size.grid(row=2, column=0, sticky="W",padx=10)
        self.side_entry_size = Entry(self.side_frame, width=width_input, font=font_input, textvariable=self.side_screen_size )
        self.side_entry_size.grid(row=3, column=0, sticky="W",padx=10)

        self.side_label_ppi = Label(self.side_frame, font=font_label_input, text="Screen PPI")
        self.side_label_ppi.grid(row=2, column=1, sticky="W",padx=10)
        self.side_entry_ppi = Entry(self.side_frame, width=width_input, font=font_input, textvariable=self.side_screen_ppi )
        self.side_entry_ppi.grid(row=3, column=1, sticky="W",padx=10)

        self.side_label_ratiox = Label(self.side_frame, font=font_label_input, text="Ratio X")
        self.side_label_ratiox.grid(row=2, column=2, sticky="W" ,padx=10)
        self.side_entry_ratiox = Entry(self.side_frame, width=width_input, font=font_input, textvariable=self.side_screen_ratiox )
        self.side_entry_ratiox.grid(row=3, column=2, sticky="W" ,padx=10)

        self.side_label_ratioy = Label(self.side_frame, font=font_label_input, text="Ratio Y")
        self.side_label_ratioy.grid(row=2, column=3, sticky="W" ,padx=10)
        self.side_entry_ratioy = Entry(self.side_frame, width=width_input, font=font_input, textvariable=self.side_screen_ratioy )
        self.side_entry_ratioy.grid(row=3, column=3, sticky="W" ,padx=10)

        self.side_entry_ratioy = Button(self.side_frame, width=width_input, height=1,  font=font_submit,
                                   text="Submit", command=self.side_command)
        self.side_entry_ratioy.grid(row=3, column=4, sticky="W", padx=10)

        self.side_label_result = Label(self.side_frame, font=font_result, textvariable=self.side_result )
        self.side_label_result.grid(row=4, column=0, columnspan=5, sticky="W" ,padx=10,pady=10)

        self.demo_side()

        #-------empty frame -----------------
        self.gui_empty_frame2 = Frame(main_frame ,height=20)
        self.gui_empty_frame2.grid(row=2, column=1 )

        #--------dpi-----------------------
        self.gui_dpi_frame = LabelFrame(main_frame,text="Calculate PPI base on Resolution, Screen size and Zoom level"
                                        , borderwidth=4, font=font_header)
        self.gui_dpi_frame.grid(row=3, column=1, sticky="WNE")
        self.gui_dpi_frame.configure(padx=0, pady=10)
        #self.gui_dpi_frame.configure(background='#aabbaa')

        self.dpi_screen_width = StringVar()
        self.dpi_screen_height = StringVar()
        self.dpi_screen_size = StringVar()
        self.dpi_screen_zoom = StringVar()

        self.dpi_result = StringVar()

        self.label_width = Label(self.gui_dpi_frame, font=font_label_input, text="Screen Width")
        self.label_width.grid(row=2, column=0, sticky="W", padx=10)
        self.entry_width = Entry(self.gui_dpi_frame, width=width_input, font=font_input, textvariable=self.dpi_screen_width)
        self.entry_width.grid(row=3, column=0, sticky="W", padx=10)

        self.label_height = Label(self.gui_dpi_frame, font=font_label_input, text="Screen Height")
        self.label_height.grid(row=2, column=1, sticky="W", padx=10)
        self.entry_height = Entry(self.gui_dpi_frame, width=width_input, font=font_input, textvariable=self.dpi_screen_height)
        self.entry_height.grid(row=3, column=1, sticky="W", padx=10)

        self.label_size = Label(self.gui_dpi_frame, font=font_label_input, text="Screen Size")
        self.label_size.grid(row=2, column=2, sticky="W", padx=10)
        self.entry_size = Entry(self.gui_dpi_frame, width=width_input, font=font_input, textvariable=self.dpi_screen_size)
        self.entry_size.grid(row=3, column=2, sticky="W", padx=10)

        self.label_zoom = Label(self.gui_dpi_frame, font=font_label_input, text="Zoom Level")
        self.label_zoom.grid(row=2, column=3, sticky="W", padx=10)
        self.entry_zoom = Entry(self.gui_dpi_frame, width=width_input, font=font_input, textvariable=self.dpi_screen_zoom)
        self.entry_zoom.grid(row=3, column=3, sticky="W", padx=10)

        self.entry_dpi_submit = Button(self.gui_dpi_frame, width=width_input, height=1, font=font_submit,
                                   text="Submit", command=self.screen_dpi_command)
        self.entry_dpi_submit.grid(row=3, column=4, sticky="W", padx=10)

        self.label_dpi_result = Label(self.gui_dpi_frame, font=font_result, textvariable=self.dpi_result)
        self.label_dpi_result.grid(row=4, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        self.demo_dpi()

        # -------empty frame -----------------
        self.gui_empty_frame3 = Frame(main_frame, height=20)
        self.gui_empty_frame3.grid(row=4, column=1)

        # --------size-----------------------
        self.gui_size_frame = LabelFrame(main_frame,text="Calculate Screen size base on Resolution and PPI"
                                        , borderwidth=4, font=font_header)
        self.gui_size_frame.grid(row=5, column=1, sticky="WNE")
        self.gui_size_frame.configure(padx=0, pady=10)

        self.size_screen_width = StringVar()
        self.size_screen_height = StringVar()
        self.size_screen_ppi = StringVar()

        self.size_result = StringVar()

        self.size_label_width = Label(self.gui_size_frame, font=font_label_input, text="Screen Width")
        self.size_label_width.grid(row=2, column=0, sticky="W", padx=10)
        self.size_entry_width = Entry(self.gui_size_frame, width=width_input, font=font_input,
                                 textvariable=self.size_screen_width)
        self.size_entry_width.grid(row=3, column=0, sticky="W", padx=10)

        self.size_label_height = Label(self.gui_size_frame, font=font_label_input, text="Screen Height")
        self.size_label_height.grid(row=2, column=1, sticky="W", padx=10)
        self.size_entry_height = Entry(self.gui_size_frame, width=width_input, font=font_input,
                                  textvariable=self.size_screen_height)
        self.size_entry_height.grid(row=3, column=1, sticky="W", padx=10)

        self.size_label_ppi = Label(self.gui_size_frame, font=font_label_input, text="Screen PPI")
        self.size_label_ppi.grid(row=2, column=2, sticky="W", padx=10)
        self.size_entry_ppi = Entry(self.gui_size_frame, width=width_input, font=font_input,
                                textvariable=self.size_screen_ppi)
        self.size_entry_ppi.grid(row=3, column=2, sticky="W", padx=10)



        self.entry_size_submit = Button(self.gui_size_frame, width=width_input, height=1, font=font_submit,
                                       text="Submit", command=self.screen_size_command)
        self.entry_size_submit.grid(row=3, column=4, sticky="W", padx=10)

        self.label_size_result = Label(self.gui_size_frame, font=font_result, textvariable=self.size_result)
        self.label_size_result.grid(row=4, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        self.demo_size()

    def demo_size(self):
        width = int(1920)
        height = int(1080)
        ppi = float(141)

        self.size_screen_width.set(width)
        self.size_screen_height.set(height)
        self.size_screen_ppi.set(ppi)

        ppi = PPI(width, height, ppi)
        size_human = "%.1f" % ppi.get_ppi()
        result = "Screen Size:\t{}".format(size_human)
        self.size_result.set(result)

    def screen_size_command(self):
        try:
            width = int(self.size_screen_width.get())
            height = int(self.size_screen_height.get())
            ppi = float(self.size_screen_ppi.get())

            ppi = PPI(width, height, ppi)
            size_human = "%.1f" % ppi.get_ppi()
            result = "Screen Size:\t{}".format(size_human)
            self.size_result.set(result)
        except:
            self.size_result.set("Error: Invalid input.")



    def demo_dpi(self):

        width = int(3840)
        height = int(2160)
        size = float(15.6)
        zoom = int(2)

        self.dpi_screen_width.set(width)
        self.dpi_screen_height.set(height)
        self.dpi_screen_size.set(size)
        self.dpi_screen_zoom.set(zoom)

        ppi = PPI(width, height, size,zoom)
        ppi_human = "%.2f" % ppi.get_ppi()
        effective_resolution = ppi.get_effective_resolution()
        result = "PPI: {}".format(ppi_human) + "\t Effective Resolution: " + effective_resolution
        self.dpi_result.set(result)

    def screen_dpi_command(self):

        try:
            width = int(self.dpi_screen_width.get())
            height = int(self.dpi_screen_height.get())
            size = float(self.dpi_screen_size.get())
            zoom = float(self.dpi_screen_zoom.get())

            ppi = PPI(width, height, size, zoom)
            ppi_human = "%.2f" % ppi.get_ppi()
            effective_resolution = ppi.get_effective_resolution()
            result = "PPI: {}".format(ppi_human) + "\t Effective Resolution: " + effective_resolution
            self.dpi_result.set(result)
        except:
            self.dpi_result.set("Error: Invalid input.")

    def demo_side(self):
        self.side_screen_size.set(15.6)
        self.side_screen_ppi.set(141)
        self.side_screen_ratiox.set(16)
        self.side_screen_ratioy.set(9)
        demo = Resolution(15.6, 141.2, 16, 9)
        result= "Width: " + str( demo.get_width_pixels()) + " Pixels\t Height: " + str( demo.get_height_pixels())+" Pixels."
        self.side_result.set( result )

    def side_command(self):

        try:
            test = Resolution(
                self.side_screen_size.get(),
                self.side_screen_ppi.get(),
                self.side_screen_ratiox.get(),
                self.side_screen_ratioy.get()
            )
            result = "Width: " + str(test.get_width_pixels()) + " Pixels\t Height: " + str(
                test.get_height_pixels()) + " Pixels."
            self.side_result.set(result)
        except:
            self.side_result.set("Error: Invalid input.")


    #def quit_sofware(self, main_form):
    #    main_form.quit()

    def quit(self, event):
        #print("quitting...")
        sys.exit(0)

    def about_command(self):



        self.about_window = Toplevel()
        self.about_window.geometry("480x480")
        self.about_window.resizable(0, 0)
        self.about_window.title("About")

        self.about_window.grid_rowconfigure(0, weight=0)
        self.about_window.grid_rowconfigure(1, weight=1)
        self.about_window.grid_rowconfigure(2, weight=1)
        self.about_window.grid_rowconfigure(3, weight=1)
        self.about_window.grid_rowconfigure(4, weight=1)
        self.about_window.grid_rowconfigure(5, weight=1)
        self.about_window.grid_columnconfigure(0, weight=1)

        self.ROOT_DIR = os.path.dirname(__file__)
        self.bannerabout = PhotoImage(file=self.ROOT_DIR + '/banner480x160.png')


        self.about_link_doc = Label(self.about_window, image=self.bannerabout, width=480, height=160)
        self.about_link_doc.grid(row=0, column=0, sticky="")
        self.about_link_doc.configure(padx=10, pady=10)

        #self.about_link_doc = Label(self.about_window, text="Custom Screen Resolution version 1.5.0" )
        #self.about_link_doc.grid(row=0, column=0, sticky="WN")
        #self.about_link_doc.configure(padx=10, pady=10)

        self.about_text = "" \
                "Custom Screen Resolution version "+ str(__version__) +"  \r\r" \
                "This software helps to solve screen size and PPI problem with high PPI displays.\r\r" \
                "This program is free software under GPL V3 \r\r" \
                "Copyright (C) 2020  anopensourcecoder" \

        self.about_messagearea = Message(self.about_window, width=460, text = self.about_text)

        self.about_messagearea.grid(row=1, column=0,sticky="WN")
        self.about_messagearea.configure(padx=10, pady=10)

        self.about_link_doc = Label(self.about_window, text="Read Custom Screen Resolution’s document", fg="blue", cursor="hand2")
        self.about_link_doc.grid(row=2, column=0, sticky="WN")
        self.about_link_doc.configure(padx=10, pady=10)
        self.about_link_doc.bind("<Button-1>", lambda e: self.link("https://custom-screen-resolution.readthedocs.io/en/latest/"))

        self.about_link_github = Label(self.about_window, text="Visit Custom Screen Resolution on github", fg="blue",
                                    cursor="hand2")
        self.about_link_github.grid(row=3, column=0, sticky="WN")
        self.about_link_github.configure(padx=10, pady=10)
        self.about_link_github.bind("<Button-1>",
                                 lambda e: self.link("https://github.com/anopensourcecoder/custom_screen_resolution"))



        self.about_footer = Button( self.about_window, text="Close", command=lambda arg1=self.about_window: self.close_about_window(arg1))

        self.about_footer.grid(row=4, column=0, sticky="")
        self.about_footer.configure(padx=10, pady=10 )

        self.about_link_doc = Label(self.about_window, text=" ")
        self.about_link_doc.grid(row=5, column=0, sticky="WN")
        self.about_link_doc.configure(padx=10, pady=0)

    def logo_command(self):
        self.about_command()

    def close_about_window(self, about_window):
        about_window.destroy()

    def link(self, url):
        import webbrowser
        webbrowser.open_new(url)


def main( ):
    root = Tk(className='Custom Screen Resolution')
    my_gui = CSR_GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


