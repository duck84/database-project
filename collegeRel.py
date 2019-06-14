import csv

with open("./astronauts.csv", newline='') as csvfile:                                                                                                                 
   reader = csv.DictReader(csvfile)                                                                                                                                  
   x = 1
   collegeId = 1
   fieldnames = ['AstronautId', 'CollegeId']
   writer = csv.DictWriter(open('collegeRel.csv', 'w'), fieldnames=fieldnames)
   writer.writeheader()
   colleges = {}
   for row in reader:
      for college in row['Alma Mater'].split(';'):
         college = college.strip()
         if college not in colleges:
            colleges[college] = collegeId
            collegeId += 1
         csvData = {'AstronautId' : x, 'CollegeId' : colleges[college]}
         writer.writerow(csvData)
      x += 1
	

# AstronautId, Name, BirthDate, BirthPlace, Group, Gender, Status, Year, DeathMission, DeathDate, SpaceFlightHours, SpaceFlights, SpaceWalks, Rank, Service

# Name,Year,Group,Status,Birth Date,Birth Place,Gender,Alma Mater,Undergraduate Major,Graduate Major,Military Rank,Military Branch,Space Flights,Space Flight (hr),Space Walks,Space Walks (hr),Missions,Death Date,Death Mission

