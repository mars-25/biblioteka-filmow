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
        return f"- {self.tytul} ({self.rok})."
    
    def get_movies(self):
        return(BibliotekaFilmow)

    def serch(self):
        self.title

    def generate_views(func):
        #dekorowanie funkcji losowo wybrać element z biblioteki, a następnie
        #dodaje mu losową liczbę od 1 do 100 ilości odtworzeń 
        pass

    def tengen(funkc):
        #funkcja ma uruchomić 10 razy generate views:
        pass

    def top_titles(self):
        #parametr content_type którym wybierasz czy mają być pokazane 
        #filmy czy seriale, wybrana ilość najpopularniejszych
        pass

class Seriale(BibliotekaFilmow):
    def __init__(self, tytul, rok, gatunek, nr_odcinka, nr_sezonu):
        super().__init__(tytul, rok, gatunek)
        self.nr_odcinka = nr_odcinka
        self.nr_sezonu = nr_sezonu 
    
    def __str__(self):
        return f"- {self.tytul} S{self.nr_sezonu:02}E{self.nr_odcinka:02}"
    
    def get_series(self):
        return(Seriale)
    
if __name__ == "__main__":

    new_film = [
        BibliotekaFilmow("Batman", 2021, "triller"),
        BibliotekaFilmow("Sumatra", 2000, "sf"),
        Seriale("Simpsonowie", 1990, "kreskowka", 1, 2),
        Seriale("Moda na sukces", 1900, "popularno-naukowy", 89, 32),
        BibliotekaFilmow("Solaris", 2028, "komedia"),
        Seriale("Miś Koralgol", 2021, "kreskowka", 1, 1),
    ]

    new_film[0].play()
    new_film[1].play()
    new_film[0].play()
    new_film[1].play()

    with open("biblioteka.txt",'w') as write_file:
        write_file.write("lista filmow z rokiem produkcji:\n")
        for film in new_film:
            write_file.write(f"- {film.tytul} {film.rok} {film.gatunek} {film.liczba_odtworzen}\n")

    #tylko do sprawdzania 
    with open("biblioteka.txt", 'r') as read_file:
        for line in read_file.read().splitlines():
            print(line)

    print(f"Wyświetlanie filmu:\n {new_film[1]}")
    print(f"Wyświetlanie info o serialu:\n {new_film[2]}")