.. _tab_visualization:

******************
Tab: Visualization
******************

.. only:: html

   .. contents::
      :local:
      :depth: 2

Visualization Parameters
========================

Input stat layer
----------------

Accept layers:

* SCE
* NSM 
* EPR
* LRR
* WLR

Color Ramp
==========

Color ramp visualization uses PyQGIS to generate classification values based on mode and input stat layer.

Accept inputs:

#. # of Negative Classes (erosion values)
#. # of Positive Classes (accretion values)
#. Mode of classification

Generate outputs:

* SCE - stable, positive
* NSM, EPR - negative, stable, positive
* LRR, WLR - negative, positive


Modes
-----

Quantile
........

Equal Interval
...............

Natural Breaks (Jenks)
......................

Prettry Breaks
................