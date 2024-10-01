import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import time
from playsound import playsound
import hashlib
from cryptography.fernet import Fernet
import pyperclip as clipboard
import psycopg2
import os

from imagenes_ing_social import *
from tests_ing_social import *
from hash import *


points = 0
coins = 0
feathers = 0
diamonds = 0
lives = 5
counter_social_eng = -1


# ------------------------------------ Functions -------------------------------------------------

def login_user():

	wdatos = bytes(password_dbc.get(), 'utf-8')
	h = hashlib.new(algoritmo, wdatos)
	hash2 = HASH.generaHash(h)

	miConexion1 = psycopg2.connect(host = 'bo57mq3swtgbosiuzwsg-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'ultzq6yxafplsmbqjm5a', dbname = 'bo57mq3swtgbosiuzwsg', password = 'rV3Z5hd5SVnXnMuEpXv96SPUuc0brA')
		
	miCursor1 = miConexion1.cursor()

	sql1 = 'select * from users where username = (%s)'
	sql1_data = (username_dbc.get(), )

	sql2 = 'insert into users(username, password, position, points, coins, feathers, diamonds) values(%s,%s,%s,%s,%s,%s,%s)'
	sql2_data = (username_dbc.get(), hash2, position_dbc.get(), 0, 0, 0, 0)

	miCursor1.execute(sql1, sql1_data)
	dlt1 = miCursor1.fetchall()

	if len(dlt1) == 0:

		miCursor1.execute(sql2, sql2_data)
		hash256_passw_label.config(text = hash2)

	miConexion1.commit()
	miConexion1.close()






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


# ------------------------------------------------------------------------------------------------------------------



decrypt = tk.Tk()

decrypt.title("BirdCipher Cryptographic Machine")
decrypt.geometry('1050x540')
decrypt.resizable(0, 0)

username_dbc = tk.StringVar()
password_dbc = tk.StringVar()
position_dbc = tk.StringVar()
player_answer_decrypt = tk.IntVar()
packet = tk.IntVar()
player_message_encrypt = tk.StringVar()
passw_em = tk.StringVar()
password_for_decrypt = tk.StringVar()
password_for_ramson = tk.StringVar()


person1_var = tk.StringVar()
person2_var = tk.StringVar()
person3_var = tk.StringVar()
person4_var = tk.StringVar()

person1c_var = tk.StringVar()
person2c_var = tk.StringVar()
person3c_var = tk.StringVar()
person4c_var = tk.StringVar()

receiver_var = tk.StringVar()

person1_activated = False
person2_activated = False
person3_activated = False
person4_activated = False
	

person1c_activated = False
person2c_activated = False
person3c_activated = False
person4c_activated = False

decrypt_buttonImg = tk.PhotoImage(file = "Decrypt Message-logo1.png")
listen_buttonImg = tk.PhotoImage(file = "Listen to the message-logo1.png")
directory_browser = tk.PhotoImage(file = 'Browse directories.png')
ramson_instructions = tk.PhotoImage(file = 'Instructions.png')
generateRamsonKey_de = tk.PhotoImage(file = 'Generate RamsonBird Key.png')
bringRamsonKey_de = tk.PhotoImage(file = 'Bring RamsonBird key.png')
encryptFilesImage = tk.PhotoImage(file = 'Decrypt files.png')
decryptFilesImage = tk.PhotoImage(file = 'Encrypt files.png')
bc_logo_loginImage = tk.PhotoImage(file = 'BirdCipher Machine-logoLogin-white1.png')

notebk = ttk.Notebook(decrypt)
notebk.pack(expand=True)

hr = ttk.Frame(notebk, width = 1050, height=540)
hr.configure(style = "BW.TLabel")
hr.pack(fill = 'both', expand = True)
notebk.add(hr, text = " Login")

fr0 = ttk.Frame(notebk, width = 1050, height = 540)
fr0.pack(fill = 'both', expand = True)
notebk.add(fr0, text = '   Cybersecurity and social engineering')
		
fr = ttk.Frame(notebk, width = 1050, height=540)
fr.configure(style = "BW.TLabel")
fr.pack(fill = 'both', expand = True)
notebk.add(fr, text = "      BirdCipher Decrypt Machine")

fr2 = ttk.Frame(notebk, width = 1150, height = 540)
fr2.pack(fill = 'both', expand = True)
notebk.add(fr2, text = "   Encryption Machine")

fr3 = ttk.Frame(notebk, width = 1050, height = 540)
fr3.pack(fill = 'both', expand = True)
notebk.add(fr3, text = "   Decryption Machine")

fr0a = ttk.Frame(notebk, width = 1050, height = 540)
fr0a.pack(fill = 'both', expand = True)
notebk.add(fr0a, text = '   RamsonBird Machine')

login_label = tk.Label(hr, text = 'Log in the BirdCipher Machine!!', font = ("Comic Sans MS", 14))
login_label.config(fg = "#7e086c")
login_label.place(x = 50, y = 20)

username_label = tk.Label(hr, text = 'Username', font = ('Comic Sans MS', 12))
username_label.config(fg = "#7e086c")
username_label.place(x = 50, y = 70)

username_entry = tk.Entry(hr, textvariable = username_dbc, font = ('Comic Sans MS', 15), justify = 'center')
username_entry.config(bg = '#050005', fg = '#f7a6f1')
username_entry.place(x = 50, y = 100)

password_label = tk.Label(hr, text = 'Password', font = ('Comic Sans MS', 12))
password_label.config(fg = "#7e086c")
password_label.place(x = 50, y = 160)

password_entry = tk.Entry(hr, textvariable = password_dbc, font = ('Comic Sans MS', 15), justify = 'center')
password_entry.config(bg = '#050005', fg = '#f7a6f1', show = '*')
password_entry.place(x = 50, y = 190)

position_label = tk.Label(hr, text = 'Position', font = ('Comic Sans MS', 12))
position_label.config(fg = "#7e086c")
position_label.place(x = 50, y = 240)

position_entry = tk.Entry(hr, textvariable = position_dbc, font = ('Comic Sans MS', 15), justify = 'center')
position_entry.config(bg = '#050005', fg = '#f7a6f1')
position_entry.place(x = 50, y = 270)

send_login_data = tk.Button(hr, text = 'Send login data', command = lambda:login_user())
send_login_data.config(fg = '#7e086c', font = ('Comic Sans MS', 9))
send_login_data.place(x = 200, y = 320)

hash256_passw = tk.Label(hr, text = 'Your password hash (SHA 256) is:', font = ('Comic Sans MS', 12))
hash256_passw.config(fg = "#7e086c")
hash256_passw.place(x = 20, y = 440)

hash256_passw_label = tk.Label(hr, font = ('Comic Sans MS', 8), width = 62)
hash256_passw_label.config(bg = '#050005', fg = '#f7a6f1')
hash256_passw_label.place(x = 20, y = 480)

hash256passw_copy_btt = tk.Button(hr, text = 'Copy hash to clipboard')
hash256passw_copy_btt.config(fg = '#7e086c', font = ('Comic Sans MS', 9))
hash256passw_copy_btt.place(x = 480, y = 475)

close_machine_from_login = tk.Button(hr, text = '  Close the BirdCipher Machine  ', command = lambda:closeMachine())
close_machine_from_login.config(fg = '#7e086c', font = ('Comic Sans MS', 14))
close_machine_from_login.place(x = 700, y = 460)

bc_logo_login = tk.Label(hr, image = bc_logo_loginImage)
bc_logo_login.config(bg = '#260223')
bc_logo_login.place(x = 420, y = 30)


cipher_text = tk.Text(fr, font = ("Comic Sans MS", 9))
#cipher_text.place(x = 30, y = 30)
#cipher_text.pack(pady = 30)
cipher_text.config(bg = '#050005', fg = '#FFFFFF', padx = 30)
cipher_text.place(x = 60, y = 60)

nicknameCuad = tk.Entry(fr, textvariable=player_answer_decrypt, font = ("Comic Sans MS", 13), justify = "center")
#nicknameCuad.config(bg="black", fg="green")
#nicknameCuad.place(x=50, y=55)
#nicknameCuad.pack(padx = 30, pady = 30)
nicknameCuad.config(bg = '#050005', fg = '#7e086c')
nicknameCuad.place(x = 790, y = 100)
	
decrypt_button = tk.Button(fr, image = decrypt_buttonImg, font = ("Comic Sans MS", 8), command = lambda:comd_decrypt())
decrypt_button.config(fg = '#1af017')
decrypt_button.place(x = 800, y = 150)
	
decrypt_listen = tk.Button(fr, image = listen_buttonImg, font = ("Comic Sans MS", 8), command = lambda:listen_decrypt_text())
decrypt_listen.config(fg = '#1af017')
decrypt_listen.place(x = 900, y = 150)
	
imagen_caesar_cipher = tk.PhotoImage(file = 'Imagen_caesar.png')
imagePoints = tk.PhotoImage(file = "Points-logo1.png")
imageCoins = tk.PhotoImage(file = "Gold Coins-logo1.png")
imageFeathers = tk.PhotoImage(file = "Feather-logo1.png")
imageDiamonds = tk.PhotoImage(file = "Diamond-logo1.png")
imageLives = tk.PhotoImage(file = "Lives-logo1.png")
cryptoMachineImage = tk.PhotoImage(file = "Cryptographic Machine-logo1.png")
ramson_image = tk.PhotoImage(file = 'RamsonBird_MachineImage.png')

imagen_caesar_cipher_lab = tk.Label(fr, image = imagen_caesar_cipher)
#imagen_caesar_cipher_lab.config(bg = '#FFFFFF')
imagen_caesar_cipher_lab.place(x = 30, y = 300)

titleBirdCipherMachine = tk.Label(fr, text = "BirdCipher message about", font = ("Comic Sans MS", 12))
titleBirdCipherMachine.config(fg = "#7e086c")
titleBirdCipherMachine.place(x = 70, y = 8)

buttonPoints = tk.Button(fr, image = imagePoints, command = lambda:pointsAudio())
buttonPoints.place(x = 210, y = 300)

buttonCoins = tk.Button(fr, image = imageCoins, command = lambda:coinsAudio())
buttonCoins.place(x = 300, y = 300)

buttonFeathers = tk.Button(fr, image =imageFeathers, command = lambda:feathersAudio())
buttonFeathers.place(x = 400, y = 300)

buttonDiamonds = tk.Button(fr, image = imageDiamonds, command = lambda:diamondsAudio())
buttonDiamonds.place(x= 500, y = 300)

buttonLives = tk.Button(fr, image = imageLives, command = lambda:livesAudio())
buttonLives.place(x = 615, y = 300)

labelPoints = tk.Label(fr, text = points, font = ("Comic Sans MS", 13), justify = "center", width = 6)
labelPoints.config(bg = "#050005", fg = "#7e086c")
labelPoints.place(x = 212, y = 410)

labelCoins = tk.Label(fr, text = coins, font = ("Comic Sans MS", 13), justify = "center", width = 8)
labelCoins.config(bg = "#050005", fg = "#7e086c")
labelCoins.place(x = 300, y = 410)

labelFeathers = tk.Label(fr, text = feathers, font = ("Comic Sans MS", 13), justify = "center", width = 8)
labelFeathers.config(bg = "#050005", fg = "#7e086c")
labelFeathers.place(x = 400, y = 410)

labelDiamonds = tk.Label(fr, text = diamonds, font = ("Comic Sans MS", 13), justify = "center", width = 8)
labelDiamonds.config(bg = "#050005", fg = "#7e086c")
labelDiamonds.place(x = 500, y = 410)

labelLives = tk.Label(fr, text = lives, font = ("Comic Sans MS", 13), justify = "center", width = 7)
labelLives.config(bg = "#050005", fg = "#7e086c")
labelLives.place(x = 617, y = 410)

labelQuestionKey = tk.Label(fr, text = "Enter the secret key", font = ("Comic Sans MS", 13))
labelQuestionKey.config(fg = "#7e086c")
labelQuestionKey.place(x = 805, y = 60)

labelPlayerBCM = tk.Label(fr, text = "Welcome, ", font = ("Comic Sans MS", 11))
labelPlayerBCM.config(fg = "#7e086c", bg = "#050005")
labelPlayerBCM.place(x = 830, y = 20)

imageCryptographicMachine = tk.Label(fr, image = cryptoMachineImage)
imageCryptographicMachine.place(x = 750, y = 260)

closeMachineButton = tk.Button(fr, text = "Close the BirdCipher Cryptographic Machine", font = ("Comic Sans MS", 12), command = lambda:closeMachine())
closeMachineButton.place(x = 250, y = 460)
closeMachineButton.config(fg = "#7e086c")


# ---------------

def play_social_eng_audio():

	playsound(social_eng_audio[index_social_eng_choose])

def send_answer_social_eng():

	global feathers

	if varOption.get() == correct_answers_social_eng[index_social_eng_choose]:

		playsound('wonFeather.mp3')
		feathers = feathers + 1
		updatePlayer_feathers()
		labelFeathers.config(text = feathers)
		answer_button_social_eng.config(state = 'disabled')

	elif varOption.get() != correct_answers_social_eng[index_social_eng_choose]:

		playsound('lostFeather.mp3')
		answer_button_social_eng.config(state = 'disabled')


counter_social_eng = counter_social_eng + 1
index_social_eng = list(range(44))
index_social_eng_choose = index_social_eng[counter_social_eng]
img_social_eng = tk.PhotoImage(file = imagenes_ing_social[index_social_eng_choose])
varOption = tk.IntVar()

img_social_eng_label = tk.Button(fr0, image = img_social_eng, command = lambda:play_social_eng_audio())
img_social_eng_label.place(x = 30, y = 30)
img_social_eng_label.config(bg = '#20011c')

rad_button1 = tk.Radiobutton(fr0, text = tests_ing_social[index_social_eng_choose][0], variable = varOption, value = 0)
rad_button1.place(x = 550, y = 40)
rad_button1.config(font = ('Comic Sans MS', 9), justify = 'left')

rad_button2 = tk.Radiobutton(fr0, text = tests_ing_social[index_social_eng_choose][1], variable = varOption, value = 1)
rad_button2.place(x = 550, y = 80)
rad_button2.config(font = ('Comic Sans MS', 9), justify = 'left')

rad_button3 = tk.Radiobutton(fr0, text = tests_ing_social[index_social_eng_choose][2], variable = varOption, value = 2)
rad_button3.place(x = 550, y = 120)
rad_button3.config(font = ('Comic Sans MS', 9), justify = 'left')

rad_button4 = tk.Radiobutton(fr0, text = tests_ing_social[index_social_eng_choose][3], variable = varOption, value = 3)
rad_button4.place(x = 550, y = 160)
rad_button4.config(font = ('Comic Sans MS', 9), justify = 'left')

answer_button_social_eng = tk.Button(fr0, text = 'Send answer', command = lambda:send_answer_social_eng())
answer_button_social_eng.place(x = 600, y = 200)
answer_button_social_eng.config(fg = 'purple', font = ('Comic Sans MS', 9))
	

# ---------------

	
encryption_machine_logo = tk.PhotoImage(file = "Send Encrypted Message-logo.png")
generate_key_image = tk.PhotoImage(file = "Generate Key-logo.png")
encrypt_message_image = tk.PhotoImage(file = "Encrypt Message-logo1.png")
person1_image = tk.PhotoImage(file = 'Person1.png')
person2_image = tk.PhotoImage(file = 'Person2.png')
person3_image = tk.PhotoImage(file = 'Person3.png')
person4_image = tk.PhotoImage(file = 'Person4.png')
receiver_ramson_image = tk.PhotoImage(file = 'Receiver.png')

cipher_text2 = tk.Text(fr2, font = ("Comic Sans MS", 10), width = 80)
cipher_text2.config(bg = '#050005', fg = '#FFFFFF', padx = 30)
cipher_text2.place(x = 60, y = 40, height = 70)

scrollVetrn = tk.Scrollbar(fr2, command = cipher_text2.yview)
scrollVetrn.place(x = 710, y = 40)

key_fernet_label = tk.Label(fr2, text = "Key for Fernet algorithm")
key_fernet_label.config(font = ("Comic Sans MS", 12), fg = "#7e086c")
key_fernet_label.place(x = 65, y = 120)

key_fernet_text = tk.Label(fr2, text = "", font = ("Comic Sans MS", 10), width = 80)
key_fernet_text.config(bg = "#050005", fg = "#FFFFFF")
key_fernet_text.place(x = 60, y = 150)

encrypted_label = tk.Label(fr2, text = "Your encrypted message is: ")
encrypted_label.config(font = ("Comic Sans MS", 12), fg = "#7e086c")
encrypted_label.place(x = 65, y = 180)
	
cipher_text2_encrp = tk.Text(fr2, font = ("Comic Sans MS", 7), width = 105)
cipher_text2_encrp.config(bg = '#050005', fg = '#FFFFFF', padx = 8)
cipher_text2_encrp.place(x = 60, y = 210, height = 80)

scrollVetrn2 = tk.Scrollbar(fr2, command = cipher_text2_encrp.yview)
scrollVetrn2.place(x = 710, y = 210)

nicknameCuad2 = tk.Entry(fr2, textvariable = passw_em, font = ("Comic Sans MS", 13), justify = "center")
nicknameCuad2.config(bg = '#050005', fg = '#7e086c')
nicknameCuad2.place(x = 790, y = 100)
	
fernet_key_button = tk.Button(fr2, image = generate_key_image, font = ("Comic Sans MS", 8), command = lambda:fernet_key_gen())
fernet_key_button.config(fg = '#7e086c')
fernet_key_button.place(x = 800, y = 150)
	
fernet_encryption_message = tk.Button(fr2, image = encrypt_message_image, font = ("Comic Sans MS", 8), command = lambda:fernet_encryption_function())
fernet_encryption_message.config(fg = '#1af017')
fernet_encryption_message.place(x = 900, y = 150)

imagen_caesar_cipher_lab2 = tk.Label(fr2, image = imagen_caesar_cipher)
imagen_caesar_cipher_lab2.place(x = 30, y = 300)

titleBirdCipherMachine2 = tk.Label(fr2, text = "BirdCipher Encryption Machine: a tool to guarantee the confidentiality of your messages", font = ("Comic Sans MS", 12))
titleBirdCipherMachine2.config(fg = "#7e086c")
titleBirdCipherMachine2.place(x = 70, y = 8)

buttonPoints2 = tk.Button(fr2, image = imagePoints, command = lambda:pointsAudio())
buttonPoints2.place(x = 210, y = 300)

buttonPerson1a = tk.Button(fr2, image = person1_image, command = lambda:person1_actv())
buttonPerson1a.place(x = 300, y = 300)

buttonPerson2a = tk.Button(fr2, image = person2_image, command = lambda:person2_actv())
buttonPerson2a.place(x = 400, y = 300)

buttonPerson3a = tk.Button(fr2, image = person3_image, command = lambda:person3_actv())
buttonPerson3a.place(x= 500, y = 300)

buttonPerson4a = tk.Button(fr2, image = person4_image, command = lambda:person4_actv())
buttonPerson4a.place(x = 615, y = 300)

labelPoints2 = tk.Label(fr2, text = points, font = ("Comic Sans MS", 13), justify = "center", width = 6)
labelPoints2.config(bg = "#050005", fg = "#7e086c")
labelPoints2.place(x = 212, y = 410)

person1 = tk.Entry(fr2, textvariable = person1_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
person1.config(bg = "#050005", fg = "#7e086c")
person1.place(x = 300, y = 410)

person2 = tk.Entry(fr2, textvariable = person2_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
person2.config(bg = "#050005", fg = "#7e086c")
person2.place(x = 400, y = 410)

person3 = tk.Entry(fr2, textvariable = person3_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
person3.config(bg = "#050005", fg = "#7e086c")
person3.place(x = 500, y = 410)

person4 = tk.Entry(fr2, textvariable = person4_var, font = ("Comic Sans MS", 13), justify = "center", width = 7)
person4.config(bg = "#050005", fg = "#7e086c")
person4.place(x = 617, y = 410)

labelQuestionKey2 = tk.Label(fr2, text = "Enter your password", font = ("Comic Sans MS", 13))
labelQuestionKey2.config(fg = "#7e086c")
labelQuestionKey2.place(x = 805, y = 60)

labelPlayerBCM2 = tk.Label(fr2, text = "Welcome", font = ("Comic Sans MS", 11))
labelPlayerBCM2.config(fg = "#7e086c", bg = "#050005")
labelPlayerBCM2.place(x = 830, y = 20)

imageCryptographicMachine2 = tk.Button(fr2, image = encryption_machine_logo, command = lambda:send_message())
imageCryptographicMachine2.place(x = 760, y = 290)
imageCryptographicMachine2.config(bg = "#3f0322")

closeMachineButton2 = tk.Button(fr2, text = "Close the BirdCipher Cryptographic Machine", font = ("Comic Sans MS", 12), command = lambda:closeMachine())
closeMachineButton2.place(x = 250, y = 460)
closeMachineButton2.config(fg = "#7e086c")

# --------------

cipher_text3 = tk.Text(fr3, font = ("Comic Sans MS", 10), width = 72, height = 4)
cipher_text3.config(bg = '#050005', fg = '#FFFFFF', padx = 8)
cipher_text3.place(x = 60, y = 40)

scrollVetrn3 = tk.Scrollbar(fr3, command = cipher_text3.yview)
scrollVetrn3.place(x = 710, y = 40)

nicknameCuad3 = tk.Entry(fr3, textvariable=password_for_decrypt, font = ("Comic Sans MS", 13), justify = "center")
nicknameCuad3.config(bg = '#050005', fg = '#7e086c')
nicknameCuad3.place(x = 790, y = 100)

decrypt_button3 = tk.Button(fr3, image = decrypt_buttonImg, font = ("Comic Sans MS", 8), command = lambda:displayCiphertext())
decrypt_button3.config(fg = '#1af017')
decrypt_button3.place(x = 800, y = 150)
	
decrypt_listen3 = tk.Button(fr3, image = listen_buttonImg, font = ("Comic Sans MS", 8), command = lambda:listen_decrypt_text())
decrypt_listen3.config(fg = '#1af017')
decrypt_listen3.place(x = 900, y = 150)

imagen_caesar_cipher_lab3 = tk.Label(fr3, image = imagen_caesar_cipher)
#imagen_caesar_cipher_lab.config(bg = '#FFFFFF')
imagen_caesar_cipher_lab3.place(x = 30, y = 300)

titleBirdCipherMachine3 = tk.Label(fr3, text = "BirdCipher Decryption Machine", font = ("Comic Sans MS", 12))
titleBirdCipherMachine3.config(fg = "#7e086c")
titleBirdCipherMachine3.place(x = 70, y = 8)

key_fernet_label2 = tk.Label(fr3, text = "Key for Fernet algorithm")
key_fernet_label2.config(font = ("Comic Sans MS", 12), fg = "#7e086c")
key_fernet_label2.place(x = 65, y = 120)

key_fernet_text2 = tk.Label(fr3, text = "", font = ("Comic Sans MS", 10), width = 80)
key_fernet_text2.config(bg = "#050005", fg = "#FFFFFF")
key_fernet_text2.place(x = 60, y = 150)

encrypted_label2 = tk.Label(fr3, text = "Your decrypted message is: ")
encrypted_label2.config(font = ("Comic Sans MS", 12), fg = "#7e086c")
encrypted_label2.place(x = 65, y = 180)
	
cipher_text2_encrp2 = tk.Text(fr3, font = ("Comic Sans MS", 10), width = 80)
cipher_text2_encrp2.config(bg = '#050005', fg = '#FFFFFF', padx = 8)
cipher_text2_encrp2.place(x = 60, y = 210, height = 80)

scrollVetrn4 = tk.Scrollbar(fr3, command = cipher_text2_encrp2.yview)
scrollVetrn4.place(x = 710, y = 210)

buttonPoints3 = tk.Button(fr3, image = imagePoints, command = lambda:pointsAudio())
buttonPoints3.place(x = 210, y = 300)

buttonPerson1b = tk.Button(fr3, image = person1_image, command = lambda:person1c_actv())
buttonPerson1b.place(x = 300, y = 300)

buttonPerson2b = tk.Button(fr3, image = person2_image, command = lambda:person2c_actv())
buttonPerson2b.place(x = 400, y = 300)

buttonPerson3b = tk.Button(fr3, image = person3_image, command = lambda:person3c_actv())
buttonPerson3b.place(x= 500, y = 300)

buttonPerson4b = tk.Button(fr3, image = person4_image, command = lambda:person4c_actv())
buttonPerson4b.place(x = 615, y = 300)

labelPoints3 = tk.Label(fr3, text = points, font = ("Comic Sans MS", 13), justify = "center", width = 6)
labelPoints3.config(bg = "#050005", fg = "#7e086c")
labelPoints3.place(x = 212, y = 410)

person1_c = tk.Entry(fr3, text = person1c_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
person1_c.config(bg = "#050005", fg = "#7e086c")
person1_c.place(x = 300, y = 410)

person2_c = tk.Entry(fr3, text = person2c_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
person2_c.config(bg = "#050005", fg = "#7e086c")
person2_c.place(x = 400, y = 410)

person3_c = tk.Entry(fr3, text = person3c_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
person3_c.config(bg = "#050005", fg = "#7e086c")
person3_c.place(x = 500, y = 410)

person4_c = tk.Entry(fr3, text = person4c_var, font = ("Comic Sans MS", 13), justify = "center", width = 7)
person4_c.config(bg = "#050005", fg = "#7e086c")
person4_c.place(x = 617, y = 410)

labelQuestionKey3 = tk.Label(fr3, text = "Enter your password", font = ("Comic Sans MS", 13))
labelQuestionKey3.config(fg = "#7e086c")
labelQuestionKey3.place(x = 805, y = 60)

labelPlayerBCM3 = tk.Label(fr3, text = "Welcome, ", font = ("Comic Sans MS", 11))
labelPlayerBCM3.config(fg = "#7e086c", bg = "#050005")
labelPlayerBCM3.place(x = 830, y = 20)

imageCryptographicMachine3 = tk.Button(fr3, image = cryptoMachineImage, command = lambda:bc_decription_machine())
imageCryptographicMachine3.place(x = 730, y = 260)

closeMachineButton3 = tk.Button(fr3, text = "Close the BirdCipher Cryptographic Machine", font = ("Comic Sans MS", 12), command = lambda:closeMachine())
closeMachineButton3.place(x = 250, y = 460)
closeMachineButton3.config(fg = "#7e086c")

# ---------------------------

ramsonBird_message = tk.Text(fr0a, font = ("Comic Sans MS", 10), width = 72, height = 4)
ramsonBird_message.config(bg = '#050005', fg = '#FFFFFF', padx = 30)
ramsonBird_message.place(x = 60, y = 40)

labelPlayerBCM3 = tk.Label(fr0a, text = "Welcome,", font = ("Comic Sans MS", 11))
labelPlayerBCM3.config(fg = "#7e086c", bg = "#050005")
labelPlayerBCM3.place(x = 830, y = 20)

labelQuestionKey3 = tk.Label(fr0a, text = "Enter your password", font = ("Comic Sans MS", 13))
labelQuestionKey3.config(fg = "#7e086c")
labelQuestionKey3.place(x = 805, y = 60)

ramsonBird_password = tk.Entry(fr0a, textvariable=password_for_ramson, font = ("Comic Sans MS", 13), justify = "center")
ramsonBird_password.config(bg = '#050005', fg = '#7e086c')
ramsonBird_password.place(x = 790, y = 100)

ramsonBird_directory = tk.Button(fr0a, image = directory_browser, font = ("Comic Sans MS", 8), command = lambda:selectDirectory())
ramsonBird_directory.config(fg = '#1af017')
ramsonBird_directory.place(x = 800, y = 150)
	
ramsonBird_instructions = tk.Button(fr0a, image = ramson_instructions, font = ("Comic Sans MS", 8), command = lambda:listen_decrypt_text())
ramsonBird_instructions.config(fg = '#1af017')
ramsonBird_instructions.place(x = 930, y = 150)

ramsonBird_Image = tk.Label(fr0a, image = ramson_image)
ramsonBird_Image.config(bg = '#20011c')
ramsonBird_Image.place(x = 60, y = 280)

ramsonBirdMessageTitle = tk.Label(fr0a, text = "Enter your message for identifying the ramson action", font = ("Comic Sans MS", 12))
ramsonBirdMessageTitle.config(fg = "#7e086c")
ramsonBirdMessageTitle.place(x = 70, y = 8)

ramsonKeyTitle = tk.Label(fr0a, text = "Key for Fernet algorithm")
ramsonKeyTitle.config(font = ("Comic Sans MS", 12), fg = "#7e086c")
ramsonKeyTitle.place(x = 65, y = 120)

ramsonKey = tk.Label(fr0a, text = "", font = ("Comic Sans MS", 10), width = 80)
ramsonKey.config(bg = "#050005", fg = "#FFFFFF")
ramsonKey.place(x = 60, y = 150)

ramsonDirectoryTitle = tk.Label(fr0a, text = "You have chosen the directory: ")
ramsonDirectoryTitle.config(font = ("Comic Sans MS", 12), fg = "#7e086c")
ramsonDirectoryTitle.place(x = 65, y = 180)
	
ramsonDirectoryUrl = tk.Label(fr0a, text = "", font = ("Comic Sans MS", 10), width = 80)
ramsonDirectoryUrl.config(bg = '#050005', fg = '#FFFFFF')
ramsonDirectoryUrl.place(x = 60, y = 210, height = 30)

buttonReceiver = tk.Button(fr0a, image = receiver_ramson_image, command = lambda:receiver_ramson_actv())
buttonReceiver.place(x = 570, y = 280)

entry_receiver_ramson = tk.Entry(fr0a, textvariable = receiver_var, font = ("Comic Sans MS", 13), justify = "center", width = 13)
entry_receiver_ramson.config(bg = "#050005", fg = "#7e086c")
entry_receiver_ramson.place(x = 570, y = 430)

packet_entry = tk.Entry(fr0a, textvariable = packet, font = ('Comic Sans MS', 11), justify = 'center', width = 6)
packet_entry.place(x = 650, y = 465)
packet_entry.config(bg = '#050005', fg = '#7e086c')

packet_label = tk.Label(fr0a, text = 'Packet No. ', font = ('Comic Sans MS', 11))
packet_label.place(x = 570, y = 465)
packet_label.config(fg = '#7e086c')

generateKeyRamson = tk.Button(fr0a, image = generateRamsonKey_de, command = lambda:generate_key_ramson())
generateKeyRamson.place(x = 330, y = 280)

bringKeyRamson = tk.Button(fr0a, image = bringRamsonKey_de, command = lambda:bring_key_ramson())
bringKeyRamson.place(x = 330, y = 390)

encryptFilesButton = tk.Button(fr0a, image = decryptFilesImage, command = lambda:encrypt_files_ramson_funct())
encryptFilesButton.place(x = 830, y = 260)

decryptFilesButton = tk.Button(fr0a, image = encryptFilesImage, command = lambda:decrypt_files_ramson_funct())
decryptFilesButton.place(x = 830, y = 380)




#decrypt.protocol("WM_DELETE_WINDOW", lambda: None)

decrypt.mainloop()

