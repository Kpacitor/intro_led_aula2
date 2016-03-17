#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


print "Limpando as configurações dos ports"
GPIO.cleanup()

print "Configurando o Esquema de numeração dos ports"
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

led1	= GPIO.PWM(17, 100)
led2	= GPIO.PWM(22, 100)
led3	= GPIO.PWM(23, 100)
led4	= GPIO.PWM(27, 100)

def ativando_led(port_gpio, duty_cycle):	
	if duty_cycle <= 100:
		if port_gpio == 17:
			print "GPIO 17 on"
			led1.start(duty_cycle)
		elif port_gpio == 22:
			print "GPIO 22 on"
			led2.start(duty_cycle)
		elif port_gpio == 23:
			print "GPIO 23 on"
			led3.start(duty_cycle)
		elif port_gpio == 27:
			print "GPIO 27 on"
			led4.start(duty_cycle)
		else:	
			print "Port Inválido"
			return
	else:
		print "Duty Cycle Inválido!! Deve ser maior que zero e menor que 100"




def main():
	ativando_led(17, 100) #Ativando o led 1 com duty cycle de 100%
	time.sleep(1)
	ativando_led(22, 100) #Ativando o led 1 com duty cycle de 100%
	time.sleep(1)
	ativando_led(23, 100) #Ativando o led 1 com duty cycle de 100%
	time.sleep(1)
	ativando_led(27, 100) #Ativando o led 1 com duty cycle de 100%	
	print "Waiting....."
	time.sleep(5)	
	led4.stop()
	led3.stop()
	led2.stop()
	led1.stop()		
	print "Limpando as configurações dos ports"
	GPIO.cleanup()	
	print "Fim da execução do programa"

if __name__ == "__main__":
    main()




