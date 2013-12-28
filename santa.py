name = raw_input("What is your name? ")
husband = frozenset (["Paul", "paul", "Paul Ford", "Paul E Ford", "Paul Edmund Ford"])
if name in husband:
	print "I choo-choo-choose you!"
else:
	print "I'm sorry. I was really hoping you were Paul."

print "Tell me about your family."
kids = []
while True:
    kid = raw_input("What is your kid's name: ")
    if kid == "quit":
            break
    kids.append(kid)
    if len(kids) == 2:
        print "Whoah. That's a lot of kids. I'm pretty happpy with that. Let's stop there, buckaroo!"
        break
                
