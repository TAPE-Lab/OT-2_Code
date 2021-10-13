from opentrons import protocol_api
from opentrons import types

metadata = {
    'apiLevel': '2.10',
    'author': 'Jahangir.Sufi'}


def distribute_dissociation_solution_01(dissociation_solution_reservoir_source, WellPlate_96_destination, pipette, tiprack):
    pipette.pick_up_tip(tiprack.wells()[0])
    pipette.distribute(150, dissociation_solution_reservoir_source.bottom(2), WellPlate_96_destination, new_tip='never', disposal_volume=0, blow_out=True, blowout_location='source well')  #blowout_location has to be the source well because it can't be the destination well in the distribute function and I don't want it to be the trash bin.
    pipette.distribute(50, dissociation_solution_reservoir_source.bottom(2), WellPlate_96_destination, new_tip='never', disposal_volume=0, blow_out=True, blowout_location='source well')


                                                                                        #** WIDE_BORE_TIP **
def scraping_using_wide_bore_tip(aspiration_sources, pipette):
    center_location = aspiration_sources.bottom(0.5) #diameter of helena well is 6.6 mm
    adjusted_location_01 = center_location.move(types.Point(x=-1.85, y=0))
    adjusted_location_02 = adjusted_location_01.move(types.Point(x=0, y=1.75))
    adjusted_location_03 = adjusted_location_02.move(types.Point(x=1.75, y=1.75))
    adjusted_location_04 = adjusted_location_03.move(types.Point(x=1.75, y=0))
    adjusted_location_05 = adjusted_location_04.move(types.Point(x=1.75, y=-2))
    adjusted_location_06 = adjusted_location_05.move(types.Point(x=0, y=-2.8))
    adjusted_location_07 = adjusted_location_06.move(types.Point(x=-1.85, y=-2.8))
    adjusted_location_08 = adjusted_location_07.move(types.Point(x=-1.85, y=-1.5))

    pipette.move_to(center_location, False, 0)
    pipette.move_to(adjusted_location_01, True, 0, 25)
    pipette.move_to(adjusted_location_02, True, 0, 25)
    pipette.move_to(adjusted_location_03, True, 0, 25)
    pipette.move_to(adjusted_location_04, True, 0, 25)
    pipette.move_to(adjusted_location_05, True, 0, 25)
    pipette.move_to(adjusted_location_06, True, 0, 25)
    pipette.move_to(adjusted_location_07, True, 0, 25)
    pipette.move_to(adjusted_location_08, True, 0, 25)

    pipette.move_to(adjusted_location_04, True, 0, 25)     
    pipette.move_to(adjusted_location_07, True, 0, 25)
    pipette.move_to(adjusted_location_03, True, 0, 25)
    pipette.move_to(adjusted_location_06, True, 0, 25)
    pipette.move_to(adjusted_location_02, True, 0, 25)
    pipette.move_to(adjusted_location_05, True, 0, 25)
    pipette.move_to(adjusted_location_01, True, 0, 25)

    pipette.move_to(adjusted_location_03, True, 0, 25)
    pipette.move_to(adjusted_location_05, True, 0, 25)
    pipette.move_to(adjusted_location_07, True, 0, 25)
    pipette.move_to(adjusted_location_01, True, 0, 25)
    pipette.move_to(adjusted_location_04, True, 0, 25)
    pipette.move_to(adjusted_location_07, True, 0, 25)
    pipette.move_to(adjusted_location_02, True, 0, 25)
    pipette.move_to(adjusted_location_05, True, 0, 25)
    pipette.move_to(adjusted_location_08, True, 0, 25)

    pipette.move_to(adjusted_location_01, True, 0, 25)
    pipette.move_to(adjusted_location_02, True, 0, 25)
    pipette.move_to(adjusted_location_03, True, 0, 25)
    pipette.move_to(adjusted_location_04, True, 0, 25)
    pipette.move_to(adjusted_location_05, True, 0, 25)
    pipette.move_to(adjusted_location_06, True, 0, 25)
    pipette.move_to(adjusted_location_07, True, 0, 25)
    pipette.move_to(adjusted_location_08, True, 0, 25)

    pipette.move_to(aspiration_sources.bottom(), False, 0, 25)

    pipette.touch_tip(aspiration_sources, 0.5, -10.75, 20)
    pipette.touch_tip(aspiration_sources, 0.5, -10.75, 20)

