#!/usr/bin/env python3
# coded by TURB0
# github https://github.com/turbo-hackers

import hashlib,base64,os,sys,time

# colors
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
cyan = '\033[96m'
reset = '\033[0m'

# banner Code
def banner():
	os.system("clear")
	r ='\033[91m' # red
	g ='\033[92m' # green
	b ='\033[96m' # blue
	y ='\033[93m' # yellow
	reset = '\033[0m'
	blink = "\033[5;96m"
	os.system("clear")
	print(b+"""
	        //  //
	     ==//==//=="""+g+""" ┌  ┐┌──┐┌──┐┌  ┐     ┌──┐┌──┐┌──┐"""+b+"""
	      //  //"""+g+"""    ├──┤├──┤└──┐├──┤┌───┐│ ─┐├┤  │  │"""+b+"""
	   ==//==//=="""+g+"""   └  ┘└  ┘└──┘└  ┘└───┘└──┘└──┘└  ┘"""+b+"""
	    //  // """+g+"""v 1.0
	"""+reset)
	print (y+"                     <===[["+b+" coded by"+blink+" TURB0 "+reset+y+"]]===>\n"+reset)
	print (y+"                  <---("+r+" GitHub- Turbo Hackers "+y+")--->"+reset+"\n")

# gen code

def gen():
	banner()
	print(red+" [ "+green+"Selected : Hashing {SHA256,MD5}"+red+" ]"+reset)
	print(" ")
	def sha256_gen():
		banner()
		print(red+" [ "+green+"Selected : SHA256 Hashing "+red+" ]"+reset)
		print(" ")
		string_sha256 = input(green+"Enter The String :-\n : "+reset)
		result_sha256 = hashlib.sha256(string_sha256.encode())
		print(cyan+"\n  String = "+green,string_sha256)
		print(cyan+"\n  SHA256 Hash = "+green,result_sha256.hexdigest())
		print(yellow+"\n\t\t["+green+"1"+yellow+"]➟ "+green+"Main Menu"+reset)
		print(yellow+"\t\t["+green+"2"+yellow+"]➟ "+green+"Back"+reset)
		print(yellow+"\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
		back_choice = int(input(green+"\nSelect Option : "+reset))
		if back_choice == 1:
			main()
		if back_choice == 2:
			gen()
		elif back_choice == 0:
			print(cyan+"\nThanks For Using This Program"+reset)
		else:
			print(cyan+"\n Wrong Input ! , Try again"+reset)
			time.sleep(2)
			sha256_gen()
	def md5_gen():
		banner()
		print(red+" [ "+green+"Selected : MD5 Hashing "+red+" ]"+reset)
		print(" ")
		string_md5 = input(green+"Enter The String :-\n : "+reset)
		result_md5 = hashlib.md5(string_md5.encode())
		print(cyan+"\n  String = "+green,string_md5)
		print(cyan+"\n  MD5 Hash = "+green,result_md5.hexdigest())
		print(yellow+"\n\t\t["+green+"1"+yellow+"]➟ "+green+"Main Menu"+reset)
		print(yellow+"\t\t["+green+"2"+yellow+"]➟ "+green+"Back"+reset)
		print(yellow+"\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
		back_choice = int(input(green+"\nSelect Op/tion : "+reset))
		if back_choice == 1:
			main()
		if back_choice == 2:
			gen()
		elif back_choice == 0:
			print(cyan+"\nThanks For Using This Program"+reset)
		else:
			print(cyan+"\n Wrong Input ! , Try again"+reset)
			time.sleep(2)
			md5_gen()
	print(yellow+"\t\t\t      ["+green+"1"+yellow+"]➟ "+green+"SHA256"+reset)
	print(yellow+"\t\t\t      ["+green+"2"+yellow+"]➟ "+green+"MD5"+reset)
	print(yellow+"\t\t\t      ["+green+"3"+yellow+"]➟ "+green+"Back"+reset)
	print(yellow+"\t\t\t      ["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
	gen_choice = int(input(green+"\nSelect option : "+reset))
	if gen_choice == 1:
		sha256_gen()
	elif gen_choice == 2:
		md5_gen()
	elif gen_choice == 3:
		main_choice()
	elif gen_choice == 0:
		print(cyan+"\nThanks For Using This Program"+reset)
	else:
		print(cyan+"\n Wrong Input ! , Try again"+reset)
		time.sleep(2)
		gen()

# verifier code

def verifier():
	banner()
	print(red+" [ "+green+"Selected : Verifier {SHA256,MD5}"+red+" ]"+reset)
	print(" ")
	def sha256_verifier():
		banner()
		print(red+" [ "+green+"Selected : SHA256 Verifier"+red+" ]"+reset)
		print(" ")
		string1_sha256 = input(green+"Enter The Hash String 1 :-\n : "+reset)
		string2_sha256 = input(green+"\nEnter The Hash String 2 :-\n : "+reset)
		if (string1_sha256 == string2_sha256):
			print(cyan+"\n\t\t!!! Hash String is Matching !!!"+reset)
			print(yellow+"\n\t\t["+green+"1"+yellow+"]➟ "+green+"Main Menu"+reset)
			print(yellow+"\t\t["+green+"2"+yellow+"]➟ "+green+"Back"+reset)
			print(yellow+"\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
			back_choice = int(input(green+"\nSelect Option : "+reset))
			if back_choice == 1:
				main()
			if back_choice == 2:
				verifier()
			elif back_choice == 0:
				print(cyan+"\nThanks For Using This Program"+reset)
			else:
				print(cyan+"\n Wrong Input ! , Try again"+reset)
				time.sleep(2)
				sha256_verifier()
		else:
			print(cyan+"\n\t\tHash String is not Matching"+reset)
			print(yellow+"\n\t\t["+green+"1"+yellow+"]➟ "+green+"Main Menu"+reset)
			print(yellow+"\t\t["+green+"2"+yellow+"]➟ "+green+"Back"+reset)
			print(yellow+"\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
			back_choice = int(input(green+"\nSelect Option : "+reset))
			if back_choice == 1:
				main()
			if back_choice == 2:
				verifier()
			elif back_choice == 0:
				print(cyan+"\nThanks For Using This Program"+reset)
			else:
				print(cyan+"\n Wrong Input ! , Try again"+reset)
				time.sleep(2)
				sha256_verifier()
		print(yellow+"\n\t\t["+green+"1"+yellow+"]➟ "+green+"Main Menu"+reset)
		print(yellow+"\t\t["+green+"2"+yellow+"]➟ "+green+"Back"+reset)
		print(yellow+"\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
		back_choice = int(input(green+"\nSelect Option : "+reset))
		if back_choice == 1:
			main()
		if back_choice == 2:
			verifier()
		elif back_choice == 0:
			print(cyan+"\nThanks For Using This Program"+reset)
		else:
			print(cyan+"\n Wrong Input ! , Try again"+reset)
			time.sleep(2)
			sha256_verifier()
	def md5_verifier():
		banner()
		print(red+" [ "+green+"Selected : MD5 Verifier"+red+" ]"+reset)
		print(" ")
		string1_md5 = input(green+"Enter The String 1 :-\n : "+reset)
		string2_md5 = input(green+"Enter The String 2 :-\n : "+reset)
		if (string1_md5 == string2_md5):
			print(cyan+"\n\t\t!!! Hash String is Matching !!!"+reset)
			print(yellow+"\n\t\t["+green+"1"+yellow+"]➟ "+green+"Main Menu"+reset)
			print(yellow+"\t\t["+green+"2"+yellow+"]➟ "+green+"Back"+reset)
			print(yellow+"\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
			back_choice = int(input(green+"\nSelect Option : "+reset))
			if back_choice == 1:
				main()
			if back_choice == 2:
				verifier()
			elif back_choice == 0:
				print(cyan+"\nThanks For Using This Program"+reset)
			else:
				print(cyan+"\n Wrong Input ! , Try again"+reset)
				time.sleep(2)
				md5_verifier()
		else:
			print(cyan+"\n\t\tHash String is not Matching"+reset)
			print(yellow+"\n\t\t["+green+"1"+yellow+"]➟ "+green+"Main Menu"+reset)
			print(yellow+"\t\t["+green+"2"+yellow+"]➟ "+green+"Back"+reset)
			print(yellow+"\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
			back_choice = int(input(green+"\nSelect Option : "+reset))
			if back_choice == 1:
				main()
			if back_choice == 2:
				md5_verifier()
			elif back_choice == 0:
				print(cyan+"\nThanks For Using This Program"+reset)
			else:
				print(cyan+"\n Wrong Input ! , Try again"+reset)
				time.sleep(2)
				md5_verifier()
		print(yellow+"\n\t\t["+green+"1"+yellow+"]➟ "+green+"Main Menu"+reset)
		print(yellow+"\t\t["+green+"2"+yellow+"]➟ "+green+"Back"+reset)
		print(yellow+"\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
		back_choice = int(input(green+"\nSelect Op/tion : "+reset))
		if back_choice == 1:
			main()
		if back_choice == 1:
			md5_verifier()
		elif back_choice == 0:
			print(cyan+"\nThanks For Using This Program"+reset)
		else:
			print(cyan+"\n Wrong Input ! , Try again"+reset)
			time.sleep(2)
			md5_verifier()
	print(yellow+"\t\t\t      ["+green+"1"+yellow+"]➟ "+green+"SHA256"+reset)
	print(yellow+"\t\t\t      ["+green+"2"+yellow+"]➟ "+green+"MD5"+reset)
	print(yellow+"\t\t\t      ["+green+"3"+yellow+"]➟ "+green+"Back"+reset)
	print(yellow+"\t\t\t      ["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
	verifier_choice = int(input(green+"\nSelect option : "+reset))
	if verifier_choice == 1:
		sha256_verifier()
	elif verifier_choice == 2:
		md5_verifier()
	elif verifier_choice == 3:
		main_choice()
	elif verifier_choice == 0:
		print(cyan+"\nThanks For Using This Program"+reset)
	else:
		print(cyan+"\n Wrong Input ! , Try again"+reset)
		time.sleep(2)
		verifier()


# base64 code

def base64_gen():
	banner()
	print(red+" [ "+green+"Selected : Base64 Encoder/Decoder"+red+" ]"+reset)
	print(" ")
	def base64_encode_gen():
		banner()
		print(red+" [ "+green+"Selected : Base64 Encoder"+red+" ]"+reset)
		print(" ")
		string_base64 = input(green+"Enter The String To Encode :-\n : "+reset)
		result_base64 = base64.b64encode(string_base64.encode("utf-8")).decode("utf-8")
		print(cyan+"\n  String = "+green,string_base64)
		print(cyan+"\n  Base64 Encoded String = "+green,result_base64)
		print(yellow+"\n\t\t["+green+"1"+yellow+"]➟ "+green+"Main Menu"+reset)
		print(yellow+"\t\t["+green+"2"+yellow+"]➟ "+green+"Back"+reset)
		print(yellow+"\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
		back_choice = int(input(green+"\nSelect Option : "+reset))
		if back_choice == 1:
			main()
		if back_choice == 2:
			base64_gen()
		elif back_choice == 0:
			print(cyan+"\nThanks For Using This Program"+reset)
		else:
			print(cyan+"\n Wrong Input ! , Try again"+reset)
			time.sleep(2)
			base64_encode_gen()
	def base64_decode_gen():
		banner()
		print(red+" [ "+green+"Selected : Base64 Decoder"+red+" ]"+reset)
		print(" ")
		string_base64 = input(green+"Enter The String To Decode :-\n : "+reset)
		result_base64 = base64.b64decode(string_base64.encode("utf-8")).decode("utf-8")
		print(cyan+"\n  String = "+green,string_base64)
		print(cyan+"\n  Base64 Decoded String = "+green,result_base64)
		print(yellow+"\n\t\t["+green+"1"+yellow+"]➟ "+green+"Main Menu"+reset)
		print(yellow+"\t\t["+green+"2"+yellow+"]➟ "+green+"Back"+reset)
		print(yellow+"\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
		back_choice = int(input(green+"\nSelect Option : "+reset))
		if back_choice == 1:
			main()
		if back_choice == 2:
			base64_gen()
		elif back_choice == 0:
			print(cyan+"\nThanks For Using This Program"+reset)
		else:
			print(cyan+"\n Wrong Input ! , Try again"+reset)
			time.sleep(2)
			base64_decode_gen()
	print(yellow+"\t\t\t      ["+green+"1"+yellow+"]➟ "+green+"Base64 Encoding"+reset)
	print(yellow+"\t\t\t      ["+green+"2"+yellow+"]➟ "+green+"Base64 Decoding"+reset)
	print(yellow+"\t\t\t      ["+green+"3"+yellow+"]➟ "+green+"Back"+reset)
	print(yellow+"\t\t\t      ["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
	base_gen_choice = int(input(green+"\nSelect option : "+reset))
	if base_gen_choice == 1:
		base64_encode_gen()
	elif base_gen_choice == 2:
		base64_decode_gen()
	elif base_gen_choice == 3:
		main_choice()
	elif base_gen_choice == 0:
		print(cyan+"\nThanks For Using This Program"+reset)
	else:
		print(cyan+"\n Wrong Input ! , Try again"+reset)
		time.sleep(2)
		base64_gen()

# choice code

def main_choice():
	banner()
	print(yellow+"\t\t\t["+green+"1"+yellow+"]➟ "+green+"Hashing {SHA256,MD5}"+reset)
	print(yellow+"\t\t\t["+green+"2"+yellow+"]➟ "+green+"Verifier {SHA256,MD5}"+reset)
	print(yellow+"\t\t\t["+green+"3"+yellow+"]➟ "+green+"Base64 Encoder/Decoder"+reset)
	print(yellow+"\t\t\t["+green+"0"+yellow+"]➟ "+green+"Exit"+reset)
	choice_1 = int(input(green+"\nSelect option : "+reset))
	if choice_1 == 1:
		gen()
	elif choice_1 == 2:
		verifier()
	elif choice_1 == 3:
		base64_gen()
	elif choice_1 == 0:
		print(cyan+"\nThanks For Using This Program"+reset)
	else:
		print(cyan+"\n Wrong Input ! , Try again"+reset)
		time.sleep(2)
		s.system("clear")
		print(green+"Tool Restarting..../"+reset)
		time.sleep(2)
		main_choice()

# main code
try:
	main_choice()
except:
	print(yellow+"\n["+red+"Error"+yellow+"]"+cyan+" Something went wrong! Please try again after some time."+reset)
	error_msg = input(cyan+"Press any key to Close the program ..."+reset)
	exit(0)

