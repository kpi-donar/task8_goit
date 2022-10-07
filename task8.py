import datetime


def get_birthdays_per_week(users):
	week_list = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}


	for user in users:
		d = user['birthday']
		d = d.replace(year = datetime.date.today().year)
		if not 0 <= (d-datetime.date.today()).days <= 7:
			continue
		week_day = d.strftime("%A")
		if week_day in ('Saturday', 'Sunday'):
			week_day = 'Monday'
		week_list[week_day].append(user['name'])

	# printing
	for key, value in week_list.items():
		if value:
			print('{:<10} {:<10}'.format(key+':', ','.join(value)))

def main():
	# users defined for checking purposes

	users = [{'name' : '1', 'birthday' : datetime.date(1988, 10, 10)}, {'name' : '1', 'birthday' : datetime.date(1998, 10, 10)},
	{'name' : '2', 'birthday' : datetime.date(1988, 10, 11)}, {'name' : '2', 'birthday' : datetime.date(1998, 10, 11)},
	{'name' : '3', 'birthday' : datetime.date(1988, 10, 12)}, {'name' : '3', 'birthday' : datetime.date(1998, 10, 12)},
	{'name' : '4', 'birthday' : datetime.date(1988, 10, 6)}, {'name' : '4', 'birthday' : datetime.date(1998, 10, 6)},
	{'name' : '5', 'birthday' : datetime.date(1988, 10, 7)}, {'name' : '5', 'birthday' : datetime.date(1998, 10, 7)},
	{'name' : '6', 'birthday' : datetime.date(1988, 10, 8)}, {'name' : '6', 'birthday' : datetime.date(1998, 10, 8)},
	{'name' : '7', 'birthday' : datetime.date(1988, 10, 9)}, {'name' : '7', 'birthday' : datetime.date(1998, 10, 9)}]

	get_birthdays_per_week(users)

if __name__ == '__main__':
	main()