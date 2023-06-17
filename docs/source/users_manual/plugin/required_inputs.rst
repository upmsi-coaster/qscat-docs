.. _plugin_required_inputs:

***************
Required Inputs
***************

To use this plugin, you only need these two vector layers:

#. **Shorelines layer:** vectors of shoreline positions for different years; and 
#. **Baseline layer:** vector that serves as a starting point for all transects cast by ``QSCAT`` :cite:p:`2018:dsasv5`.

.. _plugin_required_inputs_shorelines:

Shorelines Layer
================

The first primary data required in ``QSCAT`` is the :menuselection:`Shoreline`, or roughly the boundary between land and water. In practice, the shoreline is not usually taken as the `waterline`, or the boundary between land and sea due to tides. Owing to tidal fluctuation, the shoreline can be anywhere between the low-tide line (LTL) and high-tide line (HTL). In many cases, high water features such as high-tide line (HTL), continuous scarps, or the vegetation line are used as shoreline proxies to minimize the effects of tides and at the same time, take into account the net effect of high-wave energy events such as storms on a coastline.

Preparing the shoreline vectors
-------------------------------

Shoreline data can be acquired through mapping using a handheld GPS unit, or traced on topographic maps, satellite images, and aerial photographs. The methods for extracting the shoreline on topographic map, and satellite images are discussed in detail in the accompanying **Manual on Shoreline Change Analysis**. The shoreline vectors generated in this step will be the main input dataset to ``QSCAT``.

Merging shoreline layers
------------------------

If shoreline vectors are traced or gathered for each year and stored in separate layers, it is required to merge those shoreline layers into a single layer.

The following are steps to merge multiple shoreline layers into a single layer using ``QGIS``:

#. xx
#. xx

Adding attribute fields and values
----------------------------------

After merging, each feature in the shoreline layer should contain the necessary information for each shoreline, including the shoreline date and uncertainty. The table below illustrates the required attribute table for the shoreline layer and the format of the attribute values:

=========================== ============ =========== ===========
Field                       Name         Data Type   Format
=========================== ============ =========== ===========
``QSCAT`` date field        ``any_name`` ``String``  ``mm/yyyy``
``QSCAT`` uncertainty field ``any_name`` ``Decimal`` ``x.xx``
=========================== ============ =========== ===========

.. note:: **Attribute fields and values**
    
    * You need to add the two fields with proper data type above.
    * The date value should be in the format ``mm/yyyy``. Ensure that the date is valid to avoid errors. Use ``mm`` for ``January`` such as ``01``.
    * The uncertainty field should be of decimal data type and follow the format ``x.xx``. However, if the uncertainty value is an integer, a decimal value is not required.
    * Editing the uncertainty value in the attribute table is optional but recommended. If it is not defined (``0`` or ``None``), the plugin will default to the uncertainty value defined in the :ref:`shorelines_parameters`.

.. tip:: **Automating attribute table**

   You can manually add the attribute table, but you can also automate the addition of the required attribute fields name and data types using the ``QSCAT`` :ref:`tab_automator_shoreline_fields` automator.

.. _plugin_required_inputs_baseline:

Baseline Layer
==============

Another important input data is the :menuselection:`Baseline`, a vector constructed by the user that is parallel to and at a certain distance from the shoreline. Similar to ``DSAS``, the :menuselection:`Baseline` is the starting point for all shoreline change calculations to be made in ``QSCAT``.  It is not part of the ``QSCAT`` plugin but can be generated using ``QGIS`` or any GIS software with the same functionality.

Unlike ``DSAS``, ``QSCAT`` does not currently supports multiple base segments on a single transect casting. It is recommended to run separate transect casting for each baseline segment to increase versatility, allowing for different input parameters for each baseline segment. Thus, ``QSCAT`` does not have any required attribute table for the baseline layer.

Generating the baseline vectors
-------------------------------

A common technique when generating the baseline is buffer the shape  of all