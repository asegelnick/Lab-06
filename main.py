# encodes the users password by shifting each number by 3
def encode(password):
	# creates a new string to store the encoded password
	encoded_password = ''
	for i in range(len(password)):
		# adds 3 to each digit and adds it to the new string
		digit = str((int(password[i])) + 3)
		encoded_password += digit
	# returns the new password
	return encoded_password


# decodes the user's encoded password by shifting each number left by 3
def decode(password):
	pass


# creates the main function
def main():

	# displays the menu options

	user_choice = 0
	while True:
		print('Menu')
		print('-' * 13)
		print('1. Encode')
		print('2. Decode')
		print('3. Quit')

		user_choice = int(input('Please enter an option: '))

		if user_choice == 1:
			password = input('Please enter your password to encode: ')
			encoded_password = encode(password)
			print('Your password has been encoded and stored!\n')

		elif user_choice == 2:
			decoded_password = decode(encoded_password)
			print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.\n')

		elif user_choice == 3:
			break


main()
