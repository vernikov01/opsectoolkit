import random

def main():
    country_code = input("Enter country e.g., '1' for USA\n'2' for UK\n'3' for India\n'4' for Australia\n'5' for Japan\n'6' for China\nInput: ")
    fake_address = generate_fake_address(country_code)
    print("Fake Address:", fake_address)

COUNTRY_CODES = {
    "1": "USA",
    "2": "UK",
    "3": "India",
    "4": "Australia",
    "5": "Japan",
    "6": "China",
    "7": "Germany"

}

def generate_fake_address(country_code="1"):
    
    if country_code == "1":  # USA
        street = f"{random.randint(100, 999)} {random.choice(['Main', 'Oak', 'Maple', 'Cedar'])} St"
        city = random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'])
        state = random.choice(['NY', 'CA', 'IL', 'TX', 'PA'])
        postal_code = f"{random.randint(10000, 99999)}"
    elif country_code == "2":  # UK
        street = f"{random.randint(10, 99)} {random.choice(['High', 'Main', 'Park', 'Church'])} St"
        city = random.choice(['London', 'Manchester', 'Birmingham', 'Liverpool', 'Glasgow'])
        state = ''
        postal_code = f"{random.choice(['SW', 'W', 'E', 'NW', 'SE'])}{random.randint(1, 20)} {random.randint(1, 9)}{random.choice(['AA', 'AB', 'AC'])}"
    elif country_code == "3":  # India
        street = f"{random.choice(['Surya', 'Shivaji', 'Gandhi', 'Nehru'])} {random.choice(['Nagar', 'Colony', 'Street', 'Avenue'])}"
        city = random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Chennai'])
        state = random.choice(['MH', 'DL', 'KA', 'WB', 'TN'])
        postal_code = f"{random.randint(400000, 799999)}"
    elif country_code == "4":  # Australia
        street = f"{random.randint(10, 99)} {random.choice(['King', 'George', 'Queen', 'Elizabeth'])} St"
        city = random.choice(['Sydney, NSW', 'Melbourne, VIC', 'Brisbane, QLD', 'Perth, WA', 'Adelaide, SA'])
        state = random.choice([''])
        postal_code = f"{random.randint(2000, 7999)}"
    elif country_code == "5":  # Japan
        street = f"{random.choice(['Shinjuku', 'Shibuya', 'Ginza', 'Akihabara'])} {random.choice(['1-chome', '2-chome', '3-chome'])}"
        city = random.choice(['Tokyo', 'Osaka', 'Kyoto', 'Yokohama', 'Nagoya'])
        state = ''
        postal_code = f"{random.randint(1000000, 9999999)}"
    elif country_code == "6":  # China
        street = f"{random.choice(['Nan', 'Bei', 'Dong', 'Xi'])} {random.choice(['Lu', 'Jie', 'Dao', 'Hua'])}"
        city = random.choice(['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Tianjin'])
        state = ''
        postal_code = f"{random.randint(100000, 999999)}"
    elif country_code == "7":  # Germany
        street = f"{random.choice(['Haupt', 'Kirch', 'Berg', 'Schul'])}strasse {random.randint(1, 99)}"
        city = random.choice(['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt'])
        state = ''
        postal_code = f"{random.randint(10000, 99999)}"

    address = f"{street}, {city}, {state}, {postal_code}, {COUNTRY_CODES.get(country_code, 'Unknown')}"

    return address

if __name__ == "__main__":
    main()
