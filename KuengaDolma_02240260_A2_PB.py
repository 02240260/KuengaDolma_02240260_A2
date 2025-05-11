# Constants
MAX_POKEDEX_NUMBER = 1025
CARDS_PER_PAGE = 64
ROWS = 8
COLUMNS = 8

# This class stores and manages the Pokémon binder
class PokemonCardBinder:
    def __init__(self):
        # A dictionary to store added cards using Pokedex number as key
        # Each value is a tuple: (page_number, row, col)
        self.cards = {}

    def add_card(self, pokedex_number):
        # Validate number
        if pokedex_number < 1 or pokedex_number > MAX_POKEDEX_NUMBER:
            print("Invalid Pokedex number. Please enter a number between 1 and 1025.")
            return

        if pokedex_number in self.cards:
            print(f"Status: Pokedex #{pokedex_number} already exists in binder.")
            location = self.cards[pokedex_number]
            print(f"Page: {location[0]}, Position: Row {location[1]}, Column {location[2]}")
            return

        # Calculate the zero-based index for the card
        index = pokedex_number - 1

        # Calculate page number
        page_number = index // CARDS_PER_PAGE + 1

        # Position in 8x8 grid
        position_in_page = index % CARDS_PER_PAGE
        row = position_in_page // COLUMNS + 1
        col = position_in_page % COLUMNS + 1

        # Store the card
        self.cards[pokedex_number] = (page_number, row, col)

        print(f"Page: {page_number}")
        print(f"Position: Row {row}, Column {col}")
        print(f"Status: Added Pokedex #{pokedex_number} to binder.")

    def view_binder(self):
        if not self.cards:
            print("The binder is empty.")
        else:
            print("Current Binder Contents:")
            for number in sorted(self.cards):
                page, row, col = self.cards[number]
                print(f"Pokedex #{number}: Page {page}, Position: Row {row}, Column {col}")
        total = len(self.cards)
        percent = (total / MAX_POKEDEX_NUMBER) * 100
        print(f"\nTotal cards in binder: {total}")
        print(f"% completion: {percent:.1f}%")
        if total == MAX_POKEDEX_NUMBER:
            print("You have caught them all!")

    def reset_binder(self):
        print("WARNING: This will delete ALL Pokemon cards from the binder.")
        print("This action cannot be undone.")
        confirmation = input("Type 'CONFIRM' to reset or 'EXIT' to return to the Main Menu: ").strip()
        if confirmation.upper() == "CONFIRM":
            self.cards.clear()
            print("The binder reset was successful! All cards have been removed.")
        else:
            print("Binder reset canceled.")

    def card_count(self):
        return len(self.cards)


# This class manages the menu and user interaction
class PokemonBinderManager:
    def __init__(self):
        self.binder = PokemonCardBinder()

    def display_menu(self):
        print("\nMain Menu:")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")

    def run(self):
        print("Welcome to Pokemon Card Binder Manager!")
        while True:
            self.display_menu()
            choice = input("Select option: ").strip()
            if choice == "1":
                try:
                    pokedex = int(input("Enter Pokedex number: "))
                    self.binder.add_card(pokedex)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == "2":
                self.binder.reset_binder()
            elif choice == "3":
                self.binder.view_binder()
            elif choice == "4":
                print("Thank you for using Pokemon Card Binder Manager!")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 4.")


# Run the program
if __name__ == "__main__":
    manager = PokemonBinderManager()
    manager.run()





