import sys

def textToList():
	text = ""
	for arg in sys.argv[1:]:
		text += '"{}", '.format(arg)
	return text.strip()[:-1]

print(textToList())
