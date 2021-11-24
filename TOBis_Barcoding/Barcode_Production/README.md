# OT-2 Automated Barcode Production

<sup name=" "></sup>

[Section 1:](#Link1) Introduction

[Section 2:](#Link2) Custom Functions

[Section 3:](#Link3) Editing the Script

[Section 4:](#Link4) IMPORTANT: Before Starting

[Section 5:](#Link5) Notes

[Section 6:](#Link6) Acknowledgements


## Introduction<sup name="Link1"></sup>:

The scripts in this section were created in order to produce the 35-plex or 126-plex TOBis barcodes using the OT-2 robot. Using the OT-2 robot reduces human error during production, increases individual pipetting accuracy and also accuracy between batches and saves the user a substantial amount of time.

An excel sheet has been uploaded to give the users more information in understanding why the specific concentrations and volumes are used in the master and working stocks in producing both the 35-plex and 126-plex TOBis barcodes, along with the amount of DMSO needed to make 1 mL of barcodes. This can then be aliquoted in 20 µL amounts to make approximately 45-50 full 35-plex or 126-plex barcoding kits.
- Ideally, for the ease of the user and in preventing any other errors, the concentrations and volumes should be kept exactly how they have been detailed in the excel sheet. This also means the script does not need to be edited or adjusted whatsoever.


## Custom Functions<sup name="Link2"></sup>:

The following explains certain functions used in the scripts which specifically and greatly minimises any possible flaws/mistakes during the production of the barcodes whilst also vastly increasing the accuracy of the transfers.

**`def custom_transfer`:**
- This function utilises a collection of commands including:
    - **`air_gap`**: The pipette aspirates a set amount of air to ensure no solution can accidentally drop out of the pipette tip when the robot arm is moving positions.
    - **`blow_out`**: After the pipette has completely dispensed the solution into the destination tube, the pipette dispenses an extra amount of air to ensure all of the solution is dispensed out of the pipette tip.
    - **`touch_tip`**: Post-`blow_out`, this `touch_tip` command has been specifically optimised to ensure that any remaining droplet on the pipette tip itself falls only into the destination well, whilst simultaneously not touching the sides of the destination well. This ensures that any remaining droplet on the pipette tip will not fall into any other destination well whilst the robot arm is in transit. It also ensures the pipette tip is not contaminated with any other elements within the barcoding structure so that the same tip can be used for that specific element. 


**`def custom_batch`:**
- This is the main function, which includes the function above, to produce the barcodes.
- It essentially loops over a list of destination wells from the `destinations_list` and pipettes a set `volume` of a specific `source` isotope into all of the wells listed in the `destinations_list`.
- It also includes a mathematical equation, `mm_lost_per_ul_eppendorf`, to allow the robot arm to decrease in height into the tube every time the specific volume is aspirated. This ensures that after each transfer, as the amount of volume in the `source` tube decreases, the robot arm decreases in height proportional to the decrease in volume of the eppendorf, ensuring the pipette tip is always in contact with and aspirating the solution.

[Return to contents](# )



## Editing the Script<sup name="Link3"></sup>:

- As mentioned in the introduction, if the user replicates the concentrations and volumes used exactly in the excel sheet, uses the same labware and places them in the same position as stated in the script, there is no need to edit the script. This is highly recommended.

- However, if different labware, concentrations and volumes of any solution were used, then the script must be edited. Within the script itself, under the `def run(protocol: protocol_api.ProtocolContext):` function, enter the location of the labware on the OT-2 deck and the type used of the:
    - tiprack
    - tuberack<sup>[a](#subfootnote)</sup>
    - deep well plate(s)<sup>[a](#subfootnote)</sup>

    In addition to the above:
    - Under the '#This is the SOURCE' heading, enter the positions of each individual isotopes located on the tuberack. Ensure the `source` eppendorfs are the same used for all the isotopes, i.e. do not use a 15mL falcon for one isotope and a 1.5 mL eppendorf for another.
    - Under the '#This is the SOURCE_HEADROOM' heading, enter the distance, in millimetres, between the top of the source tube (excluding the cap/lid) and the meniscus of the solution. This is measured using a digital caliper. 1 or 2 millimetres can be added onto this value to ensure the pipette tip enters into the solution.
    - Lastly, under  '# mm_lost_per_ul' heading, measure, in millimetres, the inner diameter of your source tube and enter the value here.

<sup name="subfootnote">a</sup> Note that if you are using a custom tuberack or plate that is not already loaded on the [OT-2 Labware](https://docs.opentrons.com/v2/new_labware.html), then you must load it on using their [custom labware setup](https://labware.opentrons.com/create/) guide.



<!-- 
## IMPORTANT: Before Starting<sup name="Link4"></sup>

the same consumables **(WRITE DOWN A LIST OF CONSUMABLES ON A WORD DOCUMENT!!)**

[Return to contents](# )
 -->



## Notes<sup name="Link5"></sup>:

- Seal the deep-well plate tightly using an aluminium or transparent sealing film after the protocol is completed.





## Acknowledgements<sup name="Link6"></sup>:

I would like to acknowledge the aid of and thank:
- Dr Alaric Taylor, in helping me write the script and teaching me how to use the OT-2 machine.
- Ferran Cardoso ([@FerranC96](https://github.com/FerranC96)) for helping me set up the 'OT-2 Automated Barcode Pipetting' GitHub repository. 
- And lastly, the [TAPE Lab](http://tape-lab.com/lab) group for their continuous support in helping create the TOBis barcoding strategy.

The work here is actively being developed by Jahangir Sufi.

[Return to contents](# )
