## Data structures

This folder contains the data analysis and the figure-rendering scripts.   

All figures were directly generated from Matplotlib instead of going through Adobe Illustrator for the first time.

### ./Reduced_Data

#### ./Reduced_Data/G2g2_Trim.ipynb:
* Copies the manually-averaged hdf files for XPCS from `/net/wolf`;
   - Contains water, NaCl, NH4, and the 1st and 2nd half of water.
* Recalculates g$_2$ by removing the hot pixels at the first delay point on G2;
* Repacks g$_2$ back into the hdf field and generates fixed hdf file with extension `XPCS_Trim` 


#### * ./Reduced_Data/SAXS_AbsCroSec.ipynb:
* Copies the manullay-averaged hdf files for SAXS (big roung beamstop mask) from `/net/wolf`;
* Recalculates `saxs_1d` in the unit of absolute cross-sections;
* Repacks `saxs_1d` into the hdf field and generates fixed hdf file with extension `SAXS_Abs_Cross` 

### ./Analysis

#### ./Analysis/Plot_SAXS.ipynb
* Generates the stacked SAXS 1D and SAXS 2D figure (Fig. 2)

#### ./Analysis/Plot_g2_tauQ.ipynb
* Generates the g$_2$ and $\tau$ vs. Q figure for water (Fig. 3)

#### ./Analysis/Plot_tauQ_AllSamples.ipynb
* Generates the $\tau$ vs. Q figure for water, NaCl and NH4 (Fig. 4)
