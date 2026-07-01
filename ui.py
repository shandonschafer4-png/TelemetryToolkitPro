import customtkinter as ctk


class TelemetryToolkitApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Telemetry Toolkit Pro v1.0")
        self.geometry("1200x800")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.build_ui()

    def build_ui(self):

        # -------------------------
        # Title
        # -------------------------

        title = ctk.CTkLabel(
            self,
            text="Telemetry Toolkit Pro",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(pady=20)

        subtitle = ctk.CTkLabel(
            self,
            text="Professional Telemetry Analysis Toolkit",
            font=("Segoe UI", 16)
        )

        subtitle.pack()

        # -------------------------
        # JSON Textbox
        # -------------------------

        self.json_box = ctk.CTkTextbox(
            self,
            width=1100,
            height=500
        )

        self.json_box.pack(padx=20, pady=20)

        # -------------------------
        # Buttons
        # -------------------------

        button_frame = ctk.CTkFrame(self)

        button_frame.pack(pady=10)

        self.paste_button = ctk.CTkButton(
            button_frame,
            text="Paste JSON"
        )

        self.paste_button.grid(row=0, column=0, padx=10)

        self.open_button = ctk.CTkButton(
            button_frame,
            text="Open JSON"
        )

        self.open_button.grid(row=0, column=1, padx=10)

        self.convert_button = ctk.CTkButton(
            button_frame,
            text="Convert to Excel"
        )

        self.convert_button.grid(row=0, column=2, padx=10)

        self.clear_button = ctk.CTkButton(
            button_frame,
            text="Clear"
        )

        self.clear_button.grid(row=0, column=3, padx=10)

        # -------------------------
        # Status
        # -------------------------

        self.status = ctk.CTkLabel(
            self,
            text="Ready"
        )

        self.status.pack(pady=20)