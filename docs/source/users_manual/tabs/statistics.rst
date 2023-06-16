.. _tab_statistics:

***************
Tab: Statistics
***************

.. only:: html

   .. contents::
      :local:
      :depth: 2

After casting the transects, QSCAT is now ready to calculate the following shoreline change statistics: (a) shoreline change envelope (SCE), (b) net shoreline movement (NSM), (c) end point rate (EPR), and (d) linear regression rate (LRR). The first three statistics (SCE, NSM and EPR) require only two shoreline vectors while LRR requires at least three (3) shoreline vectors to compute the rate of change. Note that both SCE and NSM refer to magnitude or distance in meters (m) while EPR and LRR are rate-of-change statistics, in meters/year (m/y).

Statistics Parameters
=====================

Select transects layer
----------------------

Select the transect layer created in Section 3.7 that will be used to calculate the selected statistics in the Statistics tab. The output statistics will be tabulated in the Attribute Table of this run, which can then be exported as a worksheet file and/or viewed in map format.

Summary Report location
-----------------------

Full content are discussed in (ref) and example file in (ref)

Shoreline Change Statistics
===========================

The four shoreline change statistics available in QSCAT and the resulting sample attribute table (Table X) are described below. 

.. list-table:: Statistics
   :header-rows: 1
   :widths: 20 80

   * - Statistics
     - Description
   * - ``SCE``
     - Shoreline Change Envelope
   * - ``NSM``
     - Net Shoreline Movement
   * - ``EPR``
     - End-Point Rate
   * - ``EPR_unc``
     - Uncertainty of End-Point Rate
   * - ``LRR``
     - Linear Regression Rate / Slope
   * - ``LR2``
     - R-Squared of Linear Regression
   * - ``LSE``
     - Standard Error of Estimate of Linear Regression
   * - ``LCI``
     - Confidence Interval of Linear Regression
   * - ``WLR``
     - Weighted Linear Regression Rate / Slope
   * - ``WR2``
     - R-Squared of Weighted Linear Regression 
   * - ``WSE``
     - Standard Error of Estimate of Weighted Linear Regression
   * - ``WCI``
     - Confidence Interval of Weighted Linear Regression

Shoreline Change Envelope (SCE)
-------------------------------

The shoreline change envelope (SCE) is the maximum distance, in meters (m), among all the shorelines that intersect a given transect (Himmelstoss et al., 2018). If there are multiple shoreline vectors, one can easily identify the greatest magnitude of shoreline movement (``SCE_value`` column) and when it occurred (``SCE_closest`` year and ``SCE_farthest`` year columns) in the resulting attribute table of shoreline change statistics (Table X). Since SCE is a distance, all values are positive. The shoreline trends can be inferred from the ``SCE_trend`` column, whether SCE represents erosion, accretion or stability. 

.. math::
   
   SCE = farthest\_year\_distance - closest\_year\_distance

Net Shoreline Movement (NSM)
----------------------------

The net shoreline movement (NSM) represents the magnitude of shoreline change between the oldest and youngest shorelines in meters (m), and is calculated as:

.. math::

   NSM = oldest\_year\_distance - newest\_year\_distance

The uncertainty is based on the shoreline with largest uncertainty values in the attribute table of the input layer. 

End-Point Rate (EPR)
--------------------

The end-point rate (``EPR``) is the rate of change based on ``NSM``, in meters/year (m/y), and is calculated as:

.. math::
   EPR = \frac{NSM}{newest\_shoreline\_year - oldest\_shoreline\_year}

The uncertainty of EPR (``EPR_unc``) is based on the following formula, after DSAS (Himmelstoss et al., 2018):

.. math::
   EPR\_unc = \frac{{\sqrt{{(uncyA)^2 + (uncyB)^2}}}}{yearA - yearB}

where:

- uncyA - uncertainty of the youngest shoreline A
- uncyB - uncertainty of the oldest shoreline B
- yearA - year of youngest shoreline A
- yearB - year of oldest shoreline B

Both ``NSM`` and ``EPR`` require only two shoreline vectors, i.e., the youngest and oldest shoreline vectors. QSCAT will ignore any shoreline vector/s between the youngest and oldest years. As such, it provides no information about shoreline movement during the intervening years even if there are multiple shoreline positions in the input layer. Additional information may be inferred from the ``SCE``, which can at least identify the greatest magnitude of change and the corresponding time period for a given set of shoreline vectors.      

Linear Regression Rate (LRR)
----------------------------
For multiple shoreline positions, a more appropriate rate-of-change statistic to use is the Linear Regression Rate-of-change (LRR) since it takes into consideration all shoreline positions in the calculation, not just the endpoints like what NSM and EPR do. In fact, LRR requires at least three (3) shoreline vectors, or intersection points to calculate the rate of change, in m/y, for a given transect. LRR is determined from the slope of a least-squares regression line fitted to all shoreline intersection points for each transect (Himmelstoss et al., 2018). 

