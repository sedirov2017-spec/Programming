import requests


def send_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return False


def main():
    url = "https://swapi.dev/api/people/1"
    data = send_request(url)

    name = data["name"]
    height = data["height"]
    mass = data["mass"]
    hair_color = data["hair_color"]

    print(f"Имя: {name}\nРост:{height}\nВес:{mass}\nЦвет волос:{hair_color}")


if __name__ == "__main__":
    main()
