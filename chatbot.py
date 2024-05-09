import nltk
import re
from nltk.tokenize import word_tokenize

# Basic pattern matching rules for healthcare symptoms
symptoms_rules = {
    "headache": "\n Description: Headaches are common and can be caused by stress, dehydration, or other factors \n Medicines: ibuprofen or paracetamol \n Advice: Rest and stay hydrated. If the headache persists, consult a doctor.",
    "fever": "\n Description: Fever is a temporary increase in body temperature, often due to illness.\n Medicines: take paracetamol and stay hydrated.\n Advice: If the fever is above 102°F (38.9°C) or persists for more than two days, seek medical advice.",
    "cough": "\n Description: Coughing is a reflex action to clear your airways \n Medication: drink warm fluids and try honey-based lozenges \n Advice: If the cough persists or worsens, consult a healthcare provider.",
    "stomach pain": "\n Description: Stomach aches can be caused by indigestion or other issues \n Medication: 1) use the tablet Omeprazole; 2) try drinking chamomile tea and eat light food.\n Advice: If you have severe pain or persistent symptoms, see a doctor.",
    "dizziness": "\n Description: It can be caused by various factors such as low blood pressure, dehydration \n Medication: Antivert, Dramamine are commonly used to treat vertigo and dizziness associated with motion sickness \n Advice: Dehydration is a common cause of dizziness. Drink plenty of water and avoid caffeine and alcohol.",
    "sore throat": "\n Description: Sore throat can be caused by infections or irritation from environmental factors.\n Medication: acetaminophen or ibuprofen, and throat lozenges or sprays containing benzocaine for numbing \n Advice: Avoid irritants like smoke, and rest your voice. Warm teas with honey or saltwater gargles can help soothe the throat.",
    "dehydration": "\n Description: Dehydration occurs when the body loses more fluids than it takes in, leading to symptoms like dry mouth, fatigue, dizziness, and dark urine.\n Medication: Oral rehydration solutions (ORS), electrolyte drinks like Gatorade, or water with added electrolytes \n Advice: Drink plenty of fluids, preferably water or electrolyte-rich drinks, and avoid diuretics like caffeine and alcohol.",
    "ear pain": "\n Description: Ear pain can be caused by various issues, including ear infections, earwax buildup, or sinus infections.\n Medication: acetaminophen or ibuprofen can help reduce ear pain. Ear drops designed to alleviate discomfort may also be used, depending on the cause\n Advice: Keep the ear dry and avoid inserting objects into it. If the pain persists or is severe, or if there's discharge, hearing loss, or other symptoms, consult a healthcare professional.",
    "muscle pain": "\n Description: Muscle pain, also known as myalgia, can occur due to strain, overuse, or injury, leading to soreness, stiffness, or discomfor \n  Medication: ibuprofen or acetaminophen \n Advice: Rest the affected area, apply ice or heat, and avoid overexertion. If pain persists, seek medical advice.",
    "acidity": "\n Description: Acidity refers to excess stomach acid, causing discomfort, heartburn, or acid reflux.\n Medication: Tums, Rolaids, or Pepto-Bismol.\n Advice: Avoid spicy and fatty foods, reduce alcohol and caffeine intake, and try not to eat late at night."
}

# Function to process user input and determine response
def get_response(user_input):
    tokens = word_tokenize(user_input.lower())
    response = "Please describe your symptoms more clearly?"

    # Check for known symptoms in user input
    for symptom, advice in symptoms_rules.items():
        if any(symptom in token for token in tokens):
            response = advice
            break

    return response

# A simple chatbot loop

def healthcare_chatbot():
    print("Hello! I can provide preliminary advice for mild symptoms.How can I help you today?")
    while True:
        user_input = input("You: ")

        # Exit conditions
        if re.search(r"\b(thank you|ok)\b", user_input.lower()):
            print("chatbot: Goodbye! Take care of your health")
            break
        
        response = get_response(user_input)
        print(f"{response}")
        continue_input = input("chatbot: Would you like to ask about any other symptom? (yes/no): ")

        # Check if the user wants to continue
        if re.search(r"\b(no|nah|nope)\b", continue_input.lower()):
            print("chatbot: Goodbye! Take care of your health")
            break
            continue_chat = False
        elif re.search(r"\b(yes|yeah|yup)\b", continue_input.lower()):
            print("chatbot: please ask about another symptom.")
        else:
            print("chatbot: I didn't understand your response. I'll assume you want to continue.")

# Run the chatbot
healthcare_chatbot()
