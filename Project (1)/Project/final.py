import requests
from bs4 import BeautifulSoup
import os
import urllib.request

pname=''
y=''
opl=''
cap=''

def core(pname,y):

	u='https://www.ebay.in/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR10.TRC0.A0.H0.Xhello.TRS0&_nkw='

	url=u+pname+'&_sacat=0&_udlo=0&_udhi=10000'

	r=requests.get(url)

	soup=BeautifulSoup(r.text,"html.parser")

	c=0
	b=0
	pre='Rs.'
	cnf=[]
	j=0
	temp=''
	with open('ebay.text','w')as fp:
		for price in soup.findAll('span',{'class':'bold'}):
			cnf=price.text        		
			cnf=cnf[len(pre)+1:]
			if(len(cnf)>4):
				cnf=cnf[:6]
			while j < len(cnf):
                    		
                    		if(cnf[j] == ','):
                    			temp = temp + str(cnf[j+1])
                    			j+=1
                    		else:
                    			temp = temp + cnf[j]
                    		j+=1
			cnf=temp	
			cnf=float(cnf)
			cnf=int(cnf)
			fp.write(str(cnf)+'\n')
			b += 1
			if b > 0:
				break
		for data in soup.findAll('a',{'class':'vip'}):
			fp.write(data.get('href')+'\n')
			c+=1
			if c>0:
        			break
	fp.close()
	c=0
	b=0

	u='https://www.flipkart.com/search?q='

	url=u+pname+'&otracker=start&as-show=on&as=off'

	r=requests.get(url)

	soup=BeautifulSoup(r.text,"html.parser")
	m =[]
	fkpf=0
	with open('fk.text','w') as fp1:
		for price in soup.findAll('div',{'class':'_1vC4OE'}):
			fkpf = price.text
			fkpf=fkpf[1:] 
			b += 1
			if b > 0:
				break
		
		temp=''
		newlist = []
		j=0
		while j < len(fkpf):
            		if(fkpf[j] == ','):
                		temp = temp + str(fkpf[j+1])
                		j+=1
            		else:
                		temp = temp + fkpf[j]
            		j+=1
		newlist.append(temp)
		fkpf=newlist[0]
		fp1.write(str(fkpf)+'\n')
		
		for fdat in soup.findAll('a',{'class':'_2cLu-l'}):
			fp1.write('https://www.flipkart.com'+ fdat.get('href') + '\n')
			c += 1
			if c > 0:
				break
	fp1.close()
	
	u='https://www.jabong.com/clothing/find/shirts/?q='

	url=u+pname

	r=requests.get(url)

	soup=BeautifulSoup(r.text,"html.parser")

	b=0
	c=0
	with open('jbng.text','w') as fp2:
		for jpre in soup.findAll('div',{'class':'col-xxs-6 col-xs-4 col-sm-4 col-md-3 col-lg-3 product-tile img-responsive'}):
        		if jpre.get('data-discount-price')and jpre.get('data-discount-price')!='NaN':
            			fp2.write(jpre.get('data-discount-price')+'\n')
            			c += 1
            			if c > 0:
                			break
		for jdat in soup.findAll('a',{'data-pos':'1'}):      
			fp2.write('https://www.jabong.com'+ jdat.get('href'))
			b += 1
			if b > 0:
				break
	fp2.close()
	
	u='https://www.snapdeal.com/search?keyword='

	url=u+pname	+'&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'

	r=requests.get(url)

	soup=BeautifulSoup(r.text,"html.parser")
	b=0
	c=0
	with open('pml.text','w') as fp3:
		for ptml in soup.findAll('span',{'class':'lfloat product-price'}):
        		fp3.write(ptml.get('display-price')+'\n')       
        		b += 1
        		if b > 0:
            			break
		for data in soup.findAll('a',{'class':'dp-widget-link noUdLine'}):

        		fp3.write(data.get('href') + '\n')      
        		c += 1
        		if c > 0:
            			break
	fp3.close()
	
	with open('ebay.text','r') as fe:
    		cmp1=fe.readline()
    		ln1=fe.readline()
	fe.close()
	with open('jbng.text','r') as fj:
    		cpm2=fj.readline()
    
    		ln2=fj.readline()
	fj.close()

	with open('pml.text','r') as fk:
    		cmp3=fk.readline()
    		ln3=fk.readline()
	fk.close()
	
	with open('fk.text','r') as fkr:
    		cmp4=fkr.readline()
    		ln4=fkr.readline()
	
	'''if int(cmp1)<int(cpm2):
    		if int(cmp3)>int(cmp1):
        		print('This product is cheapest in all'+'\n'+'Price:'+cmp1+'\n'+'Link:'+ln1)
    		else:
        		print('This product is cheapest in all'+'\n'+'Price:'+cmp3+'\n'+'Link:'+ln3)
	else:
        	if int(cmp3)>int(cpm2):
            		print('This product is cheapest in all'+'\n'+'Price:'+cpm2+'\n'+'Link:'+ln2)
        	else:
            		print('This product is cheapest in all' + '\n' + 'Price:' + cmp3 + '\n' + 'Link:' + ln3)'''
	
            		
	
	cmp1=int(cmp1)
	if str(cpm2) is None:
		cpm2='999999'
		cpm2=int(cpm2)
	else:
		cpm2=int(cpm2)
	cmp3=int(cmp3)
	cmp4=int(cmp4)		
	m=[cmp1,cpm2,cmp3,cmp4]
	m.sort()
	if m[0]==int(cmp1):
		print('This product is cheapest in all'+'\n'+'Price:'+str(cmp1)+'\n'+'Link:'+ln1)
	elif m[0]==(cpm2):	
		print('This product is cheapest in all'+'\n'+'Price:'+str(cpm2)+'\n'+'Link:'+ln2)	
	elif m[0]==(cmp3):
		print('This product is cheapest in all' + '\n' + 'Price:' + str(cmp3) + '\n' + 'Link:' + ln3)
	else:
		print('This product is cheapest in all' + '\n' + 'Price:' + str(cmp4) + '\n' + 'Link:' + ln4)
				
	

