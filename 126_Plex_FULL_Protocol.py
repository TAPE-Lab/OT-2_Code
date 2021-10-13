from opentrons import protocol_api
import numpy as np

metadata = {
    'apiLevel': '2.10',
    'author': 'Jahangir.Sufi'}
    
def custom_transfer(volume, source, source_headroom, destination, pipette):
    pipette.aspirate(volume, source.top(-source_headroom -5))
    pipette.touch_tip()
    pipette.air_gap(2)
    pipette.dispense(volume+10, destination.top())
    pipette.blow_out()
    pipette.touch_tip(radius=0.1, v_offset=5, speed=80)
    pipette.touch_tip(radius=0.1, v_offset=5, speed=80)
    pipette.touch_tip(radius=0.1, v_offset=5, speed=80)
        
def custom_batch(volume, source, source_headroom, destinations_list, pipette, mm_lost_per_ul):
    headroom = source_headroom
    
    pipette.pick_up_tip()
    pipette.mix(10, 20, source, 2)
    for destination in destinations_list:
        custom_transfer(volume, source, headroom, destination, pipette)
        headroom += mm_lost_per_ul * volume
    pipette.drop_tip()

def run(protocol: protocol_api.ProtocolContext):
    plate_1 = protocol.load_labware('starlab_96_wellplate_1200ul', 2)
    plate_2 = protocol.load_labware('starlab_96_wellplate_1200ul', 3)

    tuberack = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 5)
    DMSO_reservoir = protocol.load_labware('thermoscientific_1_reservoir_300000ul', 6)

    tiprack_p20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 8)
    tiprack_p1000 = protocol.load_labware('opentrons_96_filtertiprack_1000ul', 9)
    
    p20_single = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_p20])
    p1000_single = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_p1000])
    


    #This is the SOURCE
    Te122 = tuberack.well('C2')   #ENTER LOCATION
    Te123 = tuberack.well('C3')
    Te124 = tuberack.well('C4')
    Te125 = tuberack.well('C5')
    Te126 = tuberack.well('C6')
    Te128 = tuberack.well('D3')
    Te130 = tuberack.well('D4')
    Pt196 = tuberack.well('D5')
    Pt198 = tuberack.well('D6')
    

    # Measurement of distance between meniscus and top of vial in mm. This is the SOURCE_HEADROOM.
    Te122_headroom = 21.96
    Te123_headroom = 22.60      #ENTER DEPTH FROM MINICUS TO TOP OF VIAL 
    Te124_headroom = 24.13
    Te125_headroom = 26.05
    Te126_headroom = 25.94
    Te128_headroom = 21.97
    Te130_headroom = 24.17
    Pt196_headroom = 27.65
    Pt198_headroom = 27.48
    

    #This is the DESTINATION
    TOBis001 = plate_1.well('A1')
    TOBis002 = plate_1.well('B1')
    TOBis003 = plate_1.well('C1')
    TOBis004 = plate_1.well('D1')
    TOBis005 = plate_1.well('E1')
    TOBis006 = plate_1.well('F1')
    TOBis007 = plate_1.well('G1')
    TOBis008 = plate_1.well('H1')
    TOBis009 = plate_1.well('A2')
    TOBis010 = plate_1.well('B2')
    TOBis011 = plate_1.well('C2')
    TOBis012 = plate_1.well('D2')
    TOBis013 = plate_1.well('E2')
    TOBis014 = plate_1.well('F2')
    TOBis015 = plate_1.well('G2')
    TOBis016 = plate_1.well('H2')
    TOBis017 = plate_1.well('A3')
    TOBis018 = plate_1.well('B3')
    TOBis019 = plate_1.well('C3')
    TOBis020 = plate_1.well('D3')
    TOBis021 = plate_1.well('E3')
    TOBis022 = plate_1.well('F3')
    TOBis023 = plate_1.well('G3')
    TOBis024 = plate_1.well('H3')
    TOBis025 = plate_1.well('A4')
    TOBis026 = plate_1.well('B4')
    TOBis027 = plate_1.well('C4')
    TOBis028 = plate_1.well('D4')
    TOBis029 = plate_1.well('E4')
    TOBis030 = plate_1.well('F4')
    TOBis031 = plate_1.well('G4')
    TOBis032 = plate_1.well('H4')
    TOBis033 = plate_1.well('A5')
    TOBis034 = plate_1.well('B5')
    TOBis035 = plate_1.well('C5')
    TOBis036 = plate_1.well('D5')
    TOBis037 = plate_1.well('E5')
    TOBis038 = plate_1.well('F5')
    TOBis039 = plate_1.well('G5')
    TOBis040 = plate_1.well('H5')
    TOBis041 = plate_1.well('A6')
    TOBis042 = plate_1.well('B6')
    TOBis043 = plate_1.well('C6')
    TOBis044 = plate_1.well('D6')
    TOBis045 = plate_1.well('E6')
    TOBis046 = plate_1.well('F6')
    TOBis047 = plate_1.well('G6')
    TOBis048 = plate_1.well('H6')
    TOBis049 = plate_1.well('A7')
    TOBis050 = plate_1.well('B7')
    TOBis051 = plate_1.well('C7')
    TOBis052 = plate_1.well('D7')
    TOBis053 = plate_1.well('E7')
    TOBis054 = plate_1.well('F7')
    TOBis055 = plate_1.well('G7')
    TOBis056 = plate_1.well('H7')
    TOBis057 = plate_1.well('A8')
    TOBis058 = plate_1.well('B8')
    TOBis059 = plate_1.well('C8')
    TOBis060 = plate_1.well('D8')
    TOBis061 = plate_1.well('E8')
    TOBis062 = plate_1.well('F8')
    TOBis063 = plate_1.well('G8')
    TOBis064 = plate_1.well('H8')
    TOBis065 = plate_1.well('A9')
    TOBis066 = plate_1.well('B9')
    TOBis067 = plate_1.well('C9')
    TOBis068 = plate_1.well('D9')
    TOBis069 = plate_1.well('E9')
    TOBis070 = plate_1.well('F9')
    TOBis071 = plate_1.well('G9')
    TOBis072 = plate_1.well('H9')
    TOBis073 = plate_1.well('A10')
    TOBis074 = plate_1.well('B10')
    TOBis075 = plate_1.well('C10')
    TOBis076 = plate_1.well('D10')
    TOBis077 = plate_1.well('E10')
    TOBis078 = plate_1.well('F10')
    TOBis079 = plate_1.well('G10')
    TOBis080 = plate_1.well('H10')
    TOBis081 = plate_1.well('A11')
    TOBis082 = plate_1.well('B11')
    TOBis083 = plate_1.well('C11')
    TOBis084 = plate_1.well('D11')
    TOBis085 = plate_1.well('E11')
    TOBis086 = plate_1.well('F11')
    TOBis087 = plate_1.well('G11')
    TOBis088 = plate_1.well('H11')
    TOBis089 = plate_1.well('A12')
    TOBis090 = plate_1.well('B12')
    TOBis091 = plate_1.well('C12')
    TOBis092 = plate_1.well('D12')
    TOBis093 = plate_1.well('E12')
    TOBis094 = plate_1.well('F12')
    TOBis095 = plate_1.well('G12')
    TOBis096 = plate_1.well('H12')

    TOBis097 = plate_2.well('A1')
    TOBis098 = plate_2.well('B1')
    TOBis099 = plate_2.well('C1')
    TOBis100 = plate_2.well('D1')
    TOBis101 = plate_2.well('E1')
    TOBis102 = plate_2.well('F1')
    TOBis103 = plate_2.well('G1')
    TOBis104 = plate_2.well('H1')
    TOBis105 = plate_2.well('A2')
    TOBis106 = plate_2.well('B2')
    TOBis107 = plate_2.well('C2')
    TOBis108 = plate_2.well('D2')
    TOBis109 = plate_2.well('E2')
    TOBis110 = plate_2.well('F2')
    TOBis111 = plate_2.well('G2')
    TOBis112 = plate_2.well('H2')
    TOBis113 = plate_2.well('A3')
    TOBis114 = plate_2.well('B3')
    TOBis115 = plate_2.well('C3')
    TOBis116 = plate_2.well('D3')
    TOBis117 = plate_2.well('E3')
    TOBis118 = plate_2.well('F3')
    TOBis119 = plate_2.well('G3')
    TOBis120 = plate_2.well('H3')
    TOBis121 = plate_2.well('A4')
    TOBis122 = plate_2.well('B4')
    TOBis123 = plate_2.well('C4')
    TOBis124 = plate_2.well('D4')
    TOBis125 = plate_2.well('E4')
    TOBis126 = plate_2.well('F4')



    DMSO_dict = {TOBis001: 962.3,
    TOBis002: 962.3,
    TOBis003: 959.6,
    TOBis004: 960.2,
    TOBis005: 964.8,
    TOBis006: 964.8,
    TOBis007: 963.8,
    TOBis008: 961.1,
    TOBis009: 961.7,
    TOBis010: 966.3,
    TOBis011: 966.3,
    TOBis012: 961.1,
    TOBis013: 961.7,
    TOBis014: 966.3,
    TOBis015: 966.3,
    TOBis016: 959,
    TOBis017: 963.6,
    TOBis018: 963.6,
    TOBis019: 964.2,
    TOBis020: 964.2,
    TOBis021: 968.8,
    TOBis022: 965,
    TOBis023: 962.3,
    TOBis024: 962.9,
    TOBis025: 967.5,
    TOBis026: 967.5,
    TOBis027: 962.3,
    TOBis028: 962.9,
    TOBis029: 967.5,
    TOBis030: 967.5,
    TOBis031: 960.2,
    TOBis032: 964.8,
    TOBis033: 964.8,
    TOBis034: 965.4,
    TOBis035: 965.4,
    TOBis036: 970,
    TOBis037: 963.8,
    TOBis038: 964.4,
    TOBis039: 969,
    TOBis040: 969,
    TOBis041: 961.7,
    TOBis042: 966.3,
    TOBis043: 966.3,
    TOBis044: 966.9,
    TOBis045: 966.9,
    TOBis046: 971.5,
    TOBis047: 961.7,
    TOBis048: 966.3,
    TOBis049: 966.3,
    TOBis050: 966.9,
    TOBis051: 966.9,
    TOBis052: 971.5,
    TOBis053: 964.2,
    TOBis054: 964.2,
    TOBis055: 968.8,
    TOBis056: 969.4,
    TOBis057: 965.8,
    TOBis058: 963.1,
    TOBis059: 963.7,
    TOBis060: 968.3,
    TOBis061: 968.3,
    TOBis062: 963.1,
    TOBis063: 963.7,
    TOBis064: 968.3,
    TOBis065: 968.3,
    TOBis066: 961,
    TOBis067: 965.6,
    TOBis068: 965.6,
    TOBis069: 966.2,
    TOBis070: 966.2,
    TOBis071: 970.8,
    TOBis072: 964.6,
    TOBis073: 965.2,
    TOBis074: 969.8,
    TOBis075: 969.8,
    TOBis076: 962.5,
    TOBis077: 967.1,
    TOBis078: 967.1,
    TOBis079: 967.7,
    TOBis080: 967.7,
    TOBis081: 972.3,
    TOBis082: 962.5,
    TOBis083: 967.1,
    TOBis084: 967.1,
    TOBis085: 967.7,
    TOBis086: 967.7,
    TOBis087: 972.3,
    TOBis088: 965,
    TOBis089: 965,
    TOBis090: 969.6,
    TOBis091: 970.2,
    TOBis092: 965.8,
    TOBis093: 966.4,
    TOBis094: 971,
    TOBis095: 971,
    TOBis096: 963.7,
    TOBis097: 968.3,
    TOBis098: 968.3,
    TOBis099: 968.9,
    TOBis100: 968.9,
    TOBis101: 973.5,
    TOBis102: 963.7,
    TOBis103: 968.3,
    TOBis104: 968.3,
    TOBis105: 968.9,
    TOBis106: 968.9,
    TOBis107: 973.5,
    TOBis108: 966.2,
    TOBis109: 966.2,
    TOBis110: 970.8,
    TOBis111: 971.4,
    TOBis112: 965.2,
    TOBis113: 969.8,
    TOBis114: 969.8,
    TOBis115: 970.4,
    TOBis116: 970.4,
    TOBis117: 975,
    TOBis118: 967.7,
    TOBis119: 967.7,
    TOBis120: 972.3,
    TOBis121: 972.9,
    TOBis122: 967.7,
    TOBis123: 967.7,
    TOBis124: 972.3,
    TOBis125: 972.9,
    TOBis126: 970.2}

    p1000_single.flow_rate.aspirate = 100
    p1000_single.default_speed = 200
    p1000_single.pick_up_tip()
    for location, volume in DMSO_dict.items():
        p1000_single.aspirate(volume, DMSO_reservoir.well('A1'))
        protocol.delay(2)
        p1000_single.air_gap(2)
        protocol.delay(2)
        p1000_single.dispense(volume+20, location.top(-5))
        protocol.delay(2)
        p1000_single.blow_out(location)
    p1000_single.drop_tip()
    

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
    custom_batch(11, Te122, Te122_headroom, [TOBis001,
    TOBis002,
    TOBis003,
    TOBis004,
    TOBis005,
    TOBis006,
    TOBis007,
    TOBis008,
    TOBis009,
    TOBis010,
    TOBis011,
    TOBis012,
    TOBis013,
    TOBis014,
    TOBis015,
    TOBis016,
    TOBis017,
    TOBis018,
    TOBis019,
    TOBis020,
    TOBis021,
    TOBis022,
    TOBis023,
    TOBis024,
    TOBis025,
    TOBis026,
    TOBis027,
    TOBis028,
    TOBis029,
    TOBis030,
    TOBis031,
    TOBis032,
    TOBis033,
    TOBis034,
    TOBis035,
    TOBis036,
    TOBis037,
    TOBis038,
    TOBis039,
    TOBis040,
    TOBis041,
    TOBis042,
    TOBis043,
    TOBis044,
    TOBis045,
    TOBis046,
    TOBis047,
    TOBis048,
    TOBis049,
    TOBis050,
    TOBis051,
    TOBis052,
    TOBis053,
    TOBis054,
    TOBis055,
    TOBis056], p20_single, mm_lost_per_ul)
    


    #Te-123
    custom_batch(10.2, Te123, Te123_headroom, [TOBis001,
    TOBis002,
    TOBis003,
    TOBis004,
    TOBis005,
    TOBis006,
    TOBis007,
    TOBis008,
    TOBis009,
    TOBis010,
    TOBis011,
    TOBis012,
    TOBis013,
    TOBis014,
    TOBis015,
    TOBis016,
    TOBis017,
    TOBis018,
    TOBis019,
    TOBis020,
    TOBis021,
    TOBis057,
    TOBis058,
    TOBis059,
    TOBis060,
    TOBis061,
    TOBis062,
    TOBis063,
    TOBis064,
    TOBis065,
    TOBis066,
    TOBis067,
    TOBis068,
    TOBis069,
    TOBis070,
    TOBis071,
    TOBis072,
    TOBis073,
    TOBis074,
    TOBis075,
    TOBis076,
    TOBis077,
    TOBis078,
    TOBis079,
    TOBis080,
    TOBis081,
    TOBis082,
    TOBis083,
    TOBis084,
    TOBis085,
    TOBis086,
    TOBis087,
    TOBis088,
    TOBis089,
    TOBis090,
    TOBis091], p20_single, mm_lost_per_ul)

    #Te-124
    custom_batch(9, Te124, Te124_headroom, [TOBis001,
    TOBis002,
    TOBis003,
    TOBis004,
    TOBis005,
    TOBis006,
    TOBis022,
    TOBis023,
    TOBis024,
    TOBis025,
    TOBis026,
    TOBis027,
    TOBis028,
    TOBis029,
    TOBis030,
    TOBis031,
    TOBis032,
    TOBis033,
    TOBis034,
    TOBis035,
    TOBis036,
    TOBis057,
    TOBis058,
    TOBis059,
    TOBis060,
    TOBis061,
    TOBis062,
    TOBis063,
    TOBis064,
    TOBis065,
    TOBis066,
    TOBis067,
    TOBis068,
    TOBis069,
    TOBis070,
    TOBis071,
    TOBis092,
    TOBis093,
    TOBis094,
    TOBis095,
    TOBis096,
    TOBis097,
    TOBis098,
    TOBis099,
    TOBis100,
    TOBis101,
    TOBis102,
    TOBis103,
    TOBis104,
    TOBis105,
    TOBis106,
    TOBis107,
    TOBis108,
    TOBis109,
    TOBis110,
    TOBis111], p20_single, mm_lost_per_ul)

    #Te-125
    custom_batch(7.5, Te125, Te125_headroom, [TOBis001,
    TOBis007,
    TOBis008,
    TOBis009,
    TOBis010,
    TOBis011,
    TOBis022,
    TOBis023,
    TOBis024,
    TOBis025,
    TOBis026,
    TOBis037,
    TOBis038,
    TOBis039,
    TOBis040,
    TOBis041,
    TOBis042,
    TOBis043,
    TOBis044,
    TOBis045,
    TOBis046,
    TOBis057,
    TOBis058,
    TOBis059,
    TOBis060,
    TOBis061,
    TOBis072,
    TOBis073,
    TOBis074,
    TOBis075,
    TOBis076,
    TOBis077,
    TOBis078,
    TOBis079,
    TOBis080,
    TOBis081,
    TOBis092,
    TOBis093,
    TOBis094,
    TOBis095,
    TOBis096,
    TOBis097,
    TOBis098,
    TOBis099,
    TOBis100,
    TOBis101,
    TOBis112,
    TOBis113,
    TOBis114,
    TOBis115,
    TOBis116,
    TOBis117,
    TOBis118,
    TOBis119,
    TOBis120,
    TOBis121], p20_single, mm_lost_per_ul)


    #Te-126
    custom_batch(7.5, Te126, Te126_headroom, [TOBis002,
    TOBis007,
    TOBis012,
    TOBis013,
    TOBis014,
    TOBis015,
    TOBis022,
    TOBis027,
    TOBis028,
    TOBis029,
    TOBis030,
    TOBis037,
    TOBis038,
    TOBis039,
    TOBis040,
    TOBis047,
    TOBis048,
    TOBis049,
    TOBis050,
    TOBis051,
    TOBis052,
    TOBis057,
    TOBis062,
    TOBis063,
    TOBis064,
    TOBis065,
    TOBis072,
    TOBis073,
    TOBis074,
    TOBis075,
    TOBis082,
    TOBis083,
    TOBis084,
    TOBis085,
    TOBis086,
    TOBis087,
    TOBis092,
    TOBis093,
    TOBis094,
    TOBis095,
    TOBis102,
    TOBis103,
    TOBis104,
    TOBis105,
    TOBis106,
    TOBis107,
    TOBis112,
    TOBis113,
    TOBis114,
    TOBis115,
    TOBis116,
    TOBis117,
    TOBis122,
    TOBis123,
    TOBis124,
    TOBis125], p20_single, mm_lost_per_ul)


    #Te-128
    custom_batch(11.2, Te128, Te128_headroom, [TOBis003,
    TOBis008,
    TOBis012,
    TOBis016,
    TOBis017,
    TOBis018,
    TOBis023,
    TOBis027,
    TOBis031,
    TOBis032,
    TOBis033,
    TOBis037,
    TOBis041,
    TOBis042,
    TOBis043,
    TOBis047,
    TOBis048,
    TOBis049,
    TOBis053,
    TOBis054,
    TOBis055,
    TOBis058,
    TOBis062,
    TOBis066,
    TOBis067,
    TOBis068,
    TOBis072,
    TOBis076,
    TOBis077,
    TOBis078,
    TOBis082,
    TOBis083,
    TOBis084,
    TOBis088,
    TOBis089,
    TOBis090,
    TOBis092,
    TOBis096,
    TOBis097,
    TOBis098,
    TOBis102,
    TOBis103,
    TOBis104,
    TOBis108,
    TOBis109,
    TOBis110,
    TOBis112,
    TOBis113,
    TOBis114,
    TOBis118,
    TOBis119,
    TOBis120,
    TOBis122,
    TOBis123,
    TOBis124,
    TOBis126], p20_single, mm_lost_per_ul)

    #Te-130
    custom_batch(9.6, Te130, Te130_headroom, [TOBis004,
    TOBis009,
    TOBis013,
    TOBis016,
    TOBis019,
    TOBis020,
    TOBis024,
    TOBis028,
    TOBis031,
    TOBis034,
    TOBis035,
    TOBis038,
    TOBis041,
    TOBis044,
    TOBis045,
    TOBis047,
    TOBis050,
    TOBis051,
    TOBis053,
    TOBis054,
    TOBis056,
    TOBis059,
    TOBis063,
    TOBis066,
    TOBis069,
    TOBis070,
    TOBis073,
    TOBis076,
    TOBis079,
    TOBis080,
    TOBis082,
    TOBis085,
    TOBis086,
    TOBis088,
    TOBis089,
    TOBis091,
    TOBis093,
    TOBis096,
    TOBis099,
    TOBis100,
    TOBis102,
    TOBis105,
    TOBis106,
    TOBis108,
    TOBis109,
    TOBis111,
    TOBis112,
    TOBis115,
    TOBis116,
    TOBis118,
    TOBis119,
    TOBis121,
    TOBis122,
    TOBis123,
    TOBis125,
    TOBis126], p20_single, mm_lost_per_ul)



    #PT-196
    custom_batch(5, Pt196, Pt196_headroom, [TOBis005,
    TOBis010,
    TOBis014,
    TOBis017,
    TOBis019,
    TOBis021,
    TOBis025,
    TOBis029,
    TOBis032,
    TOBis034,
    TOBis036,
    TOBis039,
    TOBis042,
    TOBis044,
    TOBis046,
    TOBis048,
    TOBis050,
    TOBis052,
    TOBis053,
    TOBis055,
    TOBis056,
    TOBis060,
    TOBis064,
    TOBis067,
    TOBis069,
    TOBis071,
    TOBis074,
    TOBis077,
    TOBis079,
    TOBis081,
    TOBis083,
    TOBis085,
    TOBis087,
    TOBis088,
    TOBis090,
    TOBis091,
    TOBis094,
    TOBis097,
    TOBis099,
    TOBis101,
    TOBis103,
    TOBis105,
    TOBis107,
    TOBis108,
    TOBis110,
    TOBis111,
    TOBis113,
    TOBis115,
    TOBis117,
    TOBis118,
    TOBis120,
    TOBis121,
    TOBis122,
    TOBis124,
    TOBis125,
    TOBis126], p20_single, mm_lost_per_ul)



    #PT-198
    custom_batch(5, Pt198, Pt198_headroom, [TOBis006,
    TOBis011,
    TOBis015,
    TOBis018,
    TOBis020,
    TOBis021,
    TOBis026,
    TOBis030,
    TOBis033,
    TOBis035,
    TOBis036,
    TOBis040,
    TOBis043,
    TOBis045,
    TOBis046,
    TOBis049,
    TOBis051,
    TOBis052,
    TOBis054,
    TOBis055,
    TOBis056,
    TOBis061,
    TOBis065,
    TOBis068,
    TOBis070,
    TOBis071,
    TOBis075,
    TOBis078,
    TOBis080,
    TOBis081,
    TOBis084,
    TOBis086,
    TOBis087,
    TOBis089,
    TOBis090,
    TOBis091,
    TOBis095,
    TOBis098,
    TOBis100,
    TOBis101,
    TOBis104,
    TOBis106,
    TOBis107,
    TOBis109,
    TOBis110,
    TOBis111,
    TOBis114,
    TOBis116,
    TOBis117,
    TOBis119,
    TOBis120,
    TOBis121,
    TOBis123,
    TOBis124,
    TOBis125,
    TOBis126], p20_single, mm_lost_per_ul)
    
