
import sys
import re

print ("Number of arguments:"+ str(len(sys.argv))+ 'arguments.')
print ('Argument List:'+ str(sys.argv))
print ('origen '+sys.argv[1])
print ('destino '+sys.argv[2])
origen=sys.argv[1]
destino=sys.argv[2]
if(len(sys.argv)==3):
	f = open(origen,"r")
	g = open(destino,"w")
	for linea in f:
			link=re.sub("( |\(|\)|\*|\/|,)+","_",linea);
			link=link.replace("#","_")
			link=re.sub("á","a",link);
			link=re.sub("é","e",link);
			link=re.sub("í","i",link);
			link=re.sub("ó","o",link);
			link=re.sub("ú","u",link);
			link=re.sub("ñ","ni",link);
			aux="\t* ["+linea.strip()+"](#"+link.strip()+")\n\n"
			g.write(aux)
			print (aux)
	g.close()
	f.close()