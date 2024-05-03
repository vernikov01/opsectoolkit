def main():
    import random
    import string

    from colorama import Fore
    import subprocess

    first_names = ['Alex', 'Bill', 'Charlie', 'David', 'Ernie']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Jacksons', 'muhummad']

    def generate_username():
        first = random_first_name
        last = random.choice(last_names)
        # Generate a random string of numbers and letters
        random_string = ''.join(random.choices('abcdelmnopqrstuvwxyzAFGIJKLQRSX1234567890_!@?.', k=4))
        # Combine parts to create the username
        username = f"{first.lower()}_{random_string}"
        return username

    random_first_name = random.choice(first_names)
    random_last_name = random.choice(last_names)
    random_username = generate_username()

    print(f"{Fore.CYAN}Random Name: {Fore.WHITE}{random_first_name} {random_last_name}\n")
    print(f"{Fore.CYAN}Random Username: {Fore.WHITE}{random_username}\n")

if __name__ == "__main__":
    main()