def core2(prod_name,y):

	def flipkart_scraper():

		am = prod_name.split(' ')	
		a = 0
		u = "https://www.flipkart.com/search?q="
		while a < len(am):
			if a < (len(am)-1):
				u = u + am[a] + "%20"
			elif (a == len(am) - 1):
				u = u + am[a]
			a+=1
			
		url = u+"&otracker=start&as-show=off&as=off"
		page= requests.get(url)
		a = 0
		
		soup = BeautifulSoup(page.text, "html.parser")
		#print('dsag')
		fl1 = 1
		fl2 = 1

		m1 = []                                                       #for first type
		m2 = []
		for data in soup.findAll('a',{'class':'_2cLu-l'}):
			fl1 = 0
			href = data.get('href')
			title = data.get('title')
			m1.append(title)
			h = 'https://www.flipkart.com'+href
			m2.append(h)


		n1 = []                                                       #for second type,n1 stores name
		n2 = []                                                       #n2 stores link
		for title in soup.findAll('div', {'class': '_3wU53n'}):            #for name
			fl2 = 0
			n1.append(title.text)
		for link in soup.findAll('a',{'class':'_1UoZlX'} ):               #for link
			href = link.get('href')
			j = 'https://www.flipkart.com'+href
			n2.append(j)

		#print('dsag')
		m = []                                                         #empty list for storing price
		for price in soup.findAll('div',{'class':'_1vC4OE'}):
			m.append(price.text)

		m = [i[1:] for i in m ]                                        #for removing indian rupee sign
		#print(m)
		newlist = []                                                   #for removing comma
		main_price = []
		temp = ""
		for i in m:
			#print('dsag')
			j = 0
			temp = ""
			while j < len(i):
				if(i[j] == ','):
					temp = temp + str(i[j+1])
					j+=1
				else:
					temp = temp + i[j]
				j+=1
			#print('dsag')
			newlist.append(temp)
			main_price.append(temp)

		for index, item in enumerate(newlist):                                       #for type conversion from string to int
			newlist[index] = int(item)
			main_price[index] = int(item)

		newlist.sort()                    #newlist consists of sorted prices and main_price consists of price in specific sequence
		
		min1 = newlist[0]                       #first minimum price

		index1 = 0
		for i in range(0,len(main_price)):
			if(main_price[i] == min1):
				index1 = i
				break

		print('\n')
		if fl1 == 0:
			print('1. Product-Name --> '+m1[index1]+'\n************************************\n')
			print('2. Link : '+m2[index1]+'\n************************************\n')
		elif fl2 == 0:
			print('1. Product-Name --> ' + n1[index1]+'\n************************************\n')
			print('2. Link : ' + n2[index1]+'\n************************************\n')
		print('3. Price --> Rs '+str(min1))

		print('\n=============================================================================================================================')

