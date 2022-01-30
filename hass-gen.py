#!/bin/python
import hashlib,base64,os,sys,time

# colors
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
cyan = '\033[96m'
black = '\033[1m'

# banner Code

print(green+"Tool is Starting....../"+green)
time.sleep(1)
def banner():
	os.system("clear")
	r ='\033[91m' # red
	g ='\033[92m' # green
	b ='\033[96m' # blue
	y ='\033[93m' # yellow
	bl ='\033[1m' # black
	os.system("clear")
	print(b+bl+"""
	        //  //
	     ==//==//=="""+g+bl+""" ┌  ┐┌──┐┌──┐┌──┐     ┌──┐┌──┐┌──┐"""+b+bl+"""
	      //  //"""+g+bl+"""    ├──┤├──┤└──┐└──┐┌───┐│ ─┐├┤  │  │"""+b+bl+"""
	   ==//==//=="""+g+bl+"""   └  ┘└  ┘└──┘└──┘└───┘└──┘└──┘└  ┘"""+b+bl+"""
	    //  // """+g+bl+"""v 1.0
	""")
	print (y+bl+"                     <===[["+b+bl+" coded by TURB0 "+y+bl+"]]===>"+y+bl+"\n")
	print (y+bl+"                  <---("+r+bl+" GitHub- Turbo Hackers "+y+bl+")--->"+y+bl+"\n")

# gen code

def gen():
	banner()
	print(red+black+" [ "+green+black+"Selected : Hashing {SHA256,MD5}"+red+black+" ]")
	print(" ")
	def sha256_gen():
		banner()
		print(red+black+" [ "+green+black+"Selected : SHA256 Hashing "+red+black+" ]")
		print(" ")
		string_sha256 = input(green+black+"Enter The String :-\n : ")
		result_sha256 = hashlib.sha256(string_sha256.encode())
		print(cyan+black+"\n  String = "+green+black,string_sha256)
		print(cyan+black+"\n  SHA256 Hash = "+green+black,result_sha256.hexdigest())
		print(yellow+black+"\n\t\t["+green+black+"1"+yellow+"]➟ "+green+black+"Main Menu")
		print(yellow+black+"\t\t["+green+black+"2"+yellow+"]➟ "+green+black+"Back")
		print(yellow+black+"\t\t["+green+black+"0"+yellow+black+"]➟ "+green+black+"Exit")
		back_choice = int(input(green+black+"\nSelect Option : "))
		if back_choice == 1:
			main()
		if back_choice == 2:
			gen()
		elif back_choice == 0:
			print(cyan+black+"\nThanks For Using This Program")
		else:
			print(cyan+black+"\n Wrong Input ! , Try again")
			time.sleep(2)
			sha256_gen()
	def md5_gen():
		banner()
		print(red+black+" [ "+green+black+"Selected : MD5 Hashing "+red+black+" ]")
		print(" ")
		string_md5 = input(green+black+"Enter The String :-\n : ")
		result_md5 = hashlib.md5(string_md5.encode())
		print(cyan+black+"\n  String = "+green+black,string_md5)
		print(cyan+black+"\n  MD5 Hash = "+green+black,result_md5.hexdigest())
		print(yellow+black+"\n\t\t["+green+black+"1"+yellow+black+"]➟ "+green+black+"Main Menu")
		print(yellow+black+"\t\t["+green+black+"2"+yellow+black+"]➟ "+green+black+"Back")
		print(yellow+black+"\t\t["+green+black+"0"+yellow+black+"]➟ "+green+black+"Exit")
		back_choice = int(input(green+black+"\nSelect Op/tion : "))
		if back_choice == 1:
			main()
		if back_choice == 2:
			gen()
		elif back_choice == 0:
			print(cyan+black+"\nThanks For Using This Program")
		else:
			print(cyan+black+"\n Wrong Input ! , Try again")
			time.sleep(2)
			md5_gen()
	print(yellow+black+"\t\t\t      ["+green+"1"+yellow+"]➟ "+green+"SHA256")
	print(yellow+black+"\t\t\t      ["+green+"2"+yellow+"]➟ "+green+"MD5")
	print(yellow+black+"\t\t\t      ["+green+"3"+yellow+"]➟ "+green+"Back")
	print(yellow+black+"\t\t\t      ["+green+"0"+yellow+"]➟ "+green+"Exit")
	gen_choice = int(input(green+black+"\nSelect option : "))
	if gen_choice == 1:
		sha256_gen()
	elif gen_choice == 2:
		md5_gen()
	elif gen_choice == 3:
		main_choice()
	elif gen_choice == 0:
		print(cyan+black+"\nThanks For Using This Program")
	else:
		print(cyan+black+"\n Wrong Input ! , Try again")
		time.sleep(2)
		gen()

