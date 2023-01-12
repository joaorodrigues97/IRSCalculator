import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

class IRSCalculator(customtkinter.CTk):
    result = 0
    LESS_7479=[0.145, 0.145]
    LESS_11284=[0.21, 0.1669]
    LESS_15992=[0.265, 0.1958]
    LESS_20700=[0.285, 0.2161]
    LESS_26355=[0.35, 0.2448]
    
    def __init__(self):
        super().__init__()

        self.geometry("500x420")
        self.title("IRS Calculator")

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=20, padx= 10, fill="both", expand=True)

        self.entry_irs = customtkinter.CTkEntry(master=self.frame, justify="center", placeholder_text="IRS Mensal")
        self.entry_irs.grid(row=0, column=1, pady=12, padx=10)

        entry_counter = 0
        self.month_entrys = []
        for i in range(4):
            for x in range(3):
                self.month_entrys.append(customtkinter.CTkEntry(master=self.frame, justify="center", placeholder_text=str(entry_counter+1)+"º Mês"))
                self.month_entrys[entry_counter].grid(row=i+1, column=x, pady=12, padx=10)
                entry_counter+=1

        self.month_entrys.append(customtkinter.CTkEntry(master=self.frame, justify="center", placeholder_text="13º Mês"))
        self.month_entrys[12].grid(row=5, column=0, pady=5, padx=10)

        self.month_entrys.append(customtkinter.CTkEntry(master=self.frame, justify="center", placeholder_text="14º Mês"))
        self.month_entrys[13].grid(row=5, column=2, pady=5, padx=10)
        
        self.label_result = customtkinter.CTkLabel(master=self.frame, text=str(self.result))
        self.label_result.grid(row=5, column=1, pady=5, padx=10)

        button_layout = customtkinter.CTkButton(master=self, text="Todos Iguais", command=self.all_equal)
        button_layout.pack(pady=5, padx=10)

        calculate_btn = customtkinter.CTkButton(master=self, text="Calcular", command=self.calculate)
        calculate_btn.pack(pady=5, padx=10)

    def calculate(self):
        self.result = 0
        for i in self.month_entrys:
            if len(i.get()) != 0:
                self.result+=int(i.get())
            else:
                self.popupmsg("Todos os meses devem estar preenchidos!")
                return
        print(self.result)
        deducoes = self.result - 4104
        parte_1 = 0
        parte_2 = 0
        if deducoes <= 7479:
            particionamento = deducoes * self.LESS_7479[0]
        elif deducoes <= 11284:
            particionamento = deducoes - 7479
            parte_1 = 7479 * self.LESS_7479[1]
            parte_2 = particionamento * self.LESS_11284[0]
        elif deducoes <= 15992:
            particionamento = deducoes - 11284
            parte_1 = 11284 * self.LESS_11284[1]
            parte_2 = particionamento * self.LESS_15992[0]
        elif deducoes <= 20700:
            particionamento = deducoes - 15992
            parte_1 = 15992 * self.LESS_15992[1]
            parte_2 = particionamento * self.LESS_20700[0]
        elif deducoes <= 26355:
            particionamento = deducoes - 20700
            parte_1 = 20700 * self.LESS_20700[1]
            parte_2 = particionamento * self.LESS_26355[0]

        if len(self.entry_irs.get()) == 0:
            self.popupmsg("IRS Mensal deve ser um valor válido!")

        self.result = (parte_1 + parte_2) - (int(self.entry_irs.get())*14)
        self.label_result.configure(text=str(round(abs(self.result),2))+"€")

    def all_equal(self):
        value = self.month_entrys[0].get()
        self.month_entrys[0].delete(0, "end")
        for i in self.month_entrys:
            i.delete(0, "end")
            i.insert(0, value)

    def popupmsg(self, msg):
        popup = customtkinter.CTk()
        popup.geometry("300x100")
        popup.wm_title("!")
        label = customtkinter.CTkLabel(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = customtkinter.CTkButton(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

if __name__ == "__main__":
    app = IRSCalculator()
    app.mainloop()


