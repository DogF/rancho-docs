

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
		#esta expresion niega su contenido ^(?:(?!boon\.ini|http).)*$\r?\n? boon.ini y/o http
		res= re.match("^(?:(?!Vea|vea|\-|\=|\n)){1}.{,60}",linea,re.S)
		if res:
			aux= str(res.group())
			#print aux, "\n otra \n",linea 
			print len(aux), " ",len(linea) 
			if aux==linea:
				g.write(linea)
				print linea
	g.close()
	f.close()