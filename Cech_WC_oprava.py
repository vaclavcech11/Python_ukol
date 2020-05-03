import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Počítač slov, znaků a řádků')
    parser.add_argument("jmeno_textoveho_souboru", help='jmeno souboru, ktery chcete nacist')
    parser.add_argument("--slova", help='pocet slov', action="store_true")
    parser.add_argument("--znaky", help='pocet znaku', action="store_true")
    parser.add_argument("--radky", help='pocet radku', action="store_true")

    arg = parser.parse_args()

    try:
        soubor = open(arg.jmeno_textoveho_souboru)
        text = soubor.read()

        if arg.znaky:
            znaky = len(text)
            print(f"\n{text} \nPočet znaků: [{znaky}]\n")
            soubor.close()

        elif arg.radky:
            radky = len(text.split("\n"))
            print(f"\n{text}\nPočet řádků: [{radky}] \n")
            soubor.close()

        elif arg.slova:
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nPočet slov: [{slova}] \n")
            soubor.close()

        elif arg.slova and arg.znaky:
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nPočet znaků: [{znaky}] , počet slov: [{slova}]\n")
            soubor.close()

        elif arg.radky and arg.slova:
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nPočet slov: [{slova}] , počet řádků: [{radky}] \n")
            soubor.close()

        elif arg.radky and arg.znaky:
            znaky = len(text)
            radky = len(text.split("\n"))
            print(f"\n{text}\nPočet znaků: [{znaky}] , počet řádků: [{radky}] \n")
            soubor.close()

        elif arg.slova and arg.znaky and arg.radky:
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nPočet znaků: [{znaky}] , počet slov:[{slova}], počet řádků: [{radky}]\n")
            soubor.close()

        else:
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nPočet znaků: [{znaky}], počet slov: [{slova}], počet řádků:[{radky}]\n")
            soubor.close()



    except PermissionError:
        print("Chyba")

    except:
        print("Chyba")


if __name__ == '__main__':
    main()