def remove_cells_from_plate_using_wide_bore_tip(aspiration_sources, aspirating_volume, dispensing_destination, dispensing_volume, pipette, wide_bore_tiprack):
    pipette.pick_up_tip(wide_bore_tiprack.wells()[0])
    for source in aspiration_sources:
        scraping_using_wide_bore_tip(source, pipette)
        scraping_using_wide_bore_tip(source, pipette)
        scraping_using_wide_bore_tip(source, pipette)
        scraping_using_wide_bore_tip(source, pipette)
        
        source01 = source.bottom(0.75)                          #Centre
        source02 = source01.move(types.Point(x=-1.9, y=0))      #Left of centre
        source03 = source02.move(types.Point(x=0, y=1.75))      #Top left of centre
        source04 = source03.move(types.Point(x=1.85, y=0))      #Top of centre
        source05 = source04.move(types.Point(x=1.95, y=-0.25))  #Top right of centre
        source06 = source05.move(types.Point(x=0, y=-1.5))      #Right of Centre
        source07 = source06.move(types.Point(x=-1.85, y=-1.75)) #Bottom right of centre
        source08 = source07.move(types.Point(x=-2.25, y=-1.5))  #Bottom left of centre

        pipette.default_speed = 5

        pipette.mix(1, 200, source.bottom(0.75), 2)
        pipette.mix(1, 200, source02, 2)
        pipette.mix(1, 200, source03, 2)
        pipette.mix(1, 200, source04, 2)
        pipette.mix(1, 200, source05, 2)
        pipette.mix(1, 200, source06, 2)
        pipette.mix(1, 200, source07, 2)
        pipette.mix(1, 200, source08, 2)

        pipette.aspirate(aspirating_volume, source02)  
        pipette.aspirate(aspirating_volume, source04)
        pipette.aspirate(aspirating_volume, source05)   
        pipette.move_to(source01, False, 0, 25)  
        pipette.default_speed = 400
        pipette.dispense(dispensing_volume, dispensing_destination)
        pipette.blow_out()

        pipette.aspirate(1, source01)  
        pipette.default_speed = 5
        pipette.aspirate(aspirating_volume, source06)  
        pipette.aspirate(aspirating_volume, source07)  
        pipette.aspirate(aspirating_volume, source08)
        pipette.move_to(source01, False, 0, 25)  
        pipette.default_speed = 400
        pipette.dispense(dispensing_volume, dispensing_destination)
        pipette.blow_out()

    pipette.drop_tip()


                                                                                            #NARROW_BORE
