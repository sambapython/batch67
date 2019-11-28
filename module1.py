#v2.1 # released v2.3(update and delete)
class Supplier:
	#*args, **kwargs
	def __init__(self,name,address,phone=None,email=None,pan=None):
		#method overloading
		self.name=name
		self.address=address
		self.phone=phone
		self.email=email
		self.pan=pan
	def create(self):
		
		print("creating suplier: %s,%s,%s,%s,%s,"%(self.name,self.address,
			self.phone,self.pan,self.email))

	def update(self):
		
		print("updating suplier: %s,%s"%(self.name,self.address))
	def delete(self):
		
		print("deleting suplier: %s,%s"%(self.name,self.address))