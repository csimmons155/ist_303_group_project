import pickle
import os 
from collections import Counter
from sqlite_dbv3 import * 

"""
Check if dorm pickle files exists. If so, load the file 

"""

if (os.path.exists("band_assignments_June.p")):
	
	band_assignments_June = pickle.load(open("band_assignments_June.p", "rb"))

else:
	
	band_assignments_June = {
	
		'Band1' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band2' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band3' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band4' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band5' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band6' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band7' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band8' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		}

	} 

if (os.path.exists("band_assignments_July.p")):
	
	band_assignments_July = pickle.load(open("band_assignments_July.p", "rb"))

else:
	
	band_assignments_July = {
	
		'Band1' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band2' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band3' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band4' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band5' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band6' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band7' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band8' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		}

	} 

if (os.path.exists("band_assignments_August.p")):
	
	band_assignments_August = pickle.load(open("band_assignments_August.p", "rb"))

else:
	
	band_assignments_August = {
	
		'Band1' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band2' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band3' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band4' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band5' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band6' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band7' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		},

		'Band8' : {
			'Singer' : [],
			'Guitarist' : [],
			'Drummer' : [],
			'Bassist' : [],
			'Keyboardist' : [],
			'Instrumentalist' : []
		}

	} 
"""
Calculate the Gender Distribution of a given Band.  

gender : camper gender to get distribution of 
temp_dict : the dictionary that represents a given Band 

Returns 1 if the gender distribution is responable for a 
camper of 'gender' to be inserted into the Band

Returns 0 Otherwise 

"""
def get_gender_distribution(gender, temp_dict):

	male_count = 0 
	female_count = 0

	for k in temp_dict:
		if len(temp_dict[k]) != 0:
			if( temp_dict[k][0][1] == "Male"):
				male_count += 1
			else:
				female_count += 1

	if gender == "Female" and female_count < 3:
		return 1
	elif gender == "Male" and male_count < 3:
		return 1
	else: 
		return 0 


"""
Assigns Band to a Camper

id : Camper ID
band_role : Camper's proposed band role 
gender : Camper's Gender

"""
def assign_band(id, band_role, gender, rank, session, avoid_band=None):

	band_filename = "band_assignments_"+session+".p"

	if (session == "June"):
		band_assignments = band_assignments_June
	elif (session == "July"):
		band_assignments = band_assignments_July
	else:
		band_assignments = band_assignments_August

	for key in band_assignments:
		if (len(band_assignments[key][band_role]) == 0 and key != avoid_band):

			temp_dict = band_assignments[key]
			rank_count = 0
			for i in temp_dict:
				if (len(temp_dict[i]) == 1):
					curr_rank = temp_dict[i][0][2]
					if curr_rank != "None": rank_count += 1


			if(get_gender_distribution(gender, temp_dict)):
				if (rank != "None" and rank_count < 4):
					band_assignments[key][band_role].append((id, gender, rank))
					pickle.dump( band_assignments, open(band_filename, "wb") )
					# returns band name
					return key 
				elif (rank == "None"):
					band_assignments[key][band_role].append((id, gender, rank))
					pickle.dump( band_assignments, open(band_filename, "wb") )
					# returns band name
					return key
				else:
					continue

	return "Error"  

				

"""
Obtain the band of a Camper of given 'id' and 'band_role'
"""
def get_band_name(id, band_role, session):
	
	if (session == "June"):
		band_assignments = band_assignments_June
	elif (session == "July"):
		band_assignments = band_assignments_July
	else:
		band_assignments = band_assignments_August

	for key in band_assignments:
		if (len(band_assignments[key][band_role]) != 0 and band_assignments[key][band_role][0][0] == id):
			return key 


"""
Manually inserts a given Camper into a given Band
"""
def insert_into_band(id, band_role, gender, rank, session, band_name):

	band_filename = "band_assignments_"+session+".p"

	if (session == "June"):
		band_assignments = band_assignments_June
	elif (session == "July"):
		band_assignments = band_assignments_July
	else:
		band_assignments = band_assignments_August

	# assuming the function band_insertion_check() was called before this function
	band_assignments[band_name][band_role].append((id, gender, rank))
	pickle.dump( band_assignments, open(band_filename, "wb") )



"""
Checks if a Camper could be inserted into a given 'band_name'
"""
def band_insertion_check(id, band_role, gender, rank, session, band_name):

	if (session == "June"):
		band_assignments = band_assignments_June
	elif (session == "July"):
		band_assignments = band_assignments_July
	else:
		band_assignments = band_assignments_August


	if (len(band_assignments[band_name][band_role]) != 0):
		return 0
	else:
		temp_dict = band_assignments[band_name]
		rank_count = 0
		for i in temp_dict:
			if (len(temp_dict[i]) == 1):
				curr_rank = temp_dict[i][0][2]
				if curr_rank != "None": rank_count += 1

		if(get_gender_distribution(gender, temp_dict)):
			if (rank != "None" and rank_count < 4):
				return 1
			elif (rank == "None"):
				return 1
			else:
				return 0
		else:
			return 0  



