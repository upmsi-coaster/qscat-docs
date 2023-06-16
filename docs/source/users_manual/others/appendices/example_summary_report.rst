.. index:: Example Summary Report
.. _appendices_example_summary_report:

Appendix X: Example Summmary Report

The following is an example of summary report for shoreline change statistic::
    
    [Author]
    Name: Last name, First name Middle Name
    Affiliation: xx
    Email: xx

    [System]
    Time generated: dd/mm/yyyy hh:mm:ss
    QGIS version: 3.22.6
    QSCAT version: v1.0.0beta

    [Input]
    [Shorelines]
    Layer: xxx
    Default uncertainty: xx
    Date field: xxx
    Dates: 01/2018, 01/2022, 01/2022
    Uncertainty field: xxx
    Uncertainty: 25.0, 25.0, 15.0

    [Baseline]
    Layer: xxx
    Placement: (sea or offshore|land or onshore)
    Orientation: (land is to the R|land is to the L)

    [Transects]
    Name: xxx
    Total number of transects
    Number of transects with negative distance
    By (transect spacing|number of transects): xx meters
    Search distance: xx meters
    Smoothing distance: xx meters
    Intersection by (distance/placement): (farthest|closest|seaward|landward)
    Clip transects: yes
    Include intersections layer: yes

    [Statistics]
    Layer: xx
    Statistics: SCE, NSM, EPR
    Newest date: mm/yyyy
    Oldest date: mm/yyy

    Area layer: xxx
    Area NSM layer: xxx

    [Visualization-not included?]

    [Results]
    Total number of transects: xxx
    ………………..
    SCE: