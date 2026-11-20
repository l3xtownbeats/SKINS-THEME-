class NeonStageMasterApp(tk.Tk):
    """
    Финальная сборка интерфейса NEON STAGE MANAGER 3.0
    """
    def __init__(self):
        super().__init__()
        self.title("PPGU - POP PUNK GUITAR ULTIMATE (NEON STAGE 3.0)")
        self.geometry("980, 620")
        self.configure(bg="#080a10")

        # 1. Верхняя панель
        self.header = TopHeaderBar(self)
        self.header.pack(fill="x", padx=8, pady=(8, 4))

        # 2. Средняя область: FX Edit + AutoChords + FX Chain
        center_frame = tk.Frame(self, bg="#080a10")
        center_frame.pack(fill="both", expand=True, padx=8, pady=4)

        # Левая часть: Модуль AutoChords
        chord_panel = tk.Frame(center_frame, bg="#101522", padx=10, pady=10, highlightbackground="#20293d", highlightthickness=1)
        chord_panel.pack(side="left", fill="y", padx=(0, 6))
        
        tk.Label(chord_panel, text="AUTOCHORDS", fg="#00d0ff", bg="#101522", font=("Helvetica", 10, "bold")).pack(anchor="w")
        self.fretboard = AutoChordsFretboard(chord_panel)
        self.fretboard.pack(pady=8)

        # Правая часть: FX Edit Модуль
        self.fx_module = FXEditModule(center_frame)
        self.fx_module.pack(side="left", fill="both", expand=True)

        # 3. Нижняя панель: Интерактивная клавиатура
        bottom_frame = tk.Frame(self, bg="#080a10", pady=6)
        bottom_frame.pack(fill="x", padx=8, pady=(0, 8))
        
        self.keyboard = NeonPianoKeyboard(bottom_frame, octaves=4, white_w=22, white_h=85)
        self.keyboard.pack(anchor="center")

if __name__ == "__main__":
    app = NeonStageMasterApp()
    app.mainloop()
