# daily_reminder.py

def generate_reminder():
    """
    Génère un rappel personnalisé pour une tâche unique avec une structure de 
    sortie conforme aux exigences de vérification.
    """
    # Saisie des informations sur la tâche
    task = input("Enter your task: ")
    
    # Validation de la priorité avec boucle
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ["high", "medium", "low"]:
            break
        print("Invalid input. Please enter high, medium, or low.")
    
    # Validation du caractère temporel
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ["yes", "no"]:
            break
        print("Invalid input. Please enter yes or no.")
    
    # Construction du message de base avec match-case
    match priority:
        case "high":
            base_msg = f"'{task}' is a high priority task"
        case "medium":
            base_msg = f"'{task}' is a medium priority task"
        case "low":
            base_msg = f"'{task}' is a low priority task"
    
    # Génération du rappel final avec impression directe
    if time_bound == "yes":
        print(f"\nReminder: {base_msg} that requires immediate attention today!")
    else:
        # Messages spécifiques pour chaque priorité (non temporel)
        match priority:
            case "high":
                print(f"\nNote: {base_msg}. Complete it soon even without deadline.")
            case "medium":
                print(f"\nNote: {base_msg}. Schedule it for this week.")
            case "low":
                print(f"\nNote: {base_msg}. Consider completing it when you have free time.")
    
    # Message final
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    generate_reminder()
