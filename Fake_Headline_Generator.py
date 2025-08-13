#1--> import the random module

import random
#2--> Create subjects using list

subjects=[
    "shahruk khan",
    "Virat Kohli",
    "Nirmala Sithraman",
    "A Mumbai cat",
    "a Group of monkeys",
    "prime minister modi",
    "Auto rikshaw driver from delhi"
]

# we will create actions
actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"

]

#create places or thing 
places_or_things=[
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat ",
    "during IPL match",
    "at India Gate"
]
#we will apply or use while loop 

#start the headline generation loop 
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    places_or_thing=random.choice(places_or_things)

    headline=f"BREAKING NEWS:{subject} {action} {places_or_thing}"
    print("\n" + headline)

    user_input=input("Do you want another Headline? (yes/no)").strip().lower()
    if user_input=="no":
        break

print("\n Thanks for using the fake News gaedline generator. Have a Fun Day!")