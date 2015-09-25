#A plot to represent the quotient group

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import math as mt
from itertools import product

"""
This program is meant to be able to take a set of lattice vectors
for the most commonlattices, sc, fcc, hcp, bcc, and retur a picture
with the desired surface, eg (100), (110), (111), as well as vectors
indicating the 2D unit cell. This is still under development and is
not generalized yet.
"""

def read_lattice_vectors():
    """
    This function will read in the lattice vectors from a file, called
    lattice_vectors.in and then return those vectors to program in a
    useable format.
    """

    return(a1, a2, a3)

# def find_reciprocal_lattice(a1,a2,a3):
#     """
#     This function takes in the real space lattice vectors (a1, a2 and a3) and finds
#     the reciprocal lattice vectors (b1, b2 and b3).
#     The formula are:
#     b1 = 2*pi*(a2 cross a3)/(a1 dot (a2 cross a3))
#     b2 = 2*pi*(a3 cross a1)/(a1 dot (a2 cross a3))
#     b3 = 2*pi*(a1 cross a2)/(a1 dot (a2 cross a3))
#     """

#     # b1 = scalar_prod(2*mt.pi,scalar_prod(1/dot_prod(a1,cross_prod(a2,a3)),cross_prod(a2,a3)))
#     # b2 = scalar_prod(2*mt.pi,scalar_prod(1/dot_prod(a1,cross_prod(a2,a3)),cross_prod(a3,a1)))
#     # b3 = scalar_prod(2*mt.pi,scalar_prod(1/dot_prod(a1,cross_prod(a2,a3)),cross_prod(a1,a2)))

#     b1 = scalar_prod(1/dot_prod(a1,cross_prod(a2,a3)),cross_prod(a2,a3))
#     b2 = scalar_prod(1/dot_prod(a1,cross_prod(a2,a3)),cross_prod(a3,a1))
#     b3 = scalar_prod(1/dot_prod(a1,cross_prod(a2,a3)),cross_prod(a1,a2))
    
#     return(b1,b2,b3)

# def distance_to_next_plane(h,k,l,a1,a2,a3):
#     """
#     Here we find the distance between the (hkl) planes. It take for
#     it's arguments the hkl indices and the lattice vectors in this
#     order (h,k,l,a1,a2,a3).
#     """

#     print('h',h)
#     print('k',k)
#     print('l',l)

#     (b1,b2,b3) = find_reciprocal_lattice(a1,a2,a3)

#     print('b1',b1)
#     print('b2',b2)
#     print('b3',b3)
    
#     v = [h*b1[0]+k*b2[0]+l*b3[0],h*b1[1]+k*b2[1]+l*b3[1],h*b1[2]+k*b2[2]+l*b3[2]]

#     print('vd',v)
#     print('mag_v',mt.sqrt(dot_prod(v,v)))
#     print('2pi',2*mt.pi)

#     # d = 2*mt.pi/mt.sqrt(dot_prod(v,v))
#     d = 1/mt.sqrt(dot_prod(v,v))

#     print('d',d)
    
#     exit()
#     return(d)

def distance_between_points(p1,p2,normal):
    """
    This function finds the vector between 2 points then projects that
    vector onto the surface normal vector then finds the magnitude of
    the projection.
    """

    if(p1 == p2):
        d = 0
    else:
        v = [p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2]]

        # print('v',v)
        # print('v.v',dot_prod(v,v))
    
        proj = scalar_prod(dot_prod(v,normal)/mt.sqrt(dot_prod(v,v)),v)

        # print('proj',proj)
        
        d = round(mt.sqrt(dot_prod(proj,proj)),10)

        # print('d_in',d)
        
    return(d)

def gcd(a,b):
    """Returns the greatest common divisor of two numbers.
    """

    if (b==0):
        return a
    else:
        return(gcd(b,a % b))

def reduced_norm(norm):
    """Finds the reduced miller index for the normal vector.
    """

    a = norm[0]
    b = norm[1]
    c = norm[2]

    mult = reduce(gcd,(a,b,c))

    new_norm = [a/mult,b/mult,c/mult]

    return(new_norm)
    
def dot_prod(a,b):

    """
    This function takes two vectors, a and b, and finds the dot
    product,c.

    """
    c = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

    return(c)

def scalar_prod(n,a):
    """
    This function takes a scalar, n, and multiplies it by every
    element in a vector.
    """
    
    c = [n*a[0],n*a[1],n*a[2]]

    return(c)

