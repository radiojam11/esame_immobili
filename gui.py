#TecnoGeppetto
#
#

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

finestra_form_elemento = ""
finestra_form_nome = ""
finestra_form_cognome = ""
finestra_form_indirizzo = ""
finestra_form_telefono = ""
fin_aggiungi = ""
fin_modifica = ""
fin_cancella = ""


def apri():
    """Richiama dal motore rubrica.py la funzione carica()"""
    # Pulisco la finestra di testo con il comando cancella la finestra di testo
    finestra_app.delete("1.0", tk.END) 
    # Carico la Rubrica dal file
    rubrica_ = rubrica.carica()
    #creo  una stringa che poi invio al Frame di testo costruito per visualizzare il contenuto di Rubrica
    for num, el in enumerate(rubrica_):
        stringa = f"Elem. {num+1} "+ "\t-"+el["nome"] + "\t-"+ el["cognome"]+ "\t-"+ el["indirizzo"] + "\t-"+ "-".join(el["telefono"])+"\n"
        finestra_app.insert(tk.END, stringa)
    window.title(f"TecnoGeppetto Rubrica App")

def handle_click(event):
    """ gestisce l'evento click sul tasto aggiungi a rubrica """
    # leggo il contenuto delle finestre di testo costruite nella finestra Aggiugni e associo il contenuto alle variabili nome cognome eccc
    nome=finestra_form_nome.get()
    cognome=finestra_form_cognome.get()
    indirizzo = finestra_form_indirizzo.get()
    telefono = finestra_form_telefono.get()
    # alla funzione della Rubrica devo passare il telefono come una lista
    # quindi la Creo prima di inviare
    telefono = telefono.split(",")
    # chiamo del "motore" della rubrica la funzione aggiungi e le passo le variabili 
    rubrica.aggiungi(nome=nome,cognome=cognome,indirizzo=indirizzo,telefono=telefono)
    # poi chiamo apri() per aggiornare la visione della Rubrica
    apri()
    #Chiudo la finestra di Aggiungi
    fin_aggiungi.destroy()

def handle_click_modifica(event):
    """ gestisce l'evento click sul tasto Modifica a rubrica """
    # leggo il contenuto delle finestre di testo costruite nella finestra Modifica e 
    # associo il contenuto alle variabili elemento nome cognome eccc
    elemento = finestra_form_elemento.get()
    nome=finestra_form_nome.get()
    cognome=finestra_form_cognome.get()
    indirizzo = finestra_form_indirizzo.get()
    telefono = finestra_form_telefono.get()
    # alla funzione della Rubrica devo passare il telefono come una lista
    # quindi la Creo prima di inviare
    telefono = telefono.split(",")
    # Richiamo da rubrica.py la funzione modifica e le passo le variabili 
    rubrica.modifica(elemento=str(int(elemento)-1), nome=nome,cognome=cognome,indirizzo=indirizzo,telefono=telefono)
    # Richiamo apri() per aggiornare la visione dela rubrica
    apri()
    # Chiudo la Finestra di Modifica
    fin_modifica.destroy()


def handle_click_cancella(event):
    """ gestisce l'evento click sul tasto Modifica a rubrica """
    # leggo il contenuto della finestra di testo costruita nella finestra Cancella e 
    # associo il contenuto alle variabili elemento nome cognome eccc
    elemento = finestra_form_elemento.get()
    # Richiamo da rubrica.py la funzione modifica e le passo le variabili 
    rubrica.cancella(elemento=str(int(elemento)-1))
    # Richiamo apri() per aggiornare la visione dela rubrica
    apri()
    # Chiudo la Finestra di Modifica
    fin_cancella.destroy()

