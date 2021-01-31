#!/usr/bin/python3
import re

titles = ["Stephen F Austin Lumberjacks Classic Court Double Shootout Basketball Game","Stephen F Austin Lumberjacks Baggo Bean Bag Toss Cornhole Game Classic Design","Stephen F Austin Lumberjacks Baggo Bean Bag Toss Cornhole Game Vintage Design","Stephen F Austin Lumberjacks Canvas Wall Art Museum Design (18x24)","Stephen F Austin Lumberjacks Canvas Wall Art Weathered Design (18x24)","Stephen F Austin Lumberjacks Canvas Wall Art Weathered Design (24x36)","Stephen F Austin Lumberjacks Canvas Wall Art Museum Design (24x36)","Stephen F Austin Lumberjacks Canvas Wall Art Museum Design (36x48)","Stephen F Austin Lumberjacks Canvas Wall Art Weathered Design (36x48)","Stephen F Austin State Lumberjacks Canvas Wall Art Triptych Rush Design (48x54 Triptych)","Stephen F Austin State Lumberjacks Canvas Wall Art Triptych Double Border Design (48x54 Triptych)","Stephen F Austin Lumberjacks Triptych Canvas Wall Art Watercolor (48x54 Inches)","Stephen F Austin Lumberjacks 8 Foot Portable Folding Tailgate Table Weathered Version","Stephen F Austin Lumberjacks 8 Foot Portable Folding Tailgate Table Stripe Version","Stephen F Austin Lumberjacks Gameday Tower","Stephen F Austin Lumberjacks 2x3 Cornhole Bag Toss","Stephen F Austin Lumberjacks Giant Wooden Tumble Tower Game ","Stephen F Austin Lumberjacks Table Tennis - Classic Table Tennis Table","Stephen F Austin Lumberjacks Grey Regulation 4 All Weather Cornhole Bags","Stephen F Austin Lumberjacks Purple Regulation 4 All Weather Cornhole Bags","Stephen F Austin Lumberjacks Solid Wood 2x3 Cornhole","Stephen F Austin Lumberjacks Washer Game Set Onyx Stained","Stephen F Austin Lumberjacks Regulation Cornhole Storage Carrying Case","Stephen F Austin Lumberjacks Desktop Cornhole Logo Stripe Design","Stephen F Austin Lumberjacks 24 Count Table Tennis Balls Logo Design","Stephen F Austin Lumberjacks Solid Wood 2x4 Cornhole Board Set Herringbone Design","Stephen F Austin Lumberjacks Pop Up Table Tennis 6Ft Weathered Design","Stephen F Austin Lumberjacks Weathered Design Hook and Ring Game","Stephen F Austin Lumberjacks Table Tennis Paddle Logo Design","Stephen F Austin Lumberjacks 4 Grey Regulation Corn Filled Cornhole Bags","Stephen F Austin Lumberjacks 4 Purple Regulation Corn Filled Cornhole Bags","Stephen F Austin Lumberjacks Regulation Cornhole Game Set Triangle Weathered Version","Stephen F Austin Lumberjacks Regulation Cornhole Game Set Vintage Version","Stephen F Austin Lumberjacks Regulation Cornhole Game Set Museum Version","Stephen F Austin Lumberjacks Regulation Cornhole Game Set Rosewood Stained Stripe Version","Stephen F Austin Lumberjacks Regulation Cornhole Game Set Onyx Stained Stripe Version","Stephen F Austin Lumberjacks Color Design Yoga Mat","Stephen F Austin Lumberjacks Earth Design Yoga Mat","Stephen F Austin Lumberjacks Yard Dominoes Game","Stephen F Austin Lumberjacks Kubb Viking Chess Game","Stephen F Austin Lumberjacks Quoits Ring Toss Game","Stephen F Austin Lumberjacks Tic-Tac-Toe Game","Stephen F Austin Lumberjacks 2-in-1 Birdie Pickleball Paddle Game","Stephen F Austin Lumberjacks Dartboard Cabinet"]
dups = []

for i in titles:
	if i not in dups:
		dups.append(i)
	elif i in dups:
		print(i)



#reader(). see also DictReader()
'''
import csv


with open("myCSV.csv", "r") as myCSV:

	reader = csv.reader(myCSV)
 
	print(reader)
	for row in reader:

		for num, cell in enumerate(row):
			print(cell)
		if num < 0:
			print("enumerated") #never prints.

myCSV.close()

with open("myCSV.csv", "r") as csv_file:
	csv_reader = csv.DictReader(csv_file)
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {", ".join(row)}')
			line_count += 1
		print(f'\t{row["Row1"]} describes {row["Row2"]}.')
		line_count += 1
	print(f'Processed {line_count} lines.')
csv_file.close()'''