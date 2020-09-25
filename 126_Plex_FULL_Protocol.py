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
    headroom = source_headroom
    
    pipette.pick_up_tip()
    custom_wetting(volume, source, headroom, pipette)
    for destination in destinations_list:
        custom_transfer(volume, source, headroom, destination, pipette)
        headroom += mm_lost_per_ul * volume
    pipette.drop_tip()

    

def run(protocol: protocol_api.ProtocolContext):
    #tiprack is yet to be determined but I'm just using the opentrons tips in this case.
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', 9)      #Need to change the location
    tuberack = protocol.load_labware('adrena_40_wellplate_1500ul', 6)     #Need to change tuberack
    plate_1 = protocol.load_labware('starlab_96_wellplate_1200ul', 3)          #Need to add labware and change location
    plate_2 = protocol.load_labware('starlab_96_wellplate_1200ul', 4)     #Need to add labware and change location
    p50 = protocol.load_instrument('p50_single', 'left', tip_racks=[tiprack])


    #This is the SOURCE
    Te122 = tuberack.well('')   #ENTER LOCATION
    Te123 = tuberack.well('')
    Te124 = tuberack.well('')
    Te125 = tuberack.well('')
    Te126 = tuberack.well('')
    Te128 = tuberack.well('')
    Te130 = tuberack.well('')
    Pt196 = tuberack.well('')
    Pt198 = tuberack.well('')
    

    # Measurement of distance between meniscus and top of vial in mm. This is the SOURCE_HEADROOM.
    Te122_headroom =
    Te123_headroom =       #ENTER DEPTH FROM MINICUS TO TOP OF VIAL 
    Te124_headroom = 
    Te125_headroom = 
    Te126_headroom = 
    Te128_headroom = 
    Te130_headroom =
    Pt196_headroom = 
    Pt198_headroom = 
    

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
    custom_batch(22, Te122, Te122_headroom, [TOBis001,
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
    TOBis056], p50, mm_lost_per_ul)



    #Te-123
    custom_batch(20.4, Te123, Te123_headroom, [TOBis001,
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
    TOBis091], p50, mm_lost_per_ul)

    #Te-124
    custom_batch(18, Te124, Te124_headroom, [TOBis001,
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
    TOBis111], p50, mm_lost_per_ul)

    #Te-125
    custom_batch(15, Te125, Te125_headroom, [TOBis001,
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
    TOBis121], p50, mm_lost_per_ul)


    #Te-126
    custom_batch(15, Te126, Te126_headroom, [TOBis002,
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
    TOBis125], p50, mm_lost_per_ul)


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
    TOBis126], p50, mm_lost_per_ul)

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
    TOBis126], p50, mm_lost_per_ul)



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
    TOBis126], p50, mm_lost_per_ul)



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
    TOBis126], p50, mm_lost_per_ul)


