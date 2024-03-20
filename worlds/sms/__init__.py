"""
Archipelago init file for Super Mario Sunshine
"""
from BaseClasses import ItemClassification
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess
from .items import ALL_ITEMS_TABLE, REGULAR_PROGRESSION_ITEMS, TICKET_ITEMS, ALL_PROGRESSION_ITEMS, SmsItem
from .locations import ALL_LOCATIONS_TABLE
from .options import SmsOptions, LevelAccess
from .regions import create_regions


class SmsWebWorld(WebWorld):
    theme = "ocean"


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
    location_name_to_id = ALL_LOCATIONS_TABLE

    def create_regions(self):
        create_regions(self)

    def create_items(self):
        pool = [self.create_item(name) for name in REGULAR_PROGRESSION_ITEMS.keys()]

        # if self.options.level_access == LevelAccess.option_tickets:
            #    pool += [self.create_item(name) for name in TICKET_ITEMS.keys()]

        if self.options.blue_coin_sanity.option_full_shuffle:
            for i in range(0, self.options.blue_coin_maximum):
                pool.append((self.create_item("Blue Coin")))

        # Assume for now that all locations are real
        for i in range(0, len(ALL_LOCATIONS_TABLE) - len(pool)):
            pool.append(self.create_item("Shine Sprite"))

        self.multiworld.itempool += pool

    def create_item(self, name: str):
        if name in ALL_PROGRESSION_ITEMS:
            classification = ItemClassification.progression
        else:
            classification = ItemClassification.filler

        return SmsItem(name, classification, ALL_ITEMS_TABLE[name], self.player)

    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)


def launch_client():
    from .SMSClient import main
    launch_subprocess(main, name="SMS client")


def add_client_to_launcher() -> None:
    version = "0.2.0"
    found = False
    for c in components:
        if c.display_name == "Super Mario Sunshine Client":
            found = True
            if getattr(c, "version", 0) < version:
                c.version = version
                c.func = launch_client
                return
    if not found:
        components.append(Component("Super Mario Sunshine Client", "SMSClient", func=launch_client, file_identifier='SMSClient.py'))


add_client_to_launcher()
