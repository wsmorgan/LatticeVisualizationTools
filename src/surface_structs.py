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

#     (b1,b2,b3) = find_reciprocal_lattice(a1,a2,a3)

#     v = [h*b1[0]+k*b2[0]+l*b3[0],h*b1[1]+k*b2[1]+l*b3[1],h*b1[2]+k*b2[2]+l*b3[2]]

#     # d = 2*mt.pi/mt.sqrt(dot_prod(v,v))
#     d = 1/mt.sqrt(dot_prod(v,v))

#     return(d)

def distance_between_planes(p1,p2,normal):
    """
    This function finds the vector between 2 points then projects that
    vector onto the surface normal vector then finds the magnitude of
    the projection.
    """

    if(p1 == p2):
        d = 0
    else:
        v = [p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2]]

        proj = scalar_prod(dot_prod(v,normal)/mt.sqrt(dot_prod(v,v)),v)

        d = round(mt.sqrt(dot_prod(proj,proj)),10)

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

def read_input():
    """This module reads input from the file 'surface.txt' to determine
    the lattice vectors, the miller indices for the surface, and the
    number of planes for the plot or poscar.
    """

    f = open('surface.txt', 'r')

    #This sequence will read in the desired data however the data
    #needs to be in the correct order in the file or else it wont
    #work.

    #First we read in the lattice vectors.
    l = f.readline()

    #Skip white space and lines that start with #
    while(('#' == l[0]) or (l.strip() == '')):
        l = f.readline()

    a1 = [float(i) for i in l.split()]
    
    l = f.readline().split()
    a2 = [float(i) for i in l]
    
    l = f.readline().split()
    a3 = [float(i) for i in l]

    #next we read in the miller indices after skipping more white
    #space

    l = f.readline()
    while(('#' == l[0]) or (l.strip() == '')):
        l = f.readline()

    miller_index = [float(i) for i in l.split()]
    
    #Now we read in the number of planes we want for the plot or the
    #poscar

    l = f.readline()

    while(('#' == l[0]) or (l.strip() == '')):
        l = f.readline()

    l = l.split()
    ns = float(l[0])

    return(a1,a2,a3,miller_index,ns)
    
