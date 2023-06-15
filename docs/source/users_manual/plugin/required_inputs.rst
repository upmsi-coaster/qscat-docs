.. _plugin_required_inputs:

***************
Required Inputs
***************

Prior to using the plugin, prepare the required vector layers: (a) shoreline/s - vector/s of shoreline positions for different years; and (b) baseline -  a vector that serves as a starting point for all transects cast by QSCAT (REF).

.. _plugin_required_inputs_shorelines:

Preparing the shoreline vectors
===============================

The primary data required in QSCAT is the shoreline, or roughly the boundary between land and water. In practice, the shoreline is not usually taken as the `waterline`, or the boundary between land and sea due to tides. Owing to tidal fluctuation, the shoreline can be anywhere between the low-tide line (LTL) and high-tide line (HTL). In many cases, high water features such as high-tide line (HTL), continuous scarps, or the vegetation line are used as shoreline proxies to minimize the effects of tides and at the same time, take into account the net effect of high-wave energy events such as storms on a coastline 

Shoreline data can be acquired through mapping using a handheld GPS unit, or traced on topographic maps, satellite images, and aerial photographs. The methods for extracting the shoreline on topographic map, and satellite images are discussed in detail in the accompanying **Manual on Shoreline Change Analysis**. The shoreline vectors generated in this step will be the main input dataset to QSCAT.

.. _plugin_required_inputs_baseline:

Generating the baseline vectors
===============================

Another important input data is the **baseline**, a vector constructed by the user that is parallel to and at a certain distance from the shoreline. Similar to DSAS, the baseline is the starting point for all shoreline change calculations to be made in QSCAT.  It is not part of the QSCAT plugin but can be generated using QGIS or any GIS software with the same functionality.
