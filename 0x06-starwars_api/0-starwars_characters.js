import sys
import requests

def fetch_movie_characters(movie_id):
    # Base URL for the Star Wars API
    base_url = "https://swapi.dev/api/films/"
    
    # Fetch movie details
    response = requests.get(f"{base_url}{movie_id}/")
    
    if response.status_code != 200:
        print(f"Failed to fetch movie with ID {movie_id}")
        return
    
    movie_data = response.json()
    
    # Iterate over the list of character URLs
    for character_url in movie_data['characters']:
        character_response = requests.get(character_url)
        
        if character_response.status_code != 200:
            print(f"Failed to fetch character details from {character_url}")
            continue
        
        character_data = character_response.json()
        print(character_data['name'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <Movie ID>")
        sys.exit(1)
    
    movie_id = sys.argv[1]
    fetch_movie_characters(movie_id)

