from typing import TYPE_CHECKING, Callable, Optional

from BaseClasses import Entrance, CollectionState
from .sms_regions.sms_region_helper import SmsLocation, Requirements, SmsRegionName
from ..generic.Rules import set_rule, add_rule, add_item_rule

if TYPE_CHECKING:
    from . import SmsWorld


def interpret_requirements(spot: Entrance | SmsLocation, requirement_set: list[Requirements], world: "SmsWorld",
    ticket_mode: Optional[str] = None) -> None:
    """Correctly applies and interprets custom requirements namedtuple for a given entrance/location."""
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

        if single_req.nozzles:
            # Requires one or more sets of at least 1 Nozzle to access.
            default_rule: Callable[[CollectionState], bool] = lambda state: True
            nozz_rule: Callable[[CollectionState], bool] = default_rule

            for nozzle_req in single_req.nozzles:
                if nozz_rule is default_rule:
                    nozz_rule = lambda state, item_set=tuple(nozzle_req): state.has_all(item_set, world.player)
                else:
                    nozz_rule = lambda state, item_set=tuple(nozzle_req), current_rule=nozz_rule: \
                        current_rule(state) or state.has_all(item_set, world.player)
            req_rules.append(lambda state: nozz_rule(state))

        if single_req.shines:
            # Requires X amount of shine sprites to access
            req_rules.append(lambda state, shine_req_count=single_req.shines:
                state.has("Shine Sprite", world.player, shine_req_count))

        if single_req.blue_coins:
            # Requires X amount of blue coins (event item or actual)
            req_rules.append(lambda state, coin_count=single_req.blue_coins: (
                state.has("Blue Coin", world.player, coin_count)))

        if single_req.location:
            req_rules.append(lambda state, loc_name=single_req.location: state.can_reach_location(loc_name, world.player))
            if isinstance(spot, Entrance):
                #  We use this to explicitly tell the generator that, when a given region becomes accessible,
                #   it is necessary to re-check a specific entrance, as we determine if a user has access to a region if they
                #   complete previous stars/regions.
                world.multiworld.register_indirect_condition(world.get_location(single_req.location).parent_region, spot)

        if single_req.corona or (hasattr(spot, "corona") and spot.corona):
            # Player requires all shine sprites that are required to reach corona mountain as well.
            req_rules.append(lambda state, shine_count=world.options.corona_mountain_shines.value:
                state.has("Shine Sprite", world.player, shine_count))

        # If no requirement rules are found, don't set any rules and continue
        if not req_rules:
            continue

        if spot.access_rule is SmsLocation.access_rule or spot.access_rule is Entrance.access_rule:
            set_rule(spot, (lambda state, all_rules=tuple(req_rules): all(req_rule(state) for req_rule in all_rules)))
        else:
            if isinstance(spot, SmsLocation):
                add_rule(spot, (lambda state, all_rules=tuple(req_rules): all(req_rule(state) for req_rule in req_rules)), combine="or")
            else:
                add_rule(spot, (lambda state, all_rules=tuple(req_rules): all(req_rule(state) for req_rule in req_rules)))
    return


def create_sms_region_and_entrance_rules(world: "SmsWorld"):
    for sms_reg in world.get_regions():
        if sms_reg.entrances:
            # Add the entrance rule for all entrances in the region based on the Requirements NamedTuple defined.
            for sms_entrance in sms_reg.entrances:
                if hasattr(sms_entrance, "requirements"):
                    interpret_requirements(sms_entrance, sms_entrance.requirements, world)

            # Add the location rules within this region.
            for sms_loc in sms_reg.locations:
                # Skip any event based locations that do not have this attribute
                if hasattr(sms_loc, "loc_reqs"):
                    interpret_requirements(sms_loc, sms_loc.loc_reqs, world)

                # A Region cannot have its own ticket item in ticket mode, so prevent that.
                if hasattr(sms_reg, "ticket_str") or any([hasattr(entr_reg.parent_region, "ticket_str") for entr_reg
                    in sms_reg.entrances]):
                    reg_ticket: str = sms_reg.ticket_str if hasattr(sms_reg, "ticket_str") else \
                        [entr_reg.parent_region.ticket_str for entr_reg in sms_reg.entrances if
                        hasattr(entr_reg.parent_region, "ticket_str")][0]
                    add_item_rule(sms_loc, (lambda item, reg_tick=reg_ticket: item.name != reg_tick))