def scraping_using_narrow_bore_tip(aspiration_sources, pipette):
    center_location = aspiration_sources.bottom(0.5) #diameter of helena well is 6.6 mm
    adjusted_location_01 = center_location.move(types.Point(x=-1.85, y=0))
    adjusted_location_02 = adjusted_location_01.move(types.Point(x=0, y=1.75))
    adjusted_location_03 = adjusted_location_02.move(types.Point(x=1.75, y=1.75))
    adjusted_location_04 = adjusted_location_03.move(types.Point(x=1.75, y=0))
    adjusted_location_05 = adjusted_location_04.move(types.Point(x=1.75, y=-2))
    adjusted_location_06 = adjusted_location_05.move(types.Point(x=0, y=-2.8))
    adjusted_location_07 = adjusted_location_06.move(types.Point(x=-1.85, y=-2.8))
    adjusted_location_08 = adjusted_location_07.move(types.Point(x=-1.85, y=-1.5))

    pipette.move_to(center_location, False, 0)
    pipette.move_to(adjusted_location_01, True, 0, 25)
    pipette.move_to(adjusted_location_02, True, 0, 25)
    pipette.move_to(adjusted_location_03, True, 0, 25)
    pipette.move_to(adjusted_location_04, True, 0, 25)
    pipette.move_to(adjusted_location_05, True, 0, 25)
    pipette.move_to(adjusted_location_06, True, 0, 25)
    pipette.move_to(adjusted_location_07, True, 0, 25)
    pipette.move_to(adjusted_location_08, True, 0, 25)

    pipette.move_to(adjusted_location_04, True, 0, 25)     
    pipette.move_to(adjusted_location_07, True, 0, 25)
    pipette.move_to(adjusted_location_03, True, 0, 25)
    pipette.move_to(adjusted_location_06, True, 0, 25)
    pipette.move_to(adjusted_location_02, True, 0, 25)
    pipette.move_to(adjusted_location_05, True, 0, 25)
    pipette.move_to(adjusted_location_01, True, 0, 25)

    pipette.move_to(adjusted_location_03, True, 0, 25)
    pipette.move_to(adjusted_location_05, True, 0, 25)
    pipette.move_to(adjusted_location_07, True, 0, 25)
    pipette.move_to(adjusted_location_01, True, 0, 25)
    pipette.move_to(adjusted_location_04, True, 0, 25)
    pipette.move_to(adjusted_location_07, True, 0, 25)
    pipette.move_to(adjusted_location_02, True, 0, 25)
    pipette.move_to(adjusted_location_05, True, 0, 25)
    pipette.move_to(adjusted_location_08, True, 0, 25)

    pipette.move_to(adjusted_location_01, True, 0, 25)
    pipette.move_to(adjusted_location_02, True, 0, 25)
    pipette.move_to(adjusted_location_03, True, 0, 25)
    pipette.move_to(adjusted_location_04, True, 0, 25)
    pipette.move_to(adjusted_location_05, True, 0, 25)
    pipette.move_to(adjusted_location_06, True, 0, 25)
    pipette.move_to(adjusted_location_07, True, 0, 25)
    pipette.move_to(adjusted_location_08, True, 0, 25)

    pipette.move_to(aspiration_sources.bottom(), False, 0, 25)  

    pipette.touch_tip(aspiration_sources, 0.5, -10.82, 20)
    pipette.touch_tip(aspiration_sources, 0.5, -10.82, 20)

def remove_cells_from_plate_using_narrow_bore_tip(aspiration_sources, aspirating_volume, dispensing_destinations, dispensing_volume, pipette, tiprack):
    for source in aspiration_sources:
        scraping_using_narrow_bore_tip(source, pipette)
        scraping_using_narrow_bore_tip(source, pipette)
        scraping_using_narrow_bore_tip(source, pipette)
        scraping_using_narrow_bore_tip(source, pipette)
        
        source01 = source.bottom(0.75)                          #Centre
        source02 = source01.move(types.Point(x=-1.9, y=0))      #Left of centre
        source03 = source02.move(types.Point(x=0, y=1.75))      #Top left of centre
        source04 = source03.move(types.Point(x=1.85, y=0))      #Top of centre
        source05 = source04.move(types.Point(x=1.95, y=-0.25))  #Top right of centre
        source06 = source05.move(types.Point(x=0, y=-1.5))      #Right of Centre
        source07 = source06.move(types.Point(x=-1.85, y=-1.75)) #Bottom right of centre
        source08 = source07.move(types.Point(x=-2.25, y=-1.5))  #Bottom left of centre


        pipette.default_speed = 5

        pipette.mix(1, 200, source.bottom(0.75), 2)
        pipette.mix(1, 200, source02, 2)
        pipette.mix(1, 200, source03, 2)
        pipette.mix(1, 200, source04, 2)
        pipette.mix(1, 200, source05, 2)
        pipette.mix(1, 200, source06, 2)
        pipette.mix(1, 200, source07, 2)
        pipette.mix(1, 200, source08, 2)

        pipette.aspirate(aspirating_volume, source02)  
        pipette.aspirate(aspirating_volume, source04)
        pipette.aspirate(aspirating_volume, source05)   
        pipette.aspirate(aspirating_volume, source06)  
        pipette.aspirate(aspirating_volume, source07)  
        pipette.aspirate(aspirating_volume, source08)
        pipette.move_to(source01, False, 0, 25)  
        pipette.default_speed = 400
        pipette.dispense(dispensing_volume, dispensing_destinations)
        pipette.blow_out()


        pipette.aspirate(1, source01)  
        pipette.default_speed = 5
        pipette.aspirate(49, source02)
        pipette.aspirate(aspirating_volume, source04)
        pipette.aspirate(aspirating_volume, source05)   
        pipette.aspirate(aspirating_volume, source06)  
        pipette.aspirate(aspirating_volume, source07)  
        pipette.aspirate(aspirating_volume, source08)
        pipette.move_to(source01, False, 0, 25)  
        pipette.default_speed = 400
        pipette.dispense(dispensing_volume, dispensing_destinations)
        pipette.blow_out()




