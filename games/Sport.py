"""Clase Sport"""
class Sport:
    """ Clase para representar un deporte """
    def __init__(self, name:str, players:int, league:str): #Contrsuctor de la clase Sport
        self.name = name
        if isinstance(players, int): # Verificamos que sea un entero
            self.players = players
        else:
            self.players = int(players)
        self.league = league
   
    def __str__(self):
        """Metodo para representar la clase como string"""
        return f"Sport(name='{self.name}', players={self.players}, league='{self.league}')"
   
    def to_json(self)->dict:
        """Metodo para representar la clase como diccionario"""
        return {"name":self.name, "players":self.players, "league":self.league}
   
if __name__ == "__main__":
    s = Sport("Soccer", 11, "FIFA")
    print(s)
    print(repr(s))
    print(s.to_json())
    nfl = Sport("Football", 11, "NFL")
    lmp = Sport("Baseball", 9, "LMP")
    mlb = Sport("Baseball", 9, "MLB")
    lmx = Sport("Soccer", 11, "Liga MX")
    nba = Sport("Basketball", 5, "NBA")
    lista_deportes = [nfl, lmp, mlb, lmx, nba, s]
    archivo_deportes = "deportes.txt"
    with open(archivo_deportes, "w") as file:
        for d in lista_deportes:
            file.write(repr(d)+"\n")
    sport_list = []
    with open(archivo_deportes, "r") as file:
        for line in file:
            d = eval(line)
            sport_list.append(d)
    print(sport_list)
    print(sport_list[0].to_json())

    import json
    archivo_deportes_json = "deportes.json"
    with open(archivo_deportes_json, "w") as file:
        for d in lista_deportes:
            json.dump(d.to_json(), file)
            file.write("\n")
    sport_list_json = []
    
           