def band_assignment_driver(camper_id_text, preferences):
	c, conn = create_db()	
	# get params from camper
	c.execute("SELECT gender, band_role, camp_dates FROM application WHERE camper_id = '"+ camper_id_text + "'")
	r0 = c.fetchone() 
	
	gender = r0[0]
	band_role = r0[1]
	session = r0[2]

	c.execute("SELECT rank FROM check_in WHERE camper_id = '"+ camper_id_text + "'")
	r0 = c.fetchone()

	rank = r0[0]

	# Check if pref. band mate has checked in
	c.execute("SELECT has_checked_in FROM check_in WHERE camper_id = '"+ preferences[2].text() + "'")
	r1 = c.fetchone()

	# Check if avoid band mate has checked in 
	c.execute("SELECT has_checked_in FROM check_in WHERE camper_id = '"+ preferences[3].text() + "'")
	r2 = c.fetchone()


	if(r1 and r1[0] == 0 and r2 and r2[0] == 0):
		
		band = assign_band(camper_id_text, band_role, gender, rank, session)
		#insert into band DB
		t = (camper_id_text, session, band, gender, int(rank))
		c.execute("INSERT INTO band VALUES (?,?,?,?,?)", t)

	# if the pref band mate has checked in, but not avoid band mate 
	elif(r1 and r1[0] == 1 and r2 and r2[0] == 0):
		c.execute("SELECT band FROM band WHERE camper_id = '"+ preferences[0].text() + "'")
		r4 = c.fetchone()
		pref_band = r4[0]

		if(band_insertion_check(camper_id_text, band_role, gender, rank, session, pref_band)):
			insert_into_band(camper_id_text, band_role, gender, rank, session, pref_band)
			# insert into band DB
			t = (camper_id_text, session, pref_band, gender, int(rank))
			c.execute("INSERT INTO band VALUES (?,?,?,?,?)", t)
		else:
			band = assign_band(camper_id_text, band_role, gender, rank, session)
			# insert into band DB
			t = (camper_id_text, session, band, gender, int(rank))
			c.execute("INSERT INTO band VALUES (?,?,?,?,?)", t)

	elif(r2 and r2[0] == 1 and r1 and r1[0] == 0):
		c.execute("SELECT band FROM band WHERE camper_id = '"+ preferences[1].text() + "'")
		r4 = c.fetchone()
		band_avoid = r4[0]

		band = assign_band(camper_id_text, band_role, gender, rank, session, avoid_band=band_avoid)
		# insert into band DB
		t = (camper_id_text, session, band, gender, int(rank))
		c.execute("INSERT INTO band VALUES (?,?,?,?,?)", t)

	elif(r2 and r2[0] == 1 and r1 and r1[0] == 1):
		c.execute("SELECT band FROM band WHERE camper_id = '"+ preferences[0].text() + "'")
		r4 = c.fetchone()
		pref_band = r4[0]

		c.execute("SELECT band FROM band WHERE camper_id = '"+ preferences[1].text() + "'")
		r5 = c.fetchone()
		band_avoid = r5[0]

		if(band_insertion_check(camper_id_text, band_role, gender, rank, session, pref_band)):
			insert_into_band(camper_id_text, band_role, gender, rank, session, pref_band)
			# insert into band DB
			t = (camper_id_text, session, pref_band, gender, int(rank))
			c.execute("INSERT INTO band VALUES (?,?,?,?,?)", t)
		else:
			band = assign_band(camper_id_text, band_role, gender, rank, session, avoid_band=band_avoid)
			# insert into band DB
			t = (camper_id_text, session, band, gender, int(rank))
			c.execute("INSERT INTO band VALUES (?,?,?,?,?)", t)


	else:
		band = assign_band(camper_id_text, band_role, gender, rank, session)
		#insert into band DB
		t = (camper_id_text, session, band, gender, int(rank))
		c.execute("INSERT INTO band VALUES (?,?,?,?,?)", t)

	save_db_changes(conn)



def swap_request(id1, band_role1, id2, band_role2):

	if band_role1 == band_role2: return 0 


	# find the bands for id1 and id2 
	for key in band_assignments:

		if( band_assignments[key][band_role1][0][0] == id1):
			id1_band = key

		if( band_assignments[key][band_role2][0][0] == id2):
			id2_band = key

	if id1_band == id2_band: return 0 




"""
assign_band("105", "Drummer", "Male", 3, "July", avoid_band="Band1")
print(band_assignments_July)
print(band_assignments_June)

#"""

