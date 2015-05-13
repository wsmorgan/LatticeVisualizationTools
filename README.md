# LatticeVisualizationTools

Python packages that will generate visuals of various lattices that are helpful for presentations.

## Python Packages Used

structures.py codes require the following python packages to run:
-matplotlib
-numpy
-termcolor
-argparse

## Running structures.py

The structures.py code takes an input string of numbers and uses that
to produce a periodic unit cell of the simple cubic(sc), body centered
cubic(bcc), face centered cubic(fcc), and hexagonal close packed(hcp)
types. The desired cell is produced by using the number of atoms in
the cell as the number of elements in the passed in list. For example
to produce a bcc cell with two different atoms in it. I would tpye:
```
python structures.py -colors 1 2
```

For an fcc cell with all the same atoms I would type:
```
python structures.py -colors 1 1 1 1
```

The list of arguments are numbers form 1 to 6. For further examples use:
```
python structures.py -examples
```