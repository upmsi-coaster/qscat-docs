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

Shoreline Change Envelope (SCE)
-------------------------------

The shoreline change envelope (SCE) is the maximum distance, in meters (m), among all the shorelines that intersect a given transect (Himmelstoss et al., 2018). If there are multiple shoreline vectors, one can easily identify the greatest magnitude of shoreline movement (SCE column) and when it occurred (SCE_closest year and SCE_farthest year columns) in the resulting attribute table of shoreline change statistics (Table X). Since SCE is a distance, all values are positive. The shoreline trends can be inferred from the SCE_trend column, whether SCE represents erosion, accretion or stability. 

Net Shoreline Movement (NSM)
----------------------------

The net shoreline movement (NSM) represents the magnitude of shoreline change between the oldest and youngest shorelines in meters (m), and is calculated as:

NSM = distance between youngest and oldest shorelines.

The uncertainty is based on the shoreline with largest uncertainty values in the attribute table of the input layer. 

End-Point Rate (EPR)
--------------------

Linear Regression Rate (LRR)
----------------------------
For multiple shoreline positions, a more appropriate rate-of-change statistic to use is the Linear Regression Rate-of-change (LRR) since it takes into consideration all shoreline positions in the calculation, not just the endpoints like what NSM and EPR do. In fact, LRR requires at least three (3) shoreline vectors, or intersection points to calculate the rate of change, in m/y, for a given transect. LRR is determined from the slope of a least-squares regression line fitted to all shoreline intersection points for each transect (Himmelstoss et al., 2018). 

Weighted Linear Regression (WLR)

--------------------------------
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



