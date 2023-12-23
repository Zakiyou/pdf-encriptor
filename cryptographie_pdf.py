import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFEncryptorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Encryptor")

        # Variables
        self.input_file_path = tk.StringVar()
        self.password_var = tk.StringVar()

        # Interface utilisateur
        self.create_widgets()

    def create_widgets(self):
        # Couleurs personnalisées
        background_color = "#e6f7ff"  # Bleu clair
        button_color = "#4da6ff"      # Bleu

        # Configurer la couleur de fond
        self.master.configure(bg=background_color)

        # Frame pour le choix du fichier
        file_frame = tk.Frame(self.master, bg=background_color)
        file_frame.pack(pady=10)

        tk.Label(file_frame, text="Choisir un fichier PDF :", bg=background_color, font=('Arial', 12)).grid(row=0, column=0, sticky=tk.W)
        tk.Entry(file_frame, textvariable=self.input_file_path, width=40, state="readonly", font=('Arial', 10)).grid(row=0, column=1)
        tk.Button(file_frame, text="Parcourir", command=self.browse_file, bg=button_color, font=('Arial', 10)).grid(row=0, column=2)

        # Frame pour le mot de passe
        password_frame = tk.Frame(self.master, bg=background_color)
        password_frame.pack(pady=10)

        tk.Label(password_frame, text="Mot de passe :", bg=background_color, font=('Arial', 12)).grid(row=0, column=0, sticky=tk.W)
        tk.Entry(password_frame, textvariable=self.password_var, show="*", font=('Arial', 10)).grid(row=0, column=1)

        # Étiquette pour les critères du mot de passe
        password_criteria_label = tk.Label(password_frame, text="Le mot de passe doit contenir au moins 8 caractères, avec des majuscules, des minuscules, des chiffres et des caractères spéciaux.", bg=background_color, font=('Arial', 10), wraplength=400)
        password_criteria_label.grid(row=1, columnspan=2, pady=5)

        # Frame pour les boutons
        button_frame = tk.Frame(self.master, bg=background_color)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Crypter", command=self.encrypt_pdf, bg=button_color, font=('Arial', 12)).grid(row=0, column=0, padx=10)

        # Phrase du développeur
        developer_label = tk.Label(self.master, text="Développé par BABABODI Zakiyou\n(Analyste Programmeur et Data Scientist)\nzakiyoubababodi@gmail.com", bg=background_color, font=('Arial', 10))
        developer_label.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.input_file_path.set(file_path)

    def is_password_strong(self, password):
        # Vérification de la force du mot de passe
        return (
            len(password) >= 8 and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~" for char in password)
        )

    def encrypt_pdf(self):
        input_path = self.input_file_path.get()
        password = self.password_var.get()

        if input_path and password:
            if self.is_password_strong(password):
                # Chiffrer le fichier PDF
                with open(input_path, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    pdf_writer = PyPDF2.PdfWriter()

                    total_pages = len(pdf_reader.pages)
                    for page_num in range(total_pages):
                        page = pdf_reader.pages[page_num]
                        pdf_writer.add_page(page)

                    pdf_writer.encrypt(password)

                    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                    if output_path:
                        with open(output_path, 'wb') as encrypted_pdf:
                            pdf_writer.write(encrypted_pdf)
                        tk.messagebox.showinfo("Sauvegardé", "Le fichier crypté a été sauvegardé avec succès.")
            else:
                tk.messagebox.showwarning("Mot de passe faible", "Le mot de passe est trop faible. Assurez-vous qu'il a au moins 8 caractères, avec des majuscules, des minuscules, des chiffres et des caractères spéciaux.")
        else:
            tk.messagebox.showwarning("Attention", "Veuillez choisir un fichier PDF et saisir un mot de passe.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFEncryptorApp(root)
    root.mainloop()
