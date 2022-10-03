import datetime


week_list = ['Monday: ', 'Tuesday: ', 'Wednesday: ', 'Thursday: ', 'Friday: ']

if not users:
	print('"Users" list is emply')

else:
	m = ''
	for i in users:
		d = i['birthday']
		d = d.replace(year = datetime.date.today().year)
		if 0 <= (d-datetime.date.today()).days <= 7:
			if d.isoweekday() == 6 or d.isoweekday() == 7 or d.isoweekday() == 1:
				week_list[0] = week_list[0] + i["name"] + ', '
			else:
				for weekday in range(len(week_list)):
					if week_list[weekday][:-2] == d.strftime("%A"):
						week_list[weekday] = week_list[weekday] + i["name"] + ', '
for i in week_list:
	print(i[:-2])