.. math::
   LRR = \frac{\sum_{i=1}^{n} (x_i - \bar{x})*(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})*(x_i - \bar{x})}

where:

- :math:`n` - length of years and distances
- :math:`\bar{x}` - mean of years
- :math:`\bar{y}` - mean of distances
- :math:`x_i` - ith year
- :math:`y_i` - ith distance

.. _supplementary_statistics:

Supplementary Statistics for Linear Regression
...............................................

**R-Squared of Linear Regression (LR2)**

xx

.. math::
   LR2 = 1 - \sqrt{\frac{\sum_{i=1}^{n} (y_i-\hat{y}_i)^2}{\sum_{i=1}^{n} (y_i-\bar{y})^2}}

where:

- :math:`n` - length of years and distances
- :math:`\hat{y}` - predicted ith distance (:math:`LRR*x_i + intercept`)
- :math:`\bar{y}` - mean of distances
- :math:`y_i` - actual ith distance

**Standard Error of Estimate of Linear Regression (LSE)**

xx

.. math::
   LSE = \sqrt{\frac{\sum_{i=1}^{n} (y_i-\hat{y}_i)^2}{n-2}}

where:

- :math:`n` - length of years and distances
- :math:`\hat{y}` - predicted ith distance (:math:`LRR*x_i + intercept`)
- :math:`y_i` - actual ith distance

**Confidence Interval of Linear Regression (LCI)**

xx

.. math::
   LCI = t\_inv(n-2,\ 1-\alpha/2) *  \sqrt{\frac{LSE^2}{\sum_{i=1}^{n}(x_i-\bar{x})^2}}

where:

- :math:`\alpha` - :math:`1 - (confidence\_interval*.01)` (confidence interval in percent)
- :math:`t\_inv()` - student's t-distribution function
- :math:`LSE` - standard error of estimate of linear regression
- :math:`n` - length of years and distances
- :math:`\bar{x}` - mean of years
- :math:`x_i` - ith year


Weighted Linear Regression (WLR)
--------------------------------

In WLR, uncertainty values are converted to weights:

.. math::
   weight = \frac{1}{e^2}

where:

- :math:`e` - uncertainty value of a shoreline

Then, a weighted linear regression is performed using the weights. The resulting slope is the WLR:

.. math::
   WLR = \frac{\sum_{i=1}^{n} (x_i - \bar{x}_w)*(y_i - \bar{y}_w)*weight_i}{\sum_{i=1}^{n} (x_i - \bar{x}_w)^2 * weight_i}

where:

- :math:`n` - length of years and distances
- :math:`\bar{x}_w` - weighted mean of years
- :math:`\bar{y}_w` - weighted mean of distances
- :math:`x_i` - ith year
- :math:`y_i` - ith distance
- :math:`weight_i` - ith weight


Supplementary Statistics for Weighted Linear Regression
.......................................................

In WLR, the supplementary statistics are calculated using the :ref:`formulas from normal linear regression <supplementary_statistics>`, but instead of LRR (slope), WLR is used. The following tables show the values of the supplementary statistics for both linear and weighted linear regressions.

============================ ===========================================================
WLR Supplementary Statistics Description
============================ ===========================================================
WR2                          predicted ith distance must use :math:`WLR*x_i + intercept`
WSE                          predicted ith distance must use :math:`WLR*x_i + intercept`
WCI                          standard error of estimate must use :math:`WSE`
============================ ===========================================================

Pairwise Comparison of Shorelines
=================================

By default, NSM and EPR calculate the magnitude and rate of shoreline changes respectively between the oldest and most recent shorelines even if multiple shorelines are available. In QSCAT, the algorithm for calculating NSM and EPR can be applied to any two shorelines from the selected shorelines layer by specifying the dates of the two shorelines for comparison.While LRR can estimate the net rate of change among multiple shorelines, the pairwise comparison can lead to a better understanding of how the shoreline has evolved over different time periods, and the possible causes of the observed trends.
 
The output file is a temporary file with the following format: name of area_NSM (inclusive date)[date and time of QSCAT run]. 


Area Change Statistics
======================

An additional functionality of QSCAT is the estimation of area change between two shoreline vectors for a given polygon layer. The polygon layer can be randomly drawn, or based on geographic boundaries (e.g., shapefiles of barangay, municipal boundaries) for which this type of analysis may be more meaningful. Monitoring how much coastal land a barangay or municipality has gained or lost is important for coastal planning and management. Make sure the boundary drawn encompasses all shorelines.

The input layers are:

#. Polygon layer - a shapefile that encompasses the area of interest; may be drawn randomly or based on geographic or administrative boundaries
#. NSM layer - a memory-based layer where the NSM results are temporarily saved. Area change is calculated based on the NSM results.

Results of area change calculation are stored as a memory-based layer, “filename_area [date time of run]”. It can also be accessed in the attribute table of area change results (Table X - sample table). Aside from the area change per shoreline trend, the attribute table also provides estimates of the length of shoreline that is undergoing erosion, accretion or remains stable, respectively, for a given polygon. 



