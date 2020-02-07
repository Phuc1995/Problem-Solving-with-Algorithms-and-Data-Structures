#The placement of a key is dependent on the idea of “hashing"
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])

capitals['Utah']='SaltLakeCity'
print(capitals)

capitals['California']='Sacramento'
print(len(capitals))

for k in capitals:
    print(capitals[k], " is capital of ", k)

#Returns the keys of the dictionary in a dict_keys object
phone_ext={'david':1410, 'brad':1137}
print(phone_ext.keys())
print("brad" in phone_ext)

#Returns the values of the dictionary in a dict_values objec
print(list(phone_ext.values()))

#Returns the key-value pairs in a dict_items object
print(list(phone_ext.items()))

#Returns the value associated with 𝑘, None otherwise
print(phone_ext.get("david"))

#Returns the value associated with 𝑘, 𝑎𝑙𝑡 otherwise
print(phone_ext.get("kent","NO ENTRY"))

del phone_ext["david"]
print(phone_ext)

print("Hello","World", sep="***")

word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)

#copy 𝑂(𝑛)
#get item 𝑂(1)
#set item 𝑂(1)
#delete item 𝑂(1)
#contains (in) 𝑂(1)
#iteration 𝑂(𝑛)
