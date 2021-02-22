import Ocean_Predictions

#creativity
#professional success
#criminal intent
#leadership

#Define characteristic by their weights
creativity = Ocean_Predictions.Characteristic(64,43,49,39,-41)
extrinsicSuccess = Ocean_Predictions.Characteristic(101,300,140,134,-300)
intrinsicSuccess = Ocean_Predictions.Characteristic(442,241,302,205,-103)
criminalChoice = Ocean_Predictions.Characteristic(-4,-10,3,-17,6)
leadership = Ocean_Predictions.Characteristic(12,55,11,-30,-50)

#This is just a demonstration, so I'm not using up-to-date averages
avg = Ocean_Predictions.Score(73,64,56,64,45)
#Also random data for user's score
user = Ocean_Predictions.Score(81,56,68,59,36)

print("Creativity: ", user.calc(creativity, avg))
print("Extrinsic Success: ", user.calc(extrinsicSuccess, avg))
print("Intrinsic Success: ", user.calc(intrinsicSuccess, avg))
print("Criminal Chance: ", user.calc(creativity, avg))
print("Leadership: ", user.calc(creativity, avg))