def crea_form_aggiungi(): #ancora non funziona la seconda window va in crash
    """Richiama da rubrica.py la funzione aggiungi()  passa  nome cognome indirizzo  num tel"""
    # dichiaro le variabili globali che altrimenti non vengono riconosciute dalla funzione che intercetta il click (handle_click())
    global finestra_form_nome
    global finestra_form_cognome
    global finestra_form_indirizzo
    global finestra_form_telefono
    global fin_aggiungi 

    # Creo la finestra che contiene un Frame e le Label e le Form di testo
    fin_aggiungi = tk.Tk()
    fin_aggiungi.title(f"Aggingi Rubrica")
    fin_aggiungi.rowconfigure(0, minsize=1, weight=1) #la grandezza della riga
    fin_aggiungi.columnconfigure(1, minsize=10, weight=1) #la colonna del form Aggiungi
    fin_aggiungi.columnconfigure(2, minsize=10, weight=1) #la colonna del campo testo dove viene scritto il contenuto della rubrica
    # Creo le Label e le Form di testo con Entry
    frame_bottoni_f2 = tk.Frame(fin_aggiungi, relief=tk.RAISED, bd=2)
    label_nome = tk.Label(frame_bottoni_f2, text="Digita Nome")
    finestra_form_nome = tk.Entry(frame_bottoni_f2)
    label_cognome = tk.Label(frame_bottoni_f2,text="Digita Cognome")
    finestra_form_cognome = tk.Entry(frame_bottoni_f2)
    label_indirizzo = tk.Label(frame_bottoni_f2,text="Digita Indirizzo")
    finestra_form_indirizzo = tk.Entry(frame_bottoni_f2)
    label_telefono = tk.Label(frame_bottoni_f2,text="Digita Telefono")
    finestra_form_telefono = tk.Entry(frame_bottoni_f2)
    bottone_aggiungi = tk.Button(
        frame_bottoni_f2,
        text="Click per Aggiungere",
        width=25,
        height=3,
        command=apri,
        )
    ### Disegno il form con le variabili per fare la modifica dei dati 
    label_nome.grid(row=0, column=1, padx=5, pady=5) # la istruzione sticky proporziona lo spazio occupato dalla label. vedi
    finestra_form_nome.grid(row=1, column=1,  padx=5, pady=5)
    label_cognome.grid(row=2, column=1, padx=5, pady=5)
    finestra_form_cognome.grid(row=3, column=1, padx=5, pady=5)
    label_indirizzo.grid(row=4, column=1, padx=5, pady=5)
    finestra_form_indirizzo.grid(row=5, column=1, padx=5, pady=5)
    label_telefono.grid(row=6, column=1,  padx=5, pady=5)
    finestra_form_telefono.grid(row=7, column=1,  padx=5, pady=5)
    bottone_aggiungi.grid(row=8, column=1,  padx=5, pady=5)
    frame_bottoni_f2.grid(row=0, column=0, sticky="ns")
    # gestisco il click sul bottone Aggiungi
    bottone_aggiungi.bind("<Button-1>", handle_click)
    
def modifica():
    """Richiama da rubrica.py la funzione modifica()  passa elemento  nome cognome indirizzo  num tel"""
    # dichiaro le variabili globali che altrimenti non vengono riconosciute dalla funzione che intercetta il click (handle_click())
    global finestra_form_elemento
    global finestra_form_nome
    global finestra_form_cognome
    global finestra_form_indirizzo
    global finestra_form_telefono
    global fin_modifica
    # Creo la finestra che contiene un Frame e le Label e le Form di testo
    fin_modifica = tk.Tk()
    fin_modifica.title(f"Modifica Rubrica")
    fin_modifica.rowconfigure(0, minsize=1, weight=1) #la grandezza della riga
    fin_modifica.columnconfigure(1, minsize=10, weight=1) #la colonna del form Aggiungi
    fin_modifica.columnconfigure(2, minsize=10, weight=1) #la colonna del campo testo dove viene scritto il contenuto della rubrica
    # Creo il frame dove disegno le Label e i Frmae Entry ed il bottone Modifica
    frame_bottoni_f2 = tk.Frame(fin_modifica, relief=tk.RAISED, bd=2)
    # Creo le Label e le Form di testo con Entry
    label_elemento = tk.Label(frame_bottoni_f2, text="Digita Elemento da modificare")
    finestra_form_elemento = tk.Entry(frame_bottoni_f2)
    label_nome = tk.Label(frame_bottoni_f2, text="Digita Nome")
    finestra_form_nome = tk.Entry(frame_bottoni_f2)
    label_cognome = tk.Label(frame_bottoni_f2,text="Digita Cognome")
    finestra_form_cognome = tk.Entry(frame_bottoni_f2)
    label_indirizzo = tk.Label(frame_bottoni_f2,text="Digita Indirizzo")
    finestra_form_indirizzo = tk.Entry(frame_bottoni_f2)
    label_telefono = tk.Label(frame_bottoni_f2,text="Digita Telefono")
    finestra_form_telefono = tk.Entry(frame_bottoni_f2)
    bottone_modifica = tk.Button(
        frame_bottoni_f2,
        text="Click per Modificare",
        width=25,
        height=3,
        command=apri,
        )
    ### Disegno il form con le variabili per fare la modifica dei dati 
    label_elemento.grid(row=0, column=1, padx=5, pady=5)  # la istruzione sticky proporziona lo spazio occupato dalla label. vedi
    finestra_form_elemento.grid(row=1, column=1,  padx=5, pady=5)
    label_nome.grid(row=2, column=1, padx=5, pady=5) 
    finestra_form_nome.grid(row=3, column=1,  padx=5, pady=5)
    label_cognome.grid(row=4, column=1, padx=5, pady=5)
    finestra_form_cognome.grid(row=5, column=1, padx=5, pady=5)
    label_indirizzo.grid(row=6, column=1, padx=5, pady=5)
    finestra_form_indirizzo.grid(row=7, column=1, padx=5, pady=5)
    label_telefono.grid(row=8, column=1,  padx=5, pady=5)
    finestra_form_telefono.grid(row=9, column=1,  padx=5, pady=5)
    bottone_modifica.grid(row=10, column=1,  padx=5, pady=5)
    frame_bottoni_f2.grid(row=11, column=0, sticky="ns")
    # gestisco il click sul bottone Aggiungi
    bottone_modifica.bind("<Button-1>", handle_click_modifica)


