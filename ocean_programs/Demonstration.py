#Demo of Ocean_Predictions
#Nate Holdych 2/24/2021

import Ocean_Predictions

#List of characteristics
chars = []

#Define characteristic by their weights
#You can also 
creativity = Ocean_Predictions.Characteristic("Creativity",64,43,49,39,-41)
chars.append(creativity)
extrinsicSuccess = Ocean_Predictions.Characteristic("Extrinsic Success",101,300,140,134,-300)
chars.append(extrinsicSuccess)
intrinsicSuccess = Ocean_Predictions.Characteristic("Intrinsic Success",442,241,302,205,-103)
chars.append(intrinsicSuccess)
criminalChoice = Ocean_Predictions.Characteristic("Criminal Chance",-4,-10,3,-17,6)
chars.append(criminalChoice)
leadership = Ocean_Predictions.Characteristic("Leadership",12,55,11,-30,-50)
chars.append(leadership)

#Team roles are made as characteristics but should be stored separately
roles = []

analyst = Ocean_Predictions.Characteristic("Analyst",6,2,6,0,0,"Your personality traits suggest that the best role for you in a team setting would be as an analyst. Analysts are the researchers of the group and are skilled with gathering and interpreting the data needed to complete the task.")
roles.append(analyst)
designer = Ocean_Predictions.Characteristic("Designer",6,4,8,2,0,"Your personality traits suggest that the best role for you in a team setting would be as a designer. Designers are the creative minds of the group and are skilled with assembling the concepts that will be built by others.")
roles.append(designer)
engineer = Ocean_Predictions.Characteristic("Engineer",6,6,5,2,0,"Your personality traits suggest that the best role for you in a team setting would be as an engineer. Engineers are the builders of the group and are skilled with taking the conceptual plans and turning them into a reality.")
roles.append(engineer)
tester = Ocean_Predictions.Characteristic("Tester",1,1,1,0,0,"Your personality traits suggest that the best role for you in a team setting would be as a Tester. Testers are skilled at exploring every possible situation that might break a product to ensure that every problem is fixed before it’s too late.")
roles.append(tester)
maintainer = Ocean_Predictions.Characteristic("Maintainer",7,2,4,2,0,"Your personality traits suggest that the best role for you in a team setting would be as a Maintainer. Maintainers have a broad skill set that allows them to perform many different tasks of upkeep and prevent any issues from arising.")
roles.append(maintainer)

#This is just a demonstration, so I'm not using up-to-date averages
avg = Ocean_Predictions.Score(73,64,56,64,45)
#Also random data for user's score
user = Ocean_Predictions.Score(81,56,68,59,36)

for char in chars:
    print(char.name + ": " + str(user.calc(char,avg)))

print("\n")

#Role assignment
userRole = None
userRoleScore = -1
for role in roles:
    currScore = user.calc(role,avg)
    if currScore > userRoleScore:
        userRole = role
        userRoleScore = currScore

print("Team role: " + userRole.name)
print(userRole.description)

#Political compass map coordinate system
polSocial = Ocean_Predictions.Characteristic("Social Political Leaning",53,-26,-5,-12,13)
polEconomic = Ocean_Predictions.Characteristic("Economic Political leaning",48,-22,-14,20,43)

polMapWidth = 200 #This will be the width of the political compass map on the screen
polMapHeight = 200 #This will be the height of the political compass map on the screen
economicPos = user.calc(polEconomic,avg)
socialPos = user.calc(polSocial,avg)
polMapX = polMapWidth/2 * (economicPos * -1 + 1)
polMapY = polMapHeight/2 * (socialPos * -1 + 1)

print("\n")
print("Your x position on the political compass (0-"+ str(polMapWidth) + "): " + str(polMapX))
print("Your y position on the political compass (0-"+ str(polMapHeight) + "): " + str(polMapY))

if(economicPos < 0):
    if(socialPos < 0):
        print("Authoritarian Right")
    else:
        print("Authoritarian Left")
else:
    if(socialPos < 0):
        print("Libertarian Right")
    else:
        print("Libertarian Left")
