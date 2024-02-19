class Term:
	def __init__(self, multiplier, exponent):
		self.multiplier = multiplier
		self.exponent = exponent

def findExponent(string):
	for i in range(len(string)):
		if string[i] == "^":
			return string[i + 1]
	return 1

def derive(terms):
	result = []
	for term in terms:
		newTerm = Term(term.multiplier * term.exponent, term.exponent - 1)
		result.append(newTerm)

	return result

def stringToTerms(terms):
	parsedTerms = []

	for term in terms:

		multiplier = ""

		negative = 0

		if term[0] == "-":
			negative = 1

		start = 1 if negative else 0

		for i in range(start, len(term)):
			if term[i].isnumeric():
				multiplier += term[i]

			else:
				break

		if negative:
			multiplier = int(multiplier) * -1

		exponent = 0
		if term.find("x") > 0:
			exponent = findExponent(term)

		parsedTerms.append(Term(int(multiplier), int(exponent)))

	return parsedTerms


def termsToString(terms):
	output = ""
	for i in range(len(derivedTerms)):

		term = derivedTerms[i]

		if term.exponent < 0:
			continue

		if term.multiplier < 0:
			output = output + " - "

		elif i != 0:
			output = output + " + "

		term.multiplier = abs(term.multiplier)

		if term.exponent == 0:
			output += (f"{term.multiplier}")

		elif term.exponent == 1:
			output += str(term.multiplier) + deriveFor

		else:
			# output += (f"{term.multiplier}x^{term.exponent}")
			output += str(term.multiplier) + deriveFor + "^" + str(term.exponent)

	return output

# entry


# lasku = input("Anna derivoitava lauseke: ")

lasku = "2x^4 + 10x^3 + 123x^2 - 12x + 3"
deriveFor = "x"

terms = lasku.replace(" ", "")
terms = terms.replace("-", "+-")
terms = terms.split("+")

parsedTerms = stringToTerms(terms)

derivedTerms = derive(parsedTerms)

output = termsToString(derivedTerms)

print(output)