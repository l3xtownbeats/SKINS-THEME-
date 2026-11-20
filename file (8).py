if __name__ == "__main__":
    root = tk.Tk()
    root.title("NEON STAGE 3.0 - UI Components")
    root.configure(bg="#0a0c14")
    root.geometry("640, 420")

    # Контейнер для демонстрации
    frame = tk.Frame(root, bg="#10141f", padx=20, pady=20, highlightbackground="#20283c", highlightthickness=1)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    header = tk.Label(frame, text="FX CHAIN & CONTROLS", fg="#00d0ff", bg="#10141f", font=("Helvetica", 11, "bold"))
    header.pack(anchor="w", pady=(0, 15))

    # Секция кнопок
    btn_box = tk.Frame(frame, bg="#10141f")
    btn_box.pack(anchor="w", pady=5)
    
    comp_btn = NeonFXButton(btn_box, text="COMP", icon_char="∿", active=True)
    comp_btn.pack(side="left", padx=5)

    eq_btn = NeonFXButton(btn_box, text="EQ", icon_char="ılı", active=False)
    eq_btn.pack(side="left", padx=5)

    dist_btn = NeonFXButton(btn_box, text="DIST", icon_char="⚡", active=True)
    dist_btn.pack(side="left", padx=5)

    # Секция переключателя и дисплея
    ctrl_box = tk.Frame(frame, bg="#10141f")
    ctrl_box.pack(anchor="w", pady=15, fill="x")

    toggle = NeonToggle(ctrl_box, state=True)
    toggle.pack(side="left", padx=5)

    disp = CompressorDisplay(ctrl_box, width=240, height=120)
    disp.pack(side="left", padx=20)

    root.mainloop()
