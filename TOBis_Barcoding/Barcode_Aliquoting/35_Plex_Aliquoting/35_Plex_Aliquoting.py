from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'author': 'Jahangir.Sufi'}

def barcode_aliquoting(aspiration_volume, aspiration_source, dispensing_volume, dispensing_destinations, pipette):
    pipette.pick_up_tip()
    pipette.mix(2, 200, aspiration_source.bottom(1))
    pipette.aspirate(aspiration_volume, aspiration_source.bottom(1))
    pipette.touch_tip()
    for destination in dispensing_destinations:
        pipette.dispense(dispensing_volume, destination.bottom(5))
        pipette.touch_tip(v_offset=-11)
    pipette.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', 11)
    tuberack = protocol.load_labware('starlab_96_wellplate_1200ul', 10)
    pcr_plate_01 = protocol.load_labware('fluidigmorange_96_tuberack_200ul', 1)
    pcr_plate_02 = protocol.load_labware('fluidigmorange_96_tuberack_200ul', 2)
    pcr_plate_03 = protocol.load_labware('fluidigmorange_96_tuberack_200ul', 3)
    pcr_plate_04 = protocol.load_labware('fluidigmorange_96_tuberack_200ul', 4)
    pcr_plate_05 = protocol.load_labware('fluidigmorange_96_tuberack_200ul', 5)
    pcr_plate_06 = protocol.load_labware('fluidigmorange_96_tuberack_200ul', 6)
    pcr_plate_07 = protocol.load_labware('fluidigmorange_96_tuberack_200ul', 7)
    pcr_plate_08 = protocol.load_labware('fluidigmorange_96_tuberack_200ul', 8)
    pcr_plate_09 = protocol.load_labware('fluidigmorange_96_tuberack_200ul', 9)
    p300_multi_right = protocol.load_instrument('p300_multi', 'right', tip_racks=[tiprack])
    protocol.max_speeds['X'] = 300
    protocol.max_speeds['Y'] = 300


    #This is the SOURCE
    TOBis01_Source = tuberack.well('A1')
    TOBis09_Source = tuberack.well('A2')
    TOBis17_Source = tuberack.well('A3')
    TOBis25_Source = tuberack.well('A4')
    TOBis33_Source = tuberack.well('A5')
    

    #This is the DESTINATION
    TOBis01_Destinations = [pcr_plate_01.wells_by_name()['A1'],
    pcr_plate_02.wells_by_name()['A1'],
    pcr_plate_03.wells_by_name()['A1'],
    pcr_plate_04.wells_by_name()['A1'],
    pcr_plate_05.wells_by_name()['A1'],
    pcr_plate_06.wells_by_name()['A1'],
    pcr_plate_07.wells_by_name()['A1'],
    pcr_plate_08.wells_by_name()['A1'],
    pcr_plate_09.wells_by_name()['A1']]

    TOBis09_Destinations = [pcr_plate_01.wells_by_name()['A3'],
    pcr_plate_02.wells_by_name()['A3'],
    pcr_plate_03.wells_by_name()['A3'],
    pcr_plate_04.wells_by_name()['A3'],
    pcr_plate_05.wells_by_name()['A3'],
    pcr_plate_06.wells_by_name()['A3'],
    pcr_plate_07.wells_by_name()['A3'],
    pcr_plate_08.wells_by_name()['A3'],
    pcr_plate_09.wells_by_name()['A3']]

    TOBis17_Destinations = [pcr_plate_01.wells_by_name()['A5'],
    pcr_plate_02.wells_by_name()['A5'],
    pcr_plate_03.wells_by_name()['A5'],
    pcr_plate_04.wells_by_name()['A5'],
    pcr_plate_05.wells_by_name()['A5'],
    pcr_plate_06.wells_by_name()['A5'],
    pcr_plate_07.wells_by_name()['A5'],
    pcr_plate_08.wells_by_name()['A5'],
    pcr_plate_09.wells_by_name()['A5']]

    TOBis25_Destinations = [pcr_plate_01.wells_by_name()['A7'],
    pcr_plate_02.wells_by_name()['A7'],
    pcr_plate_03.wells_by_name()['A7'],
    pcr_plate_04.wells_by_name()['A7'],
    pcr_plate_05.wells_by_name()['A7'],
    pcr_plate_06.wells_by_name()['A7'],
    pcr_plate_07.wells_by_name()['A7'],
    pcr_plate_08.wells_by_name()['A7'],
    pcr_plate_09.wells_by_name()['A7']]

    TOBis33_Destinations = [pcr_plate_01.wells_by_name()['A9'],
    pcr_plate_02.wells_by_name()['A9'],
    pcr_plate_03.wells_by_name()['A9'],
    pcr_plate_04.wells_by_name()['A9'],
    pcr_plate_05.wells_by_name()['A9'],
    pcr_plate_06.wells_by_name()['A9'],
    pcr_plate_07.wells_by_name()['A9'],
    pcr_plate_08.wells_by_name()['A9'],
    pcr_plate_09.wells_by_name()['A9']]

   
    #Below is the code to aliquot the barcodes into their respective wells and respective plates.
    barcode_aliquoting(181, TOBis01_Source, 20, TOBis01_Destinations, p300_multi_right)
    
    barcode_aliquoting(181, TOBis09_Source, 20, TOBis09_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis17_Source, 20, TOBis17_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis25_Source, 20, TOBis25_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis33_Source, 20, TOBis33_Destinations, p300_multi_right)