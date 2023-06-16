.. _tab_shorelines:

***************
Tab: Shorelines
***************

.. only:: html

   .. contents::
      :local:
      :depth: 2

The :menuselection:`Shorelines Tab` allows the user to select and load the shorelines to be used for the analysis.

Shorelines Parameters
=====================

#. **The input layer:** Should be the merged shorelines, created in Section  3.1.2a; and

#. **Default data uncertainty:** If the uncertainty value for each shoreline data in the attribute table is set to 0 or None, the plugin will automatically assign this defined value (defaults to 15 meters). This value represents the uncertainty inherent in the resolution of Landsat images, which are the readily available sources of shoreline data in the country. This default value may underestimate or overestimate the uncertainty inherent in different types of digital images. Thus, it is recommended for the user to provide the uncertainty value in the attribute table of the selected shoreline layer.

For the input layer merged shorelines, the uncertainty value should be based on the map or digital image with the lowest resolution. Hence, QSCAT automatically selects the highest or maximum uncertainty value in the attribute table of the merged shorelines.

Shorelines Fields
=================

Under the :menuselection:`Shoreline Fields`, select the ``date`` and ``ucertainty`` fields of the currently selected shoreline layer to be used. These are the fields that are automatically (:ref:`shorelines fields automator <_tab_automator_shoreline_fields>`) or manually created.