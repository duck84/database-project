import csv

with open("./astronauts.csv", newline='') as csvfile:                                                                                                                 
   reader = csv.DictReader(csvfile)                                                                                                                                  
   x = 1
   majorId = 1
   fieldnames = ['AstronautId', 'MajorId']
   writer = csv.DictWriter(open('gradMajorsRel.csv', 'w'), fieldnames=fieldnames)
   writer.writeheader()
   majors = {}
   for row in reader:
      major = row['Graduate Major']  
      if major not in majors:
         majors[major] = majorId
         majorId += 1
      csvData = {'AstronautId' : x, 'MajorId' : majors[major]}
      writer.writerow(csvData)
      x += 1
	

# AstronautId, Name, BirthDate, BirthPlace, Group, Gender, Status, Year, DeathMission, DeathDate, SpaceFlightHours, SpaceFlights, SpaceWalks, Rank, Service

# Name,Year,Group,Status,Birth Date,Birth Place,Gender,Alma Mater,Undergraduate Major,Graduate Major,Military Rank,Military Branch,Space Flights,Space Flight (hr),Space Walks,Space Walks (hr),Missions,Death Date,Death Mission

