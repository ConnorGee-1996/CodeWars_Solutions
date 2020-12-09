# Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

# Constraints:
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

def valid_parentheses(string):
	# steps:
	# 1. remove all characters that are not ( or ).
	# delete every () pair from the string. If the string does not have size zero then its wrong?
	new_string = ""
	for n in string:
		if n in [")","("]:
			new_string = new_string + n

	while True:
		if "()" in new_string:
			new_string = new_string.replace("()", "")
		else:
			break

	if len(new_string) == 0:
		return True
	else:
		return False


print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses("()((()())())"))