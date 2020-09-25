# OT-2 Automated Barcode Pipetting

<>[Outline](#Link1)</>
Custom Functions <sup>[2](#Link2)</sup>
In the Script <sup>[3](#Link3)</sup>
IMPORTANT: Before Starting <sup>[4](#Link4)</sup>
Notes <sup>[5](#Link5)</sup>
Acknowledgements <sup>[6](#Link6)</sup>



## < name="Link1">1.</> Outline

Before beginning, it is recommended to read the 2020 Nature Methods, Qin et al. paper here: [Cell-type-specific signaling networks in heterocellular organoids](https://www.nature.com/articles/s41592-020-0737-8). This will give an overview of why TOBis is used instead of the traditional Fluidigm barcoding, it's advantages and also an application of its use on intestinal organoids.

Secondly, to understand the latest version of TOBis, to know the concentrations used and a very specific, step-by-step guide in carrying out the entire TOBis CyTOF protocol, please read the 2020 Nature Protocols, Qin et al. paper here: [Multiplexed Single-Cell Analysis of Organoid Signaling Networks](#Enter LINK here).

Lastly, a guide of using the OT-2 software and writing protocols can all be found on their [website](https://docs.opentrons.com/v2/). It includes the explanation of and how to use:
- Versioning
- Labware
- Hardware Modules
- Pipettes
- Building Block Commands
- Complex Commands
- API Version 2 Reference
- Advanced Control
With some example protocols as well. Custom protocols can also be made using their 'Protocol Designer', however it's not recommended to do use for complex protocols.
[↩](#Link1)



## 2. Custom Functions:<sup name="Link2">a</sup>

The following is an explanation/description of some functions used in the scripts:

**`def custom_wetting`:**
- The first transfer of any solution, the pipette tip is completely unused. With some solutions, this means the first transfer will not pipette the same volume of solution as the subsequent transfers using the same pipette tip. This is because the subsequent transfers are using a tip which has already been 'wet' by the solution, whereas the first transfer is not 'wet'.
- Therefore, this function aspirates a certain volume of solution and then dispenses that solution into the same tube. This allows the pipette tip to be 'wet' before the first transfer is made. Thus it reduces any variability in pipetting between the first and subsequent transfers using this step.
- This step is only performed at the beginning of every isotope which will be pipetted. So 7 and 9 times in total for the 35-plex and 126-plex, respectively.


**`def custom_transfer`:**
- This function is a collection of commands that is more than the basic `transfer` command used in the OT-2 software.
- It includes the following commands, as well as the simple `aspirate` and `dispense`:
    - **`touch_tip`**: After each aspiration of the pipette. The robot arm touches the pipette tip onto 4 opposite sides of the inner part of the tube. This allows any remaining solution on the outside of the pipette tip to fall off into the tube it was aspirated from. 
    - **`air_gap`**: After the `touch_tip` command, the pipette aspirates a set amount of air. This is to ensure that no solution can accidentally drop out of the pipette tip when the robot arm is moving positions.
    - **`blow_out`**: After the pipette has completely dispensed the solution into the destination tube, the pipette then dispenses an extra amount of air. This is to ensure that all of the volume is dispensed out of the pipette tip.
- All the additional commands above, in unision, vastly increases the accuracy of the transfer, as they do not allow any extra solution to cling onto the exterior of the pipette tip and be added to the destination tube (using `touch_tip`), it ensures all of the solution is transferred from the `source` to the `destination` (using`air_gap`) and lastly ensures that all of the solution is added to the `destination` (using`blow_out`). 


**`def custom_batch`:**
- This is the main function which includes the two functions above.
- It allows a list of destinations, `destinations_list`, to be added as a parameter of the function. So that the specific barcode number, i.e. TOBis001/TOBis002...TOBis053, etc, can be added to that list. The robot will pipette the specific isotope allocated under `source` and pipette the specific `volume` into all of the barcodes listed in `destinations_list`.
- It also includes a mathematical equation to allow the robot arm to decrease into the tube every time a specific volume is aspirated. This ensures that after each transfer, as the amount of volume in the `source` tube decreases, the robot arm decreases in height proportional to the decrease in volume. Ensuring the pipette tip is always in contact with and aspirating the solution.
[↩](#Link2)



## 3. In the Script:<sup name="Link3">a</sup>

Within the script itself, under the `def run(protocol: protocol_api.ProtocolContext):` function, enter the:
- location of tiprack on OT-2 deck
- the tuberack used and its location on OT-2 deck<sup>[a](#subfootnote)</sup>
- the plate used and its location on OT-2 deck

 <sup name="subfootnote">a</sup> note that if you are using a custom tuberack or plate that is note already loaded on the OT-2 Labware (enter link for OT-2 labware), then you must load it on using their custom labware setup guide.

Under the '# Source' heading, enter the positions of each individual isotope.

Under the '# Source_Headroom' heading, enter the distance, in millimetres, between the top of the source tube (excluding the cap/lid) and the meniscus of the solution.

Lastly, under  '# mm_lost_per_ul' heading, measure, in millimetres, the inner diameter of your source tube and enter value here.
[↩](#Link3)




## 4. IMPORTANT: Before Starting<sup name="Link4">a</sup>

- Ensure the `source` tubes/falcons/eppendorfs are the same used for all the isotopes, i.e. do not use a 15mL falcon for one isotope and a 1.5 mL eppendorf for another.
- Measure the inner diameter of the `source` tube, in millimetres, using a precise caliper and enter into the `diameter` variable under the '# mm_lost_per_ul' heading.
- Under `source_headroom`, you will need to measure and insert the distance, in millimetres, from the top of the `source` tube (excluding the cap/lid) to the top of the meniscus of the solution using a precise caliper. 1 or 2 millimetres can be added onto this value to ensure the pipette tip enters into the solution.
- The scripts only pipette the isotopes themselves and not the DMSO base solution. You will need to pipette this yourself into the `destination` plate before using this script.
[↩](#Link4)




## 5. Notes:<sup name="Link5">a</sup>

- For any tubes/eppendorfs/falcons used, it is recommended to use ones with a detachable lid/cap. This is so that the robot arm does not come into contact with any open lids whilst it moves positions.
- It is recommended that a polypropylene 96 Deep Well Plate, which can hold at least 1 mL of volume, is used as a `destination` plate. It is also preferable to seal the plate tightly using an Aluminium Sealing film or a transparent after the protocol is completed.
[↩](#Link5)




## 6. Acknowledgements:<sup name="Link6">a</sup>

I would like to acknowledge the aid of and thank:
- Dr Alaric Taylor, in helping me write the script and teaching me how to use the OT-2 machine.
- Ferran Cardoso ([@FerranC96](https://github.com/FerranC96)) for helping me set up the 'OT-2 Automated Barcode Pipetting' GitHub repository. 
- And lastly, the [TAPE Lab](http://tape-lab.com/lab) group for their continuous support in helping create the TOBis barcoding strategy.

The work here is actively being developed by Jahangir Sufi.
[↩](#Link6)