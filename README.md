WaveformNumerics  
================
Taylor Cathcart  
11/8/13  

Python script to write data sets for several interesting Physics functions, expressed as series  
Writes data sets to .txt files which can be pasted into spreadsheet/plotting software  
  
Top-level functions:  
write_func(func, res, n, x0, x1, name = None, param1 = None, param2 = None)  
	Writes x and y value to two separate text files  

write_deriv(func, res, n, x0, x1, derivs, name = None, param1 = None, param2 = None) 
	Writes x and value of a specified derivative of func(x) to two separate text files  
  
func (function) - function to be computed  
res (float) - delta x  
x0 (float) - minimum value in domain  
x1 (float) - max value in domain  
derivs (int) - number of derivatives to take  
name (str) - prefix for .txt name
param1 (float) - for wave packet, dominant wavenumber; for diffraction, slit width  
param2 (float) - for wave packet, wavenumber resolution; for diffraction, incident wavenumber  
  
Superposition functions can be added to the repository by defining f(x,n)  
Example calls to functions are included in ex.py  

Included Physics functions:  
square - series approximating square waveform, from sine transform of amplitude distribution
sawtooth - series approximating sawtooth waveform, from sine transform of amplitude distribution
diffraction - series approximating intensity as function of angle for single-slit diffraction
packet - series approximating wave packet with a dominant wavenumber


