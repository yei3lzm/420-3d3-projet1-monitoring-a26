import tkinter as tk
from observer.observer import Observateur

class AffichageCPU(Observateur):

    def __init__(self, fenetre_parent: tk.Tk):

        self.fenetre = fenetre_parent
        self.frame_cpu = tk.LabelFrame(self.fenetre, text="CPU", padx=10, pady=10)
        self.frame_cpu.pack(fill=tk.X, padx=10, pady=5)

        self.label_cpu = tk.Label(self.frame_cpu, text="0%", font=("Arial", 24, "bold"))
        self.label_cpu.pack()

        self.canvas_cpu = tk.Canvas(self.frame_cpu, width=300, height=20, bg="white")
        self.canvas_cpu.pack()

        self.var_80_cpu = tk.Label(self.frame_cpu, text="Avertissement", fg="red" , font=("Arial", 12))
        self.var_80_cpu.pack()

    def actualiser(self, sujet) -> None:
        # À compléter: Récupérez la valeur CPU depuis sujet.get_donnees()
        # À compléter: Mettez à jour le label et la barre
        donnees_metrique = sujet.get_donnees() # obiten les donnees du sujet
        donnees_cpu = donnees_metrique["cpu"] # recupere la valeur du cpu

        self.label_cpu.config(text=f"{donnees_cpu:.1f}%")
        self._dessiner_barre(donnees_cpu)
    def _dessiner_barre(self, valeur: float) -> None:
        # À compléter: 
        # Effacez le canvas
        # Calculez la largeur (300 * valeur / 100)
        # Choisissez la couleur : vert < 50%, orange < 80%, rouge sinon
        # Dessinez le rectangle
        self.label_cpu.config(text=f"{valeur:.1f}%")
        self.canvas_cpu.delete("all")
        largeur_cpu = int(300 * valeur / 100)
        if valeur < 50:
            couleur_cpu = "green"
        elif valeur < 80:
            couleur_cpu = "orange"
        else:
            couleur_cpu = "red"
        self.canvas_cpu.create_rectangle(0, 0, largeur_cpu, 20, fill=couleur_cpu, outline="")
