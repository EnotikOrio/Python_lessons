#зробити так щоб виведення ігор було по зростпнню ціни або по спаданню ціни вивести всі игри окремоі компанії
class Game:
    def __init__(self, title, genre, price, rating, release_date, developer):
        self.title = title
        self.genre = genre
        self.price = price
        self.rating = rating
        self.release_date = release_date
        self.developer = developer
    def __str__(self):
        return f"{self.title} ({self.genre}): ${self.price} {self.rating}"

class Game_Store:
    def __init__(self, title):
        self.title = title
        self.games = []
    def add_game(self, game):
        self.games.append(game)
    def info_games_for_genre(self, genre):
        return [game.title for game in self.games if game.genre == genre]
    def games_by_price(self, ascending=True):
        return sorted(self.games, key=lambda game: game.price, reverse=not ascending)
    def games_by_developer(self, developer):
        return [game for game in self.games if game.developer == developer]

game_store = Game_Store('EnoStore')    
game_store.add_game(Game("Half-Life 2", "Action", 29.99, 10, "2004", "Valve"))
game_store.add_game(Game("Counter-Strike: Global Offensive", "FPS", 14.99, 9, "2012", "Valve"))
game_store.add_game(Game("Portal 2", "Puzzle", 19.99, 8, "2011", "Valve"))

action_games = game_store.info_games_for_genre('Action')
min_price = game_store.minimal_price_game()

print("Games by ascending price:")
for game in game_store.games_by_price(ascending=True):
    print(game)

print()

print("Games by descending price:")
for game in game_store.games_by_price(ascending=False):
    print(game)

print()

developer_games = game_store.games_by_developer('Valve')
print("Games by Valve:")
for game in developer_games:
    print(game)
