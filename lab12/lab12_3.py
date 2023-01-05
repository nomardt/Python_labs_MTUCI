from random import randint

def generate_ip(
    first_octet: str = '192',
    second_octet: str = '168',
    third_octet: str = '1'
) -> None:
    fourth_octet = randint(1, 254)
    print(f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}")

if __name__ == '__main__':
    generate_ip()
    generate_ip(first_octet='10', second_octet='0', third_octet='0')