#### Fonctions secondaires
"""stocker dans une liste les valeurs de la suite étaient calculées à la volée"""
# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Permet de construire un graphique. Pour l'utiliser il faut installer Plotly """
    title="Syracuse"+"(n = " + str(lsyr[0]) +")"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x=[i for i in range(len(lsyr))]
    t=Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None


# calcul de la suite de syracuse
def syracuse_l(n):
    l=[]
    """retourne la suite de Syracuse de source n
    Args:
        n (int): la source de la suite
    Returns:
        list: la suite de Syracuse de source n"""
    l.append(n)
    while n != 1:
        if n%2 == 0:
            n = n//2
            l.append(n)
        else:
            n = n*3 +1
            l.append(n)
    return l

# calcul de temps de vol
def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse
    Args:
        l (list): la suite de Syracuse
    Returns:
        int: le temps de vol"""
    n = 0
    for i in range(len(l)):
        if l[i]==1:
            n = i 
            break
    return n

#Calcul altitude maximale
def altitude_maximale(l):
    """Retourne le maximum d'altitude d'une suite de Syracuse
    Args:
        l (list): la suite de Syracuse
    Returns:
        int: altitude maximum """
    return max(l)


# Calcul le temps de vol en altitude
def temps_de_vol_en_altitude(l):
    """retourne temps_de_vol_en_altitude d'une suite de Syracuse
    Args:
        l (list): la suite de Syracuse
    Returns:
        int: le temps de vol en altitude
    """
    n = 0
    for i in range (len(l)):
        if l[i]<l[0]:
            n = i-1
            break
    return n

#### Fonction principale

def main():
    """Retourne la suite de Syracuse de source n
    Retourne le temps de vol d'une suite de Syracuse
    Retourne le temps de vol en altitude d'une suite de Syracuse
    Retourne l'altitude maximale d'une suite de Syracuse"""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
