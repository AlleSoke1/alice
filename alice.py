# -*- coding: utf-8 -*-
#!/usr/bin/env python
#the year is [2012]
#Alin1337 - creat undeva prin luna Aprilie 
import alice_lib
from cbot import ChatterBotFactory, ChatterBotType
import random
import sys
import re
import hashlib
import urllib
import urllib2
#import pyfoobar
import cmd
import time
import threading
#import thread
import datetime
import os.path
from random import randrange
import pickle
if sys.version_info[0] > 2:
	import urllib.request as urlreq
else:
	import urllib2 as urlreq


	
dictionary = dict() #volatile... of course...





#from pyfoobar import foobar
#fb2k = foobar()

#initialize QUIZ
QuizActiv = False
QuizID = -1
QuizRow = -1
#alte variabile
isFreeze = False
EnableTalk = True

##variabile de jucat ^^
isDefineActiv = True

dancemoves = [
	"(>^.^)>",
	"(v^.^)v",
	"v(^.^v)",
	"<(^.^<)"
]



ver = "1.5.0.7 - 12 July 2014 (zummer)"

cuvinte_care_dauneaza_grav_ochiilor = [
	"xxxxx",
	"xxxxx"
]

banned_list = [
	"royalgoofansub",
	"animekage",
	"deseneanimechat"
] #bad boys bad boys we`re gonna get you.

administratori = [
	"arinsupahaka",
	"alin1337",
	"alindesuka",
	"masy10",
	"melty1"
] #her` masters
	
	
class Alice(alice_lib.RoomManager):
	def onInit(self):
		self.setNameColor("F9F")
		self.setFontColor("222") #kuroi wa FFF 
		self.setFontFace("1") 
		self.setFontSize(11)
	#	self.setTimeout(15, room.reconnect(),NULL)
		self.enableRecording()
		self.enableBg()

	# prompt = 'Alice: '
	
	
	#q = Quote(number, text, agree, disagree)


		
	
	def onConnect(self, room):
		#print("^_^ connected i Am!")
		#room.message("Arisu koko ni aru!")
		#room.message("Alice este aici.")
		#START QUIZ
		print("[%s] --- Alice Engine STATO --- ver:%s"%(room.name,ver))
		def quiz():
			def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("(.*)<br />(.*)<br />(.*)<br />(.*)<br />(.*)<br /><id>(.*?)</id>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>QUIZ:</b> <br /> %s  <br />A. %s  <br />B. %s  <br />C. %s <br />D. %s <br />" %(m.group(1),m.group(2),m.group(3),m.group(4),m.group(5))).replace("%20", " "), html = True)
						#print("%s <br" % (m.group(2)))
						global QuizID
						QuizID = m.group(6)
						#room.message("%s"%(QuizID))
					else:
						room.message("Probleme , incearca mai tarziu...")
					#http://tracker.anime-nolimit.ro/api.php?data=nr rezultatului
			now = datetime.datetime.now()
		#	if now.hour <1 and now.hour >=8:  #check , sa mearga de la 8 la 24
			self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_quiz.php?get_question")
			global QuizActiv
			QuizActiv = True
			t = threading.Timer(3600, quiz) #1ora
			t.start()
		#t = threading.Timer(3600, quiz) #1ora
		#t.start()
		
		#CUPON !!!
		def cupon():
			def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("<cod>(.*?)</cod>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>COD:</b> <br /> %s  <br /><br />?????" %(m.group(1))).replace("%20", " "), html = True)
					else:
						room.message("Probleme , incearca mai tarziu...")
			self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_cupon.php?get")
			t2 = threading.Timer(10800, cupon) #1ora
			t2.start()
		#t2 = threading.Timer(10800, cupon) #1ora
		#t2.start()	
		#ANNOUNCER !!!
		def announcer():
		#	while True:
			def rfinish(doc):
				doc = doc.read().decode()
				m = re.search("<r>(.*)", doc, re.DOTALL | re.IGNORECASE)
				if m:
					room.message(("%s" %(m.group(1))).replace("%20", " "), html = True)
			#	else:
			#		room.message("Probleme , nu pot lua feed-ul...")
			self.deferToThread(rfinish, urlreq.urlopen, "http://catalin.linu.ro/py_forum_stuff.php?get&grup=%s"%(room.name))
			def spinit():
				time.sleep(60)
				announcer()
			spinit()
		#thread.start_new_thread(announcer)
		#threading.start_new_thread(announcer, ())
			
