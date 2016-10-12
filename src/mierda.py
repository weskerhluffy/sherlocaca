import logging
import fileinput

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG

logger_cagada = None

def sherlocaca_core(tam_num):
	num_5s=tam_num//3
	sobrantes_de_5s=tam_num%3
	logger_cagada.debug("respetacion de %u %u %u"%(tam_num,num_5s,sobrantes_de_5s))
	if(sobrantes_de_5s==1):
		logger_cagada.debug("1 mod 3")
		if(tam_num<9):
			return None,None
		num_3s=2
		num_5s=(tam_num-10)//3
		return num_5s,num_3s

	
	if(not num_5s):
		return None,None

	if(sobrantes_de_5s==2):
		num_5s-=1
		sobrantes_de_5s+=3
	num_3s=sobrantes_de_5s//5
	logger_cagada.debug("respetacion si necesita ajuste %u %u"%(num_5s,num_3s))

	return num_5s,num_3s

def sherlocaca_transf_a_num(num_5s,num_3s):
	cadena_res=""
	for _ in range(num_5s):
		cadena_res+="555"
	for _ in range(num_3s):
		cadena_res+="33333"

	return cadena_res

def sherlocaca_main():
	primer_linea=True
	for line in fileinput.input():
		if(primer_linea):
			primer_linea=False
			continue
		if(not line.strip()):
			break
		num_act=int(line)
		num_5s,num_3s=sherlocaca_core(num_act)
		if(num_5s or num_3s):
			logger_cagada.debug("num 5s %u num 3s %u"%(num_5s,num_3s))
			caca=sherlocaca_transf_a_num(num_5s,num_3s)
		else:
			caca="-1"
#		print("%u:\t%s"%(num_act,caca))
		print("%s"%(caca))
		


if __name__ == '__main__':


	FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
	logging.basicConfig(level=nivel_log, format=FORMAT)

	logger_cagada = logging.getLogger("asa")
	logger_cagada.setLevel(nivel_log)
	logger_cagada.debug("mierda")

#	sherlocaca_core(1)
#	sherlocaca_core(3)
#	sherlocaca_core(5)
#	sherlocaca_core(11)
	sherlocaca_main()

   
