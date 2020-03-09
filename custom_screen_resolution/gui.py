
try:
    from custom_screen_resolution.resolutions import  PPI, Scale, Height, Resolution
except ModuleNotFoundError:
    from resolutions import  PPI, Scale, Height, Resolution

from tkinter import *

class ResolutionsGUI:


    def __init__(self, main_form):
        print("ResolutionsGUI init")
        font_gui = "Arial 11"
        font_header = "Arial 20"
        font_label_input = "Arial 10"
        font_input = "Arial 16"
        width_input = 7
        font_submit = "Arial 11"
        font_result = "Arial 16"
        main_form.title("Resolutions GUI")
        main_form.geometry("600x600")
        main_form.grid_rowconfigure(0, weight=1)
        main_form.grid_columnconfigure(0, weight=1)

        #root.configure()
        main_frame = Frame(main_form )
        main_frame.grid(row=0, column=0, sticky="NEW")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)


        # menu
        menu_bar = Menu(main_form)
        main_form.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        #file_menu.add_command(font=guifont, label="About")
        #file_menu.add_command(font=guifont, label="Save")
        #file_menu.add_command(font=guifont, label="Settings")
        #file_menu.add_command(font=guifont, label="Import")
        #file_menu.add_command(font=guifont, label="Export")



        file_menu.add_separator()
        file_menu.add_command(font=font_gui, label="Exit", command=lambda arg1=main_form: self.quit_sofware(arg1))
        menu_bar.add_cascade(font=font_gui, label="File", menu=file_menu)



        self.resolution_frame = Frame(main_frame)
        self.resolution_frame.grid(row=0, column=0, sticky="N")
        self.resolution_frame.configure(padx=0, pady=5)

        self.label_header = Label(self.resolution_frame, font=font_header, text="Screen Width and Height Calculator")
        self.label_header.grid(row=0, column=1, columnspan=5, sticky="W",padx=10 ,pady=10)

        self.screen_size = StringVar()
        self.screen_ppi = StringVar()
        self.screen_ratiox = StringVar()
        self.screen_ratioy = StringVar()
        self.result = StringVar()

        self.label_size = Label(self.resolution_frame, font=font_label_input, text="Screen Size" )
        self.label_size.grid(row=2, column=1, sticky="W",padx=10)
        self.entry_size = Entry(self.resolution_frame, width=width_input, font=font_input, textvariable=self.screen_size )
        self.entry_size.grid(row=3, column=1, sticky="N",padx=10)

        self.label_ppi = Label(self.resolution_frame, font=font_label_input, text="Screen PPI")
        self.label_ppi.grid(row=2, column=2, sticky="W",padx=10)
        self.entry_ppi = Entry(self.resolution_frame, width=width_input, font=font_input, textvariable=self.screen_ppi )
        self.entry_ppi.grid(row=3, column=2, sticky="N",padx=10)

        self.label_ratiox = Label(self.resolution_frame, font=font_label_input, text="Ratio X")
        self.label_ratiox.grid(row=2, column=3, sticky="W" ,padx=10)
        self.entry_ratiox = Entry(self.resolution_frame, width=width_input, font=font_input, textvariable=self.screen_ratiox )
        self.entry_ratiox.grid(row=3, column=3, sticky="N" ,padx=10)

        self.label_ratioy = Label(self.resolution_frame, font=font_label_input, text="Ratio Y")
        self.label_ratioy.grid(row=2, column=4, sticky="W" ,padx=10)
        self.entry_ratioy = Entry(self.resolution_frame, width=width_input, font=font_input, textvariable=self.screen_ratioy )
        self.entry_ratioy.grid(row=3, column=4, sticky="N" ,padx=10)

        self.entry_ratioy = Button(self.resolution_frame, width=width_input, height=1,  font=font_submit,
                                   text="Submit", command=self.screen_width_and_height_command)
        self.entry_ratioy.grid(row=3, column=5, sticky="N", padx=10)

        self.label_resolution_result = Label(self.resolution_frame, font=font_result, textvariable=self.result )
        self.label_resolution_result.grid(row=4, column=1, columnspan=5, sticky="W" ,padx=10,pady=10)

        self.demo_resolution()



    def demo_resolution(self):
        self.screen_size.set(15.6)
        self.screen_ppi.set(141)
        self.screen_ratiox.set(16)
        self.screen_ratioy.set(9)
        demo = Resolution(15.6, 141.2, 16, 9)
        result= "Width: " + str( demo.get_width_pixels()) + " Pixels\t Height: " + str( demo.get_height_pixels())+" Pixels."
        self.result.set( result )

    def screen_width_and_height_command(self):

        try:
            test = Resolution(
                self.screen_size.get(),
                self.screen_ppi.get(),
                self.screen_ratiox.get(),
                self.screen_ratioy.get()
            )
            result = "Width: " + str(test.get_width_pixels()) + " Pixels\t Height: " + str(
                test.get_height_pixels()) + " Pixels."
            self.result.set(result)
        except:
            self.result.set("Error: Invalid input.")




    def display_resolution(self):
        pass

    def quit_sofware(self, main_form):
        main_form.quit()



def main( ):
    root = Tk()
    my_gui = ResolutionsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


