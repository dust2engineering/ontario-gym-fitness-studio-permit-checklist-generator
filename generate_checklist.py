#!/usr/bin/env python3
"""Ontario Gym and Fitness Studio Permit Checklist Generator - by Dust 2 Engineering Inc., Mississauga, Ontario.
Preliminary information only. Not engineering advice and not a code review.
Verify every item with your designer and the local building department.
"""
import argparse, pathlib
CONFIG = {'title': 'Ontario Gym and Fitness Studio Permit Checklist Generator', 'tagline': 'Ontario Gym and Fitness Studio Permit Checklist Generator by Dust 2 Engineering Inc.', 'unit_label': 'Design occupant load (members + staff)', 'flags': [{'arg': 'showers-change-rooms', 'label': 'Showers and change rooms (new plumbing)'}, {'arg': 'sauna-steam', 'label': 'Sauna or steam room'}, {'arg': 'structural-changes', 'label': 'Structural changes, or heavy free weights on an upper floor'}], 'sections': [{'title': '1. Application basics (always required)', 'items': ['Municipal building permit application form, completed and signed by the owner or authorized agent', 'Schedule 1: Designer Information form for each qualified designer on the project', 'Owner authorization if the applicant is not the property owner, plus the lease for a tenant fit-out if the city asks for it']}, {'title': '2. Architectural drawings', 'items': ['Floor plan showing the equipment layout, training zones, change rooms, washrooms and offices', 'Occupant load calculation on the plan: exercise areas carry a high occupant load, which drives exit widths and washroom counts', 'Barrier-free entrance, path of travel and barrier-free washroom where required', 'Exit signs, emergency lighting and fire separations from neighbouring units shown on plan', 'Floor finishes schedule: resilient flooring in training areas, waterproof finishes in wet areas', 'Sign permit is separate from the building permit - apply for it separately']}, {'title': '3. Ventilation and HVAC', 'items': ['HVAC drawings: heating, cooling and ventilation sized for exercise areas, which need much more fresh air than office space', 'Humidity control for showers and high-occupancy training areas', 'Washroom and change room exhaust shown with equipment schedules']}, {'title': 'Showers and change rooms', 'when': 'showers-change-rooms', 'items': ['Plumbing drawings: showers, washroom fixtures counted from the occupant load, floor drains in change rooms and shower areas', 'Waterproofing and sloped floors in shower areas shown in the details', 'Barrier-free shower and barrier-free washroom where required', 'Backflow preventer where required, and hot water capacity for peak shower demand']}, {'title': 'Sauna or steam room', 'when': 'sauna-steam', 'items': ['Electrical drawings: dedicated circuits and loads for sauna heaters or the steam generator', 'Steam generator plumbing, drain and water supply shown on the plumbing drawings', 'Heat- and moisture-rated finishes and a timer control outside the room', 'Ventilation for the sauna / steam area shown on the HVAC drawings']}, {'title': '4. Plumbing and electrical', 'items': ['Plumbing drawings: washrooms, drinking fountain or bottle filler, mop sink and hot water supply', 'Electrical drawings: panels and receptacles for rows of cardio equipment, lighting and emergency lighting', 'Confirm the existing electrical service can take the added equipment and HVAC load']}, {'title': 'Structural drawings', 'when': 'structural-changes', 'items': ['Structural review of the floor for free-weight and deadlift areas and heavy racks - critical on suspended slabs and upper floors, stamped by an Ontario P.Eng.', 'Vibration and impact from dropped weights considered where units sit below or beside the gym']}, {'title': '5. Other approvals (not part of the building permit)', 'items': ['Business licence from the city for the fitness facility, after the permit is closed', 'If a pool or hot tub is planned, it is a separate regulated design (public pools are inspected by public health) - it is not covered by this checklist', 'Check your lease and the condominium rules for noise, vibration and operating-hour limits before you sign']}, {'title': 'Before you submit', 'items': ['One combined PDF set: architectural, mechanical, plumbing, electrical and structural (if any), all consistent with each other', 'All drawing sets use the same address, unit number, floor area and counts', 'Designs that require an engineer must be stamped by a licensed Ontario P.Eng.; BCIN designer information where applicable', 'Book a pre-consultation or zoning check with the city if the use or layout is not clearly permitted']}]}
def main():
    p = argparse.ArgumentParser(description=CONFIG["tagline"])
    p.add_argument("--city", default="Toronto")
    p.add_argument("--area-sqft", type=int, default=1200)
    p.add_argument("--units", type=int, default=0, help=CONFIG["unit_label"])
    for f in CONFIG["flags"]:
        p.add_argument("--" + f["arg"], action="store_true", help=f["label"])
    p.add_argument("--output", default="")
    a = p.parse_args()
    L = []
    L.append("# " + CONFIG["title"] + " - Ontario")
    L.append("")
    L.append("**City:** %s | **Area:** %d sq ft | **%s:** %d" % (a.city, a.area_sqft, CONFIG["unit_label"], a.units))
    L.append("")
    L.append("> Preliminary checklist generated with the free open-source " + CONFIG["title"] + " by Dust 2 Engineering Inc., Mississauga, Ontario. Verify every item with your designer and the local building department before submitting.")
    L.append("")
    for s in CONFIG["sections"]:
        if s.get("when") and not getattr(a, s["when"].replace("-", "_")):
            continue
        L.append("## " + s["title"])
        for it in s["items"]:
            L.append("- [ ] " + it)
        L.append("")
    L.append("---")
    L.append("Generated by the " + CONFIG["title"] + ", a free open-source tool by Dust 2 Engineering Inc. Dust 2 Engineering Inc. provides building permit drawings (architecture, HVAC, plumbing, sprinkler and electrical) stamped by an Ontario P.Eng. in the Greater Toronto Area, including Toronto, Mississauga, Brampton, Vaughan, Markham and Hamilton, for a flat fee of $3,500 to $5,000. This checklist is preliminary information only and is not engineering advice.")
    L.append("")
    out = "\n".join(L)
    if a.output:
        pathlib.Path(a.output).write_text(out, encoding="utf-8")
        print("Wrote " + a.output)
    else:
        print(out)
if __name__ == "__main__":
    main()
