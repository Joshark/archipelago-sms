"""
Archipelago init file for Super Mario Sunshine
"""
import math
from dataclasses import fields
import os, logging
from typing import Dict, Any, ClassVar
import settings


import Options
from BaseClasses import ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess

from .items import ALL_ITEMS_TABLE, REGULAR_PROGRESSION_ITEMS, ALL_PROGRESSION_ITEMS, TICKET_ITEMS, JUNK_ITEMS, SmsItem
from .options import *
from .regions import create_regions, ALL_REGIONS
from .iso_helper.sms_rom import SMSPlayerContainer
from .sms_regions.sms_region_helper import SmsRegionName, SmsLocation, Requirements, NozzleType, TURSPRAY
from .sms_rules import create_sms_region_and_entrance_rules

logger = logging.getLogger()


def run_client(*args):
    from .SMSClient import main
    launch_subprocess(main, name="SMS Client", args=args)

components.append(
    Component("Super Mario Sunshine Client", func=run_client, component_type=Type.CLIENT,
        file_identifier=SuffixIdentifier(".apsms")))

class SuperMarioSunshineSettings(settings.Group):
    class ISOFile(settings.UserFilePath):
        description = "Super Mario Sunshine (USA) NTSC-U ISO File"
        copy_to = None

    iso_file: ISOFile = ISOFile(ISOFile.copy_to)

class SmsWebWorld(WebWorld):
    theme = "ocean"
    option_groups = [
        Options.OptionGroup("SMS Basic", [
            options.LevelAccess,
            options.StartingNozzle,
            options.EnableCoinShines,
            options.CoronaMountainShines,
            options.BlueCoinSanity,
            options.BlueCoinMaximum,
            options.TradeShineMaximum,
        ])
    ]

    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Super Mario Sunshine software on your computer. This guide covers"
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "sms/en",
        ["Joshark"]
    )

    tutorials = [setup]

def get_location_name_to_id():
    dict_locs: dict[str, int] = {}
    for sms_reg in ALL_REGIONS.values():
        for shine_loc in sms_reg.shines:
            dict_locs.update({f"{sms_reg.name} - {shine_loc.name}": len(dict_locs)+1})
        for blue_loc in sms_reg.blue_coins:
            dict_locs.update({f"{sms_reg.name} - {blue_loc.name}": len(dict_locs)+1})
        for nozz_loc in sms_reg.nozzle_boxes:
            dict_locs.update({f"{sms_reg.name} - {nozz_loc.name}": len(dict_locs)+1})
    return dict_locs

