# -*- coding: utf-8 -*-

# This script calculates 
# the likelihood of winning on freebitco.in

from random import randint, choice, shuffle


def get_array_of_probability(percent):
	percent = percent*10
	result = []
	while len(result) <= 1000:
		if len(result) <= percent:
			result.append(1)
		else: result.append(0)
	shuffle(result)
	return result

def game(deposit,profit):
	array_of_probability = get_array_of_probability(47.5)
	# statistic money
	deposit_start = deposit
	bet_cost = 1
	max_bit_cost = 0
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
		if bet_cost > max_bit_cost:
			max_bit_cost = bet_cost
	print 'You won!(%s rolls)' % rolls_done

	# Another statistic if you needs
	# print 'wins: %s\nlost: %s' % (wins,lost)
	# print 'persent won: %3.2f%%' % (wins*100.0/(wins+lost))
	# print 'max cost: %s' % max_bit_cost
	# print 'deposit: %s\nprofit: %s' % (deposit, deposit-deposit_start)
	# print 'rolls done: %s' % rolls_done
	return 1

won_range = [game(2000,100) for i in range(100)]
# won_range if you needs
# print won_range

# statistic counters
wins = 0
lost = 0

# Cycle for calculating the probability
# of winning in 100 packs of rolls
for i in won_range:
	if i == 1:
		wins+=1
	else: lost+=1
print 'persent won: %3.2f%%' % (wins*100./(wins+lost))

