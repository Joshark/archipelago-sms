from typing import TYPE_CHECKING

from BaseClasses import CollectionState, Region, ItemClassification
from .items import SmsItem
from .locations import SmsLocation
from .options import LevelAccess
from .static_logic import ALL_REGIONS, SmsRegion, Shine, Requirements, NozzleType

if TYPE_CHECKING:
    from . import SmsWorld


def sms_requirements_satisfied(state: CollectionState, requirements: Requirements, world: "SmsWorld"):
    my_nozzles: NozzleType = NozzleType.spray
    if state.has("Hover Nozzle", world.player):
        my_nozzles |= NozzleType.hover
    if state.has("Rocket Nozzle", world.player):
        my_nozzles |= NozzleType.rocket
    if state.has("Turbo Nozzle", world.player):
        my_nozzles |= NozzleType.turbo

    for req in requirements.nozzles:
        if my_nozzles & req == NozzleType(0):
            return False

    if requirements.shines is not None and not state.has("Shine Sprite", world.player, requirements.shines):
        return False

    if requirements.yoshi and not state.has("Yoshi", world.player):
        return False

    if requirements.corona and not state.has("Shine Sprite", world.player, world.options.corona_mountain_shines.value):
        return False

    return True


def sms_can_get_shine(state: CollectionState, shine: Shine, world: "SmsWorld"):
    return sms_requirements_satisfied(state, shine.requirements, world)


def sms_can_use_entrance(state: CollectionState, region: SmsRegion, world: "SmsWorld"):
    if region.ticketed and world.options.level_access == LevelAccess.option_tickets:
        return state.has(f"{region.name} Ticket", world.player)
    else:
        return sms_requirements_satisfied(state, region.requirements, world)


def make_shine_lambda(shine: Shine, world: "SmsWorld"):
    return lambda state: sms_can_get_shine(state, shine, world)


def make_entrance_lambda(region: SmsRegion, world: "SmsWorld"):
    return lambda state: sms_can_use_entrance(state, region, world)


def create_region(region: SmsRegion, world: "SmsWorld"):
    new_region = Region(region.name, world.player, world.multiworld)
    for shine in region.shines:
        if shine.hundred and not world.options.enable_coin_shines.value:
            continue

        new_location = SmsLocation(world.player, f"{region.name} - {shine.name}", shine.id, new_region)
        new_location.access_rule = make_shine_lambda(shine, world)
        new_region.locations.append(new_location)

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

        regions["Menu"].connect(regions[region.name], None, make_entrance_lambda(region, world))

    world.multiworld.regions += regions.values()
