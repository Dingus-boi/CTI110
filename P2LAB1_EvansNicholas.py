#Nicholas Evans
#Feb 29 2024
#P2LAB1
#A program that calculates the cost of driving using floating point numbers.



#!/usr/bin/env python3

miles_per_gallon = float(input())
cost_per_gallon = float(input())

gas_used_20 = 20 / miles_per_gallon
cost_20 = gas_used_20 * cost_per_gallon

gas_used_75 = 75 / miles_per_gallon
cost_75 = gas_used_75 * cost_per_gallon

gas_used_500 = 500 / miles_per_gallon
cost_500 = gas_used_500 * cost_per_gallon

print(f'{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}')




