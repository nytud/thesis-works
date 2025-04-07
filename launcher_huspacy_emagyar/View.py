import customtkinter
import tkinter
import CTkMessagebox

from Main import Main


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.model = None

        self.title("Launcher_huspacy_emagyar")

        self.args = []

        self.button = customtkinter.CTkButton(self, text="Elemzés indítása", command=self.button_launch)
        self.button.grid(row=0, column=0, padx=20, pady=20)

        self.label_launcher_state = customtkinter.CTkLabel(self, text="Launcher kész az indításra")
        self.label_launcher_state.grid(row=1, column=0, padx=20, pady=20)

        self.frame_checkbox = customtkinter.CTkFrame(self)
        self.frame_checkbox.grid(row=0, rowspan=3, column=1, padx=20, pady=20)

        self.button_filepicker = customtkinter.CTkButton(self, text="Fájl kiválasztása", command=self.file_open)
        self.button_filepicker.grid(row=2, column=0, padx=20, pady=20)

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

        self.checkbox_outh = customtkinter.CTkCheckBox(self.frame_checkbox, text="HuSpaCy nyers kimenete", command=self.outh)
        self.checkbox_outh.grid(row=4, column=0, padx=20, pady=20, sticky="w")

        self.checkbox_oute = customtkinter.CTkCheckBox(self.frame_checkbox, text="e-magyar nyers kimenete", command=self.oute)
        self.checkbox_oute.grid(row=4, column=1, padx=20, pady=20, sticky="w")
        
        self.checkbox_csv = customtkinter.CTkCheckBox(self.frame_checkbox, text="Exportálás csv-be", command=self.csv)
        self.checkbox_csv.grid(row=4, column=2, padx=20, pady=20, sticky="w")


        self.table = []
        


    def button_launch(self):
        try:
            self.model = Main(self.args)
            self.label_launcher_state.configure(text="Launcher indul, elemzés folyamatban")
            #app.update_idletasks()
            self.model.launch()
            self.label_launcher_state.configure(text="Elemzés kész")
            #self.button.configure(state="disabled")
            self.create_table()
            self.restart()
        except Exception as e:
            CTkMessagebox.CTkMessagebox(title="Hiba", message=str(e), icon="cancel")

    def restart(self):
        self.model = None
        self.args = []
        self.checkbox_huspacy.deselect()
        self.checkbox_emagyar.deselect()
        self.checkbox_tok.deselect()
        self.checkbox_morph.deselect()
        self.checkbox_lem.deselect()
        self.checkbox_pos.deselect()
        self.checkbox_dep.deselect()
        self.checkbox_ner.deselect()
        self.checkbox_outh.deselect()
        self.checkbox_oute.deselect()
        self.checkbox_csv.deselect()
        app.update_idletasks()
        

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

    def outh(self):
        self.args.append("-outh")

    def oute(self):
        self.args.append("-oute")

    def file_open(self):
        fnames = tkinter.filedialog.askopenfilenames(filetypes=[("Szövegfájl", "*.txt")])
        for f in list(fnames):
            self.args.append(f)

    def csv(self):
        self.args.append("-csv")


    def create_table(self):
        whole_frame = customtkinter.CTkScrollableFrame(self, width=1200, height=350)
        whole_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=30, sticky="ew")

        table_row = 0 #for placing the mini-frames in the big frame dynamically

        if(self.model.launcher.outh and self.model.launcher.is_huspacy):
            outh_tables = self.model.launcher.outh_print

            for outh_table in outh_tables:
                outh_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                outh_frame.grid(row=table_row, column=0, padx=10, pady=10, sticky="ew")
                outh_title_label = customtkinter.CTkLabel(outh_frame, text="HuSpaCy nyers kimenete:", fg_color="blue1", font=("Arial", 20, "bold"), text_color="black")
                
                
                outh_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(outh_table[0]))
                row = 1
                for t in outh_table:
                    h = outh_frame.cget("height")
                    outh_frame.configure(height=h + 35)
                    col = 0
                    for cell in t:
                        label = customtkinter.CTkLabel(outh_frame, text=cell)
                        label.grid(row=row, column=col, padx=20, pady=1, sticky="w")
                        col += 1
                    row += 1
                table_row += 1

        
        if(self.model.launcher.oute and self.model.launcher.is_emagyar):
            oute_tables = self.model.launcher.oute_print
            
            for oute_table in oute_tables:
                oute_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                oute_frame.grid(row=table_row, column=0, padx=10, pady=10, sticky="ew")
                oute_title_label = customtkinter.CTkLabel(oute_frame, text="e-magyar nyers kimenete:", fg_color="orange", font=("Arial", 20, "bold"), text_color="black", anchor="w")
                
                
                oute_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(oute_table[0]))
                row = 1
                for t in oute_table:
                    h = oute_frame.cget("height")
                    oute_frame.configure(height=h + 35)
                    col = 0
                    for cell in t:
                        label = customtkinter.CTkLabel(oute_frame, text=cell)
                        label.grid(row=row, column=col, padx=20, pady=1, sticky="w")
                        col += 1
                    row += 1
                table_row += 1


        if(self.model.launcher.is_emagyar and self.model.launcher.is_huspacy):
            if(self.model.launcher.tok_comp):
                tok_tables = self.model.launcher.tok_res

                for tok_table in tok_tables:
                    
                    tok_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                    tok_frame.grid(row=table_row, column=0, padx=10, pady=10, sticky="ew")
                    tok_title_label = customtkinter.CTkLabel(tok_frame, text="Tokenizálás:", fg_color="#ed574c", font=("Arial", 20, "bold"), text_color="black")
                    
                    
                    
                    tok_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(tok_table[4]))
                    row = 1
                    for t in tok_table:
                        h = tok_frame.cget("height")
                        tok_frame.configure(height=h + 30)
                        col = 0
                        for cell in t:
                            label = customtkinter.CTkLabel(tok_frame, text=cell)
                            label.grid(row=row, column=col, padx=20, pady=1)
                            col += 1
                        row += 1
                    table_row += 1


            if(self.model.launcher.morph_comp):
                morph_tables = self.model.launcher.morph_res

                for morph_table in morph_tables:
                    morph_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                    morph_frame.grid(row=table_row, column=0, padx=10, pady=10, sticky="nsw")
                    
                    morph_title_label = customtkinter.CTkLabel(morph_frame, text="Morfológia:", fg_color="#eda54c", font=("Arial", 20, "bold"), text_color="black")
                    morph_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(morph_table[4]))
                    row = 1
                    for t in morph_table:
                        h = morph_frame.cget("height")
                        morph_frame.configure(height=h + 30)
                        col = 0
                        for cell in t:
                            label = customtkinter.CTkLabel(morph_frame, text=cell)
                            label.grid(row=row, column=col, padx=20, pady=1)
                            col += 1
                        row += 1
                    table_row += 1


            if(self.model.launcher.lem_comp):
                lem_tables = self.model.launcher.lem_res

                for lem_table in lem_tables:
                    lem_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                    lem_frame.grid(row=table_row, column=0, padx=10, pady=10, sticky="nsw")
                    
                    lem_title_label = customtkinter.CTkLabel(lem_frame, text="Lemmatizálás:", fg_color="#e8ed4c", font=("Arial", 20, "bold"), text_color="black")
                    lem_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(lem_table[4]))
                    row = 1
                    for t in lem_table:
                        h = lem_frame.cget("height")
                        lem_frame.configure(height=h + 30)
                        col = 0
                        for cell in t:
                            label = customtkinter.CTkLabel(lem_frame, text=cell)
                            label.grid(row=row, column=col, padx=20, pady=1)
                            col += 1
                        row += 1
                    table_row += 1


            if(self.model.launcher.pos_comp):
                pos_tables = self.model.launcher.pos_res

                for pos_table in pos_tables:
                    pos_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                    pos_frame.grid(row=table_row, column=0, padx=10, pady=10, sticky="nsw")
                    
                    pos_title_label = customtkinter.CTkLabel(pos_frame, text="Szófajok:", fg_color="#6aed4c", font=("Arial", 20, "bold"), text_color="black")
                    pos_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(pos_table[4]))
                    row = 1
                    for t in pos_table:
                        h = pos_frame.cget("height")
                        pos_frame.configure(height=h + 30)
                        col = 0
                        for cell in t:
                            label = customtkinter.CTkLabel(pos_frame, text=cell)
                            label.grid(row=row, column=col, padx=20, pady=1)
                            col += 1
                        row += 1
                    table_row += 1

            
            if(self.model.launcher.dep_comp):
                dep_tables = self.model.launcher.dep_res

                for dep_table in dep_tables:
                    dep_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                    dep_frame.grid(row=table_row, column=0, padx=10, pady=10, sticky="nsw")
                    
                    dep_title_label = customtkinter.CTkLabel(dep_frame, text="Függőségi elemzés:", fg_color="#4cdded", font=("Arial", 20, "bold"), text_color="black")
                    dep_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(dep_table[4]))
                    row = 1
                    for t in dep_table:
                        h = dep_frame.cget("height")
                        dep_frame.configure(height=h + 30)
                        col = 0
                        for cell in t:
                            label = customtkinter.CTkLabel(dep_frame, text=cell)
                            label.grid(row=row, column=col, padx=20, pady=1)
                            col += 1
                        row += 1
                    table_row += 1


            if(self.model.launcher.ner_comp):
                ner_tables = self.model.launcher.ner_res

                for ner_table in ner_tables:
                    ner_frame = customtkinter.CTkScrollableFrame(whole_frame, width=1200, orientation="horizontal")
                    ner_frame.grid(row=table_row, column=0, padx=10, pady=10, sticky="nsw")
                    
                    ner_title_label = customtkinter.CTkLabel(ner_frame, text="Névelemek:", fg_color="#a24ced", font=("Arial", 20, "bold"), text_color="black")
                    ner_title_label.grid(row=0, padx=10, pady=10, sticky="ew", columnspan=len(ner_table[4]))
                    row = 1
                    for t in ner_table:
                        h = ner_frame.cget("height")
                        ner_frame.configure(height=h + 30)
                        col = 0
                        for cell in t:
                            label = customtkinter.CTkLabel(ner_frame, text=cell)
                            label.grid(row=row, column=col, padx=20, pady=1)
                            col += 1
                        row += 1
                    table_row += 1









app = App()
app.mainloop()