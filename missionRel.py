import csv

with open("./astronauts.csv", newline='') as csvfile:                                                                                                                 
   reader = csv.DictReader(csvfile)                                                                                                                                  
   x = 1
   missionId = 1
   fieldnames = ['AstronautId', 'MissionId']
   writer = csv.DictWriter(open('missionRel.csv', 'w'), fieldnames=fieldnames)
   writer.writeheader()
   missions = {}
   for row in reader:
      for mission in row['Missions'].split(','):
         mission = mission.strip()
         if mission not in missions:
            missions[mission] = missionId
            missionId += 1
         csvData = {'AstronautId' : x, 'MissionId' : missions[mission]}
         writer.writerow(csvData)
      x += 1
	

# AstronautId, Name, BirthDate, BirthPlace, Group, Gender, Status, Year, DeathMission, DeathDate, SpaceFlightHours, SpaceFlights, SpaceWalks, Rank, Service

# Name,Year,Group,Status,Birth Date,Birth Place,Gender,Alma Mater,Undergraduate Major,Graduate Major,Military Rank,Military Branch,Space Flights,Space Flight (hr),Space Walks,Space Walks (hr),Missions,Death Date,Death Mission

