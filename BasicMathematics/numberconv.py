def  dechex(n):        #Receives an decimal  number . Converts to hex
    return(hex(n)[2:])

def  decoct(n):        #Receives an decimal number . Converts to oct
    return(oct(n)[2:])

def decbin(n):         #Receives an decimal number . Converts to bin 
    return(bin(n)[2:])

def hexdec(n):         #Receives an hex number . Converts to decimal 
    return(int(n , base=16))

def octdec(n):         #Receives an oct number . Converts to  decimal
    return(int(n , base=8))

def bindec(n):         #Receives an binary number . Converts to decimal 
    return(int(n , base=2))


