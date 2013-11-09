# script to write data points to a text file
# can handle any defined f(x,n) and numerical derivatives
# taylor cathcart 11/8/13

def write_func(func, res, n, x0, x1, name = None, param1 = None, param2 = None):
    write(func, res, n, x0, x1, 0, name, param1, param2)
    
def write_deriv(func, res, n, x0, x1, derivs, name = None, param1 = None, param2 = None):
    write(func, res, n, x0, x1, derivs, name, param1, param2)
    
def write(func, res, n, x0, x1, derivs, name, param1, param2):
    
    # initialize name if uninitialized
    if name == None:
        name = "n" + str(n)
        name = func.__name__ + "_" + name
    if derivs != 0:
        name = "deriv" + str(derivs) + "_" + name
    
    # open new files
    xfile = open(name + "_x_values.txt", "w")
    yfile = open(name + "_y_values.txt", "w")
    
    # generate value list
    outputlist = getderiv(func, res, n, x0, x1, derivs, param1, param2)
    
    i = 0

    while i < len(outputlist):
        xfile.write(str(i * res + x0) + "\n")
        yfile.write(str(outputlist[i]) + "\n")
        i += 1
            
    # close file after finishing
    xfile.close()
    yfile.close()
    
    # construct and print confirmation string
    message = "function " + func.__name__
    if derivs > 0:
        message = "derivative " + str(derivs) + " of " + message
    print "Successfully wrote data for " + message + ". Filename prefix: " + name
    
def generate(func, res, n, x0, x1, param1, param2):
    
    #initialize empty list to return
    size = (x1 - x0) / res
    retlist = [None] * int(size)
    i = 0
    
    # fill in list
    while i < len(retlist):
        x = x0 + (i * res)
        if param1 == None:
            retlist[i] = func(n, x)
        else:
            retlist[i] = func(n, x, param1, param2)
        i += 1
        
    print "Values successfully computed."
    
    return retlist
    
def getderiv(func, res, n, x0, x1, derivs, param1 = None, param2 = None):
    
    # base case
    if derivs == 0:
        return generate(func, res, n, x0, x1, param1, param2)
    
    # recursively find d^n-1/dx, then derive
    values = getderiv(func, res, n, x0, x1, (derivs - 1), param1, param2)
    
    derivlist = [None] * (len(values))
    i = 1
    
    # average slope for both neighbors
    while i < (len(values) - 1):
        
        current = values[i]
        nextval = values[i + 1]
        prev = values[i - 1]
        
        prevderiv = float(current - prev) / res
        nextderiv = float(nextval - current) / res
        
        # find average
        deriv = (prevderiv + nextderiv) / 2
        
        derivlist[i] = deriv
        
        i += 1
        
    # deal with endpoints
    derivlist[0] = float(values[1] - values[0]) / res
    derivlist[i] = float(values[i] - values[i - 1]) / res
    
    print "Derivative " + str(derivs) + " successfully computed."
        
    return derivlist
    
