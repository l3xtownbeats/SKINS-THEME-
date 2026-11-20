class FXEditModule(tk.Frame):
    """
    Полнофункциональный модуль FX EDIT с точной компоновкой макета.
    """
    def __init__(self, parent):
        super().__init__(parent, bg="#101522", padx=12, pady=12, highlightbackground="#00d0ff", highlightthickness=1)
        
        # 1. Заголовок окна (Header Bar)
        header = tk.Frame(self, bg="#101522")
        header.pack(fill="x", pady=(0, 10))
        
        tk.Label(header, text="∿  FX EDIT", fg="#00d0ff", bg="#101522", font=("Helvetica", 11, "bold")).pack(side="left")
        
        close_btn = tk.Label(header, text="✕", fg="#506180", bg="#101522", font=("Helvetica", 10, "bold"), cursor="hand2")
        close_btn.pack(side="right")
        
        # 2. Основная рабочая область (График + Регуляторы + VU-Метры)
        body = tk.Frame(self, bg="#101522")
        body.pack(fill="both", expand=True)

        # Дисплей графика кривой компрессора
        self.display = CompressorDisplay(body, width=220, height=130)
        self.display.pack(side="left", padx=(0, 12))

        # Секция регуляторов параметров (Knobs Grid)
        knobs_frame = tk.Frame(body, bg="#101522")
        knobs_frame.pack(side="left", padx=5)

        # Верхний ряд ручек
        row1 = tk.Frame(knobs_frame, bg="#101522")
        row1.pack(pady=4)
        self._add_knob_group(row1, "Threshold", "-18.0 dB", 40)
        self._add_knob_group(row1, "Ratio", "3.5:1", 60)
        self._add_knob_group(row1, "Attack", "10.0 ms", 25)

        # Нижний ряд ручек
        row2 = tk.Frame(knobs_frame, bg="#101522")
        row2.pack(pady=4)
        self._add_knob_group(row2, "Release", "120 ms", 50)
        self._add_knob_group(row2, "Makeup", "3.0 dB", 30)
        self._add_knob_group(row2, "Mix", "100%", 100)

        # Блок VU-индикаторов
        meters_frame = tk.Frame(body, bg="#101522")
        meters_frame.pack(side="left", padx=(10, 0))
        
        tk.Label(meters_frame, text="GR", fg="#627394", bg="#101522", font=("Helvetica", 7, "bold")).pack()
        self.vu_gr = NeonVUMeter(meters_frame, segments=20, width=12, height=115)
        self.vu_gr.pack(side="left", padx=3)
        self.vu_gr.set_level(0.45)

        self.vu_out = NeonVUMeter(meters_frame, segments=20, width=12, height=115)
        self.vu_out.pack(side="left", padx=3)
        self.vu_out.set_level(0.82)

    def _add_knob_group(self, parent, title, val_text, initial_val):
        box = tk.Frame(parent, bg="#101522", padx=4)
        box.pack(side="left")
        knob = NeonKnob(box, size=46, initial=initial_val)
        knob.pack()
        tk.Label(box, text=title, fg="#8a9ab8", bg="#101522", font=("Helvetica", 7)).pack()
        tk.Label(box, text=val_text, fg="#00d0ff", bg="#101522", font=("Helvetica", 7, "bold")).pack()

if __name__ == "__main__":
    app = tk.Tk()
    app.title("PPGU - NEON STAGE 3.0 CONSOLE")
    app.configure(bg="#080a10")
    
    module = FXEditModule(app)
    module.pack(padx=20, pady=20)
    
    app.mainloop()
