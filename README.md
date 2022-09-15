
Jupyter Notebook files for analyzing XPCS data and generating figures. The figures are plotted using [Matplotlib](https://matplotlib.org/). The data readout and analysis code is built on [*pyXpcsViewer*](https://github.com/AdvancedPhotonSource/pyXpcsViewer). See Miaoqi Chu *et al.*, [J. Synchrotron Rad. **29**, 1122 (2022)](https://scripts.iucr.org/cgi-bin/paper?S1600577522004830). 

Vector graphic figures (`.pdf`) generated from Jupyter Notebooks are used directly in *Overleaf* manuscript without any further scaling or editing.

#### ./Analysis/Plot_SAXS.ipynb
* Generates stacked SAXS 1D and SAXS 2D figure (Fig. 2)

#### ./Analysis/Plot_g2_tauQ.ipynb
* Generates g<sub>2</sub> vs. τ and τ<sub>0</sub>(Q) vs. Q figure for Sample A (Fig. 3)

#### ./Analysis/Plot_tauQ_AllSamples.ipynb
* Generates τ<sub>0</sub>(Q) vs. Q figure for Sample A, B and C (Fig. 4)

#### ./Reduced_Data
* Contains g<sub>2</sub> and I vs. Q data for replotting the figures in the main manuscript. The data files can be opened directly in *pyXpcsviewer*.
