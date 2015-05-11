import matplotlib.pyplot as plt
import numpy as np
from termcolor import cprint               
import argparse

def examples():
    """Prints the examles for the help script"""
    script = "structures.py"
    explain = ("Constructs visualizations unit cells of simple cubic(sc), "
               " body centered cubic(bcc), face centered cubic(fcc), and hexagonal"
               " close packed(hcp) structures.")
    contents =[(("Create visual of sc cell."),
                ("structures 1"),
                ("Please note that any number between 1 and 6 may be entered and that"
                 " the number entered will correspond to the color that will be used"
                 " to make the sc unit cell. Use only 1 number for the sc case, more" 
                 " will produce a different cell.")),
               (("Create visual of bcc cell."),
                ("structures 1 2"),
                ("Please note that any number between 1 and 6 may be entered and that"
                 " the number entered will correspond to the color that will be used"
                 " to make the bcc unit cell. Use only 2 numbers for the bcc case, more"
                 " or less will produce a different cell. Different arrangements of the 2"
                 " numbers will alternate the colors.")),
               (("Create visual of fcc cell."),
                ("structures 1 2 3 4"),
                ("Please note that any number between 1 and 6 may be entered and that"
                 " the number entered will correspond to the color that will be used"
                 " to make the fcc unit cell. Use only 4 numbers for the bcc case, more"
                 " or less will produce a different cell. Different arrangements of the 4"
                  " numbers will alternate the colors.")),
               (("Create visual of hcp cell."),
                ("structures 1 2 3 4 5 6"),
                ("Please note that any number between 1 and 6 may be entered and that"
                 " the number entered will correspond to the color that will be used"
                 " to make the bcc unit cell. Use only 6 numbers for the hcp case, more"
                 " or less will produce a different cell. Differenc arrangements of the 6"
                 " numbers will alternate the colors."))]
    required = ("REQUIRED: A list of 1, 2, 4, or 6 number ranging form 1 to 6 with spaces and no"
                "commas between them.")
    output = ("RETURNS: Creates a pdf of the desired cell. It will have the name of the created"
              "cell, i. e. sc.pdf, bcc.pdf, fcc.pdf, hcp.pdf.")
    outputfmt =('.pdf')
    details = ('')
    
    example(script,explain,contents,required,output,outputfmt,details)
    
def example(script, explain, contents, requirements, output, outputfmt, details):
    """Prints the example help for the script. Taken from Matt Burbidge."""
    blank()
    cprint(script.upper(), "yellow")
    cprint(''.join(["=" for i in range(70)]) + '\n', "yellow")

    cprint("DETAILS", "blue")
    std(explain + '\n')

    cprint(requirements, "red")
    cprint(output, "green")
    blank()

    if details != "":
        std(details)
        blank()

    cprint("OUTPUT FORMAT", "blue")
    std(outputfmt)
    blank()

    cprint("EXAMPLES", "blue")
    for i in range(len(contents)):
        pre, code, post = contents[i]
        std("{}) {}".format(i + 1, pre))
        cprint("    " + code, "cyan")
        if post != "":
            std('\n' + post)
        blank()

def blank(n=1):
    """Prints a blank line to the terminal. Taken from Matt Burbidge (mmb90)."""
    for i in range(n):
        print("")

def std(msg):
    """Prints a message in white to the terminal. Taken from Matt Burbidge (mmb90)."""
    cprint(msg, "white")
       
def err(msg):
    """Prints the specified message as an error; prepends "ERROR" to
    the message, so that can be left off. Taken from Matt Burbidge (mmb90).
    """
    cprint("ERROR: " + msg, "red")
    
def _parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-examples', help='See details on how to use program.',
                        action='store_true')
    parser.add_argument('-colors',nargs='+',help='The list of colors to be entered.')

    args = parser.parse_args()
    if args.examples:
        examples()
        exit(0)
    else:
        return args.colors

