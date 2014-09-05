
import sys
import re

print ("Number of arguments:"+ str(len(sys.argv))+ 'arguments.')
print ('Argument List:'+ str(sys.argv))
print ('origen '+sys.argv[1])
print ('lista '+sys.argv[2])
print ('destino '+sys.argv[3])
origen=sys.argv[1]
lista=sys.argv[2]
destino=sys.argv[3]
if(len(sys.argv)==4):
	f = open(origen,"r")
	h = open(lista,"r")
	g = open(destino,"w")
	titulo = h.readline()
	if(titulo!=""):
		for linea in f:
			print (linea+"\notro\n"+titulo)
			if(linea==titulo):
				link=re.sub("( |\(|\)|\*|\/|,)+","_",linea);
				link=link.replace("#","_")
				link=re.sub("á","a",link);
				link=re.sub("é","e",link);
				link=re.sub("í","i",link);
				link=re.sub("ó","o",link);
				link=re.sub("ú","u",link);
				link=re.sub("ñ","ni",link);
				aux='<a name="'+link.strip()+'"></a>'+linea.strip()+"\n"
				g.write(aux)
				titulo = h.readline()
				print (aux)
			else:
				link=re.match("^[\-\=]{1,3}",linea);
				g.write(linea)
				if link:
					g.write("\n######[Arriba](#indice)\n")

	g.close()
	f.close()
	h.close()