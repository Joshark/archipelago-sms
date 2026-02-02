import copy
from typing import TYPE_CHECKING, Callable

from ..generic.Rules import add_rule
from BaseClasses import CollectionState, Entrance, Region

from .sms_regions.sms_region_helper import SmsLocation, SmsRegionName, SmsRegion, Requirements
from .sms_regions.delfino_plaza import DELFINO_PLAZA
from .sms_regions.delfino_airstrip import DELFINO_AIRSTRIP
from .sms_regions.corona_mountain import CORONA_MOUNTAIN
from .sms_regions.bianco_hills import (BIANCO_HILLS_ENTRANCE, BIANCO_HILLS_ONE, BIANCO_HILLS_THREE, BIANCO_HILLS_FOUR,
    BIANCO_HILLS_FIVE, BIANCO_HILLS_SIX, BIANCO_HILLS_SEVEN, BIANCO_HILLS_EIGHT)
from .sms_regions.gelato_beach import (GELATO_BEACH_ENTRANCE, GELATO_BEACH_ONE, GELATO_BEACH_ONE_TWO_FOUR, GELATO_BEACH_SIX,
    GELATO_NOT_THREE, GELATO_BEACH_FIVE_EIGHT, GELATO_BEACH_FOUR_ONLY, GELATO_BEACH_TWO_FOUR_THRU_EIGHT)
from .sms_regions.noki_bay import NOKI_BAY_ENTRANCE, NOKI_BAY_ALL, NOKI_BAY_FOUR_EIGHT, NOKI_BAY_SIX_EIGHT, NOKI_BAY_TWO_FOUR_EIGHT
from .sms_regions.pinna_park import PINNA_PARK_ENTRANCE, PINNA_PARK_ONE, PINNA_PARK_ONE_THREE_FIVE_EIGHT, \
    PINNA_PARK_FIVE_EIGHT, PINNA_PARK_SIX, PINNA_PARK_TWO
from .sms_regions.ricco_harbor import RICCO_HARBOR_ENTRANCE, RICCO_HARBOR_ONE, RICCO_HARBOR_EIGHT, \
    RICCO_HARBOR_FOUR_SEVEN, RICCO_HARBOR_THREE, RICCO_HARBOR_TWO
from .sms_regions.sirena_beach import SIRENA_BEACH_ENTRANCE, SIRENA_BEACH_ONE_SIX, SIRENA_BEACH_TWO_EIGHT, \
    SIRENA_BEACH_FOUR_EIGHT, SIRENA_BEACH_THREE_EIGHT, SIRENA_BEACH_SEVEN_EIGHT, SIRENA_BEACH_FOUR_FIVE, \
    SIRENA_BEACH_FIVE_ONLY, SIRENA_BEACH_SIX_ONLY
