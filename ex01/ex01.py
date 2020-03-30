

def main() :
	x = float(input())
	y = float(input())
	dentro = False
	if(x < 0):
		x = -x

	if(x < 5 and 0 < y and y < 8) :		#Confere se está no rosto
		dentro = True
	if(x < 3 and 1 < y and y < 2) :			#Confere se é a boca
		dentro = False			
	if(1<x and x<4 and 4<y and y<7) :	#Confere se é o olho
		dentro = False	
	if(2<x and x<3 and 5<y and y<6) :	#Confere se é a pupila
		dentro = True	
	
	if(dentro):
		print("O ponto está dentro!")
	else :
		print("O ponto está fora!")



main()