#self.deferToThread( self , callback , func )
		#t2 = threading.Timer(60, announcer) #1 minut
		#t2.start()	

		
	def onReconnect(self, room):
		print("Reconnected")
	
	def onDisconnect(self, room):
		print("Disconnected")
	
	def onMessage(self, room, user, message):
		
	#	if os.path.exists("/alice/remind/"+user.name.lower()+".txt"):
	#		file = open("/alice/remind/"+user.name.lower()+'.txt','r')
	#		data = file.read()
	#		file.close()
	#		final = data.replace(' \n','')
	#		room.message(final)
	#		print(final)
	#		print(data)
	#		os.remove("/alice/remind/"+user.name.lower()+".txt")
	
		#if room.getLevel(self.user) > 0:
		#	print(room.name,message.ip,user.name,message.body)
		#else:
	
		#	print(room.name,user.name,message.body)
	
		if self.user == user: return
		
		
		#log ^^
		#if user.name[0:1] != "!" and user.name[0:1] != "#" and len(message.ip) >1 : #diferit de restu userilor normali si sa aiba si ip.
		#	def rfinish(doc):
		#			doc = doc.read().decode()
		#			m = re.search("<return>ok</return>", doc, re.DOTALL | re.IGNORECASE)
		#			if m:
		#				print("%s added to db!"%(user.name))
		#	self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_log.php?user=%s&ip=%s"%(user.name,message.ip))
		
		#BAN
		
#		if message.ip[1:8] == "92.81.26":
	
		#FIX ALIN HTTPS://
		
		#if message.body[0:8] == "https://" and user.name in administratori:
	#		link = "http://" + message.body[8:].split()[0]
