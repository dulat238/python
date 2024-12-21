import requests
import json
import random

class RickAndMortyClient:
    BASE_URL = "https://rickandmortyapi.com/api"

    def get_random_character(self):
        """Получает информацию о случайном персонаже."""
        response = requests.get(f"{self.BASE_URL}/character")
        response_data = json.loads(response.text)

        if response_data.get("results"):
            random_character = random.choice(response_data["results"])
            return random_character
        return None

    def search_characters(self, name):
        """Ищет персонажей по имени."""
        response = requests.get(f"{self.BASE_URL}/character/?name={name}")
        response_data = json.loads(response.text)
        return response_data.get("results", [])

    def get_all_locations(self):
        """Получает список всех локаций."""
        response = requests.get(f"{self.BASE_URL}/location")
        response_data = json.loads(response.text)
        return response_data.get("results", [])

    def search_episodes(self, name):
        """Ищет эпизоды по названию."""
        response = requests.get(f"{self.BASE_URL}/episode/?name={name}")
        response_data = json.loads(response.text)
        return response_data.get("results", [])

client = RickAndMortyClient()

def get_random_character_info():
    random_character = client.get_random_character()
    if random_character:
        print("Случайный персонаж:")
        print(f"Имя: {random_character['name']}")
        print(f"Статус: {random_character['status']}")
        print(f"Раса: {random_character['species']}")
        print(f"Пол: {random_character['gender']}")
        print(f"Место нахождения: {random_character['location']['name']}")
        print(f"Изображение: {random_character['image']}\n") 
    else:
        print("Ошибка: не удалось получить случайного персонажа.\n")

def search_character_by_name():
    character_name = input("Введите имя персонажа для поиска: ")
    characters = client.search_characters(character_name)
    if characters:
        print(f"Персонажи с именем '{character_name}':")
        for char in characters:
            print(f"- {char['name']} (Статус: {char['status']}, Пол: {char['gender']}, Место нахождения: {char['location']['name']})")
    else:
        print(f"Персонажи с именем '{character_name}' не найдены.\n")

def get_all_locations_info():
    locations = client.get_all_locations()
    print("Локации:")
    for location in locations:
        print(f"- {location['name']}")
    print() 

def search_episode_by_name():
    episode_name = input("Введите название эпизода для поиска: ")
    episodes = client.search_episodes(episode_name)
    if episodes:
        print(f"Эпизоды с именем '{episode_name}':")
        for episode in episodes:
            print(f"- {episode['name']} (Эпизод: {episode['episode']})")
    else:
        print(f"Эпизоды с именем '{episode_name}' не найдены.\n")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Получить случайного персонажа")
        print("2. Поиск персонажа по имени")
        print("3. Получить все локации")
        print("4. Поиск эпизодов по названию")
        print("5. Выход")
        
        choice = input("Введите номер действия: ")

        if choice == '1':
            get_random_character_info()
        elif choice == '2':
            search_character_by_name()
        elif choice == '3':
            get_all_locations_info()
        elif choice == '4':
            search_episode_by_name()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: неверный ввод. Пожалуйста, выберите действие от 1 до 5.")

if __name__ == "__main__":
    main()
