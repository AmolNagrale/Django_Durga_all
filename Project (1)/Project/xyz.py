import pymongo
from pymongo import MongoClient
client=MongoClient('localhost',27017)
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

db7=client.allcategories

electronics=db7.allcategories
db7.electronics.insert({"electronics":0})
appliances=db7.allcategories
db7.appliances.insert({"appliances":0})
men=db7.allcategories
db7.men.insert({"men":0})
women=db7.allcategories
db7.women.insert({"women":0})
kid=db7.allcategories
db7.kid.insert({"kid":0})
home=db7.allcategories
db7.home.insert({"home":0})
bookandmore=db7.allcategories
db7.bookandmore.insert({"bookandmore":0})

db.elec.insert({"elec":"Blackberry"})
db.elec.insert({"elec":"Samsung"})
db.elec.insert({"elec":"Xiaomi"})
db.elec.insert({"elec":"Oppo"})
db.elec.insert({"elec":"Apple"})
db.elec.insert({"elec":"Vivo"})
db.elec.insert({"elec":"Micromax"})
db.elec.insert({"elec":"Lenovo"})
db.elec.insert({"elec":"Power Bank"})
db.elec.insert({"elec":"Memory Card"})
db.elec.insert({"elec":"HeadPhone"})
db.elec.insert({"elec":"Charger"})
db.elec.insert({"elec":"Watches"})
db.elec.insert({"elec":"Sunglass"})
db.elec.insert({"elec":"Laptop"})
db.elec.insert({"elec":"Hard Disk"})
db.elec.insert({"elec":"Pendrives"})
db.elec.insert({"elec":"Printer"})
db.elec.insert({"elec":"Speakers"})
db.elec.insert({"elec":"DTH"})
db.elec.insert({"elec":"Camera"})
db.elec.insert({"elec":"Router"})
db.elec.insert({"elec":"PlayStation"})


db1.appl.insert({"appl":"Sony TV"})
db1.appl.insert({"appl":"Samsung TV"})
db1.appl.insert({"appl":"Lg TV"})
db1.appl.insert({"appl":"Washing Machine"})
db1.appl.insert({"appl":"Refrigators"})
db1.appl.insert({"appl":"AC"})
db1.appl.insert({"appl":"Microwave"})
db1.appl.insert({"appl":"Mixer"})
db1.appl.insert({"appl":"Irons"})
db1.appl.insert({"appl":"Geysers"})
db1.appl.insert({"appl":"Water Purifiers"})
db1.appl.insert({"appl":"Vacuum Cleaner"})
db1.appl.insert({"appl":"Micromax TV"})


db2.men.insert({"Men":"Men Sport Shoes"})
db2.men.insert({"Men":"Men Casual Shoes"})
db2.men.insert({"men":"Men Formal Shoes"})
db2.men.insert({"men":"Floaters"})
db2.men.insert({"men":"Sandals"})
db2.men.insert({"men":"Men Running Shoes"})
db2.men.insert({"men":"Sneakers"})
db2.men.insert({"men":"Perfume"})
db2.men.insert({"men":"Men T-Shirt"})
db2.men.insert({"men":"Men Shirt"})
db2.men.insert({"men":"Men Jackets"})
db2.men.insert({"men":"Men Suit"})
db2.men.insert({"men":"Men Jeans"})
db2.men.insert({"men":"Men Trouser"})
db2.men.insert({"men":"Men Shorts"})
db2.men.insert({"men":"Men Watches"})
db2.men.insert({"men":"Men Wallets"})
db2.men.insert({"men":"Belts"})
db2.men.insert({"men":"Trimmers"})
db2.men.insert({"men":"Shavers"})
db2.men.insert({"men":"Boxers"})


db3.women.insert({"women":"Women Sport Shoes"})
db3.women.insert({"women":"Women Casual Shoes"})
db3.women.insert({"women":"Women T-Shirt"})
db3.women.insert({"women":"Women Shirt"})
db3.women.insert({"women":"Women Jeans"})
db3.women.insert({"women":"Women Trouser"})
db3.women.insert({"women":"Women Shorts"})
db3.women.insert({"women":"Bras"})
db3.women.insert({"women":"Panties"})
db3.women.insert({"women":"Nightwear"})
db3.women.insert({"women":"Sarees"})
db3.women.insert({"women":"Lehenga"})
db3.women.insert({"women":"Blouse"})
db3.women.insert({"women":"Leggings"})
db3.women.insert({"women":"Women Sandals"})
db3.women.insert({"women":"Women Watches"})
db3.women.insert({"women":"Women Deodrants"})
db3.women.insert({"women":"MakeUp"})


