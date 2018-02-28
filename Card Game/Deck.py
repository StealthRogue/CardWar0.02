#tuk shte napravim funkciqta da vikame testeto v display-a i on-click kakvo da pravi + image za testeto
class Deck:
	def __init__(self):
		pass

#dovurshih ti decka i podredih kartite po sila i sum fixnal kak se pishat na angliiski
Ace_of_Clubs,Ace_of_Diamonds,Ace_of_Hearts,Ace_of_Spades = 20.1,20.2,20.3,20.4
King_of_Clubs,King_of_Diamonds,King_of_Hearts,King_of_Spades = 14.1,14.2,14.3,14.4
Queen_of_Clubs,Queen_of_Diamonds,Queen_of_Hearts,Queen_of_Spades = 13.1,13.2,13.3,13.4
Jack_of_Clubs,Jack_of_Diamonds,Jack_of_Hearts,Jack_of_Spades = 12.1,12.2,12.3,12.4
Nine_of_Clubs,Eight_of_Clubs,Seven_of_Clubs,Six_of_Clubs,Five_of_Clubs,Four_of_Clubs,Three_of_Clubs,Two_of_Clubs = 9.1,8.1,7.1,6.1,5.1,4.1,3.1,2.1
Nine_of_Diamonds,Eight_of_Diamonds,Seven_of_Diamonds,Six_of_Diamonds,Five_of_Diamonds,Four_of_Diamonds,Three_of_Diamonds,Two_of_Diamonds = 9.2,8.2,7.2,6.2,5.2,4.2,3.2,2.2
Nine_of_Hearts,Eight_of_Hearts,Seven_of_Hearts,Six_of_Hearts,Five_of_Hearts,Four_of_Hearts,Three_of_Hearts,Two_of_Hearts = 9.3,8.3,7.3,6.3,5.3,4.3,3.3,2.3
Nine_of_Spades,Eight_of_HSpades,Seven_of_Spades,Six_of_Spades,Five_of_Spades,Four_of_Spades,Three_of_Spades,Two_of_Spades = 9.4,8.4,7.4,6.4,5.4,4.4,3.4,2.4


#Hearts = [Ace,King,Queen,Jack,10,9,8,7,6,5,4,3,2] #kupa 10_1,20.1
#Spades = [Ace,King,Queen,Jack,10,9,8,7,6,5,4,3,2] #pika 10_2,20.2
#Clubs = [Ace,King,Queen,Jack,10,9,8,7,6,5,4,3,2] #spatiq 10_3,20.3
#Diamonds = [Ace,King,Queen,Jack,10,9,8,7,6,5,4,3,2] #karo 10_4,20.4
Deck = [Ace_of_Clubs,Ace_of_Diamonds,Ace_of_Hearts,Ace_of_Spades,
King_of_Clubs,King_of_Diamonds,King_of_Hearts,King_of_Spades,
Queen_of_Clubs,Queen_of_Diamonds,Queen_of_Hearts,Queen_of_Spades,
Jack_of_Clubs,Jack_of_Diamonds,Jack_of_Hearts,Jack_of_Spades,
Nine_of_Clubs,Eight_of_Clubs,Seven_of_Clubs,Six_of_Clubs,Five_of_Clubs,Four_of_Clubs,Three_of_Clubs,Two_of_Clubs,
Nine_of_Diamonds,Eight_of_Diamonds,Seven_of_Diamonds,Six_of_Diamonds,Five_of_Diamonds,Four_of_Diamonds,Three_of_Diamonds,Two_of_Diamonds,
Nine_of_Hearts,Eight_of_Hearts,Seven_of_Hearts,Six_of_Hearts,Five_of_Hearts,Four_of_Hearts,Three_of_Hearts,Two_of_Hearts,
Nine_of_Spades,Eight_of_HSpades,Seven_of_Spades,Six_of_Spades,Five_of_Spades,Four_of_Spades,Three_of_Spades,Two_of_Spades]
