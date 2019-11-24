# 3-Dimensional-LMA-leaf-level

This repository contains models for estimating leaf mass per area (LMA) from leaf-level
spectra collected using ASD FS3 and SE PSR 3500+ spectrometers.

<span style="color:red">*As with all empirical models use these models with caution!!! Before using the models fully read the model metadata to understand what data was used to build the model, how it was built and how well models performed.
Ideally compare model estimates against validation data, or at least have an idea of the range of values expected for your dataset.*</span>

## Included files
- **plsr\_apply\_model.py**: Python script to apply models
- **3d_leaf\_lma\_g\_m2\_ASD\_FS3.json**: ASD FS3 JSON file with model coefficients and ancillary data
- **3d_leaf\_lma\_g\_m2\_ASD\_FS3.png**: ASD FS3 model diagnostics
- **3d_leaf\_lma\_g\_m2\_SE\_PSR.json**: SE PSR 3500+ JSON file with model coefficients and ancillary data
- **3d_leaf\_lma\_g\_m2\_SE\_PSR.png**: SE PSR 3500+ model diagnostics

*See below for JSON file contents*

## Script requirements
- numpy
- scipy
- pandas (*optional for loading spectra*)

## Measurement details

Sampling took place on sites within Domain 5 (Great Lakes) of the NEON network in September 2016
(ASD FS3) and September 2017 (SE PSR 3500+). Leaves were collected from a range of heights
throughout the canopy, spectral measurements were generally made immediately after collection, in
cases when that was not possible leavea were stored in a cooler until measurements could be made. A
single spectra was collected per leaf, spectra were referenced against a measurement on a Spectralon panel
to derive reflectance. The same day, leaf area was measured with a LI-3100 leaf area meter. Leaves
were dried in a freeze-drier (>120 hrs) and dry mass was measured with a precision balance. Dry mass
was divided by the one-sided fresh area to derive LMA g/m<sup>2</sup>.

## Species
- Red maple (*Acer rubrum*)
- Sugar maple (*Acer saccharum*)
- River birch (*Betula alleghaniensis*)
- Paper birch (*Betula papyrifera*)
- Beaked hazelnut (*Corylus cornuta*)
- White ash (*Fraxinus americana*)
- Black ash (*Fraxinus nigra*)
- Ironwood (*Ostrya virginiana*)
- Bigtooth aspen (*Populus grandidentata*)
- Trembling aspen(*Populus tremuloides*)
- Cherry (*Prunus sp.*)
- Red oak(*Quercus rubra*)
- American basswood (*Tilia americana*)
- American elm (*Ulmus americana*)

## Modeling building 
Models were built using partial least squares regression (PLSR). Prior to model building ASD
spectra were jump corrected. A Monte Carlo-like outlier test was applied to the data prior to model
building, information about the number of outliers detected can be found in the model
diagnostics. The data were split randomly 50/50 into calibration and validation. The calibration
data was used to determine the number of model components by minimizing predicted residual sum of squares
(PRESS). The adjusted Wold's R was used as the component selection criterion (p=0.05) {Li_2002}. The
calibration data was used to create 500 models each using a random 70% of the calibration data. The
series of 500 models was applied to the validation data to assess model performance. Finally, all the data,
calibration and validation, were used to created a series of 500 permuted models using a random 70% of the
data, the coefficients for those 500 models are included here.

## JSON file

- **model\_wavelengths** : list of wavelengths used in model
- **vector\_norm** : bool indicating whether to vector normalize
- **vector\_scaler**: *not used*
- **vector\_norm\_wavelengths**: wavelengths to use for vector normalization and for transformations
- **fwhm:**  *not used*
- **transform**: X transform type
- **description**: model description
- **trait\_name**
- **units**
- **wavelength\_units** 
- **model\_diagnostics**: validation diagnostics
  - **rmse**: root mean square error
  - **r_squared**: coefficient of determination
  - **range**: range of data used to build model
  - **bias**: model bias
- **intercept**: model intercepts
- **coefficients**: model coefficients
- **model\_interations**: number of model permutations