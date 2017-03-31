# This script calculates 
# the likelihood of winning on freebitco.in

from random import randint, choice, shuffle


def get_perсent_win(perсent):
	perсent = perсent*1000
	result = []
	while len(result) <= 1000:
		if len(result) <= perсent:
			result.append(1)
		else: result.append(0)
	shuffle(result)
	return result

def game(deposit,profit):
	array_of_probability = get_persent_win(47.5)
	deposit_start = deposit
	bet_cost = 1
	max_cost = 0
	# statistic counters
	rolls_done = 0
	wins = 0
	lost = 0
	while deposit-deposit_start <= profit:
		rolls_done+=1
		if choice(array_of_probability) is not 1:
			deposit-=bet_cost
			bet_cost*=2
			lost+=1
			if deposit < bet_cost:
				print 'You lost!(%s rolls)' % rolls_done
				return 0
		else: 
			deposit+=bet_cost
			bet_cost = 1
			wins+=1
		if bet_cost > max_cost:
			max_cost = bet_cost
	print 'You won!(%s rolls)' % rolls_done

	# Other statistic if you needs
	# print 'wins: %s\nlost: %s' % (wins,lost)
	# print 'persent won: %3.2f%%' % (wins*100.0/(wins+lost))
	# print 'max cost: %s' % max_cost
	# print 'deposit: %s\nprofit: %s' % (deposit, deposit-deposit_start)
	# print 'rolls done: %s' % rolls_done
	return 1

won_range = [game(50000,1000) for i in range(100)]
print won_range
# statistic counters
wins = 0
lost = 0
for i in won_range:
	if i == 1:
		wins+=1
	else: lost+=1
print 'persent won: %3.2f%%' % (wins*100.0/(wins+lost))

