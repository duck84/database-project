import csv

with open("./astronauts.csv", newline='') as csvfile:                                                                                                                 
   reader = csv.DictReader(csvfile)                                                                                                                                  
   x = 1
   fieldnames = ['CollegeId', 'Name']
   writer = csv.DictWriter(open('almaMater.csv', 'w'), fieldnames=fieldnames)
   writer.writeheader()
   used = []
   for row in reader:
      for name in row['Alma Mater'].split(';'):
         name = name.strip()
#      name = row['Alma Mater']                                                     
         if name in used:
            continue
         used.append(name)
         csvData = {'CollegeId' : x, 'Name' : name}
         writer.writerow(csvData)
         x += 1
	

# AstronautId, Name, BirthDate, BirthPlace, Group, Gender, Status, Year, DeathMission, DeathDate, SpaceFlightHours, SpaceFlights, SpaceWalks, Rank, Service

# Name,Year,Group,Status,Birth Date,Birth Place,Gender,Alma Mater,Undergraduate Major,Graduate Major,Military Rank,Military Branch,Space Flights,Space Flight (hr),Space Walks,Space Walks (hr),Missions,Death Date,Death Mission

