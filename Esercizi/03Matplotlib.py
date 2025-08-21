import pandas as pd
import matplotlib as mp
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta

pokemon = pd.read_csv("FilesDati\\pokemon.csv")

# Primo inizio di grafico
'''
x = [25,26,27,28,29,30]
y = [100,90,120,140,120,150]

plt.plot(x,y)
plt.savefig("figura.png")
plt.show()
'''

# Personalizzare i grafici
# titolo, etichetta, seconda linea, legenda
# griglia, colore, dimensione, stile linea, marcatori e stile grafico

x = [25,26,27,28,29,30]
y1 = [100,90,120,140,120,150]
y2 = [90,80,120,150,170,140]

# Utilizzo delle palette, legenda, titolo, labels, grid
'''
print(plt.style.available)
plt.style.use("seaborn-v0_8-dark-palette")

plt.plot(x,y1, label="italiano", color = "red", linewidth=5, linestyle="--")
plt.plot(x,y2, label="tedeschi", color="#212121", linestyle="dotted", marker="o")
plt.title("Nome del grafico")
plt.xlabel("Età")
plt.ylabel("Importi")
plt.legend()
plt.grid()

plt.show()
'''


# Grafici a barre e a barre affiancate
# Così vengono grafici sovrapposti
'''
plt.bar(x,y1, label="italiano", color = "red")
plt.bar(x,y2, label="tedeschi", color="#212121")
plt.show()
'''

# L'unico modo per fare i grafici non sovrapposti è utilizzare numpy
# Divido le barre a livello visivo
'''
indexes = np.arange(6)      # sostituiamo i valori delle x e y
width = 0.3

plt.bar(indexes,y1, label="italiano", width=width, color = "red")
plt.bar(indexes+width,y2, label="tedeschi", width=width, color="#212121")

plt.xticks(indexes+width/2,x) # Il problema che i ticks non sono al centro. Questo metodo li mette al centro e rinomina i ticks

plt.show()
'''

# Per le barre orizzontale
'''
indexes = np.arange(6)      # sostituiamo i valori delle x e y
w2 = 0.3

plt.barh(indexes,y1, label="italiano", height=w2, color = "red")
plt.barh(indexes+w2,y2, label="tedeschi", height=w2, color="#212121")
plt.xticks(indexes+w2/2,x)

plt.show()
'''


# Grafici a torta (pie chart)
# creare, aggiunta etichette, bordi
# colori, percentuali, explode, startangle
'''
plt.style.use("ggplot")
plt.title("Titolo del grafico")
labels = ['FR','IT','SP','DE']
colors = ['black','green','red','brown']
explode = [0,0.02,0.02,0]
x1 = [10,40,20,20]
plt.pie(x1,
        labels=labels, 
        colors=colors, 
        startangle=70,
        explode=explode,
        autopct='%1.1f%%',                          # percentuali
        wedgeprops={'edgecolor': '#000000'}) # wedgeprops è dizionario con molte chiavi


plt.show()
'''

# Grafici ad Area
# Rifare il plot a linee, riempiere area, alpha
# riempire tra linee e punto, aggiungere condizione
'''
plt.style.use("ggplot")
plt.title("Titolo del grafico")

media = np.mean(y1)
xx = np.array(x)
yy = np.array(y1)

plt.plot(xx,yy)
plt.fill_between(xx,yy,media, where=(yy>110), alpha = 0.2, interpolate=True, color = "blue")

plt.show()
'''

# Istogrammi
# basico con bins, usare bins personalizzati, color, edgecolor, axvline
# Di base fa un conteggio
'''
plt.style.use("ggplot")
plt.title("Titolo del grafico")

x_anni = [13,18,18,22,25,27,29,29,30,35,36,47,40,41,45,45,54,56,65]

# plt.hist(x_anni, bins=6) # diviso in 6 contenitori
bins = [20,30,50,70] 
plt.hist(
    x_anni, 
    bins=bins, # In alternativa posso creare io i bins.
    color='grey',
    edgecolor= 'black')

plt.axvline(27, color='red', linewidth=3)


plt.show()
'''

# Grafico a dispersione (scatter)
# grafico, dimensione punti, colore, marker, edgecolor, linewidth, alpha
# intensita colori come dati, cmap e colorbar, dimensione come dati
''' 
xs = [1,5,6,8,3,2,2,7,9,1]
ys = [8,8,4,6,2,7,1,3,1,7]
colorss = [2,4,6,6,1,9,4,6,2,8]   # Dovrebbero essere da 0 a 9
sizes = [200,250,120,500,430,700,567, 312,691, 443]

plt.scatter(
    x=xs,
    y=ys,
    #s=200,    # S sta per size fissa
    s = sizes,   # size variabile
    # c= 'green',   # Unico colore
    c=colorss,       # Multipli colori
    cmap='Greens',   # Intensità legata ai colori
    #marker='*',
    #edgecolors='red',
    #linewidth=2,
    alpha=0.5
    )

cbar = plt.colorbar()
cbar.set_label("Intensità colori")

plt.style.use("ggplot")
plt.title("Titolo del grafico")



plt.show()
'''

# Come lavorare con le date
# formato data datetime(anno, mese, giorno), creare grafico base
# aggiungere linestyle, rendere date più leggibili, cambiare formato date
'''
xt = [
    datetime(2022,1,10),
    datetime(2022,1,15),
    datetime(2022,1,20),
    datetime(2022,1,25),
    datetime(2022,1,30)
]

yt = [3,6,2,8,5]

date_formattate = mpl_dates.DateFormatter('%d %b %Y')

plt.plot_date(xt,yt, linestyle = 'solid')
plt.gcf().autofmt_xdate()  # get current figure. AutoFormat
plt.gca().xaxis.set_major_formatter(date_formattate) # Get current axies
plt.show()
'''

# Subplot
# 
'''
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
fig, ax = plt.subplots()
plt.style.use('ggplot')

ax1.plot(x,y1)
ax1.set_title('Titolo Grafico')
ax1.set_xlabel('Prova')

ax2.plot(x,y2)
ax2.set_title('Titolo Secondo Grafico')
ax2.set_xlabel('Altra Prova')

ax.plot(x,y1)


plt.show()
'''


