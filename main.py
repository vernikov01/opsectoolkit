from colorama import Fore
import requests
import time
import subprocess
from src import option1


def main():
    subprocess.call('clear')
    print("\033[H\033[3J", end="")
    time.sleep(0.25)
    banner()
    time.sleep(0.5)
    print(f"{Fore.RED}Choose Between options 1-6 or type: help for more commands{Fore.RESET}\n")
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
        op1 = input(f"{Fore.RED}OpsecToolkit{Fore.RESET}>: ")
        if op1 == '1':
            option1.main()
            main()
        else:
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
    print(f"{Fore.RED}OPTION 1: Fake Name and Username Generator.\n")
    print("OPTION 2: Fake Profile Picture Generator Choose between male or female.\n")
    print(f"OPTION 3: A Fake Address Generator With your Choice of the Selected Region of the World.\n")
    print(f"OPTION 4: A Fake Phone number generator to go with your Identity you Build\n")
    print(f"OPTION 5: A Fake pastebin dox generator that dumps your fake identity to pastebin\n to throw off anyone doing recon on you.\n")
    print(f"OPTION 6: Extra Opsec strengthening advice and resources.\n\n Press Enter to Continue...\n\n")
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
    time.sleep(0.5)
    print(f"\n{Fore.BLUE}Version 1.0.0   A Toolkit to Help Strengthen your OpSec.{Fore.RESET}\n\n")

if __name__ == "__main__":
    main()