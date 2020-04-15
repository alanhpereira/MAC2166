
import math

#função que calcula a distancia entre dois pontos
def dist(x1,y1,x2,y2):
	return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def main():
	x0=float(input())
	y0 = float(input())
	n = int(input())
	xp = float(input()) #x do ponto mais próximo
	yp = float(input()) #y do ponto mais próximo
	p = 1				#número do ponto mais prómimos
	for i in range(2, n+1):
		xi = float(input())
		yi = float(input())
		if(dist(x0,y0,xi,yi)<dist(x0,y0,xp,yp)):
			p = i
			xp = xi
			yp = yi
	print("O ponto mais proximo de (%.2f, %.2f) é o ponto %d com ditancia %.3f"%(x0,y0,p,dist(x0,y0,xp,yp)))
	
main()