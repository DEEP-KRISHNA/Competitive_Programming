# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	cipher = ''
	shift = shift%26
	for i in msg:
		temp = ord(i)
		if (temp >= 97 and temp <= 122):
			if (shift<0 and temp + shift - 97 < 0):
				cipher = cipher + chr(122 - (temp + shift - 97))
			elif (shift > 0 and temp + shift > 122):
				cipher = cipher + chr(temp + shift - 122 + 97 - 1)
			else:
				cipher = cipher + chr(temp + shift)
		elif (temp >= 65 and temp <= 90):
			if (shift < 0 and temp + shift - 65 < 0):
				cipher = cipher + chr(90 - (temp + shift - 65))
			elif (shift > 0 and temp + shift > 90):
				cipher = cipher + chr(temp + shift - 90 + 65 - 1)
			else:
				cipher = cipher + chr(temp + shift)
		else:
			cipher = cipher + chr(temp)
	return cipher

def test():
	s = 'a'
	print(ord(s))
	print(chr(97))

if __name__ == "__main__":
	print(fun_applycaesarcipher("abcdxyz", -3))