from .sms_regions.pianta_village import PIANTA_VILLAGE_EVEN, PIANTA_VILLAGE_ODD, PIANTA_VILLAGE_ENTRANCE, \
    PIANTA_VILLAGE_EIGHT, PIANTA_VILLAGE_SIX, PIANTA_VILLAGE_THREE, PIANTA_VILLAGE_FIVE_ONLY, \
    PIANTA_VILLAGE_FIVE_BEYOND, PIANTA_VILLAGE_ANY

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
    SmsRegionName.GELATO_ENTRANCE: GELATO_BEACH_ENTRANCE,
    SmsRegionName.GELATO_ONE: GELATO_BEACH_ONE,
    SmsRegionName.GELATO_ONE_TWO_FOUR: GELATO_BEACH_ONE_TWO_FOUR,
    SmsRegionName.GELATO_NOT_THREE: GELATO_NOT_THREE,
    SmsRegionName.GELATO_TWO_FOUR_THRU_EIGHT: GELATO_BEACH_TWO_FOUR_THRU_EIGHT,
    SmsRegionName.GELATO_FOUR_ONLY: GELATO_BEACH_FOUR_ONLY,
    SmsRegionName.GELATO_FIVE_EIGHT: GELATO_BEACH_FIVE_EIGHT,
    SmsRegionName.GELATO_SIX: GELATO_BEACH_SIX,
    SmsRegionName.PINNA_ENTRANCE: PINNA_PARK_ENTRANCE,
    SmsRegionName.PINNA_ONE: PINNA_PARK_ONE,
    SmsRegionName.PINNA_ONE_THREE_FIVE_EIGHT: PINNA_PARK_ONE_THREE_FIVE_EIGHT,
    SmsRegionName.PINNA_TWO: PINNA_PARK_TWO,
    SmsRegionName.PINNA_FIVE_EIGHT: PINNA_PARK_FIVE_EIGHT,
    SmsRegionName.PINNA_SIX: PINNA_PARK_SIX,
    SmsRegionName.NOKI_ENTRANCE: NOKI_BAY_ENTRANCE,
    SmsRegionName.NOKI_ALL: NOKI_BAY_ALL,
    SmsRegionName.NOKI_TWO_FOUR_EIGHT: NOKI_BAY_TWO_FOUR_EIGHT,
    SmsRegionName.NOKI_FOUR_EIGHT: NOKI_BAY_FOUR_EIGHT,
    SmsRegionName.NOKI_SIX_EIGHT: NOKI_BAY_SIX_EIGHT,
    SmsRegionName.SIRENA_ENTRANCE: SIRENA_BEACH_ENTRANCE,
    SmsRegionName.SIRENA_ONE_SIX: SIRENA_BEACH_ONE_SIX,
    SmsRegionName.SIRENA_TWO_EIGHT: SIRENA_BEACH_TWO_EIGHT,
    SmsRegionName.SIRENA_THREE_EIGHT: SIRENA_BEACH_THREE_EIGHT,
    SmsRegionName.SIRENA_FOUR_FIVE: SIRENA_BEACH_FOUR_FIVE,
    SmsRegionName.SIRENA_FOUR_EIGHT: SIRENA_BEACH_FOUR_EIGHT,
    SmsRegionName.SIRENA_FIVE_ONLY: SIRENA_BEACH_FIVE_ONLY,
    SmsRegionName.SIRENA_SIX_ONLY: SIRENA_BEACH_SIX_ONLY,
    SmsRegionName.SIRENA_SEVEN_EIGHT: SIRENA_BEACH_SEVEN_EIGHT,
    SmsRegionName.PIANTA_ENTRANCE: PIANTA_VILLAGE_ENTRANCE,
    SmsRegionName.PIANTA_ANY: PIANTA_VILLAGE_ANY,
    SmsRegionName.PIANTA_ODD: PIANTA_VILLAGE_ODD,
    SmsRegionName.PIANTA_EVEN: PIANTA_VILLAGE_EVEN,
    SmsRegionName.PIANTA_THREE: PIANTA_VILLAGE_THREE,
    SmsRegionName.PIANTA_FIVE_ONLY: PIANTA_VILLAGE_FIVE_ONLY,
    SmsRegionName.PIANTA_FIVE_BEYOND: PIANTA_VILLAGE_FIVE_BEYOND,
    SmsRegionName.PIANTA_SIX: PIANTA_VILLAGE_SIX,
    SmsRegionName.PIANTA_EIGHT: PIANTA_VILLAGE_EIGHT,

    SmsRegionName.CORONA: CORONA_MOUNTAIN
}


