from models.metrics import MetriquesSysteme
from observer.cpu_display import AffichageCPU
import tkinter as tk

metriques = MetriquesSysteme()
root = tk.Tk()
cpu = AffichageCPU(root)
metriques.abonner(cpu)

def rafraichir():
    metriques.actualiser_metriques()
    root.after(2000, rafraichir)

rafraichir()
root.mainloop()