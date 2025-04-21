class BibliotekaFilmow:
    def __init__(self, tytul, rok, gatunek):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        #zmienna
        self.liczba_odtworzen = 0

    def play(self, step = 1):
        self.liczba_odtworzen += step

    def __str__(self):
        return f"Tytuł: {self.tytul}\nRok wydania: ({self.rok})."


class Seriale(BibliotekaFilmow):
    def __init__(self, tytul, rok, gatunek, nr_odcinka, nr_sezonu):
        super().__init__(tytul, rok, gatunek)
        self.nr_odcinka = nr_odcinka
        self.nr_sezonu = nr_sezonu 
    
    def __str__(self):
        return f"Tytuł: {self.tytul} S{self.nr_sezonu}E{self.nr_odcinka}"
    

new_film = [
    {"tytul": "Batman", "rok": 2021},
    {"tytul": "Sumatra", "rok": 2000}
]

with open("biblioteka.txt",'w') as write_file:
    write_file.write("lista filmow z rokiem produkcji:\n")
    for film in new_film:
        write_file.write(f"- {film['tytul']} ({film['rok']})\n")
 
with open("biblioteka.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)