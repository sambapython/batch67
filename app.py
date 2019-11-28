from module1 import Supplier
from module2 import Customer

class MySupplier(Supplier):
	def # overriding Supplier class create method in to Mysupplier class
		print("validation")
		#self.create()
		Supplier.create(self)

s=MySupplier("sup1","ad1")
s.create()
s2=MySupplier("sup2","ad2",pan="sfsd")
s2.create()
s3=MySupplier("sup3","ad3",pan="sfsd",email="sup3@gmail.com")
s3.create()
#update and delete
c1=Customer("cust1","ad1")
c1.create()

