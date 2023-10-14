from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    korting = prijs - prijs*korting
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro.")

aanbieding_1("aardbei", 4, 0.1)

def inkomsten_totaal(inkomsten,btw):
    btw = btw/100
    totaal = sum(inkomsten)
    bedrag = totaal*btw
    
    return(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")



    
def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return(laagste,hoogste)



def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    bedrag = totaal/aantal
    return(f"De gemiddelde inkomsten van deze week zijn {bedrag} euro.")



def meervoudig(invoer_lijst):
    invoer_lijst = laag_en_hoog(invoer_lijst)
    return(invoer_lijst)



def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer