alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
# texts = input("type your message: ").lower()
# shiftn = int(input("type the shift number: "))

# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         n_pos = position + shift
#         n_letter = alphabet[n_pos]
#         cipher_text += n_letter
#     print(f"the encoded text is {cipher_text}")


# def decrypt(c_text, shift_num):
#     plain_text = ""
#     for letter in c_text:
#         position = alphabet.index(letter)
#         n_pos = position - shift_num
#         n_letter = alphabet[n_pos]
#         plain_text += n_letter
#     print(f"the decoded text is {plain_text}")
# if direction == "encode":
#     encrypt(text = texts,shift = shiftn)
# elif direction == "decode":
#     decrypt(c_text  = texts,shift_num = shiftn)
should_continue = True
while should_continue:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
    texts = input("type your message: ").lower()
    shiftn = int(input("type the shift number: "))

    def caeser(start_text,shift_amount,c_dirn):
        end_text = ""
        if c_dirn == "decode":
                shift_amount *= -1
        for letter in start_text:
            position = alphabet.index(letter)
            
            n_pos = position + shift_amount
            end_text += alphabet[n_pos]
        print(f"the {c_dirn}d text is {end_text}")
    caeser(start_text = texts, shift_amount = shiftn,c_dirn = direction)
    result =input("type 'yes' if you want to go again, otherwise no: ")
    if result == "no":
         should_continue = False