# weather_advice.py

def weather_recommendation():
    """
    Demande à l'utilisateur les conditions météorologiques actuelles
    et fournit des recommandations vestimentaires.
    """
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower().strip()

    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    weather_recommendation()
