from os import system
system("cls")
from colorama import init, Fore

init(autoreset=True)

board = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"]
]

count = 1
while count <= 9:
    system('cls')
    for i in board:
        print(Fore.RESET + " | ".join(i))

    if count % 2:
        value = int(input(Fore.GREEN + "Ishtirokchi_1: Raqam kiriting: "))
        if value == 1:
            if board[0][0] == "*":
                board[0][0] = "X"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 2:
            if board[0][1] == "*":
                board[0][1] = "X"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 3:
            if board[0][2] == "*":
                board[0][2] = "X"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 4:
            if board[1][0] == "*":
                board[1][0] = "X"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 5:
            if board[1][1] == "*":
                board[1][1] = "X"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 6:
            if board[1][2] == "*":
                board[1][2] = "X"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 7:
            if board[2][0] == "*":
                board[2][0] = "X"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 8:
            if board[2][1] == "*":
                board[2][1] = "X"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 9:
            if board[2][2] == "*":
                board[2][2] = "X"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        else:
            print(Fore.RED + "Noto'g'ri qiymat kiritdingiz!")
            continue

        if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or \
           (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or \
           (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or \
           (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or \
           (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or \
           (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or \
           (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
            print(Fore.LIGHTGREEN_EX + "Birinchi o'yinchi g'olib bo'ldi🥳!")
            break
        count += 1
        continue

    else:
        value = int(input(Fore.GREEN + "Ishtirokchi_2: Raqam kiriting: "))
        if value == 1:
            if board[0][0] == "*":
                board[0][0] = "0"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 2:
            if board[0][1] == "*":
                board[0][1] = "0"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 3:
            if board[0][2] == "*":
                board[0][2] = "0"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 4:
            if board[1][0] == "*":
                board[1][0] = "0"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 5:
            if board[1][1] == "*":
                board[1][1] = "0"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 6:
            if board[1][2] == "*":
                board[1][2] = "0"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 7:
            if board[2][0] == "*":
                board[2][0] = "0"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 8:
            if board[2][1] == "*":
                board[2][1] = "0"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        elif value == 9:
            if board[2][2] == "*":
                board[2][2] = "0"
            else:
                print(Fore.RED + "Bu joy bo'sh emas! Qaytadan kiriting!")
                count -= 1
        else:
            print(Fore.RED + "Noto'g'ri qiymat kiritdingiz!")
            continue

        if (board[0][0] == "0" and board[0][1] == "0" and board[0][2] == "0") or \
           (board[1][0] == "0" and board[1][1] == "0" and board[1][2] == "0") or \
           (board[2][0] == "0" and board[2][1] == "0" and board[2][2] == "0") or \
           (board[0][0] == "0" and board[1][0] == "0" and board[2][0] == "0") or \
           (board[0][0] == "0" and board[1][1] == "0" and board[2][2] == "0") or \
           (board[0][2] == "0" and board[1][2] == "0" and board[2][2] == "0") or \
           (board[0][2] == "0" and board[1][1] == "0" and board[2][0] == "0"):
            print(Fore.LIGHTGREEN_EX + "Ikkinchi o'yinchi g'olib bo'ldi🥳!")
            break
        count += 1
else:
    print(Fore.LIGHTYELLOW_EX +"Durrang!")
