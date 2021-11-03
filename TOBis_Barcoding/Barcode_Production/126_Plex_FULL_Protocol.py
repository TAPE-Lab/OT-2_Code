from opentrons import protocol_api
import numpy as np

metadata = {
    'apiLevel': '2.10',
    'author': 'Jahangir.Sufi'}
    
def custom_transfer(volume, source, source_headroom, destination, pipette):
    pipette.aspirate(volume, source.top(-source_headroom -5))
    pipette.touch_tip()
    pipette.air_gap(2)
    pipette.dispense(volume+5, destination.top(-2))
    pipette.blow_out()
    pipette.touch_tip(radius=0.15, v_offset=-1, speed=80)
    pipette.touch_tip(radius=0.15, v_offset=-1, speed=80)
    pipette.touch_tip(radius=0.15, v_offset=-1, speed=80)
    pipette.touch_tip(radius=0.15, v_offset=-1, speed=80)
        
def custom_batch(volume, source, source_headroom, destinations_list, pipette, mm_lost_per_ul):
    headroom = source_headroom
    
    pipette.pick_up_tip()
    pipette.mix(10, 20, source, 2)
    for destination in destinations_list:
        custom_transfer(volume, source, headroom, destination, pipette)
        headroom += mm_lost_per_ul * volume
    pipette.drop_tip()



def run(protocol: protocol_api.ProtocolContext):
    tiprack_p20 = protocol.load_labware('opentrons_96_filtertiprack_20ul', 8)
    tiprack_p1000 = protocol.load_labware('opentrons_96_filtertiprack_1000ul', 9)

    p20_single = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_p20])
    p1000_single = protocol.load_instrument('p1000_single_gen2', 'right', tip_racks=[tiprack_p1000])

    plate_1_001_096 = protocol.load_labware('starlab_96_wellplate_1200ul', 2)
    plate_2_097_126 = protocol.load_labware('starlab_96_wellplate_1200ul', 3)

    individual_elements = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 5)
    DMSO_reservoir = protocol.load_labware('thermoscientific_1_reservoir_300000ul', 6)

    
    #This is the SOURCE
    Te122 = individual_elements.well('C2')
    Te123 = individual_elements.well('C3')
    Te124 = individual_elements.well('C4')
    Te125 = individual_elements.well('C5')
    Te126 = individual_elements.well('C6')
    Te128 = individual_elements.well('D3')
    Te130 = individual_elements.well('D4')
    Pt196 = individual_elements.well('D5')
    Pt198 = individual_elements.well('D6')
    

    # Measurement of distance between meniscus and top of vial in mm. This is the SOURCE_HEADROOM.
    Te122_headroom = 17.00
    Te123_headroom = 17.90      #ENTER DEPTH FROM MINICUS TO TOP OF VIAL 
    Te124_headroom = 16.10
    Te125_headroom = 20.00
    Te126_headroom = 20.00
    Te128_headroom = 18.75
    Te130_headroom = 18.75
    Pt196_headroom = 22.00
    Pt198_headroom = 22.00
    

    #This is the DESTINATION
    TOBis001 = plate_1_001_096.well('A1')
    TOBis002 = plate_1_001_096.well('B1')
    TOBis003 = plate_1_001_096.well('C1')
    TOBis004 = plate_1_001_096.well('D1')
    TOBis005 = plate_1_001_096.well('E1')
    TOBis006 = plate_1_001_096.well('F1')
    TOBis007 = plate_1_001_096.well('G1')
    TOBis008 = plate_1_001_096.well('H1')
    TOBis009 = plate_1_001_096.well('A2')
    TOBis010 = plate_1_001_096.well('B2')
    TOBis011 = plate_1_001_096.well('C2')
    TOBis012 = plate_1_001_096.well('D2')
    TOBis013 = plate_1_001_096.well('E2')
    TOBis014 = plate_1_001_096.well('F2')
    TOBis015 = plate_1_001_096.well('G2')
    TOBis016 = plate_1_001_096.well('H2')
    TOBis017 = plate_1_001_096.well('A3')
    TOBis018 = plate_1_001_096.well('B3')
    TOBis019 = plate_1_001_096.well('C3')
    TOBis020 = plate_1_001_096.well('D3')
    TOBis021 = plate_1_001_096.well('E3')
    TOBis022 = plate_1_001_096.well('F3')
    TOBis023 = plate_1_001_096.well('G3')
    TOBis024 = plate_1_001_096.well('H3')
    TOBis025 = plate_1_001_096.well('A4')
    TOBis026 = plate_1_001_096.well('B4')
    TOBis027 = plate_1_001_096.well('C4')
    TOBis028 = plate_1_001_096.well('D4')
    TOBis029 = plate_1_001_096.well('E4')
    TOBis030 = plate_1_001_096.well('F4')
    TOBis031 = plate_1_001_096.well('G4')
    TOBis032 = plate_1_001_096.well('H4')
    TOBis033 = plate_1_001_096.well('A5')
    TOBis034 = plate_1_001_096.well('B5')
    TOBis035 = plate_1_001_096.well('C5')
    TOBis036 = plate_1_001_096.well('D5')
    TOBis037 = plate_1_001_096.well('E5')
    TOBis038 = plate_1_001_096.well('F5')
    TOBis039 = plate_1_001_096.well('G5')
    TOBis040 = plate_1_001_096.well('H5')
    TOBis041 = plate_1_001_096.well('A6')
    TOBis042 = plate_1_001_096.well('B6')
    TOBis043 = plate_1_001_096.well('C6')
    TOBis044 = plate_1_001_096.well('D6')
    TOBis045 = plate_1_001_096.well('E6')
    TOBis046 = plate_1_001_096.well('F6')
    TOBis047 = plate_1_001_096.well('G6')
    TOBis048 = plate_1_001_096.well('H6')
    TOBis049 = plate_1_001_096.well('A7')
    TOBis050 = plate_1_001_096.well('B7')
    TOBis051 = plate_1_001_096.well('C7')
    TOBis052 = plate_1_001_096.well('D7')
    TOBis053 = plate_1_001_096.well('E7')
    TOBis054 = plate_1_001_096.well('F7')
    TOBis055 = plate_1_001_096.well('G7')
    TOBis056 = plate_1_001_096.well('H7')
    TOBis057 = plate_1_001_096.well('A8')
    TOBis058 = plate_1_001_096.well('B8')
    TOBis059 = plate_1_001_096.well('C8')
    TOBis060 = plate_1_001_096.well('D8')
    TOBis061 = plate_1_001_096.well('E8')
    TOBis062 = plate_1_001_096.well('F8')
    TOBis063 = plate_1_001_096.well('G8')
    TOBis064 = plate_1_001_096.well('H8')
    TOBis065 = plate_1_001_096.well('A9')
    TOBis066 = plate_1_001_096.well('B9')
    TOBis067 = plate_1_001_096.well('C9')
    TOBis068 = plate_1_001_096.well('D9')
    TOBis069 = plate_1_001_096.well('E9')
    TOBis070 = plate_1_001_096.well('F9')
    TOBis071 = plate_1_001_096.well('G9')
    TOBis072 = plate_1_001_096.well('H9')
    TOBis073 = plate_1_001_096.well('A10')
    TOBis074 = plate_1_001_096.well('B10')
    TOBis075 = plate_1_001_096.well('C10')
    TOBis076 = plate_1_001_096.well('D10')
    TOBis077 = plate_1_001_096.well('E10')
    TOBis078 = plate_1_001_096.well('F10')
    TOBis079 = plate_1_001_096.well('G10')
    TOBis080 = plate_1_001_096.well('H10')
    TOBis081 = plate_1_001_096.well('A11')
    TOBis082 = plate_1_001_096.well('B11')
    TOBis083 = plate_1_001_096.well('C11')
    TOBis084 = plate_1_001_096.well('D11')
    TOBis085 = plate_1_001_096.well('E11')
    TOBis086 = plate_1_001_096.well('F11')
    TOBis087 = plate_1_001_096.well('G11')
    TOBis088 = plate_1_001_096.well('H11')
    TOBis089 = plate_1_001_096.well('A12')
    TOBis090 = plate_1_001_096.well('B12')
    TOBis091 = plate_1_001_096.well('C12')
    TOBis092 = plate_1_001_096.well('D12')
    TOBis093 = plate_1_001_096.well('E12')
    TOBis094 = plate_1_001_096.well('F12')
    TOBis095 = plate_1_001_096.well('G12')
    TOBis096 = plate_1_001_096.well('H12')

    TOBis097 = plate_2_097_126.well('A1')
    TOBis098 = plate_2_097_126.well('B1')
    TOBis099 = plate_2_097_126.well('C1')
    TOBis100 = plate_2_097_126.well('D1')
    TOBis101 = plate_2_097_126.well('E1')
    TOBis102 = plate_2_097_126.well('F1')
    TOBis103 = plate_2_097_126.well('G1')
    TOBis104 = plate_2_097_126.well('H1')
    TOBis105 = plate_2_097_126.well('A2')
    TOBis106 = plate_2_097_126.well('B2')
    TOBis107 = plate_2_097_126.well('C2')
    TOBis108 = plate_2_097_126.well('D2')
    TOBis109 = plate_2_097_126.well('E2')
    TOBis110 = plate_2_097_126.well('F2')
    TOBis111 = plate_2_097_126.well('G2')
    TOBis112 = plate_2_097_126.well('H2')
    TOBis113 = plate_2_097_126.well('A3')
    TOBis114 = plate_2_097_126.well('B3')
    TOBis115 = plate_2_097_126.well('C3')
    TOBis116 = plate_2_097_126.well('D3')
    TOBis117 = plate_2_097_126.well('E3')
    TOBis118 = plate_2_097_126.well('F3')
    TOBis119 = plate_2_097_126.well('G3')
    TOBis120 = plate_2_097_126.well('H3')
    TOBis121 = plate_2_097_126.well('A4')
    TOBis122 = plate_2_097_126.well('B4')
    TOBis123 = plate_2_097_126.well('C4')
    TOBis124 = plate_2_097_126.well('D4')
    TOBis125 = plate_2_097_126.well('E4')
    TOBis126 = plate_2_097_126.well('F4')



    DMSO_dict = {TOBis001: 932.4,
    TOBis002: 932.4,
    TOBis003: 931.4,
    TOBis004: 931.4,
    TOBis005: 934.9,
    TOBis006: 934.9,
    TOBis007: 935.4,
    TOBis008: 934.4,
    TOBis009: 934.4,
    TOBis010: 937.9,
    TOBis011: 937.9,
    TOBis012: 934.4,
    TOBis013: 934.4,
    TOBis014: 937.9,
    TOBis015: 937.9,
    TOBis016: 933.4,
    TOBis017: 936.9,
    TOBis018: 936.9,
    TOBis019: 936.9,
    TOBis020: 936.9,
    TOBis021: 940.4,
    TOBis022: 934.4,
    TOBis023: 933.4,
    TOBis024: 933.4,
    TOBis025: 936.9,
    TOBis026: 936.9,
    TOBis027: 933.4,
    TOBis028: 933.4,
    TOBis029: 936.9,
    TOBis030: 936.9,
    TOBis031: 932.4,
    TOBis032: 935.9,
    TOBis033: 935.9,
    TOBis034: 935.9,
    TOBis035: 935.9,
    TOBis036: 939.4,
    TOBis037: 936.4,
    TOBis038: 936.4,
    TOBis039: 939.9,
    TOBis040: 939.9,
    TOBis041: 935.4,
    TOBis042: 938.9,
    TOBis043: 938.9,
    TOBis044: 938.9,
    TOBis045: 938.9,
    TOBis046: 942.4,
    TOBis047: 935.4,
    TOBis048: 938.9,
    TOBis049: 938.9,
    TOBis050: 938.9,
    TOBis051: 938.9,
    TOBis052: 942.4,
    TOBis053: 937.9,
    TOBis054: 937.9,
    TOBis055: 941.4,
    TOBis056: 941.4,
    TOBis057: 935.0,
    TOBis058: 934.0,
    TOBis059: 934.0,
    TOBis060: 937.5,
    TOBis061: 937.5,
    TOBis062: 934.0,
    TOBis063: 934.0,
    TOBis064: 937.5,
    TOBis065: 937.5,
    TOBis066: 933.0,
    TOBis067: 936.5,
    TOBis068: 936.5,
    TOBis069: 936.5,
    TOBis070: 936.5,
    TOBis071: 940.0,
    TOBis072: 937.0,
    TOBis073: 937.0,
    TOBis074: 940.5,
    TOBis075: 940.5,
    TOBis076: 936.0,
    TOBis077: 939.5,
    TOBis078: 939.5,
    TOBis079: 939.5,
    TOBis080: 939.5,
    TOBis081: 943.0,
    TOBis082: 936.0,
    TOBis083: 939.5,
    TOBis084: 939.5,
    TOBis085: 939.5,
    TOBis086: 939.5,
    TOBis087: 943.0,
    TOBis088: 938.5,
    TOBis089: 938.5,
    TOBis090: 942.0,
    TOBis091: 942.0,
    TOBis092: 936.0,
    TOBis093: 936.0,
    TOBis094: 939.5,
    TOBis095: 939.5,
    TOBis096: 935.0,
    TOBis097: 938.5,
    TOBis098: 938.5,
    TOBis099: 938.5,
    TOBis100: 938.5,
    TOBis101: 942.0,
    TOBis102: 935.0,
    TOBis103: 938.5,
    TOBis104: 938.5,
    TOBis105: 938.5,
    TOBis106: 938.5,
    TOBis107: 942.0,
    TOBis108: 937.5,
    TOBis109: 937.5,
    TOBis110: 941.0,
    TOBis111: 941.0,
    TOBis112: 938.0,
    TOBis113: 941.5,
    TOBis114: 941.5,
    TOBis115: 941.5,
    TOBis116: 941.5,
    TOBis117: 945.0,
    TOBis118: 940.5,
    TOBis119: 940.5,
    TOBis120: 944.0,
    TOBis121: 944.0,
    TOBis122: 940.5,
    TOBis123: 940.5,
    TOBis124: 944.0,
    TOBis125: 944.0,
    TOBis126: 943.0}

    p1000_single.flow_rate.aspirate = 250
    p1000_single.default_speed = 250
    p1000_single.pick_up_tip()
    p1000_single.mix(2, 1000, DMSO_reservoir.well('A1'))
    for location, volume in DMSO_dict.items():
        p1000_single.aspirate(volume, DMSO_reservoir.well('A1'))
        protocol.delay(1)
        p1000_single.air_gap(5)
        protocol.delay(1)
        p1000_single.dispense(volume+20, location.top(-5))
        protocol.delay(1)
        p1000_single.blow_out(location.top(-2))
    p1000_single.drop_tip()
    




    diameter = 9.9
    disc_area = np.pi * (diameter/2) * (diameter/2)
    mm_lost_per_ul = 1/disc_area
        
    #Te-122 - 1.25 mM Working Concentration
    custom_batch(17.60, Te122, Te122_headroom, [TOBis001,
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
    

    #Te-123 - 1.20 mM Working Concentration
    custom_batch(17.90, Te123, Te123_headroom, [TOBis001,
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

    #Te-124 - 1.00 mM Working Concentration
    custom_batch(18.0, Te124, Te124_headroom, [TOBis001,
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

    #Te-125 - 1.00 mM Working Concentration
    custom_batch(15.0, Te125, Te125_headroom, [TOBis001,
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

    #Te-126 - 1.00 mM Working Concentration
    custom_batch(15.0, Te126, Te126_headroom, [TOBis002,
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

    #Te-128 - 0.70 mM Working Concentration
    custom_batch(16.0, Te128, Te128_headroom, [TOBis003,
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

    #Te-130  - 1.25 mM Working Concentration
    custom_batch(16.0, Te130, Te130_headroom, [TOBis004,
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

    #Pt-196
    custom_batch(12.5, Pt196, Pt196_headroom, [TOBis005,
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

    #Pt-198
    custom_batch(12.5, Pt198, Pt198_headroom, [TOBis006,
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
    