def interpret_requirements(spot: Entrance | SmsLocation, requirement_set: list[Requirements], world: "SmsWorld") -> None:
    """Correctly applies and interprets requirements for a given entrance/location."""
    import inspect
    # If a region/location does not have any items required, make the section(s) return no logic.
    if requirement_set is None or len(requirement_set) < 1:
        return

    # Otherwise, if a region/location DOES have items required, make the section(s) return list of logic.
    skip_forward_locs: bool = world.options.starting_nozzle.value == 2 or world.options.level_access.value == 1
    any_skip_locs: bool = any([reqs for reqs in requirement_set if reqs.skip_forward])
    for single_req in requirement_set:
        # If entry is set to ticket mode or fludless and this location is not set to skip forward
        if (skip_forward_locs and any_skip_locs) and not single_req.skip_forward:
                continue

        # Else if entry is NOT set to ticket mode or fludless and this location is set to skip forward
        elif not (skip_forward_locs and any_skip_locs) and single_req.skip_forward:
            continue

        req_rules: list[Callable[[CollectionState], bool]] = []
        nozzle_rules: list[Callable[[CollectionState], bool]] = []

        if single_req.nozzles:
            for nozzle_req in single_req.nozzles:
                nozzle_rules.append(lambda state, item_set=tuple(nozzle_req): state.has_all(item_set, world.player))

            req_rules.append(lambda state, nozz_rules=tuple(nozzle_rules): any(nozz_req(state) for nozz_req in nozz_rules))

        if single_req.blue_coins:
            req_rules.append(lambda state, coin_count=single_req.blue_coins, item_name="Blue Coin": (
                state.has(item_name, world.player, coin_count)))


        if single_req.location:
            req_rules.append(lambda state, loc_name=single_req.location: state.can_reach_location(loc_name, world.player))
            if isinstance(spot, Entrance):
                #  We use this to explicitly tell the generator that, when a given region becomes accessible,
                #   it is necessary to re-check a specific entrance, as we determine if a user has access to a region if they
                #   complete previous stars/regions.
                world.multiworld.register_indirect_condition(spot.parent_region, spot)

        if single_req.corona:
            req_rules.append(lambda state, item_name="Shine Sprite",
                shine_count=world.options.corona_mountain_shines.value: (state.has(item_name, world.player, shine_count)))

        if spot.access_rule is SmsLocation.access_rule or spot.access_rule is Entrance.access_rule:
            add_rule(spot, (lambda state, all_rules=tuple(req_rules): all(req_rule(state) for req_rule in all_rules)))
        else:
            add_rule(spot, (lambda state, all_rules=tuple(req_rules): all(req_rule(state) for req_rule in req_rules)), combine="or")
    return


def create_region(region: SmsRegion, world: "SmsWorld"):
    #coin_counter = world.options.blue_coin_maximum.value
    #shine_limiter = world.options.trade_shine_maximum.value
    curr_region = Region(region.name, world.player, world.multiworld)
    entrance_reqs: list[Requirements] = copy.deepcopy(region.requirements)
    if region.name == "Menu":
        return curr_region
    elif region.name == SmsRegionName.PLAZA and (world.options.starting_nozzle.value == 2 or
        world.options.level_access.value == 1):
        entrance_reqs = []

    # Add Entrance Logic to lock the region until you properly have access.
    parent_region: Region = world.get_region(region.parent_region)
    new_entrance: Entrance = parent_region.connect(curr_region)
    interpret_requirements(new_entrance, entrance_reqs, world)
    if world.options.level_access.value == 1 and region.ticketed:
        add_rule(new_entrance, (lambda state, ticket_str=region.ticketed:
            state.has(ticket_str, world.player)), combine="and")

    if world.options.trade_shine_maximum.value == 0 and region.trade:
        return curr_region

    for shine in region.shines:
        # Ignore any 100 Coin shinies if not enabled.
        if shine.hundred and not world.options.enable_coin_shines.value == 1:
            continue
        elif region.name == SmsRegionName.AIRSTRIP:
            # If User chose to be fluddless, don't create the Dilemma shine.
            if world.options.starting_nozzle.value == 2 and shine.name == "Delfino Airstrip Dilemma":
                continue

        shine_loc: SmsLocation = SmsLocation(world, f"{curr_region.name} - {shine.name}", curr_region)
        interpret_requirements(shine_loc, shine.requirements, world)
        curr_region.locations.append(shine_loc)

    for blue_coin in region.blue_coins:
        blue_loc: SmsLocation = SmsLocation(world, f"{curr_region.name} - {blue_coin.name}", curr_region)
        interpret_requirements(blue_loc, blue_coin.requirements, world)
        if world.options.blue_coin_sanity.value != 1:
            curr_region.add_event(f"{curr_region.name} - {blue_coin.name}", "Blue Coin",
                (lambda state: blue_loc.access_rule(state)))
        else:
            curr_region.locations.append(blue_loc)

    for nozzle_box in region.nozzle_boxes:
        nozzle_loc: SmsLocation = SmsLocation(world, f"{curr_region.name} - {nozzle_box.name}", curr_region)
        interpret_requirements(nozzle_loc, nozzle_box.requirements, world)
        curr_region.locations.append(nozzle_loc)

    return curr_region


def create_regions(world: "SmsWorld"):
    for region_name, region_data in ALL_REGIONS.items():
        world.multiworld.regions.append(create_region(region_data, world))

    corona_region: Region = world.get_region(SmsRegionName.CORONA)
    corona_region.add_event(f"{SmsRegionName.CORONA} - Father and Son Shine!", "Victory")