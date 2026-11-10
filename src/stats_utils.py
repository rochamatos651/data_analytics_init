import numpy as np
def analyser_ventes(transactions):
    ventes_valides = [ventes for ventes in transactions if ventes > 0]
    nb_transactions = len(ventes_valides)
    total_ventes = sum(ventes_valides)
    vente_max = max(ventes_valides)
    vente_min = min(ventes_valides)
    moyenne_ventes = np.mean(ventes_valides)
    median_ventes = np.median(ventes_valides)
    ecart_ventes = np.std(ventes_valides)
    anomalies = [anom for anom in ventes_valides if anom > 2 * moyenne_ventes]
    return {
        "ventes" : ventes_valides, 
        "nb transactions" : nb_transactions, 
        "total ventes" : total_ventes, 
        "vente max" : vente_max, 
        "vente min" : vente_min, 
        "moyenne" : moyenne_ventes, 
        "medianne" : median_ventes, 
        "ecart type" : ecart_ventes, 
        "anomalies" : anomalies
        }
if __name__ == "__main__":
    test = (5,5.5,10,1000,0,2,5000,6,2,0,8,0,50,80,90,500)
    resultats = analyser_ventes(test)
    for cle, valeur in resultats.items():
        print(f"{cle} : {valeur}")
    
