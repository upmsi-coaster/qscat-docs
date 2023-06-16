.. _tab_baseline:

*************
Tab: Baseline
*************

.. only:: html

   .. contents::
      :local:
      :depth: 2
      
Baseline Parameters
===================

The input layer is the **baseline** created in :ref:`generating baseline vectors <plugin_required_inputs_baseline>`:.

Baseline Placement
==================

After selecting the baseline layer, the next step is to choose the baseline placement. This selection determines whether the baseline is positioned seaward or offshore, or landward or onshore. The baseline placement defines the direction of the transects when casting. If the selected baseline placement is seaward or offshore (landward or onshore), the transects will be cast from the sea to the land (or land to the sea) as shown in :numref:`figure_baseline_placement`.

.. _figure_baseline_placement:

.. figure:: img/baseline_placement.png
   :align: center
   
   Baseline placement.

Baseline Orientation
====================

In addition to baseline placement, another important parameter is baseline orientation, which determines the relative position of the land with respect to the drawn or digitized baseline. It specifies whether the land is on the right or left side of the baseline orientation. To assist in selecting the appropriate orientation, :numref:`_figure_baseline_orientation` illustrates different scenarios based on the direction of the baseline vector. In QSCAT, users can enable the "show baseline orientation" option, which adds arrows indicating the direction of the baseline vector.

.. _figure_baseline_orientation:

.. figure:: img/baseline_orientation.png
   :align: center
   
   Guide for determining the appropriate baseline orientation.
