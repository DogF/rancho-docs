
import sys
import re

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print 'origen ',sys.argv[1]
print 'destino ',sys.argv[2]
origen=sys.argv[1]
destino=sys.argv[2]
if(len(sys.argv)==3):
	f = open(origen,"r")
	g = open(destino,"w")
	for linea in f:
			g.write(linea.strip(" \t"))
			print linea
	g.close()
	f.close()