'''
 * python file containing treemap of my Schedule
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

import sys,pygame
import data,random,time
from pygame.locals import QUIT, K_ESCAPE, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION

pygame.init()
lev=0
stack=[]
root = data.tree_struct()
curr_node=root
xwidth=640
ywidth=480
pygame.display.set_caption('My Schedule')

#create the screen
window = pygame.display.set_mode((xwidth,ywidth))
#display the tree map
flag=1
while True:
	if flag==1:
		#get the points
		xp,yp=data.trav(curr_node)
		window.fill((0,0,0))
		if len(curr_node.children)==0:
			#leaf node
			pygame.draw.rect(window, curr_node.color, (0,0,640,480))
			text_color=(255-curr_node.color[0],255-curr_node.color[1],255-curr_node.color[2])
			myfont=pygame.font.SysFont("Comic Sans MS", 50)
			label=myfont.render(curr_node.name, 1, text_color)
			window.blit(label, (100, 100))
			myfont=pygame.font.SysFont("Comic Sans MS", 20)
			label=myfont.render("You are at leaf node", 1, text_color)
			window.blit(label, (100, 200))
		else:
			#draw the map
			for i in range(len(xp)-1):
				color=curr_node.children[i].color
				pygame.draw.rect(window, color, (xp[i]*xwidth,0,(xp[i+1]-xp[i])*xwidth,480))
				text_color=(255-color[0],255-color[1],255-color[2])
				if len(yp[i])==1:
					#add text here
					myfont=pygame.font.SysFont("Comic Sans MS", 20)
					label=myfont.render(curr_node.children[i].name, 1, text_color)
					window.blit(label, (xp[i]*xwidth,0))
				for j in range(len(yp[i])-1):
					color=(curr_node.children[i]).children[j].color
					pygame.draw.rect(window,color,(xp[i]*xwidth,yp[i][j]*ywidth,(xp[i+1]-xp[i])*xwidth,(yp[i][j+1]-yp[i][j])*ywidth))
					#add text here
					text_color=(255-color[0],255-color[1],255-color[2])
					myfont=pygame.font.SysFont("Comic Sans MS", 20)
					label=myfont.render(curr_node.children[i].children[j].name, 1, text_color)
					window.blit(label, (xp[i]*xwidth,yp[i][j]*ywidth))
		flag=0
		pygame.display.update()
	for event in pygame.event.get(): 
		if event.type==MOUSEBUTTONDOWN and event.button==1:
			mousex,mousey=pygame.mouse.get_pos()
			chld=data.get_node(mousex,xp,xwidth)
			if len(curr_node.children)!=0:
				flag=1
				stack.append(curr_node)
				curr_node=curr_node.children[chld]
		elif event.type==MOUSEBUTTONDOWN and event.button==3:
			if len(stack)!=0:
				curr_node=stack.pop()
				flag=1
		elif event.type==pygame.QUIT:
			sys.exit(0)
