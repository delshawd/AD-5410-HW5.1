import requests
import os
from dotenv import load_dotenv

load_dotenv()

FILM_LIST_PATH = "http://api.themoviedb.org/3/discover/movie"
RELEASE_DATE = "2016-01-01"

API_KEY = os.getenv("API_KEY")


def get_film_list(actor_id):
    params = {
        "api_key": API_KEY,
        "with_people": actor_id,
        "primary_release_date.gte": RELEASE_DATE
    }

    r = requests.get(url=FILM_LIST_PATH, params=params)
    data = r.json()

    return data


def data_to_set(data):
    film_set = set()

    for res in data["results"]:
        film_set.add(res["title"])

    return film_set

def main():

    print("To find an actor ID:")
    print("1. Go to https://www.themoviedb.org/")
    print("2. Search for the actor.")
    print("3. Open the actor's page.")
    print("4. The actor ID is the number in the URL.")

    actor1_id = input("Enter the first actor ID: ")
    actor2_id = input("Enter the second actor ID: ")

    actor1_data = get_film_list(actor1_id)
    actor2_data = get_film_list(actor2_id)

    actor1_films = data_to_set(actor1_data)
    actor2_films = data_to_set(actor2_data)

    films_in_common = actor1_films.intersection(actor2_films)

    if len(films_in_common) > 0:
        for film in films_in_common:
            print(film)
    else:
        print("No current films in common")

if __name__ == "__main__":
    main()