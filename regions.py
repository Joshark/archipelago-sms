from typing import TYPE_CHECKING, Callable

from BaseClasses import CollectionState, Entrance, Region, Item, Location
from .sms_regions.ricco_harbor import RICCO_HARBOR_ENTRANCE, RICCO_HARBOR_ONE, RICCO_HARBOR_EIGHT, \
    RICCO_HARBOR_FOUR_SEVEN, RICCO_HARBOR_THREE, RICCO_HARBOR_TWO
from .sms_regions.sms_region_helper import SmsLocation, SmsRegionName, SmsRegion, Requirements
from .sms_regions.delfino_plaza import DELFINO_PLAZA
from .sms_regions.delfino_airstrip import DELFINO_AIRSTRIP
from .sms_regions.corona_mountain import CORONA_MOUNTAIN
from .sms_regions.bianco_hills import (BIANCO_HILLS_ENTRANCE, BIANCO_HILLS_ONE, BIANCO_HILLS_THREE, BIANCO_HILLS_FOUR,
    BIANCO_HILLS_FIVE, BIANCO_HILLS_SIX, BIANCO_HILLS_SEVEN, BIANCO_HILLS_EIGHT)

from ..generic.Rules import add_rule

if TYPE_CHECKING:
    from . import SmsWorld


ALL_REGIONS: dict[str, SmsRegion] = {
    "Menu": SmsRegion("Menu"),
    SmsRegionName.AIRSTRIP: DELFINO_AIRSTRIP,
    SmsRegionName.PLAZA: DELFINO_PLAZA,
    SmsRegionName.BIANCO_ENTRANCE: BIANCO_HILLS_ENTRANCE,
    SmsRegionName.BIANCO_ONE: BIANCO_HILLS_ONE,
    SmsRegionName.BIANCO_THREE: BIANCO_HILLS_THREE,
    SmsRegionName.BIANCO_FOUR: BIANCO_HILLS_FOUR,
    SmsRegionName.BIANCO_FIVE: BIANCO_HILLS_FIVE,
    SmsRegionName.BIANCO_SIX: BIANCO_HILLS_SIX,
    SmsRegionName.BIANCO_SEVEN: BIANCO_HILLS_SEVEN,
    SmsRegionName.BIANCO_EIGHT: BIANCO_HILLS_EIGHT,
    SmsRegionName.RICCO_ENTRANCE: RICCO_HARBOR_ENTRANCE,
    SmsRegionName.RICCO_ONE: RICCO_HARBOR_ONE,
    SmsRegionName.RICCO_TWO: RICCO_HARBOR_TWO,
    SmsRegionName.RICCO_THREE: RICCO_HARBOR_THREE,
    SmsRegionName.RICCO_FOUR_SEVEN: RICCO_HARBOR_FOUR_SEVEN,
    SmsRegionName.RICCO_EIGHT: RICCO_HARBOR_EIGHT,

    SmsRegionName.CORONA: CORONA_MOUNTAIN
}

"""
def sms_requirements_satisfied(state: CollectionState, requirements: Requirements, world: "SmsWorld"):
    if requirements.skip_into and (world.options.starting_nozzle == 2 or world.options.level_access == 1):
        return True

    my_nozzles: NozzleType = NozzleType.none
    if state.has("Spray Nozzle", world.player):
        my_nozzles |= NozzleType.spray
        my_nozzles |= NozzleType.splasher
    if state.has("Hover Nozzle", world.player):
        my_nozzles |= NozzleType.hover
        my_nozzles |= NozzleType.splasher
    if state.has("Rocket Nozzle", world.player):
        my_nozzles |= NozzleType.rocket
    if state.has("Turbo Nozzle", world.player):
        my_nozzles |= NozzleType.turbo
    if state.has("Yoshi", world.player):
        my_nozzles |= NozzleType.yoshi

    for req in requirements.nozzles:
        if my_nozzles & req == NozzleType(0):
            return False

    if requirements.shines is not None and not state.has("Shine Sprite", world.player, requirements.shines):
        return False

    if requirements.blues is not None and not state.has("Blue Coin", world.player, requirements.blues):
        return False

    if requirements.corona and not state.has("Shine Sprite", world.player, world.options.corona_mountain_shines.value):
        return False

    if requirements.location != "" and not state.can_reach(requirements.location, "Location", world.player):
        return False

    return True


def sms_can_get_shine(state: CollectionState, shine: Shine, world: "SmsWorld"):
    return sms_requirements_satisfied(state, shine.requirements, world)

def sms_can_get_blue_coin(state: CollectionState, blue_coin: BlueCoin, world: "SmsWorld"):
    return sms_requirements_satisfied(state, blue_coin.requirements, world)

def sms_can_get_one_up(state: CollectionState, one_up: OneUp, world: "SmsWorld"):
    return sms_requirements_satisfied(state, one_up.requirements, world)

def sms_can_get_nozzle_box(state: CollectionState, nozzle_box: NozzleBox, world: "SmsWorld"):
    return sms_requirements_satisfied(state, nozzle_box.requirements, world)

def sms_can_use_entrance(state: CollectionState, region: SmsRegion, world: "SmsWorld"):
    if region.ticketed and world.options.level_access == 1:
        return state.has(region.ticketed, world.player)
    else:
        return sms_requirements_satisfied(state, region.requirements, world)


def make_shine_lambda(shine: Shine, world: "SmsWorld"):
    return lambda state: sms_can_get_shine(state, shine, world)

def make_blue_coin_lambda(blue_coin: BlueCoin, world: "SmsWorld"):
    return lambda state: sms_can_get_blue_coin(state, blue_coin, world)

def make_one_up_lambda(one_up: OneUp, world: "SmsWorld"):
    return lambda state: sms_can_get_one_up(state, one_up, world)

def make_nozzle_box_lambda(nozzle_box: NozzleBox, world: "SmsWorld"):
    return lambda state: sms_can_get_nozzle_box(state, nozzle_box, world)

def make_entrance_lambda(region: SmsRegion, world: "SmsWorld"):
    return lambda state: sms_can_use_entrance(state, region, world)"""


