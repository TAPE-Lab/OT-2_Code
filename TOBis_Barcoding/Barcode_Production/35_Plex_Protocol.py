from opentrons import protocol_api
import numpy as np

metadata = {
    'apiLevel': '2.10',
    'author': 'Jahangir.Sufi'}

def custom_transfer(volume, source, source_headroom, destination, pipette):
    pipette.aspirate(volume,source.top(-source_headroom -5))
    pipette.touch_tip()
    pipette.air_gap(2)
    pipette.dispense(volume+5,destination.top(-2))
    pipette.blow_out()
    pipette.touch_tip(radius=0.15, v_offset=-1, speed=80)
    pipette.touch_tip(radius=0.15, v_offset=-1, speed=80)
    pipette.touch_tip(radius=0.15, v_offset=-1, speed=80)
    pipette.touch_tip(radius=0.15, v_offset=-1, speed=80)
    
def custom_batch(volume, source, source_headroom, destinations_list, pipette, mm_lost_per_ul_eppendorf):
    headroom = source_headroom
    
    pipette.pick_up_tip()
    pipette.mix(10, 20, source, 2)
    for destination in destinations_list:
        custom_transfer(volume, source, headroom, destination, pipette)
        headroom += mm_lost_per_ul_eppendorf * volume
    pipette.drop_tip()

    

