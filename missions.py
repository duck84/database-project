import csv

with open("./astronauts.csv", newline='') as csvfile:                                                                                                                 
   reader = csv.DictReader(csvfile)                                                                                                                                  
   x = 1
   fieldnames = ['MissionId', 'Name']
   writer = csv.DictWriter(open('missions.csv', 'w'), fieldnames=fieldnames)
   writer.writeheader()
   used = []
   for row in reader:
      for mission in row['Missions'].split(','):
         mission = mission.strip()                                                     
         if mission in used:
            continue
         used.append(mission)
         csvData = {'MissionId' : x, 'Name' : mission}
         writer.writerow(csvData)
         x += 1
	

# AstronautId, Name, BirthDate, BirthPlace, Group, Gender, Status, Year, DeathMission, DeathDate, SpaceFlightHours, SpaceFlights, SpaceWalks, Rank, Service

# Name,Year,Group,Status,Birth Date,Birth Place,Gender,Alma Mater,Undergraduate Major,Graduate Major,Military Rank,Military Branch,Space Flights,Space Flight (hr),Space Walks,Space Walks (hr),Missions,Death Date,Death Mission