# verifier code

def verifier():
	banner()
	print(red+black+" [ "+green+black+"Selected : Verifier {SHA256,MD5}"+red+black+" ]")
	print(" ")
	def sha256_verifier():
		banner()
		print(red+black+" [ "+green+black+"Selected : SHA256 Verifier"+red+black+" ]")
		print(" ")
		string1_sha256 = input(green+black+"Enter The Hash String 1 :-\n : ")
		string2_sha256 = input(green+black+"\nEnter The Hash String 2 :-\n : ")
		if (string1_sha256 == string2_sha256):
			print(cyan+black+"\n\t\tHash String is Matching")
			print(yellow+black+"\n\t\t["+green+black+"1"+yellow+"]➟ "+green+black+"Main Menu")
			print(yellow+black+"\t\t["+green+black+"2"+yellow+"]➟ "+green+black+"Back")
			print(yellow+black+"\t\t["+green+black+"0"+yellow+black+"]➟ "+green+black+"Exit")
			back_choice = int(input(green+black+"\nSelect Option : "))
			if back_choice == 1:
				main()
			if back_choice == 2:
				verifier()
			elif back_choice == 0:
				print(cyan+black+"\nThanks For Using This Program")
			else:
				print(cyan+black+"\n Wrong Input ! , Try again")
				time.sleep(2)
				sha256_verifier()
		else:
			print(cyan+black+"\n\t\tHash String is not Matching")
			print(yellow+black+"\n\t\t["+green+black+"1"+yellow+"]➟ "+green+black+"Main Menu")
			print(yellow+black+"\t\t["+green+black+"2"+yellow+"]➟ "+green+black+"Back")
			print(yellow+black+"\t\t["+green+black+"0"+yellow+black+"]➟ "+green+black+"Exit")
			back_choice = int(input(green+black+"\nSelect Option : "))
			if back_choice == 1:
				main()
			if back_choice == 2:
				verifier()
			elif back_choice == 0:
				print(cyan+black+"\nThanks For Using This Program")
			else:
				print(cyan+black+"\n Wrong Input ! , Try again")
				time.sleep(2)
				sha256_verifier()
		print(yellow+black+"\n\t\t["+green+black+"1"+yellow+"]➟ "+green+black+"Main Menu")
		print(yellow+black+"\t\t["+green+black+"2"+yellow+"]➟ "+green+black+"Back")
		print(yellow+black+"\t\t["+green+black+"0"+yellow+black+"]➟ "+green+black+"Exit")
		back_choice = int(input(green+black+"\nSelect Option : "))
		if back_choice == 1:
			main()
		if back_choice == 2:
			verifier()
		elif back_choice == 0:
			print(cyan+black+"\nThanks For Using This Program")
		else:
			print(cyan+black+"\n Wrong Input ! , Try again")
			time.sleep(2)
			sha256_verifier()
	def md5_verifier():
		banner()
		print(red+black+" [ "+green+black+"Selected : MD5 Verifier"+red+black+" ]")
		print(" ")
		string1_md5 = input(green+black+"Enter The String 1 :-\n : ")
		string2_md5 = input(green+black+"Enter The String 2 :-\n : ")
		if (string1_md5 == string2_md5):
			print(cyan+black+"\n\t\tHash String is Matching")
			print(yellow+black+"\n\t\t["+green+black+"1"+yellow+"]➟ "+green+black+"Main Menu")
			print(yellow+black+"\t\t["+green+black+"2"+yellow+"]➟ "+green+black+"Back")
			print(yellow+black+"\t\t["+green+black+"0"+yellow+black+"]➟ "+green+black+"Exit")
			back_choice = int(input(green+black+"\nSelect Option : "))
			if back_choice == 1:
				main()
			if back_choice == 2:
				verifier()
			elif back_choice == 0:
				print(cyan+black+"\nThanks For Using This Program")
			else:
				print(cyan+black+"\n Wrong Input ! , Try again")
				time.sleep(2)
				md5_verifier()
		else:
			print(cyan+black+"\n\t\tHash String is not Matching")
			print(yellow+black+"\n\t\t["+green+black+"1"+yellow+"]➟ "+green+black+"Main Menu")
			print(yellow+black+"\t\t["+green+black+"2"+yellow+"]➟ "+green+black+"Back")
			print(yellow+black+"\t\t["+green+black+"0"+yellow+black+"]➟ "+green+black+"Exit")
			back_choice = int(input(green+black+"\nSelect Option : "))
			if back_choice == 1:
				main()
			if back_choice == 2:
				md5_verifier()
			elif back_choice == 0:
				print(cyan+black+"\nThanks For Using This Program")
			else:
				print(cyan+black+"\n Wrong Input ! , Try again")
				time.sleep(2)
				md5_verifier()
		print(yellow+black+"\n\t\t["+green+black+"1"+yellow+black+"]➟ "+green+black+"Main Menu")
		print(yellow+black+"\t\t["+green+black+"2"+yellow+black+"]➟ "+green+black+"Back")
		print(yellow+black+"\t\t["+green+black+"0"+yellow+black+"]➟ "+green+black+"Exit")
		back_choice = int(input(green+black+"\nSelect Op/tion : "))
		if back_choice == 1:
			main()
		if back_choice == 1:
			md5_verifier()
		elif back_choice == 0:
			print(cyan+black+"\nThanks For Using This Program")
		else:
			print(cyan+black+"\n Wrong Input ! , Try again")
			time.sleep(2)
			md5_verifier()
	print(yellow+black+"\t\t\t      ["+green+"1"+yellow+"]➟ "+green+"SHA256")
	print(yellow+black+"\t\t\t      ["+green+"2"+yellow+"]➟ "+green+"MD5")
	print(yellow+black+"\t\t\t      ["+green+"3"+yellow+"]➟ "+green+"Back")
	print(yellow+black+"\t\t\t      ["+green+"0"+yellow+"]➟ "+green+"Exit")
	verifier_choice = int(input(green+black+"\nSelect option : "))
	if verifier_choice == 1:
		sha256_verifier()
	elif verifier_choice == 2:
		md5_verifier()
	elif verifier_choice == 3:
		main_choice()
	elif verifier_choice == 0:
		print(cyan+black+"\nThanks For Using This Program")
	else:
		print(cyan+black+"\n Wrong Input ! , Try again")
		time.sleep(2)
		verifier()


