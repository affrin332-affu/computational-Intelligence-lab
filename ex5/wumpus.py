class WumpusWorld:
    def __init__(self, size):
        self.size = size

        self.agent = None
        self.wumpus = None
        self.gold = None
        self.pits = set()

        self.wumpus_alive = True
        self.arrow_available = True

        self.bump = "None"
        self.scream = "None"

        self.print_empty_grid()
        self.configure_environment()


    def print_empty_grid(self):
        print("\n===== INITIAL EMPTY GRID =====\n")
        for r in range(self.size, 0, -1):
            print(" ".join(["."] * self.size))


    def configure_environment(self):
        print("\n===== ENTER ENVIRONMENT DETAILS =====")

        ar, ac = map(int, input("Enter Agent start location (row col): ").split())
        self.agent = (ar, ac)

        wr, wc = map(int, input("Enter Wumpus location (row col): ").split())
        gr, gc = map(int, input("Enter Gold location (row col): ").split())

        self.wumpus = (wr, wc)
        self.gold = (gr, gc)

        num_pits = int(input("Enter number of pits: "))
        for i in range(num_pits):
            pr, pc = map(int, input(f"Enter Pit {i+1} location (row col): ").split())
            self.pits.add((pr, pc))

        self.print_grid()


    def print_grid(self):
        print("\n===== CURRENT(Environment) GRID =====\n")
        for r in range(self.size, 0, -1):
            row = []
            for c in range(1, self.size + 1):
                if (r, c) == self.agent:
                    row.append("A")
                else:
                    row.append(".")
            print(" ".join(row))


    def is_valid(self, pos):
        r, c = pos
        return 1 <= r <= self.size and 1 <= c <= self.size


    def get_safe_moves(self):
        r, c = self.agent
        directions = {
            "up": (r+1, c),
            "down": (r-1, c),
            "left": (r, c-1),
            "right": (r, c+1)
        }

        safe = []

        for move, pos in directions.items():
            if self.is_valid(pos):
                if pos not in self.pits and (pos != self.wumpus or not self.wumpus_alive):
                    safe.append(move)

        return safe


    def percept(self):
        r, c = self.agent

        stench = "None"
        breeze = "None"
        glitter = "None"

        adjacent = [
            (r+1, c),
            (r-1, c),
            (r, c+1),
            (r, c-1)
        ]

        for cell in adjacent:
            if self.is_valid(cell):
                if cell == self.wumpus and self.wumpus_alive:
                    stench = "Stench"
                if cell in self.pits:
                    breeze = "Breeze"
                if cell == self.gold:
                    glitter = "Glitter"

        if self.agent == self.gold:
            glitter = "Glitter"

        print(f"\nAgent at {self.agent}")
        print(f"Percepts: [Stench={stench}, Breeze={breeze}, Glitter={glitter}, Bump={self.bump}, Scream={self.scream}]")

        self.bump = "None"
        self.scream = "None"


    def move(self, direction):
        r, c = self.agent
        nr, nc = r, c

        if direction == "up":
            nr += 1
        elif direction == "down":
            nr -= 1
        elif direction == "right":
            nc += 1
        elif direction == "left":
            nc -= 1

        if not self.is_valid((nr, nc)):
            self.bump = "Bump"
            self.percept()
            return True

        self.agent = (nr, nc)
        self.print_grid()

        if self.agent == self.wumpus and self.wumpus_alive:
            print("Agent eaten by WUMPUS. GAME OVER.")
            return False

        if self.agent in self.pits:
            print("Agent fell into PIT. GAME OVER.")
            return False

        self.percept()
        return True

    def shoot(self, direction):
        if not self.arrow_available:
            print("No arrows left!")
            return

        self.arrow_available = False

        r, c = self.agent

        while True:
            if direction == "up":
                r += 1
            elif direction == "down":
                r -= 1
            elif direction == "right":
                c += 1
            elif direction == "left":
                c -= 1

            if not self.is_valid((r, c)):
                break

            if (r, c) == self.wumpus and self.wumpus_alive:
                self.wumpus_alive = False
                self.scream = "Scream"
                break

        self.percept()


    def play(self):
        self.percept()

        while True:
            safe_moves = self.get_safe_moves()
            print("\nSafe moves:", ", ".join(safe_moves))

            action = input("Enter action (up/down/left/right/grab/shoot): ").lower()

            if action in ["up", "down", "left", "right"]:
                if not self.move(action):
                    break

            elif action.startswith("shoot"):
                parts = action.split()
                if len(parts) == 2 and parts[1] in ["up", "down", "left", "right"]:
                    self.shoot(parts[1])
                else:
                    print("Invalid shoot command! Use: shoot up")

            elif action == "grab":
                if self.agent == self.gold:
                    print("Agent grabbed the GOLD. YOU WIN!")
                    break
                else:
                    print("No gold here.")

            else:
                print("Invalid action!")



if __name__ == "__main__":
    size = int(input("Enter Grid Size: "))
    game = WumpusWorld(size)
    game.play()