db4.kid.insert({"kid":"Kid T-Shirt"})
db4.kid.insert({"kid":"Diaper"})
db4.kid.insert({"kid":"Barbie"})
db4.kid.insert({"kid":"Disney"})
db4.kid.insert({"kid":"Lego"})
db4.kid.insert({"kid":"Kid Wear"})
db4.kid.insert({"kid":"Kid Dress"})
db4.kid.insert({"kid":"Toys"})
db4.kid.insert({"kid":"Kid Shoes"})
db4.kid.insert({"kid":"Kid Sandals"})
db4.kid.insert({"kid":"Kids Bags"})
db4.kid.insert({"kid":"Lunch Box"})


db5.home.insert({"home":"Cookers"})
db5.home.insert({"home":"Kitchen Tools"})
db5.home.insert({"home":"Stoves"})
db5.home.insert({"home":"Coffee Mugs"})
db5.home.insert({"home":"Crockery"})
db5.home.insert({"home":"Flask"})
db5.home.insert({"home":"Beds"})
db5.home.insert({"home":"Sofas"})
db5.home.insert({"home":"Dining Tables"})
db5.home.insert({"home":"Mattress"})
db5.home.insert({"home":"Tables"})
db5.home.insert({"home":"Chairs"})
db5.home.insert({"home":"Wardrobes"})
db5.home.insert({"home":"Drawers"})
db5.home.insert({"home":"Bedsheets"})
db5.home.insert({"home":"Curtains"})
db5.home.insert({"home":"Pillow Cover"})
db5.home.insert({"home":"Cushion"})
db5.home.insert({"home":"Blankets"})
db5.home.insert({"home":"Towels"})
db5.home.insert({"home":"Carpets"})
db5.home.insert({"home":"Door Locks"})
db5.home.insert({"home":"Painting"})
db5.home.insert({"home":"Clocks"})
db5.home.insert({"home":"Shelves"})
db5.home.insert({"home":"Showpieces"})
db5.home.insert({"home":"Led"})
db5.home.insert({"home":"Cfl"})
db6.home.insert({"home":"Lights"})
db6.home.insert({"home":"Gifts"})


db6.bookandmore.insert({"bookandmore":"Entrance Books"})
db6.bookandmore.insert({"bookandmore":"Mpsc"})
db6.bookandmore.insert({"bookandmore":"Upsc"})
db6.bookandmore.insert({"bookandmore":"Comics"})
db6.bookandmore.insert({"bookandmore":"Business"})
db6.bookandmore.insert({"bookandmore":"Literature"})
db6.bookandmore.insert({"bookandmore":"Biographies"})
db6.bookandmore.insert({"bookandmore":"Pens"})
db6.bookandmore.insert({"bookandmore":"Daiaries"})
db6.bookandmore.insert({"bookandmore":"KeyChains"})
db6.bookandmore.insert({"bookandmore":"Calculators"})
db6.bookandmore.insert({"bookandmore":"PS3"})
db6.bookandmore.insert({"bookandmore":"PS4"})
db6.bookandmore.insert({"bookandmore":"Xbox"})
db6.bookandmore.insert({"bookandmore":"VR"})
db6.bookandmore.insert({"bookandmore":"International Music"})
db6.bookandmore.insert({"bookandmore":"Movies"})
db6.bookandmore.insert({"bookandmore":"Car Cover"})
db6.bookandmore.insert({"bookandmore":"Bike Cover"})
db6.bookandmore.insert({"bookandmore":"Media Player"})
db6.bookandmore.insert({"bookandmore":"Cricket"})
db6.bookandmore.insert({"bookandmore":"Football"})
db6.bookandmore.insert({"bookandmore":"Badminton"})
db6.bookandmore.insert({"bookandmore":"Skating"})
db6.bookandmore.insert({"bookandmore":"Cycling"})
db6.bookandmore.insert({"bookandmore":"Swimming"})
db6.bookandmore.insert({"bookandmore":"Tennis"})
db6.bookandmore.insert({"bookandmore":"Gloves"})
db6.bookandmore.insert({"bookandmore":"Royal Enfield"})
db6.bookandmore.insert({"bookandmore":"Nutrition"})
db6.bookandmore.insert({"bookandmore":"Proteins"})
db6.bookandmore.insert({"bookandmore":"Helmets"})
db6.bookandmore.insert({"bookandmore":"Guitar"})
db6.bookandmore.insert({"bookandmore":"Tabla"})
db6.bookandmore.insert({"bookandmore":"Flute"})
db6.bookandmore.insert({"bookandmore":"Music Instruments"})
db6.bookandmore.insert({"bookandmore":"Freshners"})


'''x='Blackberry0'
flag=0
er=db.elec.find({"elec":x})
for i in er:
	if len(i)!=0:
		flag=1	
	
if flag!=1:
	if len(i)!=0:
		print ("Product falls in Electronics Category")


print("hello")
'''

