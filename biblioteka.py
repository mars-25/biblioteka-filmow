import random

class BibliotekaFilmow:
    def __init__(self, tytul, rok, gatunek):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        #zmienna
        self.liczba_odtworzen = 0

    def play(self, step=1):
        self.liczba_odtworzen += step

    def __str__(self):
        return f"- {self.tytul} ({self.rok})."
    
    def get_movies(self, filmy):
        for film in filmy:
            if not isinstance(film, Seriale):
                print(film)

    def serch(self):
        self.title

    
  
    def generate_views(self, biblioteka):
        wybrany_element = random.choice(biblioteka)
        losowa_liczba = random.randint(1,100)
        wybrany_element.play(losowa_liczba)
        print(f"Wybrano: {wybrany_element}\nDodano odtworzenia: {losowa_liczba}")

 
    def tengen(self, biblioteka, ilosc=10):
        for _ in range(ilosc):
            self.generate_views(biblioteka)

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
    
    def get_series(self, filmy):
        for serial in filmy:
            if isinstance(serial, Seriale):
                print(serial)
    
if __name__ == "__main__":

    print("Biblioteka filmów\n")
    new_film = [
        BibliotekaFilmow("Batman", 2021, "triller"),
        BibliotekaFilmow("Sumatra", 2000, "sf"),
        Seriale("Simpsonowie", 1990, "kreskowka", 4, 2),
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
    print(f"\n ","***"*32, "\n")

    print("\nSeriale:")
    new_film.get_series(new_film)

    print("\nFilmy:")
    new_film.get_movies(new_film)

    print("\nGenerowanie widoków:")
    new_film.tengen(new_film)