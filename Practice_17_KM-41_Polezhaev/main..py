from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def main():
 while True:
    print("""--- Меню ---
1. fact
2. exp2
3. exp3
4. root2
5. root3
6. log
7. ln
8. lg
0. Exit""")
    choice = input("Введіть свій вибір: ")
    try:
        if choice == "0":
                print("Вихід з програми")
                break
        elif choice == "1":
                n = int(input("Введіть натуральне число: "))
                print(f"fact = {fact(n)}")
        elif choice == "2":
                x = float(input("Введіть число: "))
                print(f"exp2 = {exp2(x)}")
        elif choice == "3":
                x = float(input("Введіть число: "))
                print(f"exp3 = {exp3(x)}")
        elif choice == "4":
                x = float(input("Введіть додатнє число: "))
                print(f"root2 = {root2(x)}")
        elif choice == "5":
                x = float(input("Введіть число: "))
                print(f"root3 = {root3(x)}")
        elif choice == "6":
                a = float(input("Введіть число a (a > 0 і a != 1): "))
                b = float(input("Введіть число b (b > 0): "))
                print(f"log = {log(a, b)}")
        elif choice == "7":
                b = float(input("Введіть число b (b > 0): "))
                print(f"ln = {ln(b)}")
        elif choice == "8":
                b = float(input("Введіть число b (b > 0): "))
                print(f"lg = {lg(b)}")
        else:
                print("Ви ввели щось не те")
    except Exception as e:
     print(f"помилка: {e}")

if __name__ == "__main__":
    main()