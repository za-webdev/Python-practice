
#A function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value.

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}



def my_version(my_dict):
	a=list(my_dict.items())
	print a

my_version(my_dict)