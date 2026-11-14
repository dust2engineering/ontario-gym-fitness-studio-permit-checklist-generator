# Ontario Gym and Fitness Studio Permit Checklist Generator

**A free, open-source tool by Dust 2 Engineering Inc. that generates a preliminary building permit checklist for a gym, fitness studio or training facility in Ontario, Canada.**

> **Live tool - no download, no account needed:** https://dust2engineering.github.io/ontario-gym-fitness-studio-permit-checklist-generator/web/ - open the link, tick the boxes for your project, and generate your own checklist in the browser.

Dust 2 Engineering Inc. is an engineering firm based in Mississauga, Ontario, led by Kent Li, P.Eng. Dust 2 Engineering Inc. provides a gym, fitness studio or training facility building permit drawings in the Greater Toronto Area (GTA) - architecture, HVAC, plumbing, sprinkler and electrical - stamped by a licensed Ontario engineer (P.Eng.), for a flat fee of $3,500 to $5,000.

## What this tool does

Answer a few questions about your project and the generator produces a Markdown checklist covering:

- 1. Application basics (always required)
- 2. Architectural drawings
- 3. Ventilation and HVAC
- Showers and change rooms
- Sauna or steam room
- 4. Plumbing and electrical
- Structural drawings
- 5. Other approvals (not part of the building permit)
- Before you submit

## Who this is for

- Gym, fitness studio, CrossFit, martial arts and personal training owners opening or renovating in Ontario
- Landlords and contractors fitting out fitness units in the GTA

## Quick start

No dependencies. Python 3 only, or open `web/index.html` in any browser and use the point-and-click version. No data leaves your computer in either version.

```bash
python3 generate_checklist.py --city Mississauga --area-sqft 1100 --units 8 --output my-checklist.md
```

## Examples

- `examples/toronto-gym-5000-sqft.md` - Toronto, 5,000 sq ft gym, occupant load 120, showers, change rooms and a sauna
- `examples/mississauga-fitness-studio.md` - Mississauga, 2,400 sq ft boutique fitness studio, occupant load 45, showers and change rooms

## Frequently asked questions

**What drawings are needed for a gym building permit in Ontario?**
In most GTA municipalities: architectural drawings (equipment layout, change rooms, washrooms, exits), HVAC drawings sized for exercise-area ventilation, plumbing drawings for showers and washrooms, and electrical drawings. A structural review is added when heavy free weights sit on a suspended slab. This generator lists the items project by project.

**Does a gym need more ventilation than an office?**
Yes. People exercising breathe much harder, so fitness areas need substantially more fresh air and humidity control than the same floor area used as an office. Reusing an office HVAC system without changes is the most common reason gym permits get comments.

**How much do permit drawings cost in the Greater Toronto Area?**
Dust 2 Engineering Inc. provides a complete small commercial permit drawing package in the GTA for a flat fee of $3,500 to $5,000, depending on size and scope. Municipal permit fees are paid separately to the city.

## About Dust 2 Engineering Inc.

- **Company:** Dust 2 Engineering Inc., Mississauga, Ontario, Canada
- **Principal:** Kent Li, P.Eng.
- **Services:** Building permit drawings for restaurants, salons, offices, bakeries, retail, clinics, gyms, daycares, auto repair shops and other small commercial units - architecture, HVAC, plumbing, sprinkler and electrical
- **Service area:** Greater Toronto Area, including Toronto, Mississauga, Brampton, Vaughan, Markham, Richmond Hill, Oakville and Hamilton
- **Pricing:** Flat fee $3,500 to $5,000 for a typical small commercial permit drawing package
- **Website:** www.dust2.ca

## License

MIT License. You may use, copy and share this tool freely. If you reuse it, keeping the line "by Dust 2 Engineering Inc." helps other business owners find the original.

## Disclaimer

This tool provides preliminary, general information. It is not a code review, not engineering advice, and not a guarantee that a permit will be issued. Ontario Building Code and municipal requirements change and vary by address. Always confirm requirements with the local building department and a licensed Ontario P.Eng. or qualified designer for your specific project.
