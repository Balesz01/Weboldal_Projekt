class Segito():
    def __init__(self, anyag_tipus, hossz, szelesseg, melyseg, tobbi_kiadas):
        self.anyag_tipus = anyag_tipus
        self.hossz = float(hossz)
        self.szelesseg = float(szelesseg)
        self.melyseg = float(melyseg)
        self.tobbi_kiadas = float(tobbi_kiadas)

    def medence_koltseg(self):
        material_prices = {
            "beton": 20000,
            "muszaki_folia": 15000,
            "acel": 25000
        }

        if self.anyag_tipus not in material_prices:
            raise ValueError("Ismeretlen anyagtípus")

        terfogat = self.hossz * self.szelesseg * self.melyseg 

        if terfogat > 300:
            return None  # Nem folytatja a további számításokat

        material_cost = material_prices[self.anyag_tipus] * terfogat

        if terfogat <= 25:
            munkaber = 100000
        elif terfogat <= 50:
            munkaber = 175000
        elif terfogat <= 100:
            munkaber = 300000
        elif terfogat <= 200:
            munkaber = 600000
        else:  # terfogat <= 300
            munkaber = 1000000

        total_costs = material_cost + self.tobbi_kiadas + munkaber
        bevetel = total_costs * 1.25
        profit = bevetel - total_costs

        return {
            "anyagköltseg": round(material_cost, 0),
            "teljes_koltseg": round(total_costs, 0),
            "bevétel": round(bevetel, 0),
            "profit": round(profit, 0),
            "munkaber": round(munkaber, 0)
        }


result = Segito("beton", 6, 3, 20, 100000).medence_koltseg()

if result is None:
    print("Nem csinálunk 300 m3-nél nagyobb medencéket!")
else:
    print("Anyagköltség:", result["anyagköltseg"])
    print("Teljes költség:", result["teljes_koltseg"])
    print("Bevétel:", result["bevétel"])
    print("Profit:", result["profit"])
    print("A munkabér:", result["munkaber"])