def cancella():
    """Richiama da rubrica.py la funzione cancella()  passa elemento  da cancellare"""
    # dichiaro le variabili globali che altrimenti non vengono riconosciute dalla funzione che intercetta il click (handle_click())
    global finestra_form_elemento
    global fin_cancella
    # Creo la finestra che contiene un Frame e le Label e le Form di testo
    fin_cancella = tk.Tk()
    fin_cancella.title(f"Cancella da  Rubrica")
    fin_cancella.rowconfigure(0, minsize=1, weight=1) #la grandezza della riga
    fin_cancella.columnconfigure(1, minsize=10, weight=1) #la colonna del form Aggiungi
    fin_cancella.columnconfigure(2, minsize=10, weight=1) #la colonna del campo testo dove viene scritto il contenuto della rubrica
    # Creo il frame dove disegno le Label e i Frmae Entry ed il bottone Modifica
    frame_bottoni_f3 = tk.Frame(fin_cancella, relief=tk.RAISED, bd=2)
    # Creo le Label e le Form di testo con Entry
    label_elemento = tk.Label(frame_bottoni_f3, text="Digita Elemento da Cancellare")
    finestra_form_elemento = tk.Entry(frame_bottoni_f3)
    bottone_cancella = tk.Button(
        frame_bottoni_f3,
        text="Click per Cancellare",
        width=25,
        height=3,
        command=apri,
        )
    ### Disegno il form con le variabili per fare la modifica dei dati 
    label_elemento.grid(row=0, column=1, padx=5, pady=5)  # la istruzione sticky proporziona lo spazio occupato dalla label. vedi
    finestra_form_elemento.grid(row=1, column=1,  padx=5, pady=5)
    frame_bottoni_f3.grid(row=2, column=1, sticky="ns")
    bottone_cancella.grid(row=10, column=1,  padx=5, pady=5)
    bottone_cancella.bind("<Button-1>", handle_click_cancella)



# Creo la finestra principale della Rubrica
window = tk.Tk()
window.title(f"TecnoGeppetto Immobiliare App")
window.rowconfigure(0, minsize=1, weight=1) #la grandezza della prima riga
window.columnconfigure(1, minsize=10, weight=1) #la colonna (1)  del campo testo dove vengono stampate le informazioni
# creo la zona dove scrivero' il contenuto testuale
finestra_app = tk.Text(window)
# Creo il frame dove mettero' i tasti nella finestra principale
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
# definisco  tutti i tasti del menu principale
btn_apri = tk.Button(fr_buttons, text="Apri", command=apri)
btn_aggiungi = tk.Button(fr_buttons, text="Aggiungi", command=crea_form_aggiungi)
btn_modifica = tk.Button(fr_buttons, text="Modifica", command=modifica)
btn_cancella = tk.Button(fr_buttons, text="Cancella", command=cancella)

### costruisco i bottoni principali in un frame nella colonna 0
btn_apri.grid(row=10, column=0, sticky="ew", padx=5, pady=5)
btn_aggiungi.grid(row=1, column=0, sticky="ew", padx=5, pady=5 )
btn_modifica.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_cancella.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky="ns")

###creo la finestra in colonna 1 con il frame testo dove ricevo la rubrica
finestra_app.grid(row=0, column=1, sticky="nsew")

window.mainloop()