#			room.message("> [link fix] : %s"%(link))
		
		#REMIND CHECK
		def check_if_remind_is_there(doc):
				doc = doc.read().decode()
				m = re.search("<r>(.*)</r>", doc, re.DOTALL | re.IGNORECASE)
				if m:
					room.message(("<br />%s" %(m.group(1))).replace("%20", " "), html = True)
		if user.name[0:1] != "!" and user.name[0:1] != "#":
			self.deferToThread(check_if_remind_is_there, urlreq.urlopen, "http://alice.loa.ro/py_remind.php?check&user=%s"%(user.name))

		
		#LOG CHAT
		if len(message.ip) >1: #diferit de restu userilor normali si sa aiba si ip.
			def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("<return>ok</return>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						print("%s added to db!"%(user.name))
			self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_chat.php?store&user=%s&ip=%s&grup=%s&mesaj=%s"%(user.name,message.ip,room.name,message.body))
			def rfinish2(doc):
					doc = doc.read().decode()
					m = re.search("<raspuns>(.*)</raspuns>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("%s" %(m.group(1))).replace("%20", " "), html = True)			
			self.deferToThread(rfinish2, urlreq.urlopen, "http://alice.loa.ro/py_qanda.php?nume=%s&text=%s"%(user.name,message.body))
		else:
			def rfinish3(doc):
				doc = doc.read().decode()
				m = re.search("<return>ok</return>", doc, re.DOTALL | re.IGNORECASE)
				if m:
					print("%s added to db!"%(user.name))
			self.deferToThread(rfinish3, urlreq.urlopen, "http://alice.loa.ro/py_chat.php?store&user=%s&ip=N/A&grup=%s&mesaj=%s"%(user.name,room.name,message.body))


			#if message.ip == "79.117.140.187" or message.ip == "89.39.13.90":
			#room.message("Salutare %s !" %(user.name))
			#	print("%s - s-a conectat"%(user.name))
			def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("", doc, re.DOTALL | re.IGNORECASE)
			self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_log.php?user=%s&ip=%s"%(user.name,message.ip))
	
		if message.body == "alice cine esti":
			room.message("Nu-i treaba ta %s !" %(user.name))
		
		if message.body == "alice":
			room.message("da?")
		
		if message.body[:31] == "http://www.youtube.com/watch?v=" or message.body[:27] == "http://youtube.com/watch?v=" or message.body[0:24] == "www.youtube.com/watch?v=":
			nohttp = False
			if(message.body[:24] == "www.youtube.com/watch?v="):
				link = "http://" + message.body
				nohttp = True
			def rfinish(doc):
					doc = doc.read().decode()
					m = re.search('<meta name="title" content="(.*?)">', doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>Titlu Video-ului:</b> %s " %(m.group(1))).replace("%20", " "), html = True)
			if nohttp == True:
				self.deferToThread(rfinish, urlreq.urlopen, link)
			else:
				self.deferToThread(rfinish, urlreq.urlopen, message.body)
		
		#questions / quiz
		global QuizActiv
		global QuizID
		global QuizRow
		if QuizActiv == True:
			if message.body == "A" or message.body == "B" or  message.body == "C" or  message.body == "D" or message.body == "a" or message.body == "b" or  message.body == "c" or  message.body == "d":
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("<raspuns>(.*?)</raspuns><rezultat>(.*?)</rezultat><reward>(.*?)</reward>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>%s</b> <br /><br /> <i>%s</i>" %(m.group(1),m.group(3))).replace("%20", " "), html = True)
						QuizRow = m.group(2)
						if QuizRow == "1":
							global QuizActiv
							QuizActiv = False
						if QuizRow == "0":
							QuizActiv = False
							#room.message("%s"%(QuizRow))
					else:
						room.message("Probleme , incearca mai tarziu...")
					#http://tracker.anime-nolimit.ro/api.php?data=nr rezultatului
				self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_quiz.php?answer_question=%s&user=%s&question_id=%s"%(message.body,user.name,QuizID)) #ultimele 3
				#room.message("%s,%s,%s"%(message.body,user.name,QuizID))
			
		
		#if message.body[1:] == "sall" or message.body == ":sal" or message.body[1:6] == "salut" or message.body[1:6] == "neata" or message.body[1:7] == "neatza":
		#	room.message("Buna ^_^")
		
		#DEFINITIILE	
		#global isDefineActiv
	#	if isDefineActiv == True:
	#		if message.body[0:2] == ":!" and len(message.body[2:]) > 1:
	#			cuvant = str(message.body[2:])
		#		if os.path.exists("/alice/define/"+room.name+"_"+cuvant+".txt"):
	#				file = open("/alice/define/"+room.name+"_"+cuvant+".txt", 'r')
	#				definitie = file.read()
	#				file.close()
	#				room.message(definitie,html=True)
				
	#	clever bot
		global EnableTalk
		if message.body[0:1] == "-" and len(message.body[1:]) > 1 and EnableTalk == True:
			data = str(message.body[1:])
			factory = ChatterBotFactory()
			
			bot1 = factory.create(ChatterBotType.CLEVERBOT)
			bot1session = bot1.create_session()
			room.message("> " + bot1session.think(data)) #hehe... echo :3
	
	#if room.name != "anime-noshit":
	#		if message.body[0:1] == "-" and len(message.body[1:]) > 1:
	#			data = message.body[1:]
	#			cb = Session()
	#			room.message("> " + cb.Ask(data)) #hehe... echo :3
				
		#	room.message("Exemplu:  -Hello")
			
		#if message.body[0:3] == ":))" or message.body[0:4] == " :))" or message.body[0:3] == "=))" or message.body[0:4] == " =))":
		#	if(user.name == 'alin1337'):
		#		room.message("Kawaii ^_^ , %s-kun" %(user.name))
		#	else:
		#		room.message("%s , what's so funny?" %(user.name))
		if room.name=="animekage" or room.name=="desene-anime-online":
			return;
			
		if message.body[0:1] == "/":
			data = message.body[1:].split(" ", 1)
			if len(data) > 1:
				cmd, args = data[0], data[1]
			else:
				cmd, args = data[0], ""
		#	if   cmd == "delay":
		#		self.setTimeout(int(args), room.message, ":D")
			if cmd == "randomuser":
				room.message(random.choice(room.usernames))
		#	elif cmd == "foo":
				#if user.name in administratori:
					#room.message("<br />Acum Canta :<br /><b>%s - %s</b> [%s]" %(fb2k.getCurrentArtist(),fb2k.getCurrentTrack(),fb2k.lengthOfTrack()),html = True)
				#room.message("Now Playing : %s " %(fb2k.isCurrentlyPlaying())
			elif cmd == "mylvl":
				room.message("Your mod level: %i" %(room.getLevel(user)))
			elif cmd == "quiz":
				room.message("Imi pare rau , dar quiz-ul este DEZACTIVAT , lacking questions!")
			elif cmd == "ban":
				if user.name in administratori:
		#			print(args)
		#			room.banUser(args)
					room.message("Salut %s , tocmai ai luat ban ^_^."%(args))
				else:
					room.message("Stop hitting yourself.")
		#	elif cmd == "quiz":
		#		def rfinish(doc):
		#			doc = doc.read().decode()
		#			m = re.search("(.*)<br />(.*)<br />(.*)<br />(.*)<br />(.*)<br /><id>(.*?)</id>", doc, re.DOTALL | re.IGNORECASE)
		#			if m:
		#				room.message(("<b>QUIZ:</b> <br /> %s  <br />A. %s  <br />B. %s  <br />C. %s <br />D. %s <br />" %(m.group(1),m.group(2),m.group(3),m.group(4),m.group(5))).replace("%20", " "), html = True)
		#				#print("%s <br" % (m.group(2)))
		#				global QuizID
		#				QuizID = m.group(6)
		#				#room.message("%s"%(QuizID))
		#			else:
		#				room.message("Probleme , incearca mai tarziu...")
		#			#http://tracker.anime-nolimit.ro/api.php?data=nr rezultatului
		#		self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_quiz.php?get_question") #ultimele 3
		#		QuizActiv = True
			elif cmd == "s" and user.name in administratori:
				room.message(args,html=True)
			elif cmd == "sp" and user.name in administratori:
				room.message(args,html=True)
				room.clearUser(user)
			elif cmd == "ver":
				room.message("Alice Version: " + ver)
			elif cmd == "rawr":
				r = randrange(0,len(random_foks))
				room.message("<big>%s</big>"%(random_foks[r]),html=True)
			elif cmd == "top":
				if len(args) > 1:
					if args == "loli":
						def rfinish(doc):
							doc = doc.read().decode()
#1 - alin1337 - 73<br />2 - dumytru - 49<br />3 - doomyy3 - 33<br />4 - zeusandreo - 32<br />5 - blacksakuraa - 28<br />
							m = re.search("(.*)", doc, re.DOTALL | re.IGNORECASE)
							if m:
								room.message(("<br />%s" %(m.group(1))).replace("%20", " "), html = True)
							else:
								room.message("Probleme , incearca mai tarziu...")
						self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_top.php?loli&grup=%s"%(room.name)) 
					
					elif args == "quiz":
						def rfinish(doc):
							doc = doc.read().decode()
							m = re.search("(.*)", doc, re.DOTALL | re.IGNORECASE)
							if m:
								room.message(("<br />%s" %(m.group(1))).replace("%20", " "), html = True)
							else:
								room.message("Probleme , incearca mai tarziu...")
						self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_top.php?quiz&grup=%s"%(room.name)) 
				else:
					room.message("<br /> <i>/top loli <br /> /top quiz </i>", html = True)
			elif cmd == "a":
				if len(args) > 1:
					s = (args.split(","))
					if len(s) <= 1:
						room.message("ex: /a <cuvant1> , <cuvant2> , <cuvant3> , etc")
					else:
						room.message("%s: %s"%(user.name,''.join(random.sample(s,1))))
				else:
					room.message("ex: /a <cuvant1> , <cuvant2> , <cuvant3> , etc")
			elif cmd == "ping":
				room.message("PONG")
			elif cmd == "pong":
				room.message("1 - 0 Mai jucam?")
			elif cmd == "iloveyou":
				if user.name in administratori:
					room.message("<b>%s</b> : <FONT COLOR='#FF0000'>I</FONT><FONT COLOR='#FFff00'> </FONT><FONT COLOR='#00ff00'>l</FONT><FONT COLOR='#00ffff'>o</FONT><FONT COLOR='#0000ff'>v</FONT><FONT COLOR='#FF00ff'>e</FONT><FONT COLOR='#FF0000'> </FONT><FONT COLOR='#FFff00'>y</FONT><FONT COLOR='#00ff00'>o</FONT><FONT COLOR='#00ffff'>u</FONT><FONT COLOR='#0000ff'>!</FONT>" %(user.name), html = True)		
				else:
					room.message("go away");
			elif cmd == "horizon":
				room.message("http://www.emptyblue.it/data/wallpaper/KyoukaiSenjouNoHorizon/kyoukai_senjou_no_horizon_0983_thumb.jpg");
			elif cmd == "clear":
				if room.getLevel(user) > 0:
					room.clearUser(user)
				#else:
				#	room.clearUser(user)
			elif cmd == "clearall":
				def administrator():
					if room.getLevel(user) > 0:
						return True
				if administrator() == True:
					room.clearall()
					print("clear ok")
				if user.name in administratori:
					room.clearall()
					print("clear ok")
			elif cmd == "clearme":
				if user.name in administratori:
					room.clearUser(user)
				#room.clearUser(self.user)
				#room.clearUser(str('alin1337'))
			elif cmd == "help":
				if user.name in administratori:
					room.message("Sunt aici pentru a te ajuta!")
				room.message("Alice HELPER:<br /><br />/info - ajutor <br />/help - ajutor  <br /> /joke - spune o gluma  <br /> /nou - arata ultimul release <br /> /find nume anime - cauta in torente(ex: /find guilty) <br /> /join roomname -intra pe alte roomuri(ex: /join anime-nolimit) <br /> /dance - danseaza <br /> /td <cuvant> -  <br /> /a -  lucruri la nimereala <br /> /fuckoff <br /> /fml - Fuck My Life <br /> /gag - random 9gag post <br/> /img anime girl - poze <br/> /youtube anime music - cauta pe youtube <br/> /whois nume - cauta persoane cu acelasi ip (MODS ONLY) <br/> /remind <nume> <mesaj> : ex /remind alin1337 ce mai faci? <br/>", html=True)
			elif cmd == "info":
					room.message("-- (catalin@linu.ro) --")
					room.message("-- Alin1337 created me --")
					room.message("-- Running %s version on http://alice.loa.ro --"%(ver))
			elif cmd == "dance":
				for i, msg in enumerate(dancemoves):
					self.setTimeout(i / 2, room.message, msg)
				#room.message("%s"%(random.sample(dancemoves,1)))
				#for i, msg in enumerate(dancemoves):
				#	self.setTimeout(i / 2, room.message, msg)
			elif cmd == "fuckoff":
				room.message("%s s-a enervat!  }|+50 " %(user.name))
			elif cmd == "bunny":
				room.message("<br /><br /> ()_()<br />(-'.'-)<br />(,(')(')",html=True)
			elif cmd == "katszzu":
				room.message("http://avarez.ru/uploads/posts/2009-09/1252888296_1250537252_ne-takie-kak-vse_18783_s__13.jpg")
		#	elif cmd == "cod":
			#	def rfinish(doc):
				#	doc = doc.read().decode()
				#	m = re.search('<cod>(.*?)</cod>', doc, re.DOTALL | re.IGNORECASE)
				#	if m:
					#	room.message(("<br /><b>COD: </b><br /> %s" %(m.group(1))).replace("%20", " "), html = True)
				#self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_cupon.php?get_fake")
			elif cmd == "gag":
				def er(doc):
					doc = doc.read().decode()
					m = re.search('<link rel="image_src" href="(.*?)"', doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("%s" %(m.group(1))).replace("%20", " "), html = True)
					else:
						room.message("Nu am gasit asa ceva...")
				self.deferToThread(er, urlreq.urlopen, "http://9gag.com/random")
			elif cmd == "td":
				word = args\
					.replace(" ", "%20")\
					.replace("&", "%26")\
					.replace("%", "%25")\
					.replace("<", "%3C")\
					.replace("=", "%3D")
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("<h1>(.*?)</h1>\n(.*?)<BR><i>(.*)</i>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>%s:</b> <i>%s</i> - %s" %(m.group(1), m.group(2), m.group(3))).replace("%20", " "), html = True)
					else:
						room.message("Nu am gasit asa ceva...")
				self.deferToThread(rfinish, urlreq.urlopen, "http://thesurrealist.co.uk/slang.cgi?ref=" + word)
			elif cmd == "joke":
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("</p><p><b>(.*?)</b></p><p>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>Joke:</b> <i>%s </i>" %(m.group(1))).replace("%20", " "), html = True)
					else:
						room.message("Eroare :( ...")
				self.deferToThread(rfinish, urlreq.urlopen, "http://www.gpeters.com/laugh/google-laugh.php")
			#	room.message('Oprit momentan...')
			elif cmd == "fml":
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("TEXT: (.*?) FML", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>%s:</b> <i>%s FML</i>" %(user.name,m.group(1))).replace("%20", " "), html = True)
					else:
						room.message("Eroare :( ...")
				self.deferToThread(rfinish, urlreq.urlopen, "http://rscript.org/lookup.php?type=fml")
			elif cmd == "nou":
				def rfinish(doc):
					doc = doc.read().decode()
#<tr><a href='http://tracker.anime-nolimit.ro/torrents/<? echo $data[1]; ?>.torrent'>link</a></tr><br /><tr><? echo $data[1]; ?></tr>
					m = re.search("<tr>NR:(.*)<a href='(.*)'>link</a></tr><tr>(.*?)</tr><tr>(.*?)</tr><tr>NR:(.*)<a href='(.*)'>link</a></tr><tr>(.*?)</tr><tr>(.*?)</tr><tr>NR:(.*)<a href='(.*)'>link</a></tr><tr>(.*?)</tr><tr>(.*?)</tr>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>Ce e nou :</b> <br /> #%s <i>%s</i> - Urcat de %s <br /> <a href='%s'>Click Aici pentru Download Torrent</a><br /><br /> #%s <i>%s</i> - Urcat de %s <br /> <a href='%s'>Click Aici pentru Download Torrent</a><br /><br /> #%s <i>%s</i> - Urcat de %s <br /> <a href='%s'>Click Aici pentru Download Torrent</a>" %(m.group(1),m.group(3),m.group(4),m.group(2),m.group(5),m.group(7),m.group(8),m.group(6),m.group(9),m.group(11),m.group(12),m.group(10))).replace("%20", " "), html = True)
						#print("%s <br" % (m.group(2)))
					else:
						room.message("Nici un rezultat gasit...")
					#http://tracker.anime-nolimit.ro/api.php?data=nr rezultatului
				self.deferToThread(rfinish, urlreq.urlopen, "http://tracker.anime-nolimit.ro/api.php") #ultimele 3
			elif cmd == "loli": 
				def queryloli(doc): #get loli
					doc = doc.read().decode()
					m = re.search("<div id='main'>(.*?)</div><div id='rezultat'>(.*?)</div>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>LoliBot :</b> <br /> %s <br /> %s " %(m.group(1),m.group(2))).replace("%20", " "), html = True)
						#print("%s <br" % (m.group(2)))
					else:
						room.message("Erroare...")
				if user.name[0:1] != "!" and user.name[0:1] != "#":
					self.deferToThread(queryloli, urlreq.urlopen, "http://alice.loa.ro/py_rori.php?user=%s&grup=%s"%(user.name,room.name))	
				else:
					room.message("Trebuie sa fii logat.")
			elif cmd == "loli2" and user.name in administratori: 
				def queryloli_2(doc): #get loli
					doc = doc.read().decode()
					m = re.search("<div id='main'>(.*?)</div><div id='rezultat'>(.*?)</div>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>LoliBot :</b> <br /> %s <br /> %s " %(m.group(1),m.group(2))).replace("%20", " "), html = True)
						#print("%s <br" % (m.group(2)))
					else:
						room.message("Erroare...")
				if user.name[0:1] != "!" and user.name[0:1] != "#":
					self.deferToThread(queryloli_2, urlreq.urlopen, "http://alice.loa.ro/py_rori_v2.php?user=%s&grup=%s"%(user.name,room.name))	
				else:
					room.message("Trebuie sa fii logat.")
			elif cmd[1:6] == "loli###":
				def queryloli(doc): #ia loli
					doc = doc.read().decode()
					m = re.search("<div id='rezultat'>(.*?)</div>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>LoliBot :</b> <br /> %s <br /> %s " %(m.group(1))).replace("%20", " "), html = True)
						#print("%s <br" % (m.group(2)))
					else:
						room.message("Eroare...")
				self.deferToThread(queryloli, urlreq.urlopen, "http://alice.loa.ro/py.php?query=%s"%(user.name))	
			elif cmd == "img":
				if len(args) > 1:
					def img(doc):
						doc = doc.read().decode()
						m = re.search("<cod>(.*?)</cod>", doc, re.DOTALL | re.IGNORECASE)
						if m:
							room.message(("<b>%s:</b> <br />%s" %(user.name,m.group(1))).replace("%20", " "), html = True)
						else:
							room.message("Eroare...")
					self.deferToThread(img, urlreq.urlopen, "http://alice.loa.ro/py_curl_meme.php?cauta=%s"%(args))	
				else:
					room.message("ex: /img anime cosplay")
			elif cmd == "stopbot":
				EnableTalk=False
			elif cmd == "startbot":
				EnableTalk=True
			elif cmd == "youtube":
				if len(args) > 1:
					def youtube(doc):
						doc = doc.read().decode()
						m = re.search("<cod>(.*?)</cod><durata>(.*?)</durata><titlu>(.*?)</titlu><views>(.*?)</views>", doc, re.DOTALL | re.IGNORECASE)
						if m:
							room.message(("<b>%s:</b> <br /> %s [%s] <br /> %s Vizualizari<br /> %s" %(user.name,m.group(3),m.group(2),m.group(4),m.group(1))).replace("%20", " "), html = True)
						else:
							room.message("Nu am gasit nimic...")
					self.deferToThread(youtube, urlreq.urlopen, "http://alice.loa.ro/py_youtube.php?cauta=%s"%(args))	
				else:
					room.message("ex: /youtube anime music")
			elif cmd == "find":
				if len(args) > 1:
					def cautatorrent(doc):
						doc = doc.read().decode()
						m = re.search("(.*)", doc, re.DOTALL | re.IGNORECASE)
						if m:
							room.message(("<b>Rezultate pentru '%s':</b> <br /> %s"%(args,m.group(1))).replace("%20", " "), html = True)
						else:	
							room.message("Nu am gasit nimic...")
					self.deferToThread(cautatorrent, urlreq.urlopen, "http://alice.loa.ro/py_find.php?cauta=%s"%(args))	
				else:
					room.message("ex: /find numele anime-ului")		
			elif cmd == "join":
				if len(args) > 1:
					if args.split()[0] in banned_list:
						room.message("My master won't let me there.")
					else:
						args = args.split()[0] #DAMN MAGIE DE MAGIE haha
						room.message("Am intrat pe %s"%(args))
						self.joinRoom(args)
			elif cmd == "quit" and user.name in administratori:
				#room.message("Bye Bye.")
				self.leaveRoom(room.name)
			elif cmd == "restart" and user.name in administratori:
				sys.exit(0)
			elif cmd == "reboot" and user.name in administratori:
				sys.exit(0)
			elif cmd == "ban_class" and user.name in administartori:	
				if len(args) > 1:
					room.message("Sure thing , %s is my target."%(args))
			#elif cmd == "define":
			#	if len(args) > 1 and 'ca' in message.body:
				#	global isDefineActiv
				#	if isDefineActiv == True:
					
				#		define = message.body.split(' ca ', 1)
			#	cuvant = str(define[0][9:])
				#		definitie = define[1]
					#	room.message("<b>%s</b> este definit ca '%s'  "%(cuvant,definitie),html=True)
						
				#		if os.path.exists("/alice/define/"+room.name+"_"+cuvant+".txt"):
				#			room.message("Este deja definit.",html=True)
				#		else:
				#			room.message("Am definit!")
				#			file = open("/alice/define/"+room.name+"_"+cuvant+".txt", 'w')
				#			file.writelines(definitie)
				#			file.close()
						
			#		elif isDefineActiv == False:
			#			room.message("Define este dezactivat , incearca mai tarziu.")
		#	elif cmd == "define-off" and user.name in administratori:
			#	global isDefineActiv
		#		isDefineActiv = False
		#		room.message("Define a fost dezactivat.")
		#	elif cmd == "define-on" and user.name in administratori:
				#global isDefineActiv
		#		isDefineActiv = True
		#		room.message("Define a fost activat.")
		#	elif cmd == "undefine":
		#		cuvant = args
		#		if room.getLevel(user) > 0 or user.name in administratori:
		#			if os.path.exists("/alice/define/"+room.name+"_"+cuvant+".txt"):
		#				os.remove("/alice/define/"+room.name+"_"+cuvant+".txt")
		#				room.message(args + " sters.")
		#			else:
		#				room.message("Nimic de sters.")
			
	#		elif cmd == 'remind':	
		#		if args.find(' ') != -1:
		#			target,mesaj = args.split(" ",1)
		#			target = target.lower()
		#			if os.path.exists('/alice/remind/'+target+'.txt'):
		#				file = open(target+'.txt','a+')
		#				file.write("(REMINDER) " + target + ": " + mesaj + " -from " + user.name +' \n')
		#				room.message("I will remind " + target + " when i next see them speak")
		#			else:
		#				file = open('/alice/remind/'+target+'.txt','a+')
		#				file.write("(REMINDER) " + target + ": " + mesaj + " -from " + user.name +' \n')
		#				room.message("I will remind " + target + " when i next see them speak")
		#		else:
		#			room.message("Incorrect, please type like this: /rmind alice(user) + you message.")
			elif cmd == "remind":
				if args.find(' ') != -1:
					target,mesaj = args.split(" ",1)
					target = target.lower()
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("<r>(.*)</r>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<br />%s" %(m.group(1))).replace("%20", " "), html = True)
					else:
						room.message("Probleme , incearca mai tarziu...")
				if user.name[0:1] != "!" and user.name[0:1] != "#":
					self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_remind.php?store&user=%s&mesaj=%s&sender=%s"%(target,mesaj,user.name))
				else:
					room.message("Trebuie sa fii logat.")
			elif cmd == "loli_sub" and user.name in administratori:
				if args.find(' ') != -1:
					target,mesaj = args.split(" ",1)
					target = target.lower()
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("<r>(.*)</r>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<br />%s" %(m.group(1))).replace("%20", " "), html = True)
					else:
						room.message("Probleme , incearca mai tarziu...")
				self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_rori_manager.php?scade&user=%s&loli=%s"%(target,mesaj))
			elif cmd == "loli_add" and user.name in administratori:
				if args.find(' ') != -1:
					target,mesaj = args.split(" ",1)
					target = target.lower()
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("<r>(.*)</r>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<br />%s" %(m.group(1))).replace("%20", " "), html = True)
					else:
						room.message("Probleme , incearca mai tarziu...")
				self.deferToThread(rfinish, urlreq.urlopen, "http://alice.loa.ro/py_rori_manager.php?aduna&user=%s&loli=%s"%(target,mesaj))
			elif cmd == "whois" and room.getLevel(user) > 0:
				if len(args) > 1:
					def cautatorrent(doc):
						doc = doc.read().decode()
						m = re.search("<r>(.*)</r>", doc, re.DOTALL | re.IGNORECASE)
						if m:
							room.message(("<b>Rezultate pentru '%s':</b> <br /> %s"%(args,m.group(1))).replace("%20", " "), html = True)
						else:	
							room.message("Nu am gasit nimic...")
					self.deferToThread(cautatorrent, urlreq.urlopen, "http://alice.loa.ro/py_whois.php?namae=%s"%(args))	
				else:
					room.message("ex: /whois nume")				
					
	def onFloodWarning(self, room):
		room.reconnect()
	
	def onDisconnect(self,room):
		room.reconnect()
		
	#def onJoin(self, room, user):
		#print(user._ip)
		#if user.ip[0:6] == "46.214.":
		#	room.message("Ce faci noktiz? (:")
	#	print(user.name)
	
#	def onLeave(self, room, user):
#		room.message("ja ne, " + user.name + "!")
	
#	def onUserCountChange(self, room):
#		print("users: " + str(room.usercount))
	#<a href="torrents/Kore%20wa%20Zombie%20Desu%20ka%20of%20the%20Dead%20-%2002%20%5B720p%5D%5BRoSub%5D.torrent" class='hiddenlink' alt='titlu'>Kore wa Zombie Desu ka of the Dead - 02 [720p][RoSub]</a>
#	def onMessageDelete(self, room, user, msg):
#		room.message("Cineva a sters un mesaj! " + user.name + ": " + msg.body)
	
#	def onPMMessage(self, pm, user, body):
#		cb = Session()
#		pm.message(user, cb.Ask(body)) #speak with CLEVERBOT modafaka
#				
		


if __name__ == "__main__": 
#	print(ver)
	Alice.easy_start(['anime-nolimit','hentai-nolimit','animekage','desene-anime-online'],'AliceAishite','S3x123')
	
