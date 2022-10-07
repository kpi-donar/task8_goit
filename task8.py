import datetime


def get_birthdays_per_week(users):
	week_list = {}


	for user in users:
		d = user['birthday']
		d = d.replace(year = datetime.date.today().year)
		if 0 <= (d-datetime.date.today()).days <= 7:
			if d.isoweekday() in (1,6,7):
				if 'Monday' not in week_list:
					week_list['Monday'] = (user['name'])
				else:
					week_list['Monday'] += ', ' + (user['name'])
			else:
				if d.strftime("%A") not in week_list:
					week_list[d.strftime("%A")] = (user['name'])
				else:
					week_list[d.strftime("%A")] += ', ' + (user['name'])

	# printing

	for key, value in week_list.items():
		print('{:<10} {:<10}'.format(key+':', value))

def main():
	# users defined for checking purposes

	users = [{'name' : '1', 'birthday' : datetime.date(1988, 10, 3)}, {'name' : '1', 'birthday' : datetime.date(1998, 10, 3)},
	{'name' : '2', 'birthday' : datetime.date(1988, 10, 4)}, {'name' : '2', 'birthday' : datetime.date(1998, 10, 4)},
	{'name' : '3', 'birthday' : datetime.date(1988, 10, 5)}, {'name' : '3', 'birthday' : datetime.date(1998, 10, 5)},
	{'name' : '4', 'birthday' : datetime.date(1988, 10, 6)}, {'name' : '4', 'birthday' : datetime.date(1998, 10, 6)},
	{'name' : '5', 'birthday' : datetime.date(1988, 10, 7)}, {'name' : '5', 'birthday' : datetime.date(1998, 10, 7)},
	{'name' : '6', 'birthday' : datetime.date(1988, 10, 8)}, {'name' : '6', 'birthday' : datetime.date(1998, 10, 8)},
	{'name' : '7', 'birthday' : datetime.date(1988, 10, 9)}, {'name' : '7', 'birthday' : datetime.date(1998, 10, 9)}]

	get_birthdays_per_week(users)

if __name__ == '__main__':
	main()