#-----------------------------------------------------------------------------------------------------------------------
	def snapdeal_scraper():

		list = prod_name.split(' ')
		a = 0
		u = "https://www.snapdeal.com/search?keyword="
		while a < len(list):
			if a < (len(list) - 1):
				u = u + list[a] + "%20"
			elif (a == len(list) - 1):
				u = u + list[a]
			a += 1

		print('\n')
		url = u + "&santizedKeyword=mouse&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"
		page = urllib.request.urlopen(url)
		html = page.read()

		soup = BeautifulSoup(html, "html.parser")

		m1 = []
		m2 = []
		for data in soup.findAll('p', {'class': 'product-title'}):             #for title
			title = data.get('title')
			m1.append(title)

		link = soup.find_all('div', class_="product-tuple-description")                       #for link
		for p in link:
			soupInner = BeautifulSoup(str(p),"html.parser")
			href = soupInner.find('div').find('div').find('a').get('href')
			m2.append(href)

		main_price = []               #for getting price ; main_price list contains product prices in specific order
		sorted_price = []                                                                 #sorted_price list contains sorted prices
		for p in soup.findAll('span', {'class': 'lfloat product-price'}):
			price = p.get('data-price')
			main_price.append(price)
			sorted_price.append(price)

		for index, item in enumerate(main_price):# for type conversion from string to int
			sorted_price[index] = int(item)
			main_price[index] = int(item)

		sorted_price.sort()

		min1 = sorted_price[0]  # first minimum price

		index1 = 0

		for i in range(0, len(main_price)):
			if (main_price[i] == min1 ):
				index1 = i
				break


		print('1. PRODUCT-NAME --> ' + m1[index1]+'\n************************************\n')
		print('2. LINK : ' + m2[index1]+'\n************************************\n')
		print('3. PRICE --> Rs ' + str(min1))

		print('\n=============================================================================================================================')
#-----------------------------------------------------------------------------------------------------------------------
	def ebay_scraper():
		list = prod_name.split(' ')
		a = 0
		u = "https://www.ebay.in/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.X.TRS0&_nkw="
		while a < len(list):
			if a < (len(list) - 1):
				u = u + list[a] + "+"
			elif (a == len(list) - 1):
				u = u + list[a]
			a += 1

		url = u + "&_sacat=0"
		page = urllib.request.urlopen(url)
		html = page.read()

		soup = BeautifulSoup(html, "html.parser")

		m1 = []
		m2 = []
		n1 = []
		n2 = []
		for data in soup.findAll('h3',{'class':'lvtitle'}):             #for title
			title = data.text
			m1.append(title)

		link = soup.find_all('h3', class_="lvtitle")                 # for link
		for p in link:
			soupInner = BeautifulSoup(str(p), "html.parser")
			href = soupInner.find('a').get('href')
			m2.append(href)

		link = soup.find_all('div', class_="gvtitle")		# for title link of other layout
		for p in link:
			soupInner = BeautifulSoup(str(p), "html.parser")
			href = soupInner.find('h3').find('a').get('href')
			title = soupInner.find('h3').find('a').text
			n1.append(title)
			n2.append(href)

		ff1 = 0
		ff2 = 0
		price = []
		for p in soup.findAll('li',{'class':'lvprice prc'}):             #for getting price
			ff1 = 1
			pr = p.text
			price.append(pr)

		for p in soup.findAll('div',{'class':'gvprices'}):             #for getting price for other layout
			ff2 = 1
			pr = p.text
			price.append(pr)


		if(ff1 == 1):
			price = [i[6:-4] for i in price]                        #for removing signs like \n and Rs.

		elif(ff2 == 1):
			price = [i[10:-18] for i in price]

		newlist = []  # for removing comma
		main_price = []
		temp = ""
		for i in price:
			j = 0
			temp = ""
			while j < len(i):
				if (i[j] == ','):
					temp = temp + str(i[j + 1])
					j += 1
				else:
					temp = temp + i[j]
				j += 1
			newlist.append(temp)
			main_price.append(temp)


		for index, item in enumerate(newlist):                                       #for type conversion from string to float
			if(len(item)>4):
				item=item[:6]
			newlist[index] = float(item)
			main_price[index] = float(item)

		newlist.sort()		#newlist stores the sorted prices and main_price stores the price in order

		min1 = newlist[0]		# first minimum price
		index1 = 0

		for i in range(0, len(main_price)):
			if (main_price[i] == min1):
				index1 = i

		if (ff1 == 1):
			print('1. Product-Name --> ' + m1[index1]+'\n************************************\n')
			print('2. Link : ' + m2[index1]+'\n************************************\n')
			print('3. Price --> Rs ' + str(min1))
		elif (ff2 == 1):
			print('1. Product-Name --> ' + n1[index1]+'\n************************************\n')
			print('2. Link : ' + n2[index1]+'\n************************************\n')
			print('3. Price --> Rs ' + str(min1))

	#-----------------------------------------------------------------------------------------------------------------------

	print('############################################################ FLIPKART RESULTS ############################################################\n')
	flipkart_scraper()
	print('\n\n\n############################################################ SNAPDEAL RESULTS ############################################################\n')
	snapdeal_scraper()
	print('\n\n\n############################################################# EBAY RESULTS ################################################################\n')
	ebay_scraper()
	
	
	
	
	
	
	
	
	

