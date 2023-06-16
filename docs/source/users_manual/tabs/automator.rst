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

Shoreline Fields
----------------

The :menuselection:`Shorelines Fields` automator simplifies the process of adding attributes by automatically assigning pre-defined data types and custom field names. By simply defining the desired field name, the plugin takes care of the necessary data type assignments for each field. This requires the following input:

#. **Input layer:** A vector layer containing the merged shorelines.

#. **Date field name:** The field name that represents the date of the source of shoreline data, following the format mm/yyyy.

#. **Uncertainty field name:** The field name that captures the uncertainty associated with the measurement and/or positional accuracy inherent in the source of shoreline data.

Without the automator, the ``date`` and ``uncertainty`` fields can be manually added on the :menuselection:`Attribute Table` of the shoreline input layer. Basically, this means that the user is responsible for selecting the attribute data type.

========================= ============ ========= =======
Field                     Name         Data Type Format
========================= ============ ========= =======
QSCAT's date field        ``any_name`` String    mm/yyyy
QSCAT's uncertainty field ``any_name`` Decimal   x.xx
========================= ============ ========= =======

Baseline
=========

Baseline Geometry
-----------------
