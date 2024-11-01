================
Circular Economy
================

**Circular Economy (CircularEconomy)** includes three subsectors (* indicates non-emission subsector): 

* Liquid Waste* (WALI)
* Solid Waste (WASO)
* Wastewater Treatment (TRWW)

Circular Economy is used to account for the production of, and emissions from, liquid and solid waste from industrial and domestic sources. Circular Economy includes three subsectors: liquid waste (used only to account for the production of liquid waste), solid waste, and wastewater treatment. These three sectors are derived from Volume 5 of the IPCC guidance for national greenhouse gas inventories and include detailed estimates of of emissions from wastewater treatment and management pathways, solid waste treatment pathways, including a first order decay model of landfilled waste, and recycling, which then is passed to the industrial production model to estimate changes to production of virgin materials. Waste generation is primarily driven by per person generation factors, which are responsive to changes in GDP, GDP/capita, and population and other sectors, including livestock manure management and supply chain loss in agriculture. 


Liquid Waste (WALI)
===================

Liquid waste includes...


Categories
----------

Categories associated with Liquid Waste are identified by the ``$CAT-WASTE-LIQUID$`` variable schema element and shown in the category attribute table shown below. 

.. csv-table:: Liquid Waste categories (``$CAT-WASTE-LIQUID$`` attribute table)
   :file: ../../sisepuede/attributes/attribute_cat_liquid_waste.csv
   :header-rows: 1


Variables
---------

Variables associated with the Liquid Waste subsector are shown below. 

.. csv-table:: Trajectories of the following variables are needed for the Liquid Waste subsector. The categories that variables apply to are described in the ``category`` column.
   :file: ../../sisepuede/attributes/variable_definitions_ce_wali.csv
   :header-rows: 1


----


Wastewater Treatment (TRWW)
===========================

Wastewater can be treated using a variety of pathways. Note that aerobic and septic pathways produce sludge, which can disposed of in a variety of ways; the SISEPUEDE model does not currently integrate sludge removal and disposal from aerobic and septic treatment pathways.

.. note:: IPCC accounting (IPCC GNGHGI V5, C6 2019R) calls for emissions from secondary sludge extracted from aerobic WWTPs to be divided between decentralized treatment (uncollected) and centralized treatment, where centralized aerobic treatment includes sludge treatment on-site, accounting for emissions of sludge due to treatment--e.g., from anaerobic decomposition--in the Wastewater Treatment sector. Instead, SISEPUEDE accounts for all emissions from sludge treatment in the Solid Waste sector.


Categories
----------

Categories associated with Wastewater Treatment are identified by the ``$CAT-WASTEWATER-TREATMENT$`` variable schema element and shown in the category attribute table shown below. 

.. csv-table:: Wastewater Treatment categories (``$CAT-WASTEWATER-TREATMENT$`` attribute table)
   :file: ../../sisepuede/attributes/attribute_cat_wastewater_treatment.csv
   :header-rows: 1


Variables
---------

Variables associated with the Wastewater Treatment subsector are shown below. 

.. csv-table:: Trajectories of the following variables are needed for the Wastewater Treatment subsector. The categories that variables apply to are described in the ``category`` column.
   :file: ../../sisepuede/attributes/variable_definitions_ce_trww.csv
   :header-rows: 1


----


Solid Waste (WASO)
==================

Solid waste is generated by consumption. Growth in domestic consumption in is driven by GDP per capita, while growth in industrial consumption is driven by production (represented by value added). Solid waste can reach one of four final states: incineration (or open-burning), landfilled, recycling (or composting/anaerobic biogas production for food and yard waste).

.. note:: Process emissions for recycling of recyclable materials that affect virgin production--glass, metals, paper, plastic, rubber and leather, textiles, wood--are treated in `Industrial Processes and Product Use <./ippu.htm>`_.


Categories
----------

Categories associated with Solid Waste are identified by the ``$CAT-WASTE-SOLID$`` variable schema element and shown in the category attribute table shown below. 

.. note:: The solid waste attribute table requires the specification of parameters used to characterize different types of waste. These parameters--with the exception of industrial and chemical waste--are derived from default values provided by the IPCC in Volume 5, Chapter 2, Table 2.4 of the `2019 Refinement to the 2006 IPCC Guidelines for National Greenhouse Gas Inventories <https://www.ipcc-nggip.iges.or.jp/public/2019rf/index.html>`_ and the `2006 IPCC Guidelines for National Greenhouse Gas Inventories <https://www.ipcc-nggip.iges.or.jp/public/2006gl/index.html>`_ (which contains the table) for the source of parameters. Industrial parameters come from Volume 5, Chapter 2, Table 2.5.

.. csv-table:: Solid waste categories (``$CAT-WASTE-SOLID$`` attribute table)
   :file: ../../sisepuede/attributes/attribute_cat_solid_waste.csv
   :header-rows: 1


Variables
---------

Variables associated with the Solid Waste subsector are shown below. 

.. csv-table:: Trajectories of the following variables are needed for the Solid Waste subsector. The categories that variables apply to are described in the ``category`` column.
   :file: ../../sisepuede/attributes/variable_definitions_ce_waso.csv
   :header-rows: 1

