import pymongo
from pymongo import MongoClient
from random import randint
s=''
def func(a):
	client=MongoClient('localhost',27017)
	db7=client.allcategories	
	electronics=db7.allcategories
	appliances=db7.allcategories
	men=db7.allcategories
	women=db7.allcategories
	kid=db7.allcategories
	home=db7.allcategories
	bookandmore=db7.allcategories
	
	db=client.electronics
	elec=db.electronics
	db1=client.appliances
	appl=db1.appliances
	db2=client.men
	men=db2.men
	db3=client.women
	women=db3.women
	db4=client.kid
	kid=db4.kid
	db5=client.home
	home=db5.home
	db6=client.bookandmore
	bookandmore=db6.bookandmore
	
	if a=='electronics':
		for c in db7.electronics.find({},{'electronics':1,'_id':0}):
			t=c['electronics']
			
		db7.electronics.update({'electronics':t},{'$set':{'electronics':(t+1)}})
		
				
	elif a=='appliances':
		for c in db7.appliances.find({},{'appliances':1,'_id':0}):
			t=c['appliances']
			
		
		db7.appliances.update({'appliances':t},{'$set':{'appliances':(t+1)}})
		
			
		
	elif a=='men':
		for c in db7.men.find({},{'men':1,'_id':0}):
			t=c['men']
			
		
		db7.men.update({'men':t},{'$set':{'men':(t+1)}})
		
		
		
	elif a=='women':
		for c in db7.women.find({},{'women':1,'_id':0}):
			t=c['women']
			
		db7.women.update({'women':t},{'$set':{'women':(t+1)}})

		
	
	elif a=='kid':
		for c in db7.kid.find({},{'kid':1,'_id':0}):
			t=c['kid']
			
		db7.kid.update({'kid':t},{'$set':{'kid':(t+1)}})	
		
			
		
	elif a=='home':
		for c in db7.home.find({},{'home':1,'_id':0}):
			t=c['home']
			
		db7.home.update({'home':t},{'$set':{'home':(t+1)}})	
		
		
		
	elif a=='bookandmore':
		for c in db7.bookandmore.find({},{'bookandmore':1,'_id':0}):
			t=c['bookandmore']
		
		
		db7.bookandmore.update({'bookandmore':t},{'$set':{'bookandmore':(t+1)}})
		
			
	###########################################################		
			
	for c in db7.electronics.find({},{'electronics':1,'_id':0}):
			e=c['electronics']
			
	for c in db7.appliances.find({},{'appliances':1,'_id':0}):
			f=c['appliances']	
	
	for c in db7.men.find({},{'men':1,'_id':0}):
			g=c['men']
			
	for c in db7.women.find({},{'women':1,'_id':0}):
			h=c['women']			

	for c in db7.kid.find({},{'kid':1,'_id':0}):	
			j=c['kid']
			
	for c in db7.home.find({},{'home':1,'_id':0}):
			k=c['home']
		
	for c in db7.bookandmore.find({},{'bookandmore':1,'_id':0}):
			l=c['bookandmore']						

	count =[e,f,g,h,j,k,l]
	o= max(count)
	p= count.index(o)
	

	

	def el():
		for d in db.elec.find().limit(1).skip(randint(0,20)):
				t=d['elec']	
				s=t	
				return (s)		
	def al():
		for d in db1.appl.find().limit(1).skip(randint(0,11)):
				t=d['appl']	
				s=t
				return (s)
				
	def ml():
		for d in db2.men.find().limit(1).skip(randint(0,18)):
				t=d['men']	
				s=t
				return (s)
	def wl():	
		for d in db3.women.find().limit(1).skip(randint(0,15)):
				t=d['women']
				s=t
				return (s)	
	def kl():
		for d in db4.kid.find().limit(1).skip(randint(0,9)):
				t=d['kid']	
				s=t
				return (s)
	def hl():
		for d in db5.home.find().limit(1).skip(randint(0,20)):
				t=d['home']
				s=t
				return (s)
	def bml():
		for d in db6.bookandmore.find().limit(1).skip(randint(0,20)):
				t=d['bookandmore']									
				s=t
				return (s)
	options={0:el,1:al,2:ml,3:wl,4:kl,5:hl,6:bml}
	
	z = options.get(p)()
	return (z)
					
	
