import numpy as np

written = []
#create dictionary of irregualarly spelled numbers from 1 - 19
spell_dict = {}
teen_dict = {}
spellings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
teens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
for i in range(1, 20):
	spell_dict[i] = spellings[i-1]

for i in range(2,10):
	teen_dict[i] = teens[i-2]

for num in range(1,1000):
	digits = len(str(num))
	if digits == 1:
		written.append(spell_dict[num])
	elif digits == 2:
		first_digit = int(str(num)[0])
		second_digit = int(str(num)[1])
		if first_digit == 1:
			written.append(spell_dict[num])
		elif first_digit > 1 and second_digit == 0:
			written.append(teen_dict[first_digit])
		elif first_digit > 1:
			written.append(teen_dict[first_digit] + spell_dict[second_digit])
	#more logic for the numbers in the hundreds
	elif digits == 3:
		first_digit = int(str(num)[0])
		second_digit = int(str(num)[1])
		third_digit = int(str(num)[2])
		second_third_digits = int(str(num)[1:3])
		if second_digit == 0 and third_digit == 0:
			written.append(spell_dict[first_digit] + "hundred")
		elif second_digit == 0 and third_digit > 0:
			#just don't include spaces originally
			written.append(spell_dict[first_digit] + "hundredand" + spell_dict[third_digit])
		elif second_digit ==1:
			written.append(spell_dict[first_digit] + "hundredand" + spell_dict[second_third_digits])
		elif second_digit > 0 and third_digit == 0:
			written.append(spell_dict[first_digit] + "hundredand" + teen_dict[second_digit])
		elif third_digit > 0:
			written.append(spell_dict[first_digit] + "hundredand" + teen_dict[second_digit] + spell_dict[third_digit])

#one last line for the one thousand
written.append('onethousand')

total_chars = sum(len(s) for s in written)