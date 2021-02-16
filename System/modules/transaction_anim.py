from datetime import datetime, timedelta

class Transaction_Anim:

	def __init__(self,t,d,c):
		self.tid = t
		self.datetime = d
		self.custid = c
		self.items = []

		a = datetime.strptime(self.datetime, '%m/%d/%Y %I:%M %p')
		b = a - timedelta(minutes=20)

		self.arrival = str(b.strftime('%m/%d/%Y %I:%M %p'))

		if self.arrival[0] == "0": #setting the date string if the date was (01/21/2020 xxxx pm) turn it into (1/21/2020 xxxx pm)
			self.arrival = self.arrival[1:]

	def get_Arrival(self):
		return self.arrival

	def add_Item(self,line):
		self.items.append(line)

	def __repr__(self):
		return f"transaction ID: {self.tid} | arrival: {self.arrival} | customer ID {self.custid}"