def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 5)
    wide_bore_tiprack = protocol.load_labware('wideborestarlab_96_tiprack_200ul', 11)
    p300_multi_right = protocol.load_instrument('p300_multi', 'right')   
    p300_multi_right.default_speed = 400

    temp_mod_01 = protocol.load_module('temperature module gen2', 1)
    temp_mod_dissociation_solution = temp_mod_01.load_labware('thermoscientific_1_reservoir_300000ul', 1)

    temp_mod_02 = protocol.load_module('temperature module gen2', 3)
    temp_mod_plate_01 = temp_mod_02.load_labware('helenawith3mmaluminiumplate_96_wellplate_400ul', 3)

    temp_mod_03 = protocol.load_module('temperature module gen2', 9)
    temp_mod_collection_reservoir = temp_mod_03.load_labware('thermoscientific_1_reservoir_300000ul', 9)


    plate_01 = [temp_mod_plate_01.wells_by_name()['A1'],
    temp_mod_plate_01.wells_by_name()['A2'],
    temp_mod_plate_01.wells_by_name()['A3'],
    temp_mod_plate_01.wells_by_name()['A4'],
    temp_mod_plate_01.wells_by_name()['A5'],
    temp_mod_plate_01.wells_by_name()['A6'],
    temp_mod_plate_01.wells_by_name()['A7'],
    temp_mod_plate_01.wells_by_name()['A8'],
    temp_mod_plate_01.wells_by_name()['A9'],
    temp_mod_plate_01.wells_by_name()['A10'],
    temp_mod_plate_01.wells_by_name()['A11'],
    temp_mod_plate_01.wells_by_name()['A12']]


    temp_mod_01.set_temperature(4)
    temp_mod_01.temperature
    temp_mod_01.target
    temp_mod_01.status
    temp_mod_02.set_temperature(4)
    temp_mod_02.temperature
    temp_mod_02.target
    temp_mod_02.status
    temp_mod_03.set_temperature(4)
    temp_mod_03.temperature
    temp_mod_03.target
    temp_mod_03.status
    


    distribute_dissociation_solution_01(temp_mod_dissociation_solution.well('A1'), plate_01,  p300_multi_right, tiprack)
    p300_multi_right.return_tip(tiprack)
    remove_cells_from_plate_using_wide_bore_tip(plate_01, 50, temp_mod_collection_reservoir.well('A1'), 200, p300_multi_right, wide_bore_tiprack)

    distribute_dissociation_solution_01(temp_mod_dissociation_solution.well('A1'), plate_01,  p300_multi_right, tiprack)
    remove_cells_from_plate_using_narrow_bore_tip(plate_01, 50, temp_mod_collection_reservoir.well('A1'), 300, p300_multi_right, tiprack)
    p300_multi_right.drop_tip()
    
    p300_multi_right.default_speed = 400
  
    #temp_mod_01.deactivate()
    #temp_mod_02.deactivate()
    #temp_mod_03.deactivate()

