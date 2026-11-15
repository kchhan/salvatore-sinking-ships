import random

class SinkingShipsGame:
    def __init__(self):
        self.grid_size = 8
        self.water = "🌊"
        self.miss = "🫧"
        self.hit = "💥"
        self.cursor = "🏹"
        
        self.grid = [[self.water for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.ships = [] 
        self.ammo = 30
        self.cursor_x = 0
        self.cursor_y = 0
        self.game_over = False
        self.winner = False

        self.setup_game()

    def setup_game(self):
        ship_sizes = [4, 3, 2]
        for size in ship_sizes:
            placed = False
            while not placed:
                orientation = random.choice(['H', 'V'])
                if orientation == 'H':
                    x = random.randint(0, self.grid_size - size)
                    y = random.randint(0, self.grid_size - 1)
                    coords = [(x + i, y) for i in range(size)]
                else:
                    x = random.randint(0, self.grid_size - 1)
                    y = random.randint(0, self.grid_size - size)
                    coords = [(x, y + i) for i in range(size)]

                if all(self.grid[c[1]][c[0]] == self.water for c in coords):
                    self.ships.append({"coords": coords, "size": size, "sunken": False})
                    placed = True

    def move_cursor(self, dx, dy):
        new_x = self.cursor_x + dx
        new_y = self.cursor_y + dy
        if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size:
            self.cursor_x = new_x
            self.cursor_y = new_y
            return True
        return False

    def shoot(self):
        if self.ammo <= 0:
            return "Out of ammo!"
        
        self.ammo -= 1
        hit_ship = None
        for ship in self.ships:
            if (self.cursor_x, self.cursor_y) in ship["coords"]:
                hit_ship = ship
                break
        
        if hit_ship:
            self.grid[self.cursor_y][self.cursor_x] = self.hit
            if all(self.grid[cy][cx] == self.hit for cx, cy in hit_ship["coords"]):
                hit_ship["sunken"] = True
            return "Kaboom! 💥"
        else:
            self.grid[self.cursor_y][self.cursor_x] = self.miss
            return "Sploosh! 🫧"

    def is_won(self):
        if all(ship["sunken"] for ship in self.ships):
            self.game_over = True
            self.winner = True
            return True
        return False

    def get_sunk_count(self):
        return sum(1 for ship in self.ships if ship["sunken"])

    def get_grid_string(self):
        display = []
        for y in range(self.grid_size):
            row_str = ""
            for x in range(self.grid_size):
                if x == self.cursor_x and y == self.cursor_y:
                    row_str += self.cursor
                else:
                    row_str += self.grid[y][x]
            display.append(row_str)
        return "\n".join(display)

    def get_revealed_grid(self):
        # Create a copy of the current grid
        reveal_grid = [row[:] for row in self.grid]
        # Mark all ship coordinates with a Squid
        for ship in self.ships:
            for x, y in ship["coords"]:
                # Only place squid if the player hasn't already hit/missed it
                if reveal_grid[y][x] == self.water:
                    reveal_grid[y][x] = "🦑"
        
        display = []
        for y in range(self.grid_size):
            row_str = ""
            for x in range(self.grid_size):
                row_str += reveal_grid[y][x]
            display.append(row_str)
        return "\n".join(display)
