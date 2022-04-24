# **Problem** :

# - **Task :** Estimating the risk of death from ***coronavirus***.
# - Consider the following questions in terms of `True`/`False` regarding anyone else.
#     - Are you a **cigarette** addict older than **75** years old? Variable → `age`
#     - Do you have a **severe** chronic disease? Variable → `chronic`
#     - Is your **immune** system **too weak**? Variable → `immune`

# Set a logical algorithm using boolean logic operators (and / or ) and the given variables in order to 
# give us True (there is a risk of death) or False (there is not a risk of death) as a result.
#I did not use bool (input) because I would end up getting True for all non-empty inputs.
age = input("Are you a cigarette addict older than 75 years? (Please enter yes or no) ")
chronic = input("Do you have a severe chronic disease?(Please enter yes or no) ")
immune = input("Is your immune system too weak? (Please enter yes or no) ")
# Instead I created new variables which will give bool results
age_1= (age.lower() == "yes") # Here I used (.lower) to include both Yes and yes as True answers.
chronic_1 = (chronic.lower() == "yes")
immune_1 = (immune.lower()=="yes")

# If someone is over 75 there is risk of death whether or not the other values are True
# If someone is not over 75 then the risk is only True when both other consitions are True
risk = chronic_1 and immune_1 or age_1
print("The risk of death is :" , risk)