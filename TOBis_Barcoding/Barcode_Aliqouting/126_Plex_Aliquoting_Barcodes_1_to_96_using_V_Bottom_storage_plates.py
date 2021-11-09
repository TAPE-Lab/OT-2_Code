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
        pipette.dispense(dispensing_volume, destination)
        pipette.touch_tip()
    pipette.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', 11)
    tuberack = protocol.load_labware('starlab_96_wellplate_1200ul', 10)
    v_bottom_storage_plate_01 = protocol.load_labware('thermoscientific_96_wellplate_200ul', 1)
    v_bottom_storage_plate_02 = protocol.load_labware('thermoscientific_96_wellplate_200ul', 2)
    v_bottom_storage_plate_03 = protocol.load_labware('thermoscientific_96_wellplate_200ul', 3)
    v_bottom_storage_plate_04 = protocol.load_labware('thermoscientific_96_wellplate_200ul', 4)
    v_bottom_storage_plate_05 = protocol.load_labware('thermoscientific_96_wellplate_200ul', 5)
    v_bottom_storage_plate_06 = protocol.load_labware('thermoscientific_96_wellplate_200ul', 6)
    v_bottom_storage_plate_07 = protocol.load_labware('thermoscientific_96_wellplate_200ul', 7)
    v_bottom_storage_plate_08 = protocol.load_labware('thermoscientific_96_wellplate_200ul', 8)
    v_bottom_storage_plate_09 = protocol.load_labware('thermoscientific_96_wellplate_200ul', 9)
    p300_multi_right = protocol.load_instrument('p300_multi', 'right', tip_racks=[tiprack])
    protocol.max_speeds['X'] = 300
    protocol.max_speeds['Y'] = 300


    #This is the SOURCE
    TOBis001_Source = tuberack.well('A1')
    TOBis009_Source = tuberack.well('A2')
    TOBis017_Source = tuberack.well('A3')
    TOBis025_Source = tuberack.well('A4')
    TOBis033_Source = tuberack.well('A5')
    TOBis041_Source = tuberack.well('A6')
    TOBis049_Source = tuberack.well('A7')
    TOBis057_Source = tuberack.well('A8')
    TOBis065_Source = tuberack.well('A9')
    TOBis073_Source = tuberack.well('A10')
    TOBis081_Source = tuberack.well('A11')
    TOBis089_Source = tuberack.well('A12')


    #This is the DESTINATION
    TOBis001_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A1'],
    v_bottom_storage_plate_02.wells_by_name()['A1'],
    v_bottom_storage_plate_03.wells_by_name()['A1'],
    v_bottom_storage_plate_04.wells_by_name()['A1'],
    v_bottom_storage_plate_05.wells_by_name()['A1'],
    v_bottom_storage_plate_06.wells_by_name()['A1'],
    v_bottom_storage_plate_07.wells_by_name()['A1'],
    v_bottom_storage_plate_08.wells_by_name()['A1'],
    v_bottom_storage_plate_09.wells_by_name()['A1']]

    TOBis009_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A2'],
    v_bottom_storage_plate_02.wells_by_name()['A2'],
    v_bottom_storage_plate_03.wells_by_name()['A2'],
    v_bottom_storage_plate_04.wells_by_name()['A2'],
    v_bottom_storage_plate_05.wells_by_name()['A2'],
    v_bottom_storage_plate_06.wells_by_name()['A2'],
    v_bottom_storage_plate_07.wells_by_name()['A2'],
    v_bottom_storage_plate_08.wells_by_name()['A2'],
    v_bottom_storage_plate_09.wells_by_name()['A2']]

    TOBis017_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A3'],
    v_bottom_storage_plate_02.wells_by_name()['A3'],
    v_bottom_storage_plate_03.wells_by_name()['A3'],
    v_bottom_storage_plate_04.wells_by_name()['A3'],
    v_bottom_storage_plate_05.wells_by_name()['A3'],
    v_bottom_storage_plate_06.wells_by_name()['A3'],
    v_bottom_storage_plate_07.wells_by_name()['A3'],
    v_bottom_storage_plate_08.wells_by_name()['A3'],
    v_bottom_storage_plate_09.wells_by_name()['A3']]

    TOBis025_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A4'],
    v_bottom_storage_plate_02.wells_by_name()['A4'],
    v_bottom_storage_plate_03.wells_by_name()['A4'],
    v_bottom_storage_plate_04.wells_by_name()['A4'],
    v_bottom_storage_plate_05.wells_by_name()['A4'],
    v_bottom_storage_plate_06.wells_by_name()['A4'],
    v_bottom_storage_plate_07.wells_by_name()['A4'],
    v_bottom_storage_plate_08.wells_by_name()['A4'],
    v_bottom_storage_plate_09.wells_by_name()['A4']]

    TOBis033_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A5'],
    v_bottom_storage_plate_02.wells_by_name()['A5'],
    v_bottom_storage_plate_03.wells_by_name()['A5'],
    v_bottom_storage_plate_04.wells_by_name()['A5'],
    v_bottom_storage_plate_05.wells_by_name()['A5'],
    v_bottom_storage_plate_06.wells_by_name()['A5'],
    v_bottom_storage_plate_07.wells_by_name()['A5'],
    v_bottom_storage_plate_08.wells_by_name()['A5'],
    v_bottom_storage_plate_09.wells_by_name()['A5']]
    
    TOBis041_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A6'],
    v_bottom_storage_plate_02.wells_by_name()['A6'],
    v_bottom_storage_plate_03.wells_by_name()['A6'],
    v_bottom_storage_plate_04.wells_by_name()['A6'],
    v_bottom_storage_plate_05.wells_by_name()['A6'],
    v_bottom_storage_plate_06.wells_by_name()['A6'],
    v_bottom_storage_plate_07.wells_by_name()['A6'],
    v_bottom_storage_plate_08.wells_by_name()['A6'],
    v_bottom_storage_plate_09.wells_by_name()['A6']]

    TOBis049_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A7'],
    v_bottom_storage_plate_02.wells_by_name()['A7'],
    v_bottom_storage_plate_03.wells_by_name()['A7'],
    v_bottom_storage_plate_04.wells_by_name()['A7'],
    v_bottom_storage_plate_05.wells_by_name()['A7'],
    v_bottom_storage_plate_06.wells_by_name()['A7'],
    v_bottom_storage_plate_07.wells_by_name()['A7'],
    v_bottom_storage_plate_08.wells_by_name()['A7'],
    v_bottom_storage_plate_09.wells_by_name()['A7']]

    TOBis057_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A8'],
    v_bottom_storage_plate_02.wells_by_name()['A8'],
    v_bottom_storage_plate_03.wells_by_name()['A8'],
    v_bottom_storage_plate_04.wells_by_name()['A8'],
    v_bottom_storage_plate_05.wells_by_name()['A8'],
    v_bottom_storage_plate_06.wells_by_name()['A8'],
    v_bottom_storage_plate_07.wells_by_name()['A8'],
    v_bottom_storage_plate_08.wells_by_name()['A8'],
    v_bottom_storage_plate_09.wells_by_name()['A8']]

    TOBis065_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A9'],
    v_bottom_storage_plate_02.wells_by_name()['A9'],
    v_bottom_storage_plate_03.wells_by_name()['A9'],
    v_bottom_storage_plate_04.wells_by_name()['A9'],
    v_bottom_storage_plate_05.wells_by_name()['A9'],
    v_bottom_storage_plate_06.wells_by_name()['A9'],
    v_bottom_storage_plate_07.wells_by_name()['A9'],
    v_bottom_storage_plate_08.wells_by_name()['A9'],
    v_bottom_storage_plate_09.wells_by_name()['A9']]

    TOBis073_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A10'],
    v_bottom_storage_plate_02.wells_by_name()['A10'],
    v_bottom_storage_plate_03.wells_by_name()['A10'],
    v_bottom_storage_plate_04.wells_by_name()['A10'],
    v_bottom_storage_plate_05.wells_by_name()['A10'],
    v_bottom_storage_plate_06.wells_by_name()['A10'],
    v_bottom_storage_plate_07.wells_by_name()['A10'],
    v_bottom_storage_plate_08.wells_by_name()['A10'],
    v_bottom_storage_plate_09.wells_by_name()['A10']]

    TOBis081_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A11'],
    v_bottom_storage_plate_02.wells_by_name()['A11'],
    v_bottom_storage_plate_03.wells_by_name()['A11'],
    v_bottom_storage_plate_04.wells_by_name()['A11'],
    v_bottom_storage_plate_05.wells_by_name()['A11'],
    v_bottom_storage_plate_06.wells_by_name()['A11'],
    v_bottom_storage_plate_07.wells_by_name()['A11'],
    v_bottom_storage_plate_08.wells_by_name()['A11'],
    v_bottom_storage_plate_09.wells_by_name()['A11']]

    TOBis089_Destinations = [v_bottom_storage_plate_01.wells_by_name()['A12'],
    v_bottom_storage_plate_02.wells_by_name()['A12'],
    v_bottom_storage_plate_03.wells_by_name()['A12'],
    v_bottom_storage_plate_04.wells_by_name()['A12'],
    v_bottom_storage_plate_05.wells_by_name()['A12'],
    v_bottom_storage_plate_06.wells_by_name()['A12'],
    v_bottom_storage_plate_07.wells_by_name()['A12'],
    v_bottom_storage_plate_08.wells_by_name()['A12'],
    v_bottom_storage_plate_09.wells_by_name()['A12']]


    #Below is the code to aliquot the barcodes into their respective wells and respective plates.
    barcode_aliquoting(181, TOBis001_Source, 20, TOBis001_Destinations, p300_multi_right)
    
    barcode_aliquoting(181, TOBis009_Source, 20, TOBis009_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis017_Source, 20, TOBis017_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis025_Source, 20, TOBis025_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis033_Source, 20, TOBis033_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis041_Source, 20, TOBis041_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis049_Source, 20, TOBis049_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis057_Source, 20, TOBis057_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis065_Source, 20, TOBis065_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis073_Source, 20, TOBis073_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis081_Source, 20, TOBis081_Destinations, p300_multi_right)

    barcode_aliquoting(181, TOBis089_Source, 20, TOBis089_Destinations, p300_multi_right)