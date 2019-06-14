import csv

with open("./astronauts.csv", newline='') as csvfile:                                                                                                                 
     reader = csv.DictReader(csvfile)                                                                                                                                  
     x = 1
     fieldnames = ['Id', 'Name', 'Birth Date', 'Birth Place', 'Group', 'Gender', 'Status', 'Year', \
                   'Death Mission', 'Death Date', 'Space Flight (hr)', 'Space Flights', \
                   'Space Walks (hr)', 'Space Walks', 'Military Rank', 'Military Branch']
     writer = csv.DictWriter(open('test2.csv', 'w'), fieldnames=fieldnames)
     writer.writeheader()
     for row in reader:                                                                                                                                                
             csvData = {'Id' : x, 'Name' : row['Name'], 'Birth Date' : row['Birth Date'], 'Birth Place' : row['Birth Place'], 'Group' : row['Group'], \
		   'Gender' : row['Gender'], 'Status' : row['Status'], 'Year' : row['Year'], 'Death Mission' : row['Death Mission'], \
		   'Death Date' : row['Death Date'], 'Space Flights' : row['Space Flights'], \
		   'Space Walks (hr)' : row['Space Walks (hr)'], 'Space Walks' : row['Space Walks'], 'Military Rank' : row['Military Rank'],  \
                   'Military Branch' : row['Military Branch'], 'Space Flight (hr)' : row['Space Flight (hr)']}
             writer.writerow(csvData)
             x += 1
	

# AstronautId, Name, BirthDate, BirthPlace, Group, Gender, Status, Year, DeathMission, DeathDate, SpaceFlightHours, SpaceFlights, SpaceWalks, Rank, Service

# Name,Year,Group,Status,Birth Date,Birth Place,Gender,Alma Mater,Undergraduate Major,Graduate Major,Military Rank,Military Branch,Space Flights,Space Flight (hr),Space Walks,Space Walks (hr),Missions,Death Date,Death Mission

