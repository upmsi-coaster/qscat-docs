.. _tab_automator:

**************
Tab: Automator
**************

.. only:: html

   .. contents::
      :local:
      :depth: 2

The automator tab allows the user to automate repetitive tasks directly from the plugin.

Shorelines
==========

.. _tab_automator_shoreline_fields:

Shoreline Fields
----------------

The :guilabel:`Shorelines Fields` automator simplifies the process of adding attributes by automatically assigning pre-defined data types and custom field names. By simply defining the desired field name, the plugin takes care of the necessary data type assignments for each field. This requires the following input:

#. **Input layer:** vector layer containing the merged shorelines.
#. **Date field name:** field name that represents the date of the source of shoreline data, following the format ``mm/yyyy``.
#. **Uncertainty field name:** field name that captures the uncertainty associated with the measurement and/or positional accuracy inherent in the source of shoreline data.

The automator adds the following fields to the input layer:

============================ ==========
Field name                   Data type
============================ ==========
``<date_field_name>``        ``String``
``<uncertainty_field_name>`` ``Double``
============================ ==========

Without the automator, the ``date`` and ``uncertainty`` fields can be manually added on the :menuselection:`Attribute Table` of the shoreline input layer. Basically, this means that the user is responsible for selecting the attribute data type. To check full details about shorelines layer, please refer to the :ref:`preparing_the_shoreline_vectors`.

Baseline
========

.. _tab_automator_baseline_buffer:

Baseline Buffer
---------------

The :guilabel:`Baseline Buffer` automator simplifies the process of creating a buffer around the baseline. This requires the following input:

#. **Input layer:** vector layer containing the merged shorelines.
#. **Buffer distance:** distance in meters to create the buffer around the baseline.

The automator uses processing algorithm :guilabel:`Buffer` with pre-defined inputs to create the buffer around the merged shorelines layer. The output is then converted to ``LineString``. To read more about input baseline layer, please refer to :ref:`generating_the_baseline_vectors`. 

The following are the pre-defined inputs for the :guilabel:`Buffer` algorithm:

======================================= ====================
Parameter                               Value
======================================= ====================
:guilabel:`Distance`                    ``<input_distance>``
:guilabel:`Segments`                    5
:guilabel:`End cap style`               Flat
:guilabel:`Join style`                  Round
|checkbox| :guilabel:`Dissolve results` Checked
======================================= ====================

.. |checkbox| image:: /img/checkbox.png
   :width: 1.0em