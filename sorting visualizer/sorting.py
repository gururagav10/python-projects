import pygame
import random

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((900,500))

pygame.display.set_caption('Sorting Visualizer')

class Array():

	def __init__(self, x, y, height,color):
		self.x = x
		self.y = y
		self.height = height
		self.width = 10
		self.color = color

	def draw(self,win):
		pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height))
	
class Box():

	def __init__(self, text, textColor, boxColor, x, y):
		self.text = text
		self.textColor = textColor
		self.boxColor = boxColor
		self.x = x
		self.y = y
		self.myfont = pygame.font.SysFont('Comic Sans MS', 15)
		self.textBox = self.myfont.render(self.text, False, self.textColor)
		self.t_width = self.textBox.get_width()
		self.t_height = self.textBox.get_height()
		self.createBox = None

	def draw(self,win):
		win.blit(self.textBox,(self.x + 4,self.y))
		self.createBox = pygame.draw.rect(win, self.boxColor, (self.x,self.y,self.t_width + 8, self.t_height),2)

def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j][2] > arr[j+1][2]:
				blackOut(arr[j])
				blackOut(arr[j+1])
				arr[j][2], arr[j+1][2] = arr[j+1][2], arr[j][2]
				animate(arr[j])
				animate(arr[j+1])				 
	return arr

def partition(arr,low,high): 
	i = low - 1   
	pivot = arr[high][2]       
	for j in range(low , high): 
		if arr[j][2] <= pivot:
			blackOut(arr[j])
			blackOut(arr[i+1])
			i += 1 
			arr[i][2],arr[j][2] = arr[j][2],arr[i][2]
			animate(arr[i])
			animate(arr[j])
	blackOut(arr[i+1])
	blackOut(arr[high])
	arr[i+1][2],arr[high][2] = arr[high][2],arr[i+1][2]
	animate(arr[i+1])
	animate(arr[high])
	return ( i+1 ) 

def quickSort(arr,low,high): 	
	if low < high:  
		pi = partition(arr,low,high)
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

def merge(arr,l,m,r):
	n1 = m-l+1
	n2 = r-m
	left = [0] * (n1)
	right = [0] * (n2)
	for i in range(0,n1):

		left[i] = arr[l+i][2]
	for j in range(0, n2):
		right[j] = arr[m+j+1][2]
	i = 0
	j = 0
	k = l
	while ((i<n1) and (j<n2)):
		if (left[i] <= right[j]):
			blackOut(arr[k])
			arr[k][2] = left[i]
			i+=1
			animate(arr[k])
		else:
			blackOut(arr[k])
			arr[k][2] = right[j]
			j+=1
			animate(arr[k])
		k+=1
	while i < n1:
		blackOut(arr[k])
		arr[k][2] = left[i]
		i+=1
		animate(arr[k])
		k+=1
	while j < n2:
		blackOut(arr[k])
		arr[k][2] = right[j]
		j+=1
		animate(arr[k])
		k += 1

def mergeSort(arr, l, r):
	if l<r:
		m = (l +(r-1))//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

def heapify(arr, n, i):
	largest = i
	left = 2*i + 1
	right = 2*i + 2
	
	if left < n and arr[left][2] > arr[i][2]:
		largest = left
	
	if right < n and arr[right][2] > arr[largest][2]:
		largest = right
		
	if largest != i:
		blackOut(arr[i])
		blackOut(arr[largest])
		arr[i][2],arr[largest][2] = arr[largest][2], arr[i][2]
		animate(arr[i])
		animate(arr[largest])
		heapify(arr, n, largest)