def run(protocol: protocol_api.ProtocolContext):
    tiprack_p20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 8)
    tiprack_p1000 = protocol.load_labware('opentrons_96_filtertiprack_1000ul', 9)

    p20_single = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_p20])
    p1000_single = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_p1000])

    tuberack = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 5)
    deepwell_plate_35_plex = protocol.load_labware('starlab_96_wellplate_1200ul', 6)

    DMSO_falcon = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', 2)


    #This is the SOURCE
    Te122 = tuberack.well('A6')
    Te123 = tuberack.well('B6')
    Te124 = tuberack.well('C6')
    Te125 = tuberack.well('D6')
    Te126 = tuberack.well('B5')
    Te128 = tuberack.well('C5')
    Te130 = tuberack.well('D5')
    

    # Measurement of distance between meniscus and top of vial in mm. This is the SOURCE_HEADROOM.
    Te122_headroom = 28.21   #500 uL
    Te123_headroom = 28.77   #475 uL         #ENTER DEPTH FROM MINICUS TO TOP OF VIAL 
    Te124_headroom = 28.21   #500 uL
    Te125_headroom = 29.35   #450 uL 
    Te126_headroom = 29.35   #450 uL 
    Te128_headroom = 28.77   #475 uL 
    Te130_headroom = 28.77   #475 uL 

    DMSO_headroom = 30.18    #Pipette exactly 40 mL of DMSO
    

    #This is the DESTINATION
    TOBis01 = deepwell_plate_35_plex.well('A1')
    TOBis02 = deepwell_plate_35_plex.well('B1')
    TOBis03 = deepwell_plate_35_plex.well('C1')
    TOBis04 = deepwell_plate_35_plex.well('D1')
    TOBis05 = deepwell_plate_35_plex.well('E1')
    TOBis06 = deepwell_plate_35_plex.well('F1')
    TOBis07 = deepwell_plate_35_plex.well('G1')
    TOBis08 = deepwell_plate_35_plex.well('H1')

    TOBis09 = deepwell_plate_35_plex.well('A2')
    TOBis10 = deepwell_plate_35_plex.well('B2')
    TOBis11 = deepwell_plate_35_plex.well('C2')
    TOBis12 = deepwell_plate_35_plex.well('D2')
    TOBis13 = deepwell_plate_35_plex.well('E2')
    TOBis14 = deepwell_plate_35_plex.well('F2')
    TOBis15 = deepwell_plate_35_plex.well('G2')
    TOBis16 = deepwell_plate_35_plex.well('H2')

    TOBis17 = deepwell_plate_35_plex.well('A3')
    TOBis18 = deepwell_plate_35_plex.well('B3')
    TOBis19 = deepwell_plate_35_plex.well('C3')
    TOBis20 = deepwell_plate_35_plex.well('D3')
    TOBis21 = deepwell_plate_35_plex.well('E3')
    TOBis22 = deepwell_plate_35_plex.well('F3')
    TOBis23 = deepwell_plate_35_plex.well('G3')
    TOBis24 = deepwell_plate_35_plex.well('H3')

    TOBis25 = deepwell_plate_35_plex.well('A4')
    TOBis26 = deepwell_plate_35_plex.well('B4')
    TOBis27 = deepwell_plate_35_plex.well('C4')
    TOBis28 = deepwell_plate_35_plex.well('D4')
    TOBis29 = deepwell_plate_35_plex.well('E4')
    TOBis30 = deepwell_plate_35_plex.well('F4')
    TOBis31 = deepwell_plate_35_plex.well('G4')
    TOBis32 = deepwell_plate_35_plex.well('H4')

    TOBis33 = deepwell_plate_35_plex.well('A5')
    TOBis34 = deepwell_plate_35_plex.well('B5')
    TOBis35 = deepwell_plate_35_plex.well('C5')


    DMSO_dict = {TOBis01:947.4,
    TOBis02:950.4,
    TOBis03:950.4,
    TOBis04:949.4,
    TOBis05:949.4,
    TOBis06:949.4,
    TOBis07:949.4,
    TOBis08:948.4,
    TOBis09:948.4,
    TOBis10:952.4,
    TOBis11:951.4,
    TOBis12:951.4,
    TOBis13:951.4,
    TOBis14:951.4,
    TOBis15:950.4,
    TOBis16:950.0,
    TOBis17:950.0,
    TOBis18:949.0,
    TOBis19:949.0,
    TOBis20:953.0,
    TOBis21:952.0,
    TOBis22:952.0,
    TOBis23:952.0,
    TOBis24:952.0,
    TOBis25:951.0,
    TOBis26:952.0,
    TOBis27:951.0,
    TOBis28:951.0,
    TOBis29:951.0,
    TOBis30:951.0,
    TOBis31:950.0,
    TOBis32:954.0,
    TOBis33:954.0,
    TOBis34:953.0,
    TOBis35:953.0}




    diameter_50ml_falcon = 28
    disc_area_50ml_falcon = np.pi * (diameter_50ml_falcon/2) * (diameter_50ml_falcon/2)
    mm_lost_per_ul_50ml_falcon = 1/disc_area_50ml_falcon

    p1000_single.flow_rate.aspirate = 250
    p1000_single.default_speed = 250
    p1000_single.pick_up_tip()
    p1000_single.mix(2, 1000, DMSO_falcon.well('A3').top(-DMSO_headroom-10))
    for location, volume in DMSO_dict.items():
        p1000_single.aspirate(volume, DMSO_falcon.well('A3').top(-DMSO_headroom-15)) 
        protocol.delay(1)
        p1000_single.air_gap(5)
        protocol.delay(1)
        p1000_single.dispense(volume+20, location.top(-5))
        protocol.delay(1)
        p1000_single.blow_out(location.top(-2))
        DMSO_headroom += mm_lost_per_ul_50ml_falcon * volume
    p1000_single.drop_tip()


   

    diameter_eppendorf = 9.9
    disc_area_eppendorf = np.pi * (diameter_eppendorf/2) * (diameter_eppendorf/2)
    mm_lost_per_ul_eppendorf = 1/disc_area_eppendorf
   
    #Te-122 - working concentration = 1.25 mM
    custom_batch(17.6, Te122, Te122_headroom, [TOBis01,
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
    TOBis15], p20_single, mm_lost_per_ul_eppendorf)


    #Te-123 - working concentration = 1.20 mM
    custom_batch(17, Te123, Te123_headroom, [TOBis01,
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
    TOBis25], p20_single, mm_lost_per_ul_eppendorf)


    #Te-124 - working concentration = 1.0 mM
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
    TOBis31], p20_single, mm_lost_per_ul_eppendorf)


    #Te-125 - working concentration = 1.0 mM
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
    TOBis34], p20_single, mm_lost_per_ul_eppendorf)


    #Te-126 - working concentration = 1.0 mM
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
    TOBis35], p20_single, mm_lost_per_ul_eppendorf)


    #Te-128 - working concentration = 0.7 mM
    custom_batch(16, Te128, Te128_headroom, [TOBis04,
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
    TOBis35], p20_single, mm_lost_per_ul_eppendorf)


    #Te-130 - working concentration = 0.6 mM
    custom_batch(16, Te130, Te130_headroom, [TOBis05,
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
    TOBis35], p20_single, mm_lost_per_ul_eppendorf)
