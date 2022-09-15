
Jupyter Notebook files for analyzing XPCS data and generating figures. Vector graphic figures (`.pdf`) generated from Jupyter Notebooks are used directly in *Overleaf* manuscript without any further scaling or editing.

### Data Structures

#### ./Reduced_Data/SAXS_AbsCroSec.ipynb:
* Copies the manullay-averaged hdf files for SAXS (big roung beamstop mask) from `/net/wolf`;
* Recalculates `saxs_1d` in the unit of absolute cross-sections;
* Repacks `saxs_1d` into the hdf field and generates fixed hdf file with extension `SAXS_Abs_Cross` 

#### ./Analysis/Plot_SAXS.ipynb
* Generates the stacked SAXS 1D and SAXS 2D figure (Fig. 2)

#### ./Analysis/Plot_g2_tauQ.ipynb
* Generates the g$_2$ and $\tau$ vs. Q figure for water (Fig. 3)

#### ./Analysis/Plot_tauQ_AllSamples.ipynb
* Generates the $\tau$ vs. Q figure for water, NaCl and NH4 (Fig. 4)
