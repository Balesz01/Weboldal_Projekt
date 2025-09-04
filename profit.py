class Segito():
    def __init__(self, anyag_tipus, hossz, szelesseg, melyseg, tobbi_kiadas, bevetel,):
        self.anyag = nev
        self.hossz = int(kezdes)
        self.szelesseg = int(idotartam)
        self.melyseg = nev
        self.tobbi_kiadas = int(kezdes)
        self.bevetel = int(idotartam)self.anyag = nev
        self.hossz = int(kezdes)
        self.szelesseg = int(idotartam)


def medence_koltseg(anyag_tipus, hossz, szelesseg, melyseg, tobbi_kiadas, bevetel, min_profit, max_ar):
    # Ellenőrizzük, hogy az anyag típus benne van-e a listában
    if anyag_tipus not in material_prices:
        raise ValueError("Ismeretlen anyagtípus")

    # Térfogat számítása
    terfogat = hossz * szelesseg * melyseg 

    # Anyagköltség számítása
    material_cost = material_prices[anyag_tipus] * terfogat

    # Munkabér kiszámítása térfogat alapján
    if terfogat <= 25:
        munkaber = 100000
    elif terfogat <= 50:
        munkaber = 175000
    elif terfogat <= 100:
        munkaber = 300000
    else:
        munkaber = 450000

    # Teljes költség számítása
    total_costs = material_cost + tobbi_kiadas + munkaber
    profit = bevetel - total_costs

    # Az eredmények kerekítése egy tizedesjegyre
    return {
        "material_cost": round(material_cost, 0),
        "total_costs": round(total_costs, 0),
        "profit": round(profit, 0),
        "meets_min_profit": meets_min_profit,
        "within_max_cost": within_max_cost,
        "munkaber": round(munkaber)
    }

material_prices = {
    "beton": 20000,     # Ft/m³
    "muszaki_folia": 15000,
    "acel": 25000
}


# Frissített bemeneti adatok
anyag_tipus = "beton"
hossz = 6  # Medence hossza (m)
szelesseg = 3  # Medence szélessége (m)
melyseg = 1.2  # Medence mélysége (m)
tobbi_kiadas = 100000  # Egyéb költségek
bevetel = 1200000  # Bevétel a medence építésekor

# Kalkuláció futtatása
result = calculate_pool_costs(anyag_tipus, hossz, szelesseg, melyseg, tobbi_kiadas, bevetel,)

# Eredmények kiírása
print("Anyagköltség:", result["material_cost"])
print("Teljes költség:", result["total_costs"])
print("Profit:", result["profit"])
print("A munkabér:", result["munkaber"])
