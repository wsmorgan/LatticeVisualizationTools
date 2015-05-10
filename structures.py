import matplotlib.pyplot as plt
import numpy as np
import sys

def sc_lattice():
    #for a sc structure
    #front bottom left corner
    plt.plot(x1,x1,'o',ms = mst,color = col[0],zorder=6)
    #front top left corner
    plt.plot(x1,x2,'o',ms = mst,color = col[0],zorder=6)
    #front bottom right corner
    plt.plot(x2,x1,'o',ms = mst,color = col[0],zorder=6)
    #front top right corner
    plt.plot(x2,x2,'o',ms = mst,color = col[0],zorder=6)
    #back top right corner
    plt.plot(x2+dx,x2+dy,'o',ms = mst,color = col[0],zorder=2)
    #back bottom left corner
    plt.plot(dx,dy,'o',ms = mst,color = col[0],zorder=2)
    #back bottom right corner
    plt.plot(x2+dx,dy,'o',ms = mst,color = col[0],zorder=2)
    #back top left coner
    plt.plot(dx,x2+dy,'o',ms = mst,color = col[0],zorder=2)
    
    #connecting lines for front fac
    plt.plot((x1,x1),(x1,x2),color='k',lw = lwt,zorder=5)
    plt.plot((x1,x2),(x1,x1),color='k',lw = lwt,zorder=5)
    plt.plot((x2,x2),(x1,x2),color='k',lw = lwt,zorder=5)
    plt.plot((x1,x2),(x2,x2),color='k',lw = lwt,zorder=5)

    #connecting lines for sides
    plt.plot((x1,dx),(x1,dy),color='k',lw = lwt,zorder=1)
    plt.plot((x2,x2+dx),(x1,dy),color='k',lw = lwt,zorder=1)
    plt.plot((x1,dx),(x2,x2+dy),color='k',lw = lwt,zorder=1)
    plt.plot((x2,x2+dx),(x2,x2+dy),color='k',lw = lwt,zorder=1)
    
    #connecting lines for back
    plt.plot((dx,dx),(dy,x2+dy),color='k',lw = lwt,zorder=1)
    plt.plot((dx,x2+dx),(dy,dy),color='k',lw = lwt,zorder=1)
    plt.plot((x2+dx,x2+dx),(dy,x2+dy),color='k',lw = lwt,zorder=1)
    plt.plot((dx,x2+dx),(x2+dy,x2+dy),color='k',lw = lwt,zorder=1)


"""
This program makes unit cells for a periodic lattice. It can make
simple cubic(sc), body centered cubic(bcc), and face centered
cubic(fcc) cells. For a sc cell input one argument, for a bcc
cell input 2 arguments, for an fcc cell input 4 arguments. Each
argument indicates an atomic species on the specific lattic, the 
arguments are integers from 1 to 4.
"""
col =[]

#read in the user input and convert it to the colors to be used.
for arg in sys.argv:
    if len(sys.argv)<=7 and len(sys.argv)>1 and len(sys.argv)!=4 and len(sys.argv)!=6:        
        if arg=="structures.py":
            cal = []
        elif arg=="1":
            col.append("b")
        elif arg=="2":
            col.append("r")
        elif arg=="3":
            col.append("#33CC33")
        elif arg=="4":
            col.append("#FFFF00")
        elif arg == 5:
            col.append('m')
        elif arg == 6:
            col.append('k')
        else:
            print("Error in passed in argument. Please list integer numbers between 1 and 4 with spaces between each integer. 1=blue, 2=red, 3=green, 4=yellow.")
            exit()
    else:
        print "The number of arguments passed does not match a sc, bcc, or fcc cell. Pleas list 1(sc), 2(bcc) or 4(fcc) integers after calling tho progrom."
        exit()

#O sets the location of the origin, default is (0,0), a sets the
#length of the lattice vector a.
O = 0
a = 1

#sc plot
fig = plt.gcf()                 

mst = 40
lwt = 4

x1 = O
dx = -a*.2
x2 = x1+a
dy = a*.4

    
if len(col)==1:
    sc_lattice()
    #plotting instructions
    plt.xlim(dx*2,a+dy*2)
    plt.ylim(dx,a+dy*2)
    plt.axis('off')
    plt.show()
    fig.savefig('sc.pdf', transparent = True)

elif len(col)==2:
    sc_lattice()
    #add atom for bcc at body center
    plt.plot((x2+dx)/2,(x2+dy)/2,'o',ms = mst,color = col[1],zorder = 4)
    #add lines to body center
    plt.plot((x1,x2+dx),(x1,x2+dy),color = 'k',lw = lwt,zorder =1)
    plt.plot((x2,dx),(x1,x2+dy),color = 'k',lw = lwt,zorder =1)
    plt.plot((x1,x2+dx),(x2,dy),color = 'k',lw = lwt,zorder =1)
    plt.plot((dx,x2),(dy,x2),color = 'k',lw = lwt,zorder =1)
    
    #plotting instructions
    plt.xlim(dx*2,a+dy*2)
    plt.ylim(dx,a+dy*2)
    plt.axis('off')
    plt.show()
    fig.savefig('bcc.pdf', transparent = True)

