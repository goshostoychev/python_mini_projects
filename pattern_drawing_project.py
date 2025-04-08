# 🖼️ Python Pattern Drawing Project
from colorama import Fore, Style, init

init(autoreset=True)

while True:
    # Step 1: Display a menu to the user
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")
    print("9. Checkerboard")

    # Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7, 9]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: \n"))
    elif choice in [2, 5, 8]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: \n"))

    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        with open("right_angled_triangle.txt", 'w') as triangle:
            for i in range(rows):
                for j in range(i + 1):
                    print(Fore.YELLOW + "*", end=" ")
                    print("*", end=" ", file=triangle)
                print("")
                print("", file=triangle)

    elif choice == 2:  # Square with Hollow Center
        with open("square_hollow_center.txt", 'w') as square:
            for i in range(size):
                for j in range(size):
                    if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                        print(Fore.RED + "*", end="")
                        print("*", end="", file=square)
                    else:
                        print(" ", end="")
                        print(" ", end="", file=square)
                print("")
                print("", file=square)

    elif choice == 3:  # Diamond
        with open("diamond.txt", 'w') as diamond:
            for i in range(1, rows + 1):
                i = i - (rows // 2 + 1)
                if i < 0:
                    i = -i
                print(Fore.BLUE + " " * i + "*" * (rows - i * 2) + " " * i)
                print(" " * i + "*" * (rows - i * 2) + " " * i, file=diamond)

    elif choice == 4:  # Left-angled Triangle
        with open("left_angled_triangle.txt", 'w') as left_angled_triangle:
            for i in range(rows, 0, -1):
                for j in range(1, i + 1):
                    print(Fore.YELLOW + "* ", end="")
                    print("*", end="", file=left_angled_triangle)
                print("\r")
                print("\r", file=left_angled_triangle)

    elif choice == 5:  # Hollow Square
        with open("hollow_square.txt", 'w') as hollow_square:
            for i in range(size):
                for j in range(size):
                    if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                        print(Fore.GREEN + "*", end="")
                        print("*", end="", file=hollow_square)
                    else:
                        print(" ", end="")
                        print(" ", end="", file=hollow_square)
                print("")
                print("", file=hollow_square)

    elif choice == 6:  # Pyramid
        with open("pyramid.txt", 'w') as pyramid:
            for i in range(1, rows + 1):
                # Print leading spaces
                for j in range(rows - i):
                    print(" ", end="")
                    print(" ", end="", file=pyramid)

                # Print asterisks for the current row
                for k in range(1, 2 * i):
                    print(Fore.MAGENTA + "*", end="")
                    print("*", end="", file=pyramid)
                print()
                print(file=pyramid)

    elif choice == 7:  # Reverse Pyramid
        with open("reverse_pyramid.txt", 'w') as reverse_pyramid:
            for i in range(rows, 0, -1):
                for j in range(rows - i):
                    print(" ", end="")
                    print(" ", end="", file=reverse_pyramid)
                for k in range(2 * i - 1):
                    print(Fore.LIGHTGREEN_EX + "*", end="")
                    print("*", end="", file=reverse_pyramid)
                print("")
                print(file=reverse_pyramid)

    elif choice == 8:  # Rectangle with Hollow Center
        with open("hollow_rectangle.txt", 'w') as hollow_rectangle:
            width = int(input("Enter the width of the rectangle: "))
            height = int(input("Enter the height of the rectangle: "))
            for i in range(1, height + 1):
                for j in range(1, width + 1):
                    if (i == 1 or i == height or
                            j == 1 or j == width):
                        print(Fore.LIGHTCYAN_EX + "*", end="")
                        print("*", end="", file=hollow_rectangle)
                    else:
                        print(" ", end="")
                        print(" ", end="", file=hollow_rectangle)
                print("")
                print(file=hollow_rectangle)

    elif choice == 9:  # Checkerboard
        with open("checkerboards.txt", 'w') as checkerboards:
            checkerboard = [
                [0 if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0) else 'X' for j in range(rows)]
                for i in range(rows)]
            for i in checkerboard:
                for j in i:
                    print(Fore.RED + str(j), end=' ')
                    print(j, end=' ', file=checkerboards)
                print("")
                print(file=checkerboards)

    else:
        print(Fore.RED + "❌ Invalid choice! Please restart the program.")

    # Step 5: Optional - Allow the user to restart or exit
    play_again = input("Would you like to restart the program? (y/n)")
    print()
    if play_again.lower() != "y":
        print("Thank you for playing!")
        break