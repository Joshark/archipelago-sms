from typing import TYPE_CHECKING

from BaseClasses import CollectionState, Region, ItemClassification
from .items import SmsItem
from .locations import SmsLocation
from .static_logic import ALL_REGIONS, SmsRegion, Shine, BlueCoin, OneUp, NozzleBox, Requirements, NozzleType

if TYPE_CHECKING:
    from . import SmsWorld


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
    return lambda state: sms_can_use_entrance(state, region, world)


def create_region(region: SmsRegion, world: "SmsWorld"):
    new_region = Region(region.name, world.player, world.multiworld)
    coin_counter = world.options.blue_coin_maximum.value
    shine_limiter = world.options.trade_shine_maximum.value
    for shine in region.shines:
        if shine.hundred and not world.options.enable_coin_shines.value:
            continue
        if region.trade:
            if world.options.blue_coin_sanity == "no_blue_coins" or coin_counter < 10 or shine_limiter < 1:
                continue
            coin_counter -= 10
            shine_limiter -= 1
        if region.skipped and world.options.starting_nozzle == 2:
            continue
        new_location = SmsLocation(world.player, f"{region.display} - {shine.name}", shine.id, new_region)
        new_location.access_rule = make_shine_lambda(shine, world)
        new_region.locations.append(new_location)
    if world.options.blue_coin_sanity == "full_shuffle":
        for blue_coin in region.blue_coins:
            new_location = SmsLocation(
                world.player, f"{region.display} - {blue_coin.name} Blue Coin", blue_coin.id, new_region)
            new_location.access_rule = make_blue_coin_lambda(blue_coin, world)
            new_region.locations.append(new_location)

    # Adding Nozzle Boxes Locations
    for nozzle_box in region.nozzle_boxes:
        new_location = SmsLocation(world.player, f"{region.display} - {nozzle_box.name}", nozzle_box.id, new_region)
        new_location.access_rule = make_nozzle_box_lambda(nozzle_box, world)
        new_region.locations.append(new_location)

    for one_up in region.one_ups:
        new_location = SmsLocation(world.player, f"{region.display} - {one_up.name}", one_up.id, new_region)

    if region.name == "Corona Mountain":
        new_location = SmsLocation(world.player, "Corona Mountain - Father and Son Shine!", None, new_region)
        new_location.access_rule = lambda state: sms_requirements_satisfied(state, Requirements([NozzleType.rocket]),
                                                                            world)
        new_region.locations.append(new_location)

        event_item = SmsItem("Victory", ItemClassification.progression, None, world.player)
        new_location.place_locked_item(event_item)
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)

    return new_region


def create_regions(world: "SmsWorld"):
    regions = {
        "Menu": Region("Menu", world.player, world.multiworld)
    }

    for region in ALL_REGIONS:
        regions[region.name] = create_region(region, world)
        regions[region.parent_region].connect(regions[region.name], None, make_entrance_lambda(region, world))

    world.multiworld.regions += regions.values()
