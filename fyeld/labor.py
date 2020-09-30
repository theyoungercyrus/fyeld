import numpy as np

class labor: 

    def __init__(self, 
            remaining,
            saturations): 
        """
        n-dim series, but mostly 1-dim, 
        describing  saturations of voter contacts in respect to time remaining 
        so that linearly scaling benchmarks may be provided to campaigns
        represented as numpy array

        o(n) solution but provides discrete values where 

        a-b f(x)t(x)  | as t(x) is necessarily linear in this application, the solution may simply reduce linear space until an arbitrary limit is met 
        
        here instead the integral is approxiamted by recursively 
        dividing a series of x
   
        Parameters 
        -------------- 

        days_remaining:  
            the number of (any) unit of time remaining (days, week, month)
        saturations : int
            the number of full saturations, waves, or passes on a given set of things

        """
          
        self.lin_remaining = np.linspace(1,
                remaining, 
                remaining)
        self.saturations = saturations

    def __iter__(self):
        #yield each point in time, every unit of time remaining, 
        #should probably be k, v pair of index, work rate
        for k, v in enumerate(self.checks(self.lin_remaining)): 
            yield tuple(k, v)

    def __len__(self):
        pass

    def __add__(self): 
        pass

    def __subtract__(self):
        pass

    def __mul__(self): 
        pass

    def __truediv__(self):
        pass

    def __neg__(self):
        pass

    def checks(self, space):
        """
        """
        #the reducing gets caught up in the for loop 
        #NOT passing back outside this func, does not return 
        for i in range(1,1_000):
            #labor is of quality parameter.remaining, 
            #calling reducer changes self.lin_remaining 
            #permanently for the class in its instance use
            sa = self.reducer(i, self.lin_remaining) 
            if sa.sum() < self.saturations: 
                return sa  #returns INSIDE for loop
            else: 
                pass

    def reducer(self, s):
        """
        """
        return np.array(
                [round(x/i,2) for x in s]
                )




"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
"""

"""
Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is
        False)

    Returns
    -------
    list
        a list of strings used that are the header columns
"""
