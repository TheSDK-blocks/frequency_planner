"""
========
Frequency mask
========

A frequency domain signal class to provide methods to vcombine and merge responses 

Current docstring documentation style is Numpy
https://numpydoc.readthedocs.io/en/latest/format.html

This text here is to remind you that documentation is important.
However, youu may find it out the even the documentation of this 
entity may be outdated and incomplete. Regardless of that, every day 
and in every way we are getting better and better :).

Initially written by Marko Kosunen, marko.kosunen@aalto.fi, 22.4.2020.

"""

import os
import sys
if not (os.path.abspath('../../thesdk') in sys.path):
    sys.path.append(os.path.abspath('../../thesdk'))

from thesdk import *

import numpy as np
import matplotlib.pyplot as plt

class frequency_mask(thesdk):
    @property
    def _classfile(self):
        return os.path.dirname(os.path.realpath(__file__)) + "/"+__name__
    
    def __init__(self,*arg,**kwargs):
        self._resolution=kwargs.get('resolution',10e3)
        self._range=kwargs.get('range',100e6)


    @property
    def resolution(self):
        ''' Frequency resolution
            
            Default: 10 Khz
        '''
        if not hasattr(self,'_resolution'):
            self._resolution=10e3
         
        return self._resolution

    @property
    def range(self):
        ''' Frequency range
            
            Default: 0-1MHz
        '''
        if not hasattr(self,'_range'):
            self._range=(0,1e6)
        return self._range
    @range.setter
    def range(self,val):
        self._range=val
        return self._range

    @property
    def plot_range(self):
        ''' Frequency range vector for plotting
            
        '''
        if not hasattr(self,'_plot_range'):
            self._plot_range=np.arange(self.range[0],self.range[1],
                    self.resolution).reshape(-1,1)
        return self._plot_range

    @property
    def mask(self):
        ''' Frequency mask
            
            Default: Column vector of range divided by resolution
        '''
        if not hasattr(self,'_mask'):
            self._mask=np.zeros(((int((self.range[1]-self.range[0])/self.resolution)),1))
        return self._mask

    @mask.setter
    def mask(self,val):
        self._mask=val
        return self._mask

    def mask_set(self,**kwargs):
        bounds=kwargs.get('bounds',self.range)
        magnitude=kwargs.get('magnitude',0)
        lower=int(bounds[0]/self.resolution)
        upper=int(bounds[1]/self.resolution)
        if not hasattr(self,'_mask'):
            print('Setting')
            self._mask=np.zeros(((int((self.range[1]-self.range[0])/self.resolution)),1))
            self._mask[lower:upper,0]=magnitude
        else:
            print('Setting')
            self._mask[lower:upper,0]=magnitude
        return self._mask


    def plotf(self):
        figure,axes = plt.subplots()
        hfont = {'fontname':'Sans'}
        axes.plot(self.plot_range,self.mask)
        titlestr = 'Frequency plan'
        axes.set_xlim(self.range[0], self.range[1])
        axes.set_ylabel('Magnitude [db]' , **hfont,fontsize=18);
        axes.set_xlabel('Frequency [Hz]', **hfont,fontsize=18);
        axes.grid(True)
        plt.suptitle(titlestr,fontsize=20);
        plt.grid(True);
        #plt.subplots_adjust(top=0.8)
        #printstr=self.figurepath+"/Covid19_Recovery_in_%s.%s" %(self.name,self.figtype)
        plt.show(block=False);
        #figure.savefig(printstr, format=self.figtype, dpi=300);






if __name__=="__main__":
    import matplotlib.pyplot as plt
    from  frequency_planner import *
    from  frequency_planner.frequency_mask import frequency_mask
    import pdb

    a=frequency_mask()
    a.range=(0,100e6)
    #print(a.mask)
    a.mask_set(bounds=(1e6,2e6),magnitude=10)
    #print(a.mask)
    a.plotf()

    input()
