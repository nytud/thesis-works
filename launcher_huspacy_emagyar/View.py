import customtkinter

from Main import Main


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.model = Main()

        self.title("Launcher_huspacy_emagyar")

        self.button = customtkinter.CTkButton(self, text="Elemzés indítása", command=self.button_launch)
        self.button.grid(row=0, column=0, padx=20, pady=20)

        self.label_launcher_state = customtkinter.CTkLabel(self, text="Launcher kész az indításra")
        self.label_launcher_state.grid(row=1, column=0, padx=20, pady=20)

        self.table = []
        


    def button_launch(self):
        self.label_launcher_state.configure(text="Launcher indul")
        app.update_idletasks()
        self.model.launch()
        self.label_launcher_state.configure(text="Elemzés kész")
        self.create_table()

    def create_table(self):
        tok_frame = customtkinter.CTkFrame(self)
        tok_frame.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.tok_table = self.model.launcher.tok_res
        row = 0
        for t in self.tok_table:
            col = 0
            for cell in t:
                label = customtkinter.CTkLabel(tok_frame, text=cell)
                label.grid(row=row, column=col, padx=20, pady=1)
                col += 1
            row += 1

        morph_frame = customtkinter.CTkFrame(self)
        morph_frame.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="nsw")
        self.morph_table = self.model.launcher.morph_res
        row = 0
        for t in self.morph_table:
            col = 0
            for cell in t:
                label = customtkinter.CTkLabel(morph_frame, text=cell)
                label.grid(row=row, column=col, padx=20, pady=1)
                col += 1
            row += 1









app = App()
app.mainloop()