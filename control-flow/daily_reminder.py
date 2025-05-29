# daily_reminder.py

def generate_reminder():
    """
    Génère un rappel personnalisé pour une tâche unique en fonction de sa priorité
    et de son caractère temporel, en utilisant des structures de contrôle avancées.
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
    
    # Traitement avec match-case et conditions
    match priority:
        case "high":
            base_msg = f"'{task}' is a high priority task"
        case "medium":
            base_msg = f"'{task}' is a medium priority task"
        case "low":
            base_msg = f"'{task}' is a low priority task"
    
    # Ajout de la sensibilité temporelle
    if time_bound == "yes":
        reminder = f"Reminder: {base_msg} that requires immediate attention today!"
    else:
        match priority:
            case "high":
                reminder = f"Note: {base_msg}. Complete it soon even without deadline."
            case "medium":
                reminder = f"Note: {base_msg}. Schedule it for this week."
            case "low":
                reminder = f"Note: {base_msg}. Consider completing it when you have free time."
    
    # Affichage du résultat
    print("\n" + reminder)
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    generate_reminder()
