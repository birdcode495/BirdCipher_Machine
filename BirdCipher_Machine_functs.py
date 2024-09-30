


def selectDirectory():

	global directory

	directory = filedialog.askdirectory(title = 'Open directory')
	ramsonDirectoryUrl.config(text = directory)

def generate_key_ramson():

	global key_ramson

	key_ramson = Fernet.generate_key()
	ramsonKey.config(text = key_ramson)

def bring_key_ramson():

	global key_ramson

	wdatos = bytes(password_for_ramson.get(), 'utf-8')
	h = hashlib.new(algoritmo, wdatos)
	hash2 = HASH.generaHash(h)

	miConexion13 = psycopg2.connect(host = 'baak8kinqrfryal5bhvp-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'urnsamk6lldavmbxb6ev', dbname = 'baak8kinqrfryal5bhvp', password = 'nMjCFD00O0DJOmYjbjbZ8sCDdI8wxw')
		
	miCursor13 = miConexion13.cursor()

	sql_verf_hash_ramson = 'select * from Players where nickname = (%s)'
	sql_verf_hash_data_ramson = (nickname_db,)
	miCursor13.execute(sql_verf_hash_ramson, sql_verf_hash_data_ramson)
	dlt453 = miCursor13.fetchall()

	if dlt453[0][5] >= 1 and hash2 == dlt453[0][3]:

		if target_receiver_ramson != '':

			sql_bring_key_ramson = 'select * from ramson_bird where (client = (%s) and server = (%s) and packet = (%s))'
			sql_bring_key_data_ramson = (nickname_db, target_receiver_ramson, packet.get())
			miCursor13.execute(sql_bring_key_ramson, sql_bring_key_data_ramson)
			dlt456 = miCursor13.fetchall()
			key_ramson = dlt456[0][4]
			ramsonKey.config(text = key_ramson)

	miConexion13.commit()
	miConexion13.close()


def execution_encrypt_files(items, key):

	i = Fernet(key)

	for x in items:

		with open(x, 'rb') as file:

			file_data = file.read()

		data = i.encrypt(file_data)

		with open(x, 'wb') as file:

			file.write(data)


def execution_decrypt_files(items, key):

	i = Fernet(key)

	for x in items:

		with open(x, 'rb') as file:

			file_data = file.read()

		data = i.decrypt(file_data)

		with open(x, 'wb') as file:

			file.write(data)


def encrypt_files_ramson_funct():


	wdatos = bytes(password_for_ramson.get(), 'utf-8')
	h = hashlib.new(algoritmo, wdatos)
	hash2 = HASH.generaHash(h)

	miConexion12 = psycopg2.connect(host = 'baak8kinqrfryal5bhvp-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'urnsamk6lldavmbxb6ev', dbname = 'baak8kinqrfryal5bhvp', password = 'nMjCFD00O0DJOmYjbjbZ8sCDdI8wxw')
	
	miCursor12 = miConexion12.cursor()

	sql_verf_hash_ramson = 'select * from Players where nickname = (%s)'
	sql_verf_hash_data_ramson = (nickname_db,)
	miCursor12.execute(sql_verf_hash_ramson, sql_verf_hash_data_ramson)
	dlt5 = miCursor12.fetchall()

	if dlt5[0][5] >= 1 and hash2 == dlt5[0][3]:

		if target_receiver_ramson != '':

			sql_ramson_verf = 'select * from ramson_bird where (client = (%s) and server = (%s) and packet = (%s))'
			sql_ramson_verf_data = (nickname_db, target_receiver_ramson, packet.get())
			miCursor12.execute(sql_ramson_verf, sql_ramson_verf_data)
			df20 = miCursor12.fetchall()
			df12_test = True

			if len(df20) == 0 and df12_test == True:

				if directory != '' and ramsonBird_message.get("1.0", "end-1c") != '' and packet.get() != 0:

					sql1234 = 'insert into ramson_bird(client, password, server, key_c, description, packet) values(%s,%s,%s,%s,%s,%s)'
					datos_sql1234 = (nickname_db, hash2, target_receiver_ramson, key_ramson.decode(), ramsonBird_message.get('1.0', 'end-1c'), packet.get())
					miCursor12.execute(sql1234, datos_sql1234)
					archivos = directory
					items = os.listdir(archivos)
					archivos2 = [archivos + '/' + x for x in items]
					execution_encrypt_files(archivos2, key_ramson)
					print(key_ramson)

					playsound('bambu_click.mp3')

				elif directory == '' or ramsonBird_message.get('1.0', 'end-1c') == '' or packet.get() == 0:

					playsound('cartoon121.mp3')


			elif len(df20) > 0 and df12_test == True:

				if directory != '' and ramsonBird_message.get("1.0", "end-1c") != '' and packet.get() != 0:

					sql1235 = 'update ramson_bird set (client, password, server, key_c, description, packet) = (%s,%s,%s,%s,%s,%s) where (client = (%s) and server = (%s) and packet = (%s))'
					datos_sql1235 = (nickname_db, hash2, target_receiver_ramson, key_ramson.decode(), ramsonBird_message.get('1.0', 'end-1c'), packet.get(), nickname_db, target_receiver_ramson, packet.get())
					miCursor12.execute(sql1235, datos_sql1235)
					archivos = directory
					items = os.listdir(archivos)
					archivos2 = [archivos + '/' + x for x in items]
					execution_encrypt_files(archivos2, key_ramson)
					print(key_ramson)

					playsound('bambu_click.mp3')

				elif directory == '' or ramsonBird_message.get('1.0', 'end-1c') == '' or packet.get() == 0:

					playsound('cartoon121.mp3')


		elif target_receiver_ramson == '':

			playsound('RecipientUsername.mp3')
			df12_test = False


	if dlt5[0][5] >= 1 and hash2 != dlt5[0][3]:

		playsound('WrongPass.mp3')

	elif dlt5[0][5] < 1:

		playsound('AuthorizationSendMssg.mp3')



	miConexion12.commit()
	miConexion12.close()


def decrypt_files_ramson_funct():

	wdatos = bytes(password_for_ramson.get(), 'utf-8')
	h = hashlib.new(algoritmo, wdatos)
	hash2 = HASH.generaHash(h)

	miConexion122 = psycopg2.connect(host = 'baak8kinqrfryal5bhvp-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'urnsamk6lldavmbxb6ev', dbname = 'baak8kinqrfryal5bhvp', password = 'nMjCFD00O0DJOmYjbjbZ8sCDdI8wxw')
		
	miCursor122 = miConexion122.cursor()

	sql_verf_hash_ramson = 'select * from Players where nickname = (%s)'
	sql_verf_hash_data_ramson = (nickname_db,)
	miCursor122.execute(sql_verf_hash_ramson, sql_verf_hash_data_ramson)
	dlt909 = miCursor122.fetchall()

	if dlt909[0][5] >= 1 and hash2 == dlt909[0][3]:

		if target_receiver_ramson != '':

			sql_ramson_verf = 'select * from ramson_bird where (client = (%s) and server = (%s) and packet = (%s))'
			sql_ramson_verf_data = (target_receiver_ramson, nickname_db, packet.get())
			miCursor122.execute(sql_ramson_verf, sql_ramson_verf_data)
			df202 = miCursor122.fetchall()
			df12_test = True

			if len(df202) > 0 and df12_test == True:

				archivos = directory
				items = os.listdir(archivos)
				archivos2 = [archivos + '/' + x for x in items]
				execution_decrypt_files(archivos2, key_ramson)
				print(key_ramson)
				ramsonBird_message.insert(tk.END, df202[0][5])

			elif len(df202) == 0:

				playsound('cartoon121.mp3')

	miConexion122.commit()
	miConexion122.close()



def send_message():

	global nickname_db
	global key_encryption
	global token
	global target_person

	bdatos = bytes(passw_em.get(), 'utf-8')
	h = hashlib.new(algoritmo, bdatos)
	hash2 = HASH.generaHash(h)

	miConexion2 = psycopg2.connect(host = 'baak8kinqrfryal5bhvp-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'urnsamk6lldavmbxb6ev', dbname = 'baak8kinqrfryal5bhvp', password = 'nMjCFD00O0DJOmYjbjbZ8sCDdI8wxw')
		
	miCursor2 = miConexion2.cursor()

	sql_verf_hash = 'select * from Players where nickname = (%s)'
	sql_verf_hash_data = (nickname_db,)
	miCursor2.execute(sql_verf_hash, sql_verf_hash_data)
	dlt5 = miCursor2.fetchall()

	if dlt5[0][5] >= 10 and hash2 == dlt5[0][3]:

		if target_person != '':

			sql_verf_server = 'select * from encryptedMessages where (nickname = (%s) and server = (%s))'
			sql_verf_server_data = (nickname_db, target_person)
			miCursor2.execute(sql_verf_server, sql_verf_server_data)
			df1 = miCursor2.fetchall()
			df1_test = True

			if len(df1) == 0 and df1_test == True:

				if token != '' and key_encryption != '':

					#key_encryption = key_encryption.decode()
					sql110 = 'insert into encryptedMessages(nickname, password, server, actual_message, key_b) values(%s,%s,%s,%s,%s)'
					datos_sql110 = (nickname_db, hash2, target_person, token.decode(), key_encryption.decode())
					miCursor2.execute(sql110, datos_sql110)
					playsound('cartoon130.mp3')
					playsound('message_sent_success.mp3')

				elif token == '' or key_encryption == '':

					playsound('StepsForSending.mp3')

			elif len(df1) > 0 and df1_test == True:

				if token != '' and key_encryption != '':

					sql111 = 'update encryptedMessages set (nickname, password, server, actual_message, key_b) = (%s,%s,%s,%s,%s) where (nickname = (%s) and server = (%s))'
					datasql111 = (nickname_db, hash2, target_person, token.decode(), key_encryption.decode(), nickname_db, target_person)
					miCursor2.execute(sql111, datasql111)
					playsound('cartoon130.mp3')
					playsound('message_sent_success.mp3')

				elif token == '' or key_encryption == '':

					playsound('StepsForSending.mp3')

		elif target_person == '':

			playsound('RecipientUsername.mp3')
			df = -1
			df1_test = False


	elif dlt5[0][5] >= 10 and hash2 != dlt5[0][3]:

		playsound('WrongPass.mp3')

	elif dlt5[0][5] < 10:

		playsound('AuthorizationSendMssg.mp3')


	miConexion2.commit()
	miConexion2.close()

	
def displayCiphertext():

	global nickname_db
	global key_encryption
	global token
	global target_person_decrypt
	global message_sent_decrypt
	global key_sent_decrypt
	

	cdatos = bytes(password_for_decrypt.get(), 'utf-8')
	g = hashlib.new(algoritmo, cdatos)
	hash3 = HASH.generaHash(g)

	miConexion3 = psycopg2.connect(host = 'baak8kinqrfryal5bhvp-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'urnsamk6lldavmbxb6ev', dbname = 'baak8kinqrfryal5bhvp', password = 'nMjCFD00O0DJOmYjbjbZ8sCDdI8wxw')
		
	miCursor3 = miConexion3.cursor()

	sql33 = 'select * from Players where nickname = (%s)'
	datasql33 = (nickname_db,)

	sql330 = 'select * from encryptedMessages where server = (%s) and nickname = (%s)'
	datasql330 = (nickname_db, target_person_decrypt)

	miCursor3.execute(sql33, datasql33)
	dlt6 = miCursor3.fetchall()

	if hash3 == dlt6[0][3]:

		if target_person_decrypt != '':

			miCursor3.execute(sql330, datasql330)
			dlt7 = miCursor3.fetchall()

		elif target_person_decrypt == '':

			playsound('perder_incorrecto_no_valido.mp3')
			playsound('activatePersonFirst_toReceive.mp3')

		if len(dlt7) > 0:

			message_sent_decrypt = dlt7[0][5]
			key_sent_decrypt = dlt7[0][4]

			cipher_text3.insert(tk.END, dlt7[0][5])
			cipher_text3.config(font = ("Comic Sans MS", 10))
				
			key_fernet_text2.config(text = dlt7[0][4], justify = 'center', wraplength = 700, font = ('Comic Sans MS', 10))

	elif hash3 != dlt6[0][3]:

		playsound('WrongPass.mp3')


	miConexion3.commit()
	miConexion3.close()


def bc_decription_machine():

	global message_sent_decrypt
	global key_sent_decrypt
	global nickname_db
	global target_person_decrypt

	miConexion3 = psycopg2.connect(host = 'baak8kinqrfryal5bhvp-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'urnsamk6lldavmbxb6ev', dbname = 'baak8kinqrfryal5bhvp', password = 'nMjCFD00O0DJOmYjbjbZ8sCDdI8wxw')

	miCursor3 = miConexion3.cursor()

	sql555 = 'select * from encryptedMessages where server = (%s) and nickname = (%s)'
	datasql555 = (nickname_db, target_person_decrypt)

	miCursor3.execute(sql555, datasql555)
	dlt555 = miCursor3.fetchall()

	a = dlt555[0][5].encode()
	b = dlt555[0][4].encode()
	k = Fernet(b)
	token2 = k.decrypt(a)
	token2 = token2.decode()
	cipher_text2_encrp2.insert(tk.END, token2)
	cipher_text2_encrp2.config(font = ("Comic Sans MS", 10))

	miConexion3.commit()
	miConexion3.close()


def comd_decrypt():

		global key
		global keys
		global message
		global chances_decrypt
		global match
		global coins

		message = secret_messages[index]
		key = player_answer_decrypt.get()
		

		if chances_decrypt <= 3 and key == keys[index]:

			playsound('C:/BirdCipher/Audios/VoiceAudios/CorrectKey.mp3')
			time.sleep(2)
			cipher_text.config(text = getTranslatedMessage(message, key), font = ("Comic Sans MS", 9))
			cipher_text.config(bg = '#050005', fg = '#7e086c')
			coins = coins + 1
			playsound("rightDecrypt.mp3")
			playsound("GoldCoin.mp3")
			updatePlayer_coins()
			labelCoins.config(text = coins)
			match = True
			decrypt_button.config(state = 'disabled')
			

		elif chances_decrypt <= 3 and key!= keys[index]:

			playsound('C:/BirdCipher/Audios/VoiceAudios/WrongKey.mp3')
			cipher_text.config(text = getTranslatedMessage(message, key), font = ("Comic Sans MS", 9))
			cipher_text.config(bg = '#050005', fg = '#FFFFFF')
			chances_decrypt = chances_decrypt + 1

		elif chances_decrypt > 3:

			decrypt_button.config(state = 'disabled')
			playsound('C:/BirdCipher/Audios/VoiceAudios/chances_decrypt.mp3')


def fernet_key_gen():

	global key_encryption
	global key_encryption_test

	key_encryption = Fernet.generate_key()
		
	key_fernet_text.config(text = key_encryption)
	clipboard.copy(key_encryption)
	key_encryption_test = True


def fernet_encryption_function():

	global key_encryption
	global key_encryption_test
	global token

	if key_encryption_test == True:

		message_to_encrypt = cipher_text2.get("1.0", "end-1c")
		message_to_encrypt = message_to_encrypt.encode()
		f = Fernet(key_encryption)
		token = f.encrypt(message_to_encrypt)
		#token = token.decode()
		cipher_text2_encrp.insert(tk.END, token)
		clipboard.copy(token)

	elif key_encryption_test == False:

		playsound('MustGenerateKey.mp3')


def listen_decrypt_text():

	global key
	global keys
	global chances_decrypt
	global crypto_audios_k
	global match

	key = player_answer_decrypt.get()

	if match == True and chances_decrypt <= 3:

		playsound(crypto_audios_k[index])

	elif match == False and chances_decrypt <= 3:
			
		playsound('C:/BirdCipher/Audios/VoiceAudios/WrongKey.mp3')

	elif chances_decrypt > 3:

		playsound('C:/BirdCipher/Audios/VoiceAudios/chances_decrypt.mp3')

def audioPoints():

	playsound()

def coinsAudio():

	playsound()

def feathersAudio():

	playsound()

def diamondsAudio():

	playsound()

def closeMachine():

	global chances_decrypt
	global match
	global target_person
	global target_person_decrypt

	chances_decrypt = 0
	target_person = ''
	target_person_decrypt = ''
	decrypt.destroy()


def person1_actv():

	global target_person

	if person1_var.get() != '':

		person1_activated = True
		person2_activated = False
		person3_activated = False
		person4_activated = False
		target_person = person1_var.get()
		playsound('bambu_click.mp3')
		playsound('activatedPersonA.mp3')

	elif person1_var.get() == '':

		playsound('EnterUsername.mp3')


def person2_actv():

	global target_person

	if person2_var.get() != '':

		person1_activated = False
		person2_activated = True
		person3_activated = False
		person4_activated = False
		target_person = person2_var.get()
		playsound('bambu_click.mp3')
		playsound('activatedPersonA.mp3')

	elif person2_var.get() == '':

		playsound('EnterUsername.mp3')

def person3_actv():

	global target_person

	if person3_var.get() != '':

		person1_activated = False
		person2_activated = False
		person3_activated = True
		person4_activated = False
		target_person = person3_var.get()
		playsound('bambu_click.mp3')
		playsound('activatedPersonA.mp3')

	elif person3_var.get() == '':

		playsound('EnterUsername.mp3')

def person4_actv():

	global target_person

	if person4_var.get() != '':

		person1_activated = False
		person2_activated = False
		person3_activated = False
		person4_activated = True
		target_person = person4_var.get()
		playsound('bambu_click.mp3')
		playsound('activatedPersonA.mp3')

	elif person4_var.get() == '':

		playsound('EnterUsername.mp3')


def person1c_actv():

	global target_person_decrypt

	if person1c_var.get() != '':

		person1c_activated = True
		person2c_activated = False
		person3c_activated = False
		person4c_activated = False
		target_person_decrypt = person1c_var.get()
		playsound('button_click.mp3')
		playsound('activatedPersonB.mp3')

	elif person1c_var.get() == '':

		playsound('activatePersonReceiveMessages.mp3')

def person2c_actv():

	global target_person_decrypt

	if person2c_var.get() != '':

		person1c_activated = False
		person2c_activated = True
		person3c_activated = False
		person4c_activated = False
		target_person_decrypt = person2c_var.get()
		playsound('button_click.mp3')
		playsound('activatedPersonB.mp3')

	elif person2c_var.get() == '':

		playsound('activatePersonReceiveMessages.mp3')

def person3c_actv():

	global target_person_decrypt

	if person3c_var.get() != '':

		person1c_activated = False
		person2c_activated = False
		person3c_activated = True
		person4c_activated = False
		target_person_decrypt = person3c_var.get()
		playsound('button_click.mp3')
		playsound('activatedPersonB.mp3')

	elif person3c_var.get() == '':

		playsound('activatePersonReceiveMessages.mp3')

def person4c_actv():

	global target_person_decrypt

	if person4c_var.get() != '':

		person1c_activated = False
		person2c_activated = False
		person3c_activated = False
		person4c_activated = True
		target_person_decrypt = person4c_var.get()
		playsound('button_click.mp3')
		playsound('activatedPersonB.mp3')

	elif person4c_var.get() == '':

		playsound('activatePersonReceiveMessages.mp3')


def receiver_ramson_actv():

	global target_receiver_ramson

	if receiver_var.get() != '':

		target_receiver_ramson = receiver_var.get()
		playsound('bambu_click.mp3')

	elif receiver_var.get() == '':

		playsound('bambu_click.mp3')