def interpret_requirements(spot: Entrance | SmsLocation, requirement_set: list[Requirements], world: "SmsWorld") -> \
    (Callable[[CollectionState], bool]):
    # If a region/location does not have any items required, make the section(s) return no logic.
    if requirement_set is None or len(requirement_set) < 1:
        return spot.access_rule

    # Otherwise, if a region/location DOES have items required, make the section(s) return list of logic.
    skip_forward_locs: bool = world.options.starting_nozzle.value == 2 or world.options.level_access.value == 1
    any_skip_locs: bool = any([reqs for reqs in requirement_set if reqs.skip_forward])
    for single_req in requirement_set:
        # If entry is set to ticket mode or fludless and this location is not set to skip forward
        if skip_forward_locs and any_skip_locs and not single_req.skip_forward:
                continue

        # Else if entry is NOT set to ticket mode or fludless and this location is set to skip forward
        elif not (skip_forward_locs and any_skip_locs) and single_req.skip_forward:
            continue

        req_rule = None
        nozzle_rule = None

        if single_req.nozzles:
            for nozzle_req in single_req.nozzles:
                if nozzle_rule is None:
                    nozzle_rule = lambda state, item_set=tuple(nozzle_req): state.has_all(item_set, world.player)
                else:
                    nozzle_rule = nozzle_rule or (lambda state, item_set=tuple(nozzle_req): state.has_all(item_set, world.player))

        if nozzle_rule:
            req_rule = nozzle_rule

        if single_req.blue_coins:
            blue_rule = lambda state, coin_count=single_req.blue_coins, item_name="Blue Coin": (
                state.has(item_name, world.player, coin_count))
            if req_rule:
                req_rule = req_rule and blue_rule
            else:
                req_rule = blue_rule

        if single_req.location:
            location_rule = lambda state, loc_name=single_req.location: state.can_reach_location(loc_name, world.player)
            if req_rule:
                req_rule = req_rule and location_rule
            else:
                req_rule = location_rule

            if isinstance(spot, Entrance):
                #  We use this to explicitly tell the generator that, when a given region becomes accessible,
                #   it is necessary to re-check a specific entrance, as we determine if a user has access to a region if they
                #   complete previous stars/regions.
                world.multiworld.register_indirect_condition(spot.parent_region, spot)

        if single_req.corona:
            corona_rule = lambda state, item_name="Shine Sprite", shine_count=world.options.corona_mountain_shines.value: (
                state.has(item_name, world.player, shine_count))
            if req_rule:
                req_rule = req_rule and corona_rule
            else:
                req_rule = corona_rule

        add_rule(spot, req_rule, combine="or")
    return spot.access_rule


def create_region(region: SmsRegion, world: "SmsWorld"):
    #coin_counter = world.options.blue_coin_maximum.value
    #shine_limiter = world.options.trade_shine_maximum.value
    curr_region = Region(region.name, world.player, world.multiworld)
    if region.name == "Menu":
        return curr_region

    # Add Entrance Logic to lock the region until you properly have access.
    parent_region: Region = world.get_region(region.parent_region)
    new_entrance: Entrance = parent_region.connect(curr_region)
    new_entrance.access_rule = interpret_requirements(new_entrance, region.requirements, world)
    if world.options.level_access.value == 1:
        add_rule(new_entrance, (lambda state, ticket_str=region.ticketed:
            state.has(ticket_str, world.player)), combine="and")

    if world.options.trade_shine_maximum.value == 0 and region.trade:
        return curr_region

    for shine in region.shines:
        # Ignore any 100 Coin shinies if not enabled.
        if shine.hundred and not world.options.enable_coin_shines.value == 1:
            continue

        # TODO add Airstrip Dilemma to be ignored when skip_forward is true.
        shine_loc: SmsLocation = SmsLocation(world.player, f"{curr_region.name} - {shine.name}", curr_region)
        shine_loc.access_rule = interpret_requirements(shine_loc, shine.requirements, world)
        curr_region.locations.append(shine_loc)

    for blue_coin in region.blue_coins:
        blue_loc: SmsLocation = SmsLocation(world.player, f"{curr_region.name} - {blue_coin.name}", curr_region)
        blue_loc.access_rule = interpret_requirements(blue_loc, blue_coin.requirements, world)
        if world.options.blue_coin_sanity.value != 1:
            curr_region.add_event(f"{curr_region.name} - {blue_coin.name}", "Blue Coin",
                blue_loc.access_rule, Location, Item)
        else:
            curr_region.locations.append(blue_loc)

    for nozzle_box in region.nozzle_boxes:
        nozzle_loc: SmsLocation = SmsLocation(world.player, f"{curr_region.name} - {nozzle_box.name}", curr_region)
        nozzle_loc.access_rule = interpret_requirements(nozzle_loc, nozzle_box.requirements, world)
        curr_region.locations.append(nozzle_loc)

    return curr_region


def create_regions(world: "SmsWorld"):
    for region_name, region_data in ALL_REGIONS.items():
        if world.options.starting_nozzle.value == 2: # User chose to be fluddless
            if region_name == SmsRegionName.AIRSTRIP:
                continue
            elif region_name == SmsRegionName.PLAZA:
                region_name.parent_region = "Menu"
                region_name.requirements = None
        world.multiworld.regions.append(create_region(region_data, world))
