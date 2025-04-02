import customtkinter

from Main import Main


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.model = None

        self.title("Launcher_huspacy_emagyar")

        self.args = ["./ezegyteszt.txt"]

        self.button = customtkinter.CTkButton(self, text="Elemzés indítása", command=self.button_launch)
        self.button.grid(row=0, column=0, padx=20, pady=20)

        self.label_launcher_state = customtkinter.CTkLabel(self, text="Launcher kész az indításra")
        self.label_launcher_state.grid(row=1, column=0, padx=20, pady=20)

        self.frame_checkbox = customtkinter.CTkFrame(self)
        self.frame_checkbox.grid(row=0, rowspan=2, column=1, padx=20, pady=20)

        self.checkbox_huspacy = customtkinter.CTkCheckBox(self.frame_checkbox, text="HuSpaCy", command=self.huspacy)
        self.checkbox_huspacy.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.checkbox_emagyar = customtkinter.CTkCheckBox(self.frame_checkbox, text="e-magyar", command=self.emagyar)
        self.checkbox_emagyar.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        self.checkbox_tok = customtkinter.CTkCheckBox(self.frame_checkbox, text="Tokenizálás", command=self.tok)
        self.checkbox_tok.grid(row=2, column=0, padx=20, pady=20, sticky="w")

        self.checkbox_morph = customtkinter.CTkCheckBox(self.frame_checkbox, text="Morfológia", command=self.morph)
        self.checkbox_morph.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        self.checkbox_lem = customtkinter.CTkCheckBox(self.frame_checkbox, text="Lemmatizálás", command=self.lem)
        self.checkbox_lem.grid(row=2, column=2, padx=20, pady=20, sticky="w")

        self.checkbox_pos = customtkinter.CTkCheckBox(self.frame_checkbox, text="Szófaji elemzés", command=self.pos)
        self.checkbox_pos.grid(row=3, column=0, padx=20, pady=20, sticky="w")

        self.checkbox_dep = customtkinter.CTkCheckBox(self.frame_checkbox, text="Függőségi elemzés", command=self.dep)
        self.checkbox_dep.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        self.checkbox_ner = customtkinter.CTkCheckBox(self.frame_checkbox, text="Névelem-felismerés", command=self.ner)
        self.checkbox_ner.grid(row=3, column=2, padx=20, pady=20, sticky="w")
        

        self.table = []
        


    def button_launch(self):
        self.model = Main(self.args)
        self.label_launcher_state.configure(text="Launcher indul, elemzés folyamatban")
        app.update_idletasks()
        self.model.launch()
        self.label_launcher_state.configure(text="Elemzés kész")
        self.create_table()

    def huspacy(self):
        self.args.append("-huspacy")

    def emagyar(self):
        self.args.append("-emagyar")

    def tok(self):
        self.args.append("-tok")

    def morph(self):
        self.args.append("-morph")

    def lem(self):
        self.args.append("-lem")

    def pos(self):
        self.args.append("-pos")

    def dep(self):
        self.args.append("-dep")

    def ner(self):
        self.args.append("-ner")

    def create_table(self):
        whole_frame = customtkinter.CTkScrollableFrame(self, width=1200, height=350)
        whole_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=30, sticky="ew")

        if(self.model.launcher.is_emagyar and self.model.launcher.is_huspacy):
            if(self.model.launcher.tok_comp):
                tok_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                tok_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
                tok_title_label = customtkinter.CTkLabel(tok_frame, text="Tokenizálás:", fg_color="#ed574c", font=("Arial", 20, "bold"), text_color="black")
                
                self.tok_table = self.model.launcher.tok_res
                tok_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(self.tok_table[4]))
                row = 1
                for t in self.tok_table:
                    h = tok_frame.cget("height")
                    tok_frame.configure(height=h + 10)
                    col = 0
                    for cell in t:
                        label = customtkinter.CTkLabel(tok_frame, text=cell)
                        label.grid(row=row, column=col, padx=20, pady=1)
                        col += 1
                    row += 1


            if(self.model.launcher.morph_comp):
                morph_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                morph_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsw")
                self.morph_table = self.model.launcher.morph_res
                morph_title_label = customtkinter.CTkLabel(morph_frame, text="Morfológia:", fg_color="#eda54c", font=("Arial", 20, "bold"), text_color="black")
                morph_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(self.morph_table[4]))
                row = 1
                for t in self.morph_table:
                    h = morph_frame.cget("height")
                    morph_frame.configure(height=h + 10)
                    col = 0
                    for cell in t:
                        label = customtkinter.CTkLabel(morph_frame, text=cell)
                        label.grid(row=row, column=col, padx=20, pady=1)
                        col += 1
                    row += 1
            if(self.model.launcher.lem_comp):
                lem_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                lem_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsw")
                self.lem_table = self.model.launcher.lem_res
                lem_title_label = customtkinter.CTkLabel(lem_frame, text="Lemmatizálás:", fg_color="#e8ed4c", font=("Arial", 20, "bold"), text_color="black")
                lem_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(self.lem_table[4]))
                row = 1
                for t in self.lem_table:
                    h = lem_frame.cget("height")
                    lem_frame.configure(height=h + 10)
                    col = 0
                    for cell in t:
                        label = customtkinter.CTkLabel(lem_frame, text=cell)
                        label.grid(row=row, column=col, padx=20, pady=1)
                        col += 1
                    row += 1
            if(self.model.launcher.pos_comp):
                pos_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                pos_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsw")
                self.pos_table = self.model.launcher.pos_res
                pos_title_label = customtkinter.CTkLabel(pos_frame, text="Szófajok:", fg_color="#6aed4c", font=("Arial", 20, "bold"), text_color="black")
                pos_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(self.pos_table[4]))
                row = 1
                for t in self.pos_table:
                    h = pos_frame.cget("height")
                    pos_frame.configure(height=h + 10)
                    col = 0
                    for cell in t:
                        label = customtkinter.CTkLabel(pos_frame, text=cell)
                        label.grid(row=row, column=col, padx=20, pady=1)
                        col += 1
                    row += 1
            
            if(self.model.launcher.dep_comp):
                dep_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                dep_frame.grid(row=4, column=0, padx=10, pady=10, sticky="nsw")
                self.dep_table = self.model.launcher.dep_res
                dep_title_label = customtkinter.CTkLabel(dep_frame, text="Függőségi elemzés:", fg_color="#4cdded", font=("Arial", 20, "bold"), text_color="black")
                dep_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(self.dep_table[4]))
                row = 1
                for t in self.dep_table:
                    h = dep_frame.cget("height")
                    dep_frame.configure(height=h + 10)
                    col = 0
                    for cell in t:
                        label = customtkinter.CTkLabel(dep_frame, text=cell)
                        label.grid(row=row, column=col, padx=20, pady=1)
                        col += 1
                    row += 1

            if(self.model.launcher.ner_comp):
                ner_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                ner_frame.grid(row=5, column=0, padx=10, pady=10, sticky="nsw")
                self.ner_table = self.model.launcher.ner_res
                ner_title_label = customtkinter.CTkLabel(ner_frame, text="Névelemek:", fg_color="#a24ced", font=("Arial", 20, "bold"), text_color="black")
                ner_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(self.ner_table[4]))
                row = 1
                for t in self.ner_table:
                    h = ner_frame.cget("height")
                    ner_frame.configure(height=h + 10)
                    col = 0
                    for cell in t:
                        label = customtkinter.CTkLabel(ner_frame, text=cell)
                        label.grid(row=row, column=col, padx=20, pady=1)
                        col += 1
                    row += 1









app = App()
app.mainloop()