import json
import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint, *, headers=None, params=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            return self.session.get(url, headers=headers, params=params, timeout=15)
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] GET request failed: {e}")
            return None

    def post(
        self,
        endpoint,
        *,
        headers=None,
        json_body=None,
    ):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            return self.session.post(url, headers=headers, json=json_body, timeout=15)
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] POST request failed: {e}")
            return None


def print_response(label, response):
    print(f"\n--- {label} ---")
    if response is None:
        print("No response.")
        return
    print("Status:", response.status_code)
    content_type = response.headers.get("content-type", "")

    if "application/json" in content_type.lower():
        try:
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        except ValueError:
            print("<invalid JSON>")
            print(response.text)
    else:
        print(response.text)


def main():
    client = APIClient(base_url="http://localhost:8000")

    # ------------------------------
    # Cocktails
    # ------------------------------
    resp = client.get("/drink-ingredients")
    print_response("GET /drink-ingredients (dropdown options)", resp)

    # Mock selection: one ingredient (here: gin)
    selected_drink_ingredient = "gin"
    resp = client.get("/drinks", params={"type": selected_drink_ingredient})
    print_response("GET /drinks?type=gin (filtered items)", resp)

    # ------------------------------
    # Meals
    # ------------------------------
    resp = client.get("/meal-ingredients")
    print_response("GET /meal-ingredients (dropdown options)", resp)

    # Mock selection: one ingredient (here: chicken)
    selected_meal_ingredient = "chicken"
    resp = client.get("/meals", params={"type": selected_meal_ingredient})
    print_response("GET /meals?type=chicken (filtered items)", resp)

    # ------------------------------
    # Video games
    # ------------------------------
    resp = client.get("/game-types")
    print_response("GET /game-types (dropdown options)", resp)

    # Mock selection: one category/type (here: shooter)
    selected_game_type = "shooter"
    resp = client.get("/game", params={"type": selected_game_type})
    print_response("GET /game?type=shooter (filtered items)", resp)

    # ------------------------------
    # Music
    # ------------------------------
    resp = client.get("/music-genres")
    print_response("GET /music-genres (dropdown options)", resp)

    # Mock selection: one genre (here: rock)
    selected_music_genre = "rock"
    resp = client.get("/music", params={"genre": selected_music_genre})
    print_response("GET /music?genre=rock (filtered items)", resp)

    # ------------------------------
    # Randomized planning (POST)
    # ------------------------------
    # Minimal mocked request body (simple strings), matching the earlier style.
    # Expected response shape (per README):
    # {
    #   "drink": "...",
    #   "meal": "...",
    #   "game": "...",
    #   "music": ["...", "...", "...", "...", "..."]
    # }
    plan_request = {
        "drink": selected_drink_ingredient,
        "meal": selected_meal_ingredient,
        "game": selected_game_type,
        "music": selected_music_genre,
    }
    resp = client.post("/plan", json_body=plan_request)
    print_response("POST /plan (randomized plan)", resp)


if __name__ == "__main__":
    main()
