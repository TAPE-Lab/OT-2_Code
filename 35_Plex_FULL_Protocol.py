from opentrons import protocol_api
import numpy as np

metadata = {
    'apiLevel': '2.0',
    'author': 'Jahangir.Sufi'}
    
def custom_wetting(volume, source, source_headroom, pipette):
    pipette.aspirate(volume,source.top(-source_headroom -5))
    pipette.dispense(volume,source.top())
    pipette.blow_out()
    pipette.touch_tip()
    
def custom_transfer(volume, source, source_headroom, destination, pipette):
    pipette.aspirate(volume,source.top(-source_headroom -5))
    pipette.touch_tip()
    pipette.air_gap(2)
    pipette.dispense(volume+5,destination.top())
    pipette.blow_out()
    
def custom_batch(volume, source, source_headroom, destinations_list, pipette, mm_lost_per_ul):
    number_of_destinations = len(destinations_list)            #DO WE NEED THIS?
    headroom = source_headroom                     #DO WE NEED THIS?
    
    pipette.pick_up_tip()
    custom_wetting(volume, source, headroom, pipette)
    for destination in destinations_list:
        custom_transfer(volume, source, headroom, destination, pipette)
        headroom += mm_lost_per_ul * volume
    pipette.drop_tip()

    

def run(protocol: protocol_api.ProtocolContext):
    #tiprack is yet to be determined but I'm just using the opentrons tips in this case.
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', 9)
    tuberack = protocol.load_labware('adrena_40_wellplate_1500ul', 3)
    plate_1 = protocol.load_labware('starlab_96_wellplate_1200ul', 6)          #Need to add labware and change location
    p50 = protocol.load_instrument('p50_single', 'left', tip_racks=[tiprack])


    #This is the SOURCE
    Te122 = tuberack.well('A3')   #ENTER LOCATION
    Te123 = tuberack.well('A5')
    Te124 = tuberack.well('A7')
    Te125 = tuberack.well('C3')
    Te126 = tuberack.well('C5')
    Te128 = tuberack.well('C7')
    Te130 = tuberack.well('E3')
    

    # Measurement of distance between meniscus and top of vial in mm. This is the SOURCE_HEADROOM.
    Te122_headroom = 28.75
    Te123_headroom = 28.91     #ENTER DEPTH FROM MINICUS TO TOP OF VIAL 
    Te124_headroom = 29.32
    Te125_headroom = 31.18
    Te126_headroom = 31.17
    Te128_headroom = 33.30
    Te130_headroom = 34.10
    

    #This is the DESTINATION
    TOBis01 = plate_1.well('A1')
    TOBis02 = plate_1.well('B1')
    TOBis03 = plate_1.well('C1')
    TOBis04 = plate_1.well('D1')
    TOBis05 = plate_1.well('E1')
    TOBis06 = plate_1.well('F1')
    TOBis07 = plate_1.well('G1')
    TOBis08 = plate_1.well('H1')
    TOBis09 = plate_1.well('A2')
    TOBis10 = plate_1.well('B2')
    TOBis11 = plate_1.well('C2')
    TOBis12 = plate_1.well('D2')
    TOBis13 = plate_1.well('E2')
    TOBis14 = plate_1.well('F2')
    TOBis15 = plate_1.well('G2')
    TOBis16 = plate_1.well('H2')
    TOBis17 = plate_1.well('A3')
    TOBis18 = plate_1.well('B3')
    TOBis19 = plate_1.well('C3')
    TOBis20 = plate_1.well('D3')
    TOBis21 = plate_1.well('E3')
    TOBis22 = plate_1.well('F3')
    TOBis23 = plate_1.well('G3')
    TOBis24 = plate_1.well('H3')
    TOBis25 = plate_1.well('A4')
    TOBis26 = plate_1.well('B4')
    TOBis27 = plate_1.well('C4')
    TOBis28 = plate_1.well('D4')
    TOBis29 = plate_1.well('E4')
    TOBis30 = plate_1.well('F4')
    TOBis31 = plate_1.well('G4')
    TOBis32 = plate_1.well('H4')
    TOBis33 = plate_1.well('A5')
    TOBis34 = plate_1.well('B5')
    TOBis35 = plate_1.well('C5')



    
    diameter = 9.9
    disc_area = np.pi * (diameter/2) * (diameter/2)
    mm_lost_per_ul = 1/disc_area
    
    # # Debugging maths problems!
    # protocol.comment(str(mm_lost_per_ul))
    # protocol.pause('Has units of mm_lost_per_ul been captured correctly?')
    # protocol.comment('Headroom before calculation '+ str(Te122_headroom))
    # Te122_headroom += mm_lost_per_ul * 22
    # protocol.comment('Headroom after calculation ' + str(Te122_headroom))
    # protocol.pause('Has the calculation run correctly?')


    
    #Te-122
    custom_batch(22, Te122, Te122_headroom, [TOBis01,
    TOBis02,
    TOBis03,
    TOBis04,
    TOBis05,
    TOBis06,
    TOBis07,
    TOBis08,
    TOBis09,
    TOBis10,
    TOBis11,
    TOBis12,
    TOBis13,
    TOBis14,
    TOBis15], p50, mm_lost_per_ul)



    #Te-123
    custom_batch(20.4, Te123, Te123_headroom, [TOBis01,
    TOBis02,
    TOBis03,
    TOBis04,
    TOBis05,
    TOBis16,
    TOBis17,
    TOBis18,
    TOBis19,
    TOBis20,
    TOBis21,
    TOBis22,
    TOBis23,
    TOBis24,
    TOBis25], p50, mm_lost_per_ul)

    #Te-124
    custom_batch(18, Te124, Te124_headroom, [TOBis01,
    TOBis06,
    TOBis07,
    TOBis08,
    TOBis09,
    TOBis16,
    TOBis17,
    TOBis18,
    TOBis19,
    TOBis26,
    TOBis27,
    TOBis28,
    TOBis29,
    TOBis30,
    TOBis31], p50, mm_lost_per_ul)

    #Te-125
    custom_batch(15, Te125, Te125_headroom, [TOBis02,
    TOBis06,
    TOBis10,
    TOBis11,
    TOBis12,
    TOBis16,
    TOBis20,
    TOBis21,
    TOBis22,
    TOBis26,
    TOBis27,
    TOBis28,
    TOBis32,
    TOBis33,
    TOBis34], p50, mm_lost_per_ul)


    #Te-126
    custom_batch(15, Te126, Te126_headroom, [TOBis03,
    TOBis07,
    TOBis10,
    TOBis13,
    TOBis14,
    TOBis17,
    TOBis20,
    TOBis23,
    TOBis24,
    TOBis26,
    TOBis29,
    TOBis30,
    TOBis32,
    TOBis33,
    TOBis35], p50, mm_lost_per_ul)


    #Te-128
    custom_batch(11.2, Te128, Te128_headroom, [TOBis04,
    TOBis08,
    TOBis11,
    TOBis13,
    TOBis15,
    TOBis18,
    TOBis21,
    TOBis23,
    TOBis25,
    TOBis27,
    TOBis29,
    TOBis31,
    TOBis32,
    TOBis34,
    TOBis35], p50, mm_lost_per_ul)

    #Te-130
    custom_batch(9.6, Te130, Te130_headroom, [TOBis05,
    TOBis09,
    TOBis12,
    TOBis14,
    TOBis15,
    TOBis19,
    TOBis22,
    TOBis24,
    TOBis25,
    TOBis28,
    TOBis30,
    TOBis31,
    TOBis33,
    TOBis34,
    TOBis35], p50, mm_lost_per_ul)
