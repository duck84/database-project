import csv

with open("./astronauts.csv", newline='') as csvfile:                                                                                                                 
   reader = csv.DictReader(csvfile)                                                                                                                                  
   x = 1
   fieldnames = ['Id', 'Major']
   writer = csv.DictWriter(open('gradMajors.csv', 'w'), fieldnames=fieldnames)
   writer.writeheader()
   used = []
#   for row in reader:
#      major = row['Undergraduate Major']                                                     
#      if major in used:
#         continue
#      used.append(major)
#      csvData = {'Id' : x, 'Major' : row['Undergraduate Major']}
#      writer.writerow(csvData)
#      x += 1
   for row in reader:
      gradMajor = row['Graduate Major']
      if gradMajor in used:
         continue
      used.append(gradMajor)
      csvData = {'Id' : x, 'Major' : gradMajor}
      writer.writerow(csvData)
      x += 1	

# AstronautId, Name, BirthDate, BirthPlace, Group, Gender, Status, Year, DeathMission, DeathDate, SpaceFlightHours, SpaceFlights, SpaceWalks, Rank, Service

# Name,Year,Group,Status,Birth Date,Birth Place,Gender,Alma Mater,Undergraduate Major,Graduate Major,Military Rank,Military Branch,Space Flights,Space Flight (hr),Space Walks,Space Walks (hr),Missions,Death Date,Death Mission