def heapSort(arr):
	n = len(arr)
	
	for i in range(n//2-1, -1, -1):
		heapify(arr,n,i)
		
	for i in range(n-1, -1, -1):
		blackOut(arr[i])
		blackOut(arr[0])
		arr[i][2], arr[0][2] = arr[0][2], arr[i][2]
		animate(arr[i])
		animate(arr[0])
		heapify(arr,i,0)

def insertionSort(arr):
	n = len(arr)

	for i in range(1,n):
		smallest = arr[i][2]
		j = i - 1
		while j>=0 and arr[j][2]>smallest:
			blackOut(arr[j+1])
			arr[j+1][2] = arr[j][2]
			animate(arr[j+1])
			j -= 1
		blackOut(arr[j+1])
		arr[j+1][2] = smallest
		animate(arr[j+1])

def animate(arr):
	temp = Array(arr[0], arr[1], arr[2],(255,255,255))
	temp.draw(win)
	pygame.time.delay(speed)
	pygame.display.update() 
	temp = Array(arr[0], arr[1], arr[2],(255,0,0))
	temp.draw(win)
	pygame.time.delay(speed)
	pygame.display.update()

def blackOut(arr):
	pygame.draw.rect(win, (0,0,0), (arr[0], arr[1], 10, arr[2]))
	pygame.display.update() 

init_x = 100
init_y = 100

def refreshWindow():
	boxClass['createArray'] = Box('Create New Array', (255,0,0),(255,0,0), 300, 50)
	boxClass['heapSort'] = Box('  Heap  Sort  ', (255,0,0),(255,0,0), 700, 100)
	boxClass['quickSort'] = Box('  Quick Sort  ', (255,0,0),(255,0,0), 700, 150)
	boxClass['mergeSort'] = Box('  Merge Sort  ', (255,0,0),(255,0,0), 700, 200)
	boxClass['bubbleSort'] = Box('  Bubble Sort  ', (255,0,0),(255,0,0), 700, 250)
	boxClass['insertionSort'] = Box('Insertion Sort', (255,0,0),(255,0,0), 700, 300)
	boxClass['speedSelector'] = [Box('Speed : ', (255,0,0),(0,0,0), 220, 400),Box(' Slow ', (255,0,0),(255,0,0), 320, 400),Box('Medium', (255,0,0),(255,0,0), 415, 400),Box(' Fast ', (255,0,0),(255,0,0), 515, 400)]


	if len(arrayList) == 0:
		i = 0
		while(i<n):
			rdm = random.randint(5,250)
			arrayList.append([init_x+i*11,init_y,rdm])
			i += 1

	for item in arrayList:
		arrayClass.append(Array(item[0],item[1],item[2],(255,0,0)))

	for item in arrayClass:
		item.draw(win)

	boxClass['createArray'].draw(win)
	boxClass['bubbleSort'].draw(win)
	boxClass['quickSort'].draw(win)
	boxClass['mergeSort'].draw(win)
	boxClass['heapSort'].draw(win)
	boxClass['insertionSort'].draw(win)
	for item in boxClass['speedSelector']:
		item.draw(win)

	pygame.display.update()

mouseclick = 0
n = 50
boxClass = {}
arrayList = [] 
arrayClass = []
speed = 10

run = True

while run:
	
	pygame.time.delay(100)

	if mouseclick > 0:
		mouseclick += 1
	if mouseclick > 3:
		mouseclick = 0
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	refreshWindow()

	pos = pygame.mouse.get_pos()
	pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
	if boxClass['createArray'].createBox.collidepoint(pos) and pressed1 and mouseclick == 0:
		arrayList = []
		arrayClass = []
		win.fill((0,0,0),(100,100,900,400))
		mouseclick = 1
	if boxClass['bubbleSort'].createBox.collidepoint(pos) and pressed1 and mouseclick == 0:
		arrayList = bubbleSort(arrayList)
		arrayClass = []
		win.fill((0,0,0), (100,100,900,400))
		mouseclick = 1
	if boxClass['quickSort'].createBox.collidepoint(pos) and pressed1 and mouseclick == 0:
		quickSort(arrayList, 0, len(arrayList)-1)
		arrayClass = []
		win.fill((0,0,0), (100,100,900,400))
		mouseclick = 1
	if boxClass['mergeSort'].createBox.collidepoint(pos) and pressed1 and mouseclick == 0:
		mergeSort(arrayList, 0, len(arrayList)-1)
		arrayClass = []
		win.fill((0,0,0), (100,100,900,400))
		mouseclick = 1
	if boxClass['heapSort'].createBox.collidepoint(pos) and pressed1 and mouseclick == 0:
		heapSort(arrayList)
		arrayClass = []
		win.fill((0,0,0), (100,100,900,400))
		mouseclick = 1
	if boxClass['insertionSort'].createBox.collidepoint(pos) and pressed1 and mouseclick == 0:
		insertionSort(arrayList)
		arrayClass = []
		win.fill((0,0,0), (100,100,900,400))
		mouseclick = 1
	if boxClass['speedSelector'][1].createBox.collidepoint(pos) and pressed1 and mouseclick == 0:
		speed = 100
	if boxClass['speedSelector'][2].createBox.collidepoint(pos) and pressed1 and mouseclick == 0:
		speed = 10
	if boxClass['speedSelector'][3].createBox.collidepoint(pos) and pressed1 and mouseclick == 0:
		speed = 1

pygame.quit()
	
	
  