def main():
    """
    This program is meant to be able to take a set of lattice vectors
    for the most commonlattices, sc, fcc, hcp, bcc, and retur a picture
    with the desired surface, eg (100), (110), (111), as well as vectors
    indicating the 2D unit cell. This is still under development and is
    not generalized yet.
    """

    (a1,a2,a3,surface_normal,ns) = read_input()

    surface_normal = reduced_norm(surface_normal)

    #Here we find the atoms in the plane that passes through the
    #origin that is normal to the vector surface_normal
    atoms_in_plane = []
   
    #loop over possible lattice vector combinations.
    for i in range(-10,10):
        for j in range(-10,10):
            for m in range(-10,10):
                #find the multiples of the lattice vectors
                b1 = scalar_prod(i,a1)
                b2 = scalar_prod(j,a2)
                b3 = scalar_prod(m,a3)
                #add up the lattice vectors to determine the loctaion
                #of the atom
                atom = [b1[0]+b2[0]+b3[0],b1[1]+b2[1]+b3[1],b1[2]+b2[2]+b3[2]]
                #if the vector from the orgin to the point is in the
                #plane then it's dot product with the normal vector
                #will be zero and we want to add it to th list of
                #atoms in th plane.
                if (dot_prod(atom,surface_normal)==0):
                    atoms_in_plane.append(atom)

    #After that we find out how many atoms were in that plane, which
    #is useful for the plotting later and then start building the
    #other planes, the plane variable tracks how many planes there are
    #and the distance between the current plane and the origin, the
    #different planes should always be equadistant. The shift array
    #keeps the location of an atom in each plane, which is then
    #treated as the new origin when finding the rest of the atoms in
    #that plane.
    atoms_per_plane = [len(atoms_in_plane)]
    planes = [0]
    shift = [[0,0,0]]
    
    #ns is the number of planes we want, this if there was only one
    #were done.
    if(ns > 1):
        #keep finding new planes and new atoms until we've found each
        #desired plane.
        
        while(len(planes) < ns):
            #logical, returns true once a new plane is found.
            next_plane = False

            #temporary variable useful for the loops
            t = 0
            #nn is used to limit the number of lattice vector
            #combinations used so that we don't have to generate an
            #arbitrarily large list. Instead if we need more lattice
            #points we'll increment nn.
            nn = 2

            #here we actually find the next plane in the sequenc. This
            #is done by going through the possible lattice vector
            #combinations and find the magnitude of their projection
            #onto the normal vector. If that value isn't in the list
            #of planes then we add it to the planes array, add the
            #lattice site to the shift array, then change next_plane
            #to True.
            while(next_plane == False):
                possible_sites = list(product(range(nn),repeat=3))
                
                while((next_plane == False) and (t < len(possible_sites))):
                    v = possible_sites[t]
                    #p2 is the lattice point in concideration
                    p2 = [v[0]*a1[0]+v[1]*a2[0]+v[2]*a3[0],v[0]*a1[1]+v[1]*a2[1]+v[2]*a3[1],v[0]*a1[2]+v[1]*a2[2]+v[2]*a3[2]]
                    #dtp is the magnitude of the projection of the
                    #vector from the origin to p2 along the normal
                    #vector.
                    dtp = distance_between_planes([0,0,0],p2,surface_normal)
                    #If dpt isn't zero or in planes then we found a new plane.
                    if((dtp != 0) and (dtp not in planes)):
                        next_plane = True
                        planes.append(dtp)
                        shift.append(p2)
                        t += 1
                    else:
                        t += 1
                        
                if(next_plane == False):
                    #If we've been to all the points and haven't found
                    #a new plane then we need to increase the
                    #multiples of the lattice vectors we consider.
                    nn +=1
        
        #For every plane we've found we now need to find the atoms in
        #that plane.
        for p in range(len(planes)):
            #We don't want to do the plane through the origin, we
            #alread found all the atoms in it.
            if (planes[p] != 0):
                atoms_in_nextplane = []
                #loop over possible lattice vector combinations.
                for i in range(-10,10):
                    for j in range(-10,10):
                        for k in range(-10,10):
                            #p2 is the point that the normal vector
                            #will pass through, ie the new origin for
                            #this plane
                            p2 = shift[p]
                            #find the multiples of the lattice vectors
                            b1 = scalar_prod(i,a1)
                            b2 = scalar_prod(j,a2)
                            b3 = scalar_prod(k,a3)
                            #add up the lattice vectors to determine
                            #the loctaion of the atom
                            atom = [b1[0]+b2[0]+b3[0],b1[1]+b2[1]+b3[1],b1[2]+b2[2]+b3[2]]
                            #now shift the atom by p2 to put it in the
                            #appropriate coordinates for the plane
                            #passing through p2
                            shifted_atom = [atom[0]-p2[0],atom[1]-p2[1],atom[2]-p2[2]]
                            #if the vector from the orgin to the point
                            #is in the plane then it's dot product
                            #with the normal vector will be zero and
                            #we want to add it to th list of atoms in
                            #th plane.
                            if (dot_prod(shifted_atom,surface_normal)==0):
                                atoms_in_nextplane.append(atom)

                #Add the atoms in the plane to the complete list of
                #atoms.
                for i in atoms_in_nextplane:
                    atoms_in_plane.append(i)
                atoms_per_plane.append(len(atoms_in_nextplane))

    #Now we need to change our x,y coordinates so that we can go from
    #a 3D space to a 2D surface plot for atomic positions.
    if (surface_normal != [1,0,0]):
        new_y = cross_prod([1,0,0],surface_normal)
    else:
        new_y = cross_prod([0,0,1],surface_normal)
           
    new_x = cross_prod(new_y,surface_normal)

    #make the new x and y axis into unit vectors to get the
    #dimmensions right.
    new_z = find_unit_vector(surface_normal)
    new_y = find_unit_vector(new_y)
    new_x = find_unit_vector(new_x)

    atoms = []
    
    # we need to project our atomic positions onto the new 2D plane.
    for i in atoms_in_plane:
        # if (i!=[0,0,0]):
        #     proj_x = scalar_prod(dot_prod(i,new_x)/mt.sqrt(dot_prod(i,i)),i)
        #     proj_y = scalar_prod(dot_prod(i,new_y)/mt.sqrt(dot_prod(i,i)),i)
        #     atoms.append([proj_x,proj_y])
        # else:
        #     atoms.append(i)
        atoms.append([dot_prod(new_x,i),dot_prod(new_y,i)])

    #variables for the plot. which color changes so that each plane
    #will have a different color of atom so that we can tell which
    #atom are in the same plane.
    at_atom = 0
    which_color = 0
    
    #Now we plot each plane order
    for i in atoms_per_plane:
        for j in range(i):
            x = which_color/float(ns)
            y_mag = mt.sqrt(dot_prod(new_y,new_y))
            x_mag = mt.sqrt(dot_prod(new_x,new_x))
            plt.axis('equal')
            plt.ylim((-2.5*y_mag,2.5*y_mag))
            plt.xlim((-2.5*x_mag,2.5*x_mag))
            plt.plot(atoms[at_atom][0],atoms[at_atom][1], marker = 'o', color = cm.gist_ncar(x),ms = 40,ls = '')
            at_atom += 1
        which_color += 1

    plt.show()
    return()    
main()
