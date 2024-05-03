import random
from colorama import Fore

def generate_fake_phone_number(country_code="1"):
    num_digits = 10
    if country_code == "1":
        num_digits = 10
    elif country_code == "44":  # UK
        num_digits = 10
    elif country_code == "91":  # India
        num_digits = 10

    random_numbers = ''.join(random.choices('0123456789', k=num_digits))

    phone_number = f"+{country_code} {random_numbers}"

    return phone_number

def main():
    country_code = input(f"{Fore.CYAN}Enter country code (e.g., '1' for USA, '44' for UK, '91' for India):{Fore.WHITE} ")
    fake_phone_number = generate_fake_phone_number(country_code)
    print(f"{Fore.RED}Fake Phone Number:{Fore.WHITE}", fake_phone_number)

if __name__ == "__main__":
    main()