def cross_prod(a,b):
    """ 
    This function takes two vectors, a and b, and find's their cross product.
    """

    c = [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]

    return(c)

def find_unit_vector(a):
    """
    This function takes a vector and finds the corresponding unit
    vector.
    """

    vec_length = mt.sqrt(a[0]*a[0]+a[1]*a[1]+a[2]*a[2])
    
    unit_vec = [a[0]/vec_length,a[1]/vec_length,a[2]/vec_length]
        
    return(unit_vec)
    
def main():
    """
    This program is meant to be able to take a set of lattice vectors
    for the most commonlattices, sc, fcc, hcp, bcc, and retur a picture
    with the desired surface, eg (100), (110), (111), as well as vectors
    indicating the 2D unit cell. This is still under development and is
    not generalized yet.
    """

    # (a1,a2,a3,surface_normal,ns) = read_lattice_vectors()

    a1 = [0.5,0.5,0]
    a2 = [0.5,0,0.5]
    a3 = [0,0.5,0.5]

    surface_normal = [2,0,0]

    ns = 3

    surface_normal = reduced_norm(surface_normal)
    
    print('surf_norm',surface_normal)

    #Here we find the atoms in the plane that passes through the
    #origin that is normal to the vector surface_normal
    atoms_in_plane = []
   
    for i in range(-10,10):
        for j in range(-10,10):
            for m in range(-10,10):
                b1 = scalar_prod(i,a1)
                b2 = scalar_prod(j,a2)
                b3 = scalar_prod(m,a3)
                atom = [b1[0]+b2[0]+b3[0],b1[1]+b2[1]+b3[1],b1[2]+b2[2]+b3[2]]
                if (dot_prod(atom,surface_normal)==0):
                    atoms_in_plane.append(atom)

    atoms_per_plane = [len(atoms_in_plane)]
    planes = [0]
    shift = [[0,0,0]]
    
    if(ns > 1):
        while(len(planes) < ns):
            
            next_plane = False
            t = 0
            nn = 2

            while(next_plane == False):
                possible_sites = list(product(range(nn),repeat=3))
                
                while((next_plane == False) and (t < len(possible_sites))):
                    v = possible_sites[t]
                    p2 = [v[0]*a1[0]+v[1]*a2[0]+v[2]*a3[0],v[0]*a1[1]+v[1]*a2[1]+v[2]*a3[1],v[0]*a1[2]+v[1]*a2[2]+v[2]*a3[2]]

                    dtp = distance_between_points([0,0,0],p2,surface_normal)
                    if((dtp != 0) and (dtp not in planes)):
                        next_plane = True
                        planes.append(dtp)
                        shift.append(p2)
                        t += 1
                    else:
                        t += 1
                        
                if(next_plane == False):
                    nn +=1
        
        for p in range(len(planes)):
            if (planes[p] != 0):
                atoms_in_nextplane = []
                for i in range(-10,10):
                    for j in range(-10,10):
                        for k in range(-10,10):
                            p2 = shift[p]
                            b1 = scalar_prod(i,a1)
                            b2 = scalar_prod(j,a2)
                            b3 = scalar_prod(k,a3)
                            atom = [b1[0]+b2[0]+b3[0],b1[1]+b2[1]+b3[1],b1[2]+b2[2]+b3[2]]
                            shifted_atom = [atom[0]-p2[0],atom[1]-p2[1],atom[2]-p2[2]]
                            if (dot_prod(shifted_atom,surface_normal)==0):
                                atoms_in_nextplane.append(atom)

                for i in atoms_in_nextplane:
                    atoms_in_plane.append(i)
                atoms_per_plane.append(len(atoms_in_nextplane))

    if (surface_normal != [1,0,0]):
        new_y = cross_prod([1,0,0],surface_normal)
    else:
        new_y = cross_prod([0,0,1],surface_normal)
           
    new_x = cross_prod(new_y,surface_normal)

    atoms = []
    
    for i in atoms_in_plane:
        atoms.append([dot_prod(new_x,i),dot_prod(new_y,i)])

    at_atom = 0
    which_color = 0
    
    for i in atoms_per_plane:
        for j in range(i):
            x = which_color/float(ns)
            plt.plot(atoms[at_atom][0],atoms[at_atom][1], marker = 'o', color = cm.gist_ncar(x), ls = '')
            at_atom += 1
        which_color += 1

    plt.show()
        
    return()
    
main()
