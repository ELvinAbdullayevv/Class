class Movie:
    def __init__(self, name, director, year, genre, imdb):
        self.name = name
        self.director = director
        self.year = year
        self.genre = genre
        self.imdb = imdb

    def year_info(self):
        try:
            year = int(self.year)
            if year > 2000:
                print("New")
            else:
                print("Old")

        except ValueError:
            print("Please write a integer number")

    def __str__(self):
        return f"({self.name} ({self.year})"

    def rating_info(self):
        try:
            imdb = float(self.imdb)
            if imdb < 6:
                print('E')
            elif 6 <= imdb <= 7:
                print("D")
            elif 7 <= imdb <= 8:
                print("C")
            elif 8 <= imdb <= 9:
                print("B")
            elif 8 <= imdb <= 9:
                print("A")
            else:
                print("the number being from 6 to 10 calculates ")

        except TypeError:
            print("Your input is invalid")


class Series(Movie):
    def __init__(self, name, director, year, genre, imdb, seanum, epnum):
        super().__init__(name, director, year, genre, imdb)
        self.seanum = seanum
        self.epnum = epnum

    def season_number(self):
        try:
            seanum = int(self.seanum)
            if 1 <= seanum <= 3:
                print("Short movie ")
            elif seanum > 3:
                print("Long movie")
            else:
                print("Season number must accept at least 1")
        except ValueError:
            print("Please write integer number")

    def episode_number(self):
        print(self.epnum)


name = input("Enter a movie name ")
director = input("Enter director ")
year = input("Enter number ")
genre = input("Enter genre ")
imdb = input("Enter a number between 6 and 10 ")
seanum = input("Enter season number ")
epnum = input("Enter episode number ")

p1 = Movie(name, director, year, genre, imdb)
p2 = Series(name, director, year, genre, imdb, seanum, epnum)

print(p1)
p1.year_info()
p1.rating_info()

print(p2)
p2.year_info()
p2.rating_info()
p2.season_number()
p2.episode_number()