def sc_lattice(col):
    """This method creates the corners for the cubic cells."""
    """ARGS: col"""
    """col is the array of colors to be used for making the unit cell."""
    x1 = 0
    a = 1
    dx = -a*.2
    x2 = x1+a
    dy = a*.4

    fig = plt.gcf()                 
    mst = 40
    lwt = 4

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


def main():
    """
    This program makes unit cells for a periodic lattice. It can make
    simple cubic(sc), body centered cubic(bcc), and face centered
    cubic(fcc) cells. For a sc cell input one argument, for a bcc cell
    input 2 arguments, for an fcc cell input 4 arguments, for an hcp input
    6 arguments. Each argument indicates an atomic species on the specific
    lattic, the arguments are integers from 1 to 6.
    """
    args = _parse_args()
    col =[]
    #read in the user input and convert it to the colors to be used.
    for arg in args:
        if len(args)<=7 and len(args)>=1 and len(args)!=3 and len(args)!=5:
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
            elif arg == "5":
                col.append('#FA8072')
            elif arg == "6":
                col.append('#8B4513')
            else:
                err("The color you entered isn't valid. Please list integer numbers"
                    "between 1 and 4 with spaces between each integer. 1=blue, 2=red,"
                    "3=green, 4=yellow, 5=salmon, 6=brown.")
                exit()
        else:
            err("The number of arguments passed does not match a sc, bcc, or fcc"
                "cell. Pleas list 1(sc), 2(bcc) or 4(fcc) integers after calling tho progrom.")
            exit()

    #length of the lattice vector a.
    a = 1
    
    #sc plot
    fig = plt.gcf()                 
    
    mst = 40
    lwt = 4
    
    x1 = 0
    dx = -a*.2
    x2 = x1+a
    dy = a*.4

    
    if len(col)==1:
        sc_lattice(col)
        #plotting instructions
        plt.xlim(dx*2,a+dy*2)
        plt.ylim(dx,a+dy*2)
        plt.axis('off')
        fig.savefig('sc.pdf', transparent = True)

    elif len(col)==2:
        sc_lattice(col)
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
        fig.savefig('bcc.pdf', transparent = True)
        
    elif len(col)==4:
        sc_lattice(col)
        #add atoms for fcc
        #atom at center of front surface
        plt.plot(x2*.5,x2*.5,'o',ms = mst,color = col[2],zorder = 4)
        #atom at center of back surface
        plt.plot(x2*.5+dx,x2*.5+dy,'o',ms = mst,color = col[2],zorder = 4)
        #atom at center of top face
        plt.plot((x2+dx)*.5,x2+dy*.5,'o',ms = mst,color = col[1],zorder = 4)
        #atom at center of bottom face
        plt.plot((x2+dx)*.5,dy*.5,'o',ms = mst,color = col[1],zorder = 4)
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
        fig.savefig('fcc.pdf', transparent = True)

        #instructions for hcp lattice
    elif len(col) == 6:
        x1 = 0
        x2 = 0
        x3 = 0
        a = 6
        c = 2*a
        #atom at center of bottom of hexegon
        plt.plot(x1-1,x1,'o',ms = mst,color = col[0],zorder = 4)
        #atoms to right and to left of the central bottom atom
        plt.plot(-a-1,x1,'o',ms = mst,color = col[1],zorder = 6)
        plt.plot(a-1,x1,'o',ms = mst,color = col[2],zorder = 6)
        #atoms forming back spokes of the hexegan
        plt.plot(-a/2-2,a/3,'o',ms = mst,color = col[2],zorder = 4)
        plt.plot(a/2-2,a/3,'o',ms = mst,color = col[1],zorder = 4)
        #atoms forming front spokes of the hexegan
        plt.plot(-a/2,-a/3,'o',ms = mst,color = col[2],zorder = 6)
        plt.plot(a/2,-a/3,'o',ms = mst,color = col[1],zorder = 6)
        
        
        #atom at center of top of hexegon
        plt.plot(x1-1,c,'o',ms = mst,color = col[0],zorder = 4)
        #atoms to right and to left of the central top atom
        plt.plot(x1-a-1,c,'o',ms = mst,color = col[1],zorder = 6)
        plt.plot(x1+a-1,c,'o',ms = mst,color = col[2],zorder = 6)
        #atoms forming back spokes of the hexegan
        plt.plot(-a/2-2,c+a/3,'o',ms = mst,color = col[2],zorder = 4)
        plt.plot(a/2-2,c+a/3,'o',ms = mst,color = col[1],zorder = 4)
        #atoms forming front spokes of the hexegan
        plt.plot(-a/2,c-a/3,'o',ms = mst,color = col[2],zorder = 6)
        plt.plot(a/2,c-a/3,'o',ms = mst,color = col[1],zorder = 6)
        
        #central atoms
        plt.plot(x1-.1,c/2-a/6,'o',ms = mst,color = col[3],zorder = 4)
        plt.plot(a/2-1.5,c/2+a/6,'o',ms = mst,color = col[4],zorder = 4)
        plt.plot(-a/2-1.5,c/2+a/6,'o',ms = mst,color = col[5],zorder = 4)
        
        #draw the lines that connect the hcp atoms.
        plt.plot((-a/2,-a/2),(-a/3,c-a/3),color='k',lw = lwt,zorder=5)
        plt.plot((a/2,a/2),(-a/3,c-a/3),color='k',lw = lwt,zorder=5)
        plt.plot((a/2,-a/2),(c-a/3,c-a/3),color='k',lw = lwt,zorder=5)
        plt.plot((a/2,-a/2),(-a/3,-a/3),color='k',lw = lwt,zorder=5)
        plt.plot((a/2,a-1),(-a/3,x1),color='k',lw = lwt,zorder=5)
        plt.plot((-a/2,-a-1),(-a/3,x1),color='k',lw = lwt,zorder=5)
        plt.plot((a/2,a-1),(c-a/3,c),color='k',lw = lwt,zorder=5)
        plt.plot((-a/2,-a-1),(c-a/3,c),color='k',lw = lwt,zorder=5)
        plt.plot((a/2-2,a-1),(c+a/3,c),color='k',lw = lwt,zorder=3)
        plt.plot((-a/2-2,-a-1),(c+a/3,c),color='k',lw = lwt,zorder=3)
        plt.plot((a/2-2,a-1),(a/3,x1),color='k',lw = lwt,zorder=3)
        plt.plot((-a/2-2,-a-1),(a/3,x1),color='k',lw = lwt,zorder=3)
        plt.plot((a/2-2,-a/2-2),(c+a/3,c+a/3),color='k',lw = lwt,zorder=3)
        plt.plot((a/2-2,-a/2-2),(a/3,a/3),color='k',lw = lwt,zorder=3)
        plt.plot((a-1,a-1),(x1,c),color='k',lw = lwt,zorder=3)
        plt.plot((-a-1,-a-1),(x1,c),color='k',lw = lwt,zorder=3)
        plt.plot((a/2-2,a/2-2),(a/3,c+a/3),color='k',lw = lwt,zorder=2)
        plt.plot((-a/2-2,-a/2-2),(a/3,c+a/3),color='k',lw = lwt,zorder=2)
        # plt.plot((x1-.5,-a/2-1.5),(c/2-a/6,c/2+a/6),color='k',lw = lwt,zorder=3)
        # plt.plot((x1-.5,a/2-1.5),(c/2-a/6,c/2+a/6),color='k',lw = lwt,zorder=3)
        # plt.plot((-a/2-1.5,a/2-1.5),(c/2+a/6,c/2+a/6),color='k',lw = lwt,zorder=3)
        



        plt.xlim(-2*a,2*a)
        plt.ylim(-3.5,c+3.5)
        plt.axis('off')
        fig.savefig('hcp.pdf', transparent = True)

if __name__ == '__main__':
    main()
