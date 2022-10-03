import datetime


def get_birthdays_per_week(users):
	week_list = ['Monday: ', 'Tuesday: ', 'Wednesday: ', 'Thursday: ', 'Friday: ']
	week_list_copy = week_list.copy()
	if not users:
		print('"Users" dict is emply')

	else:
		for i in users:
			d = i['birthday']
			d = d.replace(year = datetime.date.today().year)
			if 0 <= (d-datetime.date.today()).days <= 7:
				if d.isoweekday() == 6 or d.isoweekday() == 7 or d.isoweekday() == 1:
					week_list[0] = week_list[0] + i["name"] + ', '
				else:
					for weekday in range(len(week_list_copy)):
						if week_list_copy[weekday][:-2] == d.strftime("%A"):
							week_list[weekday] = week_list[weekday] + i["name"] + ', '

		# printing the list by weekday elements
		for i in week_list:
			print(i[:-2])

def main():
	# users defined for checking purposes
'''
	users = [{'name' : '1', 'birthday' : datetime.date(1988, 10, 3)}, {'name' : '1', 'birthday' : datetime.date(1998, 10, 3)},
	{'name' : '2', 'birthday' : datetime.date(1988, 10, 4)}, {'name' : '2', 'birthday' : datetime.date(1998, 10, 4)},
	{'name' : '3', 'birthday' : datetime.date(1988, 10, 5)}, {'name' : '3', 'birthday' : datetime.date(1998, 10, 5)},
	{'name' : '4', 'birthday' : datetime.date(1988, 10, 6)}, {'name' : '4', 'birthday' : datetime.date(1998, 10, 6)},
	{'name' : '5', 'birthday' : datetime.date(1988, 10, 7)}, {'name' : '5', 'birthday' : datetime.date(1998, 10, 7)},
	{'name' : '6', 'birthday' : datetime.date(1988, 10, 8)}, {'name' : '6', 'birthday' : datetime.date(1998, 10, 8)},
	{'name' : '7', 'birthday' : datetime.date(1988, 10, 9)}, {'name' : '7', 'birthday' : datetime.date(1998, 10, 9)}]
'''
	get_birthdays_per_week(users)

if __name__ == '__main__':
	main()