# base64 code

def base64_gen():
	banner()
	print(red+black+" [ "+green+black+"Selected : Base64 Encoder/Decoder"+red+black+" ]")
	print(" ")
	def base64_encode_gen():
		banner()
		print(red+black+" [ "+green+black+"Selected : Base64 Encoder"+red+black+" ]")
		print(" ")
		string_base64 = input(green+black+"Enter The String To Encode :-\n : ")
		result_base64 = str(base64.b64encode(string_base64.encode("utf-8")),"utf-8")
		print(cyan+black+"\n  String = "+green+black,string_base64)
		print(cyan+black+"\n  Base64 Encoded String = "+green+black,result_base64)
		print(yellow+black+"\n\t\t["+green+black+"1"+yellow+"]➟ "+green+black+"Main Menu")
		print(yellow+black+"\t\t["+green+black+"2"+yellow+"]➟ "+green+black+"Back")
		print(yellow+black+"\t\t["+green+black+"0"+yellow+black+"]➟ "+green+black+"Exit")
		back_choice = int(input(green+black+"\nSelect Option : "))
		if back_choice == 1:
			main()
		if back_choice == 2:
			base64_gen()
		elif back_choice == 0:
			print(cyan+black+"\nThanks For Using This Program")
		else:
			print(cyan+black+"\n Wrong Input ! , Try again")
			time.sleep(2)
			base64_encode_gen()
	def base64_decode_gen():
		banner()
		print(red+black+" [ "+green+black+"Selected : Base64 Decoder"+red+black+" ]")
		print(" ")
		string_base64 = input(green+black+"Enter The String To Decode :-\n : ")
		result_base64 = base64.b64decode(string_base64.encode("ascii")).decode("ascii")
		print(cyan+black+"\n  String = "+green+black,string_base64)
		print(cyan+black+"\n  Base64 Decoded String = "+green+black,result_base64)
		print(yellow+black+"\n\t\t["+green+black+"1"+yellow+"]➟ "+green+black+"Main Menu")
		print(yellow+black+"\t\t["+green+black+"2"+yellow+"]➟ "+green+black+"Back")
		print(yellow+black+"\t\t["+green+black+"0"+yellow+black+"]➟ "+green+black+"Exit")
		back_choice = int(input(green+black+"\nSelect Option : "))
		if back_choice == 1:
			main()
		if back_choice == 2:
			base64_gen()
		elif back_choice == 0:
			print(cyan+black+"\nThanks For Using This Program")
		else:
			print(cyan+black+"\n Wrong Input ! , Try again")
			time.sleep(2)
			base64_decode_gen()
	print(yellow+black+"\t\t\t      ["+green+"1"+yellow+"]➟ "+green+"Base64 Encoding")
	print(yellow+black+"\t\t\t      ["+green+"2"+yellow+"]➟ "+green+"Base64 Decoding")
	print(yellow+black+"\t\t\t      ["+green+"3"+yellow+"]➟ "+green+"Back")
	print(yellow+black+"\t\t\t      ["+green+"0"+yellow+"]➟ "+green+"Exit")
	base_gen_choice = int(input(green+black+"\nSelect option : "))
	if base_gen_choice == 1:
		base64_encode_gen()
	elif base_gen_choice == 2:
		base64_decode_gen()
	elif base_gen_choice == 3:
		main_choice()
	elif base_gen_choice == 0:
		print(cyan+black+"\nThanks For Using This Program")
	else:
		print(cyan+black+"\n Wrong Input ! , Try again")
		time.sleep(2)
		base64_gen()

# choice code

def main_choice():
	banner()
	print(yellow+black+"\t\t\t ["+green+"1"+yellow+"]➟ "+green+"Hashing {SHA256,MD5}")
	print(yellow+black+"\t\t\t ["+green+"2"+yellow+"]➟ "+green+"Verifier {SHA256,MD5}")
	print(yellow+black+"\t\t\t ["+green+"3"+yellow+"]➟ "+green+"Base64 Encoder/Decoder")
	print(yellow+black+"\t\t\t ["+green+"0"+yellow+"]➟ "+green+"Exit")
	choice_1 = int(input(green+black+"\nSelect option : "))
	if choice_1 == 1:
		gen()
	elif choice_1 == 2:
		verifier()
	elif choice_1 == 3:
		base64_gen()
	elif choice_1 == 0:
		print(cyan+black+"\nThanks For Using This Program")
	else:
		print(cyan+black+"\n Wrong Input ! , Try again")
		time.sleep(2)
		s.system("clear")
		print(green+black+"Tool Restarting..../")
		time.sleep(2)
		main_choice()

# main code

def main():
	main_choice()
	
main()

