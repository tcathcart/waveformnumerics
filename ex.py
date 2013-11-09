# example calls to defined functions
# taylor cathcart 11/8/13

from functions import square, sawtooth, diffraction, packet
from writers import write_deriv, write_func

write_func(square, .0002, 50, 0, 10, "square")
write_func(sawtooth, .0002, 60, 0, 10, "sawtooth")
write_func(diffraction, .0001, 50, 0, 10, "diffraction", 0.16e-3, (2 * math.pi) / (650e-9))
write_func(packet, .0002, 50, -4, 4, "packet", 8, .01)

write_deriv(sawtooth, .0002, 50, 0, 10, 4, "sawtooth")
write_deriv(packet, .0002, 50, -4, 4, 2, "packet", 8, .01)

