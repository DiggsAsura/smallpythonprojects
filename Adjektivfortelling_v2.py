# Adjektivfortelling v2
# Let's try to make the v2 with a rng thingy for the adjectives 
# it works but the code is still ugly as hell. Especially the .format. Maybe do a v3 later on that sort this better. 

import random

print("""

		Dette er en adjektivfortelling om et troll. 
		Skriv inn 10 adjektiv, som vi plasserer inn i fortellingen.
		
""")

adj_lst = []
adj_lst.append(input("		1: "))
adj_lst.append(input("		2: "))
adj_lst.append(input("		3: "))
adj_lst.append(input("		4: "))
adj_lst.append(input("		5: "))
adj_lst.append(input("		6: "))
adj_lst.append(input("		7: "))
adj_lst.append(input("		8: "))
adj_lst.append(input("		9: "))
adj_lst.append(input("		10: "))

adj_word = random.choice(adj_lst) # well, this did not work. it ended up printing the same word all over the story. 


print("""


		Det {adj1} trollet
		Det var en gang et {adj2} troll som bodde langt ute i
		den {adj3} skogen. Trollet hadde tre {adj4} hoder
		og fire {adj5} bein. Det vokste et {adj6} tre på den
		{adj7} nesa til trollet.
		
		En {adj8} dag hørte det {adj9} trollet to {adj10}
		barn som gikk på den {adj11} stien. Det {adj12}
		trollet bestemte seg for å skremme barna. Derfor gjemte
		trollet seg under den {adj13} broa.
		
		Da barna skulle over den {adj14} broa, brølte det
		{adj15} trollet så {adj16} det kunne. ”Hvem er det som
		tramper på min {adj17} bro?”. De {adj18} barna skrek
		og la på sprang det forteste de kunne. ”Nå kommer jeg og
		tar dere!”, ropte det {adj19} trollet.
		
		Men plutselig skled trollet på en {adj20} stein. Trollet falt
		rett ned i den {adj21} fossen og ble slukt av en
		{adj22} fisk. Snipp snapp snute, så er dette {adj23}
		eventyret ute.


		""".format(adj1=random.choice(adj_lst), adj2=random.choice(adj_lst), adj3=random.choice(adj_lst), adj4=random.choice(adj_lst), adj5=random.choice(adj_lst), adj6=random.choice(adj_lst), adj7=random.choice(adj_lst), adj8=random.choice(adj_lst), adj9=random.choice(adj_lst), adj10=random.choice(adj_lst), adj11=random.choice(adj_lst), adj12=random.choice(adj_lst), adj13=random.choice(adj_lst), adj14=random.choice(adj_lst), adj15=random.choice(adj_lst), adj16=random.choice(adj_lst), adj17=random.choice(adj_lst), adj18=random.choice(adj_lst), adj19=random.choice(adj_lst), adj20=random.choice(adj_lst), adj21=random.choice(adj_lst), adj22=random.choice(adj_lst), adj23=random.choice(adj_lst))
)
