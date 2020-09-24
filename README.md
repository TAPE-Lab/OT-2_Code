# OT-2_Barcode_Pipetting

## Outline:

Scripts to allow the automated pipetting of the TOBis 35-plex and 126-plex barcoding structure using the OT-2 machine.

Before beginning, it is recommended to read the 2020 Nature Methods, Qin et al. paper here: [Cell-type-specific signaling networks in heterocellular organoids](https://www.nature.com/articles/s41592-020-0737-8). This will give an overview of why TOBis is used instead of the traditional Fluidigm barcoding, it's advantages and also an application of its use.

Secondly, to understand the latest version of TOBis, to know the concentrations used and a very specific, step-by-step guide in carrying out the entire TOBis CyTOF protocol, please read the 2020 Nature Protocols, Qin et al. paper here: [Multiplexed Single-Cell Analysis of Organoid Signaling Networks](#Enter LINK here).

Lastly, the OT-2 library, labware, protocols and definitions can all be found on their [website](https://docs.opentrons.com/v2/). It includes the explanation of and how to use:
- Versioning
- Labware
- Hardware Modules
- Pipettes
- Building Block Commands
- Complex Commands
- API Version 2 Reference
- Advanced Control
With some example protocols as well. Custom protocols can also be made using their 'Protocol Designer', however it's not recommended to do use for complex protocols.


## Custom Commands

The following is an explanation/description of some functions used in the scripts:

**`def custom_wetting`:**
- With the first transfer of any pipette, the pipette tip is completely unused. With some solutions, this means the first transfer will not pipette the same volume of solution as the subsequent transfers using the same pipette tip. This is because the subsequent transfers are using a tip which has already been 'wet' by the solution, whereas the first transfer is not 'wet'.
- Therefore, this function aspirates a certain volume of solution and then dispenses that solution into the same tube. This allows the pipette tip to be 'wet' before the first transfer is made. Thus it reduces any variability in pipetting between the first and subsequent transfers through this step.
- This step is only performed at the beginning of every isotope which will be pipetted. So 7 and 9 times in total for the 35-plex and 126-plex, respectively.


**`def custom_transfer`:**
- This function is a collection of commands that is more than the basic `transfer` command used in the OT-2 software.
- It includes the following commands, as well as the simple `aspirate` and `dispense`:
    - **`touch_tip`**: After each aspiration of the pipette. The robot arm touches the pipette tip onto the inner part of the tube on 4 opposite parts of the tube. This allows any remaining solution of the outside of the pipette tip to fall off into the tube it was aspirated from. 
    - **`air_gap`**: After the `touch_tip` command, the pipette aspirates a set amount of air. This is to ensure that no liquid can accidentally drop out of the pipette tip as the robot arm is moving positions.
    - **`blow_out`**: After the pipette has completely dispensed the solution into the destination tube, the pipette then dispenses an extra amount of air. This is to ensure that all of the volume is dispensed out of the pipette tip.
- All three of the above additional commands vastly increases the accuracy of the transfer as it doesn't allow any additional solution clinging onto the exterior of the pipette tip to be added to the destination tube (using `touch_tip`), it ensures all of the solution is transferred from the `source` to the `destination` (using`air_gap`) and lastly ensures that all of the solution is added to the `destination` (using`blow_out`). 


**`def custom_batch`:**
- This is the main function which includes the two functions above.
- It allows a list of destinations, `destinations_list`, to be added as a parameter of the function. So that the specific barcode number, i.e. TOBis001 or TOBis 025, etc, can be added to that list. Then the robot will pipette the specific isotope allocated under `source` and pipette the specific `volume` from that `source` into all of the barcodes in `destinations_list`.
- It also includes a mathematical equation to allow the robot arm to decrease in height into the tube every time a specific volume is taken out. This is to ensure that as the protocol is progressing, the amount of volume in the source tube is decreasing, and thus, the robot arm decreases along with it to ensure that the pipette tip is always aspirating liquid.


## NOTE:
- For the 'source_headroom', you will need to measure the top of the tube of the source solution to the top of the meniscus of the solution millimetres using a caliper. 1 or 2 mm can be added onto this value to ensure the pipette tip enters into the solution.


## Acknowledgements

I would like to acknowledge the aid of and thank:
- Dr Alaric Taylor, in helping me write the script and teaching me how to use the OT-2 machine.
- Ferran Cardoso ([@FerranC96](https://github.com/FerranC96)) for helping me set up the OT-2_Barcode_Pipetting GitHub repository. 
- And lastly, the [TAPE Lab](http://tape-lab.com/lab) group for their continuous support in helping create the TOBis barcoding strategy.
The work here is actively being developed by Jahangir Sufi.