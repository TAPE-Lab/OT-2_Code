from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'author': 'Jahangir.Sufi'}
    
def barcode_aliquoting(aspiration_volume, aspiration_source, dispensing_volume, dispensing_destinations_01, dispensing_destinations_02, dispensing_destinations_03, pipette):
    pipette.pick_up_tip()
    pipette.mix(2, 200, aspiration_source)
    pipette.aspirate(aspiration_volume, aspiration_source.bottom(1))
    pipette.touch_tip()
    for destination_01 in dispensing_destinations_01:
        pipette.dispense(dispensing_volume, destination_01)
        pipette.touch_tip()

    pipette.mix(2, 190, aspiration_source)     #The reason why it's 190 uL here is because there is already 1 uL of solution in the pipette tip, and it can't aspirate more than the max volume of the pipette.
    pipette.aspirate(aspiration_volume, aspiration_source.bottom(1))
    pipette.touch_tip()
    for destination_02 in dispensing_destinations_02:
        pipette.dispense(dispensing_volume, destination_02)
        pipette.touch_tip()

    pipette.mix(2, 190, aspiration_source)
    pipette.aspirate(aspiration_volume, aspiration_source.bottom(1))
    pipette.touch_tip()
    for destination_03 in dispensing_destinations_03:
        pipette.dispense(dispensing_volume, destination_03)
        pipette.touch_tip()
    pipette.drop_tip()


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', 11)     #may need to change this to the filtered one
    tuberack = protocol.load_labware('starlab_96_wellplate_1200ul', 10)
    pcr_plate_01 = protocol.load_labware('thermofisher_96_wellplate_200ul', 1)
    pcr_plate_02 = protocol.load_labware('thermofisher_96_wellplate_200ul', 2)
    pcr_plate_03 = protocol.load_labware('thermofisher_96_wellplate_200ul', 3)
    pcr_plate_04 = protocol.load_labware('thermofisher_96_wellplate_200ul', 4)
    pcr_plate_05 = protocol.load_labware('thermofisher_96_wellplate_200ul', 5)
    pcr_plate_06 = protocol.load_labware('thermofisher_96_wellplate_200ul', 6)
    pcr_plate_07 = protocol.load_labware('thermofisher_96_wellplate_200ul', 7)
    pcr_plate_08 = protocol.load_labware('thermofisher_96_wellplate_200ul', 8)
    pcr_plate_09 = protocol.load_labware('thermofisher_96_wellplate_200ul', 9)
    p300_multi_right = protocol.load_instrument('p300_multi', 'right', tip_racks=[tiprack])
    protocol.max_speeds['X'] = 300
    protocol.max_speeds['Y'] = 300


    #These are the SOURCES
    TOBis097_Source = tuberack.well('A1')
    TOBis105_Source = tuberack.well('A2')
    TOBis113_Source = tuberack.well('A3')
    TOBis121_Source = tuberack.well('A4')


    #Below are the DESTINATIONS
    TOBis097_Destinations_01 = [pcr_plate_01.wells_by_name()['A1'],
    pcr_plate_01.wells_by_name()['A5'],
    pcr_plate_01.wells_by_name()['A9'],
    pcr_plate_02.wells_by_name()['A1'],
    pcr_plate_02.wells_by_name()['A5'],
    pcr_plate_02.wells_by_name()['A9'],
    pcr_plate_03.wells_by_name()['A1'],
    pcr_plate_03.wells_by_name()['A5'],
    pcr_plate_03.wells_by_name()['A9']]
    TOBis097_Destinations_02 = [pcr_plate_04.wells_by_name()['A1'],
    pcr_plate_04.wells_by_name()['A5'],
    pcr_plate_04.wells_by_name()['A9'],
    pcr_plate_05.wells_by_name()['A1'],
    pcr_plate_05.wells_by_name()['A5'],
    pcr_plate_05.wells_by_name()['A9'],
    pcr_plate_06.wells_by_name()['A1'],
    pcr_plate_06.wells_by_name()['A5'],
    pcr_plate_06.wells_by_name()['A9']]
    TOBis097_Destinations_03 = [pcr_plate_07.wells_by_name()['A1'],
    pcr_plate_07.wells_by_name()['A5'],
    pcr_plate_07.wells_by_name()['A9'],
    pcr_plate_08.wells_by_name()['A1'],
    pcr_plate_08.wells_by_name()['A5'],
    pcr_plate_08.wells_by_name()['A9'],
    pcr_plate_09.wells_by_name()['A1'],
    pcr_plate_09.wells_by_name()['A5'],
    pcr_plate_09.wells_by_name()['A9']]


    TOBis105_Destinations_01 = [pcr_plate_01.wells_by_name()['A2'],
    pcr_plate_01.wells_by_name()['A6'],
    pcr_plate_01.wells_by_name()['A10'],
    pcr_plate_02.wells_by_name()['A2'],
    pcr_plate_02.wells_by_name()['A6'],
    pcr_plate_02.wells_by_name()['A10'],
    pcr_plate_03.wells_by_name()['A2'],
    pcr_plate_03.wells_by_name()['A6'],
    pcr_plate_03.wells_by_name()['A10']]
    TOBis105_Destinations_02 = [pcr_plate_04.wells_by_name()['A2'],
    pcr_plate_04.wells_by_name()['A6'],
    pcr_plate_04.wells_by_name()['A10'],
    pcr_plate_05.wells_by_name()['A2'],
    pcr_plate_05.wells_by_name()['A6'],
    pcr_plate_05.wells_by_name()['A10'],
    pcr_plate_06.wells_by_name()['A2'],
    pcr_plate_06.wells_by_name()['A6'],
    pcr_plate_06.wells_by_name()['A10']]
    TOBis105_Destinations_03 = [pcr_plate_07.wells_by_name()['A2'],
    pcr_plate_07.wells_by_name()['A6'],
    pcr_plate_07.wells_by_name()['A10'],
    pcr_plate_08.wells_by_name()['A2'],
    pcr_plate_08.wells_by_name()['A6'],
    pcr_plate_08.wells_by_name()['A10'],
    pcr_plate_09.wells_by_name()['A2'],
    pcr_plate_09.wells_by_name()['A6'],
    pcr_plate_09.wells_by_name()['A10']]


    TOBis113_Destinations_01 = [pcr_plate_01.wells_by_name()['A3'],
    pcr_plate_01.wells_by_name()['A7'],
    pcr_plate_01.wells_by_name()['A11'],
    pcr_plate_02.wells_by_name()['A3'],
    pcr_plate_02.wells_by_name()['A7'],
    pcr_plate_02.wells_by_name()['A11'],
    pcr_plate_03.wells_by_name()['A3'],
    pcr_plate_03.wells_by_name()['A7'],
    pcr_plate_03.wells_by_name()['A11']]
    TOBis113_Destinations_02 = [pcr_plate_04.wells_by_name()['A3'],
    pcr_plate_04.wells_by_name()['A7'],
    pcr_plate_04.wells_by_name()['A11'],
    pcr_plate_05.wells_by_name()['A3'],
    pcr_plate_05.wells_by_name()['A7'],
    pcr_plate_05.wells_by_name()['A11'],
    pcr_plate_06.wells_by_name()['A3'],
    pcr_plate_06.wells_by_name()['A7'],
    pcr_plate_06.wells_by_name()['A11']]
    TOBis113_Destinations_03 = [pcr_plate_07.wells_by_name()['A3'],
    pcr_plate_07.wells_by_name()['A7'],
    pcr_plate_07.wells_by_name()['A11'],
    pcr_plate_08.wells_by_name()['A3'],
    pcr_plate_08.wells_by_name()['A7'],
    pcr_plate_08.wells_by_name()['A11'],
    pcr_plate_09.wells_by_name()['A3'],
    pcr_plate_09.wells_by_name()['A7'],
    pcr_plate_09.wells_by_name()['A11']]


    TOBis121_Destinations_01 = [pcr_plate_01.wells_by_name()['A4'],
    pcr_plate_01.wells_by_name()['A8'],
    pcr_plate_01.wells_by_name()['A12'],
    pcr_plate_02.wells_by_name()['A4'],
    pcr_plate_02.wells_by_name()['A8'],
    pcr_plate_02.wells_by_name()['A12'],
    pcr_plate_03.wells_by_name()['A4'],
    pcr_plate_03.wells_by_name()['A8'],
    pcr_plate_03.wells_by_name()['A12']]
    TOBis121_Destinations_02 = [pcr_plate_04.wells_by_name()['A4'],
    pcr_plate_04.wells_by_name()['A8'],
    pcr_plate_04.wells_by_name()['A12'],
    pcr_plate_05.wells_by_name()['A4'],
    pcr_plate_05.wells_by_name()['A8'],
    pcr_plate_05.wells_by_name()['A12'],
    pcr_plate_06.wells_by_name()['A4'],
    pcr_plate_06.wells_by_name()['A8'],
    pcr_plate_06.wells_by_name()['A12']]
    TOBis121_Destinations_03 = [pcr_plate_07.wells_by_name()['A4'],
    pcr_plate_07.wells_by_name()['A8'],
    pcr_plate_07.wells_by_name()['A12'],
    pcr_plate_08.wells_by_name()['A4'],
    pcr_plate_08.wells_by_name()['A8'],
    pcr_plate_08.wells_by_name()['A12'],
    pcr_plate_09.wells_by_name()['A4'],
    pcr_plate_09.wells_by_name()['A8'],
    pcr_plate_09.wells_by_name()['A12']]


    #Below is the code to aliquot the barcodes into their respective wells and respective plates.
    barcode_aliquoting(181, TOBis097_Source, 20, TOBis097_Destinations_01, TOBis097_Destinations_02, TOBis097_Destinations_03, p300_multi_right)

    barcode_aliquoting(181, TOBis105_Source, 20, TOBis105_Destinations_01, TOBis105_Destinations_02, TOBis105_Destinations_03, p300_multi_right)

    barcode_aliquoting(181, TOBis113_Source, 20, TOBis113_Destinations_01, TOBis113_Destinations_02, TOBis113_Destinations_03, p300_multi_right)

    barcode_aliquoting(181, TOBis121_Source, 20, TOBis121_Destinations_01, TOBis121_Destinations_02, TOBis121_Destinations_03, p300_multi_right)