"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


class Electorate(thinkbayes2.Suite):
    """Represents hypotheses about the state of the electorate."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: 
        data: 
        """

        a_hypo = hypo
        mean, std, measurement = data
        e_hypo = measurement - a_hypo

        like = thinkbayes2.EvalNormalPdf(e_hypo, mean, std)
        return like

def PrintSuiteInfo(suite):
    print("Mean:", suite.Mean())
    print("Std:", suite.Std())
    print("Probability of Losing:", suite.ProbLess(50))

def main():
    hypos = numpy.linspace(0, 100, 101)
    suite = Electorate(hypos)

    thinkplot.Pdf(suite, label='prior')

    data = 1.1, 3.7, 53 #mean prior error, std, measurement
    suite.Update(data)
    PrintSuiteInfo(suite)

    thinkplot.Pdf(suite, label='before poll')

    newpolldata = -2.3, 4.1, 49
    suite.Update(newpolldata)
    PrintSuiteInfo(suite)

    thinkplot.Pdf(suite, label='after poll')
    thinkplot.Show()
     

if __name__ == '__main__':
    main()