elif len(col)==4:
    sc_lattice()
    #add atoms for fcc
    #atom at center of front surface
    plt.plot(x2*.5,x2*.5,'o',ms = mst,color = col[1],zorder = 4)
    #atom at center of back surface
    plt.plot(x2*.5+dx,x2*.5+dy,'o',ms = mst,color = col[1],zorder = 4)
    #atom at center of top face
    plt.plot((x2+dx)*.5,x2+dy*.5,'o',ms = mst,color = col[2],zorder = 4)
    #atom at center of bottom face
    plt.plot((x2+dx)*.5,dy*.5,'o',ms = mst,color = col[2],zorder = 4)
    #atom at center of left face
    plt.plot(dx*.5,(x2+dy)*.5,'o',ms = mst,color = col[3],zorder = 4)
    #atom at center of right face
    plt.plot(x2+dx*.5,(x2+dy)*.5,'o',ms = mst,color = col[3],zorder = 4)
    
    #lines connecting the atoms
    plt.plot((x1,x2),(x1,x2),color='k',lw = lwt,zorder=1)
    plt.plot((x2,x1),(x1,x2),color='k',lw = lwt,zorder=1)
    plt.plot((dx,x2+dx),(dy,x2+dy),color='k',lw = lwt,zorder=1)
    plt.plot((x2+dx,dx),(dy,x2+dy),color='k',lw = lwt,zorder=1)
    plt.plot((x1,x2+dx),(x1,dy),color='k',lw = lwt,zorder=1)
    plt.plot((x2,dx),(x1,dy),color='k',lw = lwt,zorder=1)
    plt.plot((x2,dx),(x2,x2+dy),color='k',lw = lwt,zorder=1)
    plt.plot((x1,x2+dx),(x2,x2+dy),color='k',lw = lwt,zorder=1)
    plt.plot((x2+dx,x2),(dy,x2),color='k',lw = lwt,zorder=1)
    plt.plot((x2,x2+dx),(x1,x2+dy),color='k',lw = lwt,zorder=1)
    plt.plot((x1,dx),(x1,x2+dy),color='k',lw = lwt,zorder=1)
    plt.plot((dx,x1),(dy,x2),color='k',lw = lwt,zorder=1)
        
    #plotting instructions
    plt.xlim(dx*2,a+dy*2)
    plt.ylim(dx,a+dy*2)
    plt.axis('off')
    plt.show()
    fig.savefig('fcc.pdf', transparent = True)

#instructions for hcp lattice
elif len(col) == 6:
    x1 = 0
    x2 = 0
    x3 = 0
    a = 6
    c = 2*a
    #atom at center of bottom of hexegon
    plt.plot(x1,x1,'o',ms = mst,color = col[1],zorder = 4)
    #atoms to right and to left of the central bottom atom
    plt.plot(-a,x1,'o',ms = mst,color = col[2],zorder = 4)
    plt.plot(a,x1,'o',ms = mst,color = col[2],zorder = 4)
    #atoms forming back spokes of the hexegan
    plt.plot(-a/2,a/3,'o',ms = mst,color = col[2],zorder = 4)
    plt.plot(a/2,a/3,'o',ms = mst,color = col[2],zorder = 4)
    #atoms forming front spokes of the hexegan
    plt.plot(-a/2,-a/3,'o',ms = mst,color = col[2],zorder = 4)
    plt.plot(a/2,-a/3,'o',ms = mst,color = col[2],zorder = 4)

    
    #atom at center of top of hexegon
    plt.plot(x1,c,'o',ms = mst,color = col[1],zorder = 4)
    #atoms to right and to left of the central top atom
    plt.plot(x1-a,c,'o',ms = mst,color = col[2],zorder = 4)
    plt.plot(x1+a,c,'o',ms = mst,color = col[2],zorder = 4)
    #atoms forming back spokes of the hexegan
    plt.plot(-a/2,c+a/3,'o',ms = mst,color = col[2],zorder = 4)
    plt.plot(a/2,c+a/3,'o',ms = mst,color = col[2],zorder = 4)
    #atoms forming front spokes of the hexegan
    plt.plot(-a/2,c-a/3,'o',ms = mst,color = col[2],zorder = 4)
    plt.plot(a/2,c-a/3,'o',ms = mst,color = col[2],zorder = 4)


    plt.xlim(-2*a,2*a)
    plt.ylim(-3.5,c+3.5)
    plt.axis('off')
    plt.show()
    fig.savefig('fcc.pdf', transparent = True)
