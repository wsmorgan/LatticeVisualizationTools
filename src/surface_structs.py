#A plot to represent the quotient group

import matplotlib.pyplot as plt
import numpy as np
import math as mt

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

#     # b1 = 2*mt.pi*np.cross(a2,a3)/np.dot(a1,np.cross(a2,a3))
#     # b2 = 2*mt.pi*np.cross(a3,a1)/np.dot(a1,np.cross(a2,a3))
#     # b3 = 2*mt.pi*np.cross(a1,a2)/np.dot(a1,np.cross(a2,a3))

#     b1 = np.cross(a2,a3)/np.dot(a1,np.cross(a2,a3))
#     b2 = np.cross(a3,a1)/np.dot(a1,np.cross(a2,a3))
#     b3 = np.cross(a1,a2)/np.dot(a1,np.cross(a2,a3))

    
#     return(b1,b2,b3)

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
    
    print('vec_length',vec_length)
    
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

    # (a1,a2,a3,surface_normal) = read_lattice_vectors()

    # h = 1
    # k = 1
    # l = 0

    a1 = [0.5,0.5,0]
    a2 = [0.5,0,0.5]
    a3 = [0,0.5,0.5]

    # (b1,b2,b3) = find_reciprocal_lattice(a1,a2,a3)
    
    # print('b1',b1)
    # print('b2',b2)
    # print('b3',b3)

    # surface_normal = h*b1 + k*b2 + l*b3
    
    # d = -np.dot(a1,surface_normal)

    surface_normal = [1,1,0]

    print(surface_normal)

    # p1 = a1-np.dot(a1,surface_normal)*surface_normal
    # p2 = a2-np.dot(a2,surface_normal)*surface_normal
    # p3 = a3-np.dot(a3,surface_normal)*surface_normal

    # print('p1',p1)
    # print('p2',p2)
    # print('p3',p3)

    atoms_in_plane = []
   
    for i in range(-10,10):
        for j in range(-10,10):
            for k in range(-10,10):
                b1 = scalar_prod(i,a1)
                b2 = scalar_prod(j,a2)
                b3 = scalar_prod(k,a3)
                atom = [b1[0]+b2[0]+b3[0],b1[1]+b2[1]+b3[1],b1[2]+b2[2]+b3[2]]
                print('atom',atom)
                if (dot_prod(atom,surface_normal)==0):
                # if ((atom*surface_normal)==0):
                    atoms_in_plane.append(atom)
    print('found atmos')

    if (surface_normal != [1,0,0]):
        new_y = cross_prod([1,0,0],surface_normal)
    else:
        new_y = cross_prod([0,0,1],surface_normal)
        
    new_x = cross_prod(new_y,surface_normal)

    print('new_y',new_y,'new_x',new_x)

    new_z = find_unit_vector(surface_normal)
    new_y = find_unit_vector(new_y)
    new_x = find_unit_vector(new_x)
    
    print('new_y',new_y,'new_x',new_x,'new_z',new_z)

    atoms_2D = []
    
    for i in atoms_in_plane:
        atoms_2D.append([dot_prod(new_x,i),dot_prod(new_y,i)])

    plt.plot(*zip(*atoms_2D), marker = 'o', color='r', ls='')
    plt.show()
        
    return()
    
main()
