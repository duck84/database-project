import csv

with open("./astronauts.csv", newline='') as csvfile:                                                                                                                 
   reader = csv.DictReader(csvfile)                                                                                                                                  
   x = 1
   fieldnames = ['Military Rank']
   writer = csv.DictWriter(open('ranks.csv', 'w'), fieldnames=fieldnames)
   writer.writeheader()
   used = []
   for row in reader:
      rank = row['Military Rank']                                                     
      if rank in used:
         continue
      used.append(rank)
      csvData = {'Military Rank' : rank}
      writer.writerow(csvData)
      x += 1
	

# AstronautId, Name, BirthDate, BirthPlace, Group, Gender, Status, Year, DeathMission, DeathDate, SpaceFlightHours, SpaceFlights, SpaceWalks, Rank, Service

# Name,Year,Group,Status,Birth Date,Birth Place,Gender,Alma Mater,Undergraduate Major,Graduate Major,Military Rank,Military Branch,Space Flights,Space Flight (hr),Space Walks,Space Walks (hr),Missions,Death Date,Death Mission

