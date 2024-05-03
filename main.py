from colorama import Fore
import requests
import time
import subprocess
from src import option1, option4, option3


def main():
    subprocess.call('clear')
    print("\033[H\033[3J", end="")
    banner()
    time.sleep(0.25)
    print(f"\n{Fore.RED}Choose Between options{Fore.CYAN} 1-6{Fore.RED} or type: {Fore.CYAN}help {Fore.RED}for more commands{Fore.RESET}\n")
    time.sleep(0.25)
    command = input(f"{Fore.RED}OpsecToolkit{Fore.RESET}>: ")

    if command == 'help':
        subprocess.call('clear')
        help()
    elif command == '1':
        subprocess.call('clear')
        print("\033[H\033[3J", end="")
        banner()
        option1.main()
        print(f"\nPRESS 1 TO REGENERATE NAME AND USERNAME\n PRESS ENTER TO SAVE TO OPSEC TEXT FILE")
        op1 = input(f"{Fore.RED}OpsecToolkit{Fore.WHITE}>: ")
        if op1 == '1':
            option1.main()
            main()
        else:
            main()
    elif command == '2':
        print("Coming Soon...")
        time.sleep(3)
        main()
    elif command == '3':
        subprocess.call('clear')
        print("\033[H\033[3J", end="")
        banner()
        option3.main()
        print(f"\nPRESS ENTER TO RETURN TO MAIN MENU...\n")
        input(f"{Fore.RED}OpsecToolkit{Fore.WHITE}>: ")

        main()

    elif command == '4':
        subprocess.call('clear')
        print("\033[H\033[3J", end="")
        banner()
        option4.main()
        print(f"\nPRESS ENTER TO RETURN TO MAIN MENU...\n")
        input(f"{Fore.RED}OpsecToolkit{Fore.WHITE}>: ")
        main()
    elif command == '5':
        print("Coming Soon...")
        time.sleep(3)
        main()
    elif command == '6':
        print("Coming Soon...")
        time.sleep(3)
        main()
        
        

    




def help():
    print("\033[H\033[3J", end="")
    print(f"""{Fore.RED}                                                                                                                                                     
 _   _  ___    _      ___              ___    _   _  _   _ 
( ) ( )(  _`\ ( )    (  _`\    /'\_/`\(  _`\ ( ) ( )( ) ( )
| |_| || (_(_)| |    | |_) )   |     || (_(_)| `\| || | | |
|  _  ||  _)_ | |  _ | ,__/'   | (_) ||  _)_ | , ` || | | |
| | | || (_( )| |_( )| |       | | | || (_( )| |`\ || (_) |
(_) (_)(____/'(____/'(_)       (_) (_)(____/'(_) (_)(_____) {Fore.RESET}""")
    print("\n")
    print(f"{Fore.RED}OPTION 1: {Fore.CYAN}Fake Name and Username Generator.\n")
    print(f"{Fore.RED}OPTION 2: {Fore.CYAN}Fake Profile Picture Generator Choose between male or female.\n")
    print(f"{Fore.RED}OPTION 3: {Fore.CYAN}A Fake Address Generator With your Choice of the Selected Region of the World.\n")
    print(f"{Fore.RED}OPTION 4: {Fore.CYAN}A Fake Phone number generator to go with your Identity you Build\n")
    print(f"{Fore.RED}OPTION 5: {Fore.CYAN}A Fake pastebin dox generator that dumps your fake identity to pastebin\n to throw off anyone doing recon on you.\n")
    print(f"{Fore.RED}OPTION 6: {Fore.CYAN}Extra Opsec strengthening advice and resources.\n\n{Fore.RED}Press Enter to Continue...\n\n")
    input(f"{Fore.RED}OpsecToolkit{Fore.RESET}>: ")
    main()





def banner():
    print(f"""{Fore.LIGHTCYAN_EX}
                                                                                                                         
                                                                                                               
              ,o888888o.     8 888888888o     d888888o.   8 8888888888       ,o888888o.                        
           . 8888     `88.   8 8888    `88. .`8888:' `88. 8 8888            8888     `88.                      
          ,8 8888       `8b  8 8888     `88 8.`8888.   Y8 8 8888         ,8 8888       `8.                     
          88 8888        `8b 8 8888     ,88 `8.`8888.     8 8888         88 8888                               
          88 8888         88 8 8888.   ,88'  `8.`8888.    8 888888888888 88 8888                               
          88 8888         88 8 888888888P'    `8.`8888.   8 8888         88 8888                               
          88 8888        ,8P 8 8888            `8.`8888.  8 8888         88 8888                               
          `8 8888       ,8P  8 8888        8b   `8.`8888. 8 8888         `8 8888       .8'                     
           ` 8888     ,88'   8 8888        `8b.  ;8.`8888 8 8888            8888     ,88'                      
              `8888888P'     8 8888         `Y8888P ,88P' 8 888888888888     `8888888P'                        
                                                                                                               
  888888 888888888 ,o888888o.         ,o888888o.      8888          8888     ,88'   8888  8888888 8888888888 
        8888    . 8888     `88.    . 8888     `88.    8888          8888    ,88'    8888        8888       
        8888   ,8 8888       `8b  ,8 8888       `8b   8888          8888   ,88'     8888        8888       
        8888   88 8888        `8b 88 8888        `8b  8888          8888  ,88'      8888        8888       
        8888   88 8888         88 88 8888         88  8888          8888 ,88'       8888        8888       
        8888   88 8888         88 88 8888         88  8888          8888 88'        8888        8888       
        8888   88 8888        ,8P 88 8888        ,8P  8888          888888<         8888        8888       
        8888   `8 8888       ,8P  `8 8888       ,8P   8888          8888 `Y8.       8888        8888       
        8888    ` 8888     ,88'    ` 8888     ,88'    8888          8888   `Y8.     8888        8888       
        8888       `8888888P'         `8888888P'      888888888888  8888     `Y8.   8888        8888         
                                                                    
                                                                                                                    """)
    print(f"\n{Fore.LIGHTBLUE_EX}Version 1.0.0   A Toolkit to Help Strengthen your OpSec.{Fore.RESET}\n\n")

if __name__ == "__main__":
    main()
