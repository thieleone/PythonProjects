

message = 'Philipp\'s Test.'
message2 = "Test's Test."
message3 = """Das ist ein
Test ueber mehr
ere Zeilen."""

print(message[3:6])
print(message[:7])
print(message[10:])
print(message.lower())
print(message.count('p'))
print(message.find('Test'))

message = message.replace('Philipp','Mac')
print(message)
print(message2[7])
print(len(message3))


greeting='Hello'
name='Philipp'

greeting_message=greeting+', '+name+'. Welcome!'

greeting_message2='{}, {}. Welcome!'.format(greeting,name)

greeting_message3='{}, {}. Welcome!'

greeting_message4=greeting_message3.format(greeting,name)

greeting_message5=f'{greeting}, {name.upper()}. Welcome!'


print(greeting_message)
print(greeting_message2)
print(greeting_message4)
print(greeting_message5)


#print(help(str))
print(help(str.replace))



languages = ['Python', 'Java', 'C++']