'''
 * python file containing data for treemap
 *
 * @author Vedsar Kushwaha
 * @version 1.0
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 '''


import random

class Node(object):
	def __init__(self, data,color,name):
		self.data = data
		self.children = []
		self.color=color
		self.name=name

	def add_node(self, obj):
		self.children.append(obj)
		self.data=(self.data)+(obj.data)

def tree_struct():
	#data addition
	#eating tree
	color=(0,50,255)
	mess=Node(420,color,'Mess')
	color=(50,0,255)
	caf=Node(150,color,'Cafeteria')

	color=(50,50,255)
	eat=Node(0,color,'Eating')
	
	eat.add_node(mess)
	eat.add_node(caf)	
	
	#Travelling Tree
	color=(0,200,100)
	intra=Node(210,color,'intra college')
	color=(0,150,100)
	inter=Node(30,color,'inter college')
	color=(0,255,150)
	outs=Node(7,color,'outside college')
	
	color=(0,255,255)
	trav=Node(0,color,'Travelling')
	
	trav.add_node(intra)
	trav.add_node(inter)
	trav.add_node(outs)
	
	#Academics
	color=(200,200,0)
	clas=Node(450,color,'Classes')
	color=(255,150,0)
	assg=Node(1050,color,'Assignments')
	color=(150,255,0)
	crs=Node(420,color,'Course Books')
	
	color=(255,255,0)
	acad=Node(0,color,'Academics')
	acad.add_node(clas)
	acad.add_node(assg)
	acad.add_node(crs)
	
	#Playing
	color=(50,100,150)
	ch=Node(120,color,'Chess')
	color=(0,150,100)
	tt=Node(60,color,'TT')
	color=(0,220,120)
	carr=Node(120,color,'Carrem')
	
	color=(10,60,110)
	swim=Node(157,color,'Swimming')
	color=(20,120,220)
	ftb=Node(210,color,'Football')
	color=(30,60,90)
	cric=Node(60,color,'Cricket')
	
	color=(200,0,200)
	indr=Node(0,color,'Indoor')
	indr.add_node(ch)
	indr.add_node(tt)
	indr.add_node(carr)
	
	color=(180,20,180)
	otdr=Node(0,color,'Outdoor')
	otdr.add_node(swim)
	otdr.add_node(ftb)
	otdr.add_node(cric)
	
	color=(50,100,150)
	play=Node(0,color,'Playing')
	play.add_node(indr)
	play.add_node(otdr)
	
	#Sleeping
	color=(140,180,220)
	frrm=Node(210,color,'Freinds Room')
	color=(0,0,255)
	myrmr=Node(1260,color,'My Room')
	color=(255,0,0)
	wrpl=Node(210,color,'Working Place')
	
	color=(200,200,200)
	slpp=Node(0,color,'Sleeping')
	
	slpp.add_node(frrm)
	slpp.add_node(myrmr)
	slpp.add_node(wrpl)
	
	#Book Reading
	
	color=(0,200,0)
	strbk=Node(10,color,'Story Books')
	color=(0,220,200)
	slfhlp=Node(315,color,'Self Help')
	
	color=(12,210,210)
	bkrd=Node(0,color,'Book Reading')
	
	bkrd.add_node(strbk)
	bkrd.add_node(slfhlp)
	
	#Root Node Schedule
	color=(100,200,255)
	sche=Node(0,color,'Schedule')
	
	sche.add_node(bkrd)
	sche.add_node(slpp)
	sche.add_node(play)
	sche.add_node(acad)
	sche.add_node(trav)
	
	"""color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	a=Node(0,color,'A')
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	b=Node(0,color,'B')
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	c=Node(0,color,'C')
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	d=Node(2,color,'D')
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	e=Node(3,color,'E')
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	f=Node(4,color,'F')
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	g=Node(10,color,'G')
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	h=Node(0,color,'H')
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	i=Node(1,color,'I')
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	j=Node(11,color,'J')
	h.add_node(i)
	h.add_node(j)
	c.add_node(g)
	c.add_node(h)
	b.add_node(d)
	b.add_node(e)
	b.add_node(f)
	a.add_node(b)
	a.add_node(c)
	return a"""
	return sche

def trav(root):
	cnt=0
	#traverse first two levels
	cnt=root.data
	x_part=[]
	y_part=[]
	x_color=[]
	y_color=[]
	x_part.append(0)
	for x in root.children:
		x_part.append(x_part[-1] + float(x.data)/cnt)
		ytemp_part=[]
		ytemp_color=[]
		ycnt=x.data
		ytemp_part.append(0)
		for y in x.children:
			ytemp_part.append(ytemp_part[-1] + float(y.data)/ycnt)
		y_part.append(ytemp_part)
	return x_part,y_part

def get_node(x,xp,width):
	n=len(xp)-1
	for i in range(n):
		if((x>(xp[i]*width)) and (x<(xp[i+1]*width))):
			return i
