#v2.1 # released v2.3(update and delete)
class Customer:
	def __init__(self,name,address):
		self.name=name
		self.address=address
	def create(self):
		
		print("creating customer: %s,%s"%(self.name,self.address))

	def update(self):
		
		print("updating customer: %s,%s"%(self.name,self.address))
	def delete(self):
		
		print("deleting customer: %s,%s"%(self.name,self.addresscustomer))