class SmsWorld(World):
    """
    The second Super Mario game to feature 3D gameplay. Coupled with F.L.U.D.D. (a talking water tank that can be used
    as a jetpack), Mario must clean the graffiti off of Delfino Isle and return light to the sky.
    """
    game = "Super Mario Sunshine"
    web = SmsWebWorld()

    data_version = 1

    options_dataclass = SmsOptions
    options: SmsOptions

    item_name_to_id = ALL_ITEMS_TABLE
    location_name_to_id = get_location_name_to_id()

    settings: ClassVar[SuperMarioSunshineSettings]

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def generate_early(self):
        if self.options.starting_nozzle.value == 0:
            self.multiworld.push_precollected(self.create_item("Spray Nozzle"))
        elif self.options.starting_nozzle.value == 1:
            self.multiworld.push_precollected(self.create_item("Hover Nozzle"))

        if self.options.level_access.value == 0 and self.options.corona_mountain_shines.value < 20:
            logger.info(f"Player's Yaml {self.player_name} had vanilla access turned on and had the required shine count"
                " too low. Adjusting their shine count down to 20...")
            self.options.corona_mountain_shines.value = 20
        elif self.options.level_access.value == 1:
            pick = self.random.choice(list(TICKET_ITEMS.keys()))
            tick = str(pick)
            print(tick)
            self.multiworld.push_precollected(self.create_item(tick))

        # If blue coins are turned on in any way, set the max trade amount to be the max blue count required.
        if self.options.blue_coin_sanity.value > 0:
            self.options.trade_shine_maximum.value = int(self.options.blue_coin_maximum.value / 10)

    def create_regions(self):
        create_regions(self)

    def create_items(self):
        # Adds the minimum amount required of shines for Corona Mountain access
        possible_shine_locations: int = len([reg_loc for reg_loc in self.multiworld.get_unfilled_locations(self.player)
            if hasattr(reg_loc, "corona") and not reg_loc.corona])

        start_inv: list[str] = [start_item.name for start_item in self.multiworld.precollected_items[self.player]]

        # Removes any progression item not in the starting items
        pool = [self.create_item(prog_name) for prog_name in REGULAR_PROGRESSION_ITEMS.keys() if not prog_name in start_inv]

        if self.options.level_access.value == 1:
            pool += [self.create_item(tick_name) for tick_name in TICKET_ITEMS.keys() if tick_name not in start_inv]

        if self.options.blue_coin_sanity == "full_shuffle":
            for _ in range(0, self.options.blue_coin_maximum.value):
                pool.append((self.create_item("Blue Coin")))

        max_location_count = int(math.ceil((possible_shine_locations - len(pool)) * 0.95))
        if self.options.corona_mountain_shines.value > max_location_count:
            logger.info(f"Player's Yaml {self.player_name} had shine count higher than maximum locations "
                f"available to them. Adjusting their shine count down to {str(max_location_count)}...")
            self.options.corona_mountain_shines.value = min(self.options.corona_mountain_shines.value, max_location_count)

        for _ in range(0, self.options.corona_mountain_shines.value):
            pool.append(self.create_item("Shine Sprite"))

        # Get the remaining locations that need to be filled, then calculate the max shine filler percentage that can be used
        #   (on super restrictive settings, 90 of 14 would result in 12, causing high generation failures)
        remaining_locs: int = len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)
        max_shine_percentage: int = min(self.options.extra_shines.value, 30 + (10 * int(remaining_locs / 10))) if remaining_locs > 10 else 0
        extra_shines = int(math.floor(remaining_locs * max_shine_percentage * .01))

        for i in range(0, remaining_locs):
            # Adds extra shines to the pool if possible
            if i < extra_shines:
                pool.append(self.create_item("Shine Sprite"))
            else:
                pool.append(self.create_item(self.random.choice(list(JUNK_ITEMS.keys()))))

        self.multiworld.itempool += pool

    def create_item(self, name: str):
        if not name in ALL_ITEMS_TABLE:
            raise Exception(f"Invalid SMS item name: {name}")

        if name in ALL_PROGRESSION_ITEMS:
            if name == "Shine Sprite":
                classification = ItemClassification.progression_deprioritized_skip_balancing
            else:
                classification = ItemClassification.progression
        else:
            classification = ItemClassification.filler

        return SmsItem(name, classification, ALL_ITEMS_TABLE[name], self.player)

    def set_rules(self):
        # Since we potentially update the shine requirement in generate_early to be lower, remake the rule for Corona Mountain.
        """corona_entrance: Entrance = self.get_entrance(f"{SmsRegionName.PLAZA} -> {SmsRegionName.CORONA}")
        set_rule(corona_entrance, (lambda state: Entrance.access_rule(state)))
        interpret_requirements(corona_entrance, ALL_REGIONS[SmsRegionName.CORONA].requirements, self)

        # Similarly, update Delfino Airstrip locations that require an updated Corona Mountain count.
        airstrip_red_coins = self.get_location("Delfino Airstrip - Red Coin Waterworks")
        set_rule(airstrip_red_coins, (lambda state: SmsLocation.access_rule(state)))
        interpret_requirements(corona_entrance, [Requirements([[NozzleType.turbo]], corona=True)], self)
        airstrip_red_coins = self.get_location("Delfino Airstrip - Ice Cube")
        set_rule(airstrip_red_coins, (lambda state: SmsLocation.access_rule(state)))
        interpret_requirements(corona_entrance, [Requirements(TURSPRAY, corona=True)], self)"""
        create_sms_region_and_entrance_rules(self)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "corona_mountain_shines": self.options.corona_mountain_shines.value,
            "blue_coin_sanity": self.options.blue_coin_sanity.value,
            "starting_nozzle": self.options.starting_nozzle.value,
            "ticket_mode": self.options.level_access.value,
            "boathouse_maximum": self.options.trade_shine_maximum.value,
            "coin_shine_enabled": self.options.enable_coin_shines.value,
            "death_link": self.options.death_link.value,
            "seed": self.multiworld.seed
        }

    def generate_output(self, output_directory: str):
        from .SMSClient import CLIENT_VERSION, AP_WORLD_VERSION_NAME

        output_data = {
            "Seed": self.multiworld.seed,
            "Slot": self.player,
            "Name": self.player_name,
            "Options": {},
            AP_WORLD_VERSION_NAME: CLIENT_VERSION
        }

        for field in fields(self.options):
            output_data["Options"][field.name] = getattr(self.options, field.name).value

        patch_path = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}"
            f"{SMSPlayerContainer.patch_file_ending}")
        sms_container = SMSPlayerContainer(output_data, patch_path, self.multiworld.player_name[self.player], self.player)
        sms_container.write()

# def launch_client():
#     from .SMSClient import main
#     launch_subprocess(main, name="SMS client")


# def add_client_to_launcher() -> None:
#     version = "0.2.0"
#     found = False
#     for c in components:
#         if c.display_name == "Super Mario Sunshine Client":
#             found = True
#             if getattr(c, "version", 0) < version:
#                 c.version = version
#                 c.func = launch_client
#                 return
#     if not found:
#         components.append(Component("Super Mario Sunshine Client", "SMSClient",
#                                     func=launch_client))


# add_client_to_launcher()