def recomm(y):
	import recommend
	if __name__ == "__main__":
		opl=recommend.func(y)
		print('\n\t\t\t\t\t\t\t'+'You may Like to see '+ str(opl) +'\n\t\t\t\t\t\t      _____________________________________\n\n')
		if cap=='1':
			core(opl,y)
		else:
			core2(opl,y)
		

def faltu(pnamee):
	import vvip
	if __name__ == "__main__":
		vvip.gotti(pnamee)							
		


def exita():
	print('\n\t\t\t\t\t   Thank You for using our software!! Hope you liked it!!\n')
	exit(0)
	
	
	
	
	
	
print('\n\n\n\t\t\t\t\t\tCHEAPEST PRODUCT FINDER AND PRODUCT RECOMMENDOR\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')	
cap=input('Enter your choice \n1. To get results between the websites\n2. To get results within the websites\n3. Exit\n\t--> ')

if cap=='1':
	cate=['electronics','appliances','men','women','kid','home','bookandmore']
	print ()
	print ('categories are : ')
	print ()
	print ('',cate[0])
	print ('',cate[1])
	print ('',cate[2])
	print ('',cate[3])
	print ('',cate[4])
	print ('',cate[5])
	print ('',cate[6])
	print ()							
	y=input('Enter category: ')

	pname=input("enter your product name: ")
	print('\n\n\t\t\t\t\t\t\tCHEAPEST PRODUCT NOTIFIER\n____________________________________________________________________________________________________________________________________________\n')
	core(pname,y)
	print('\n\n\t\t\t\t\t\t\t\tRECOMMENDOR SYSTEM\n____________________________________________________________________________________________________________________________________________\n')
	recomm(y)
	
elif cap=='2':
	cate=['electronics','appliances','men','women','kid','home','bookandmore']
	print ()
	print ('categories are : ')
	print ()
	print ('',cate[0])
	print ('',cate[1])
	print ('',cate[2])
	print ('',cate[3])
	print ('',cate[4])
	print ('',cate[5])
	print ('',cate[6])
	print ()							
	y=input('Enter category: ')
	
	pname=input("enter your product name: ")
	print('\n\n\t\t\t\t\t\t\tCHEAPEST PRODUCT NOTIFIER\n____________________________________________________________________________________________________________________________________________\n')
	
	core2(pname,y)
	print('\n\n\t\t\t\t\t\t\t\tRECOMMENDOR SYSTEM\n_____________________________________________________________________________________________________________________________________________\n')
	recomm(y)
	
	
		
else:
	exita()	

