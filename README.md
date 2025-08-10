Runescape_OSRS_Calculators - 
Repository of all the caclulators i've made during my time playing OSRS to help players be more efficent; No longer play anymore. 
So, leaving these here in case someone in the future finds use in them  

The Range XP Calculator
A simple Python GUI application built with Tkinter to calculate ranged combat DPS, XP per hour, and estimated hours to reach a target ranged level in Old School RuneScape (OSRS). It supports rapid and accurate attack styles, including the effects of Void and Elite Void equipment bonuses.

Features
Calculates effective range strength based on player stats, boosts, and prayers.

Computes maximum hit, attack rolls, defense rolls, and hit chances.

Estimates damage per hit (DPH) and damage per second (DPS) for both rapid and accurate styles.

Includes calculations with and without Void set multipliers.

Calculates XP per hour and estimates hours required to reach the target ranged level.

Simple GUI interface for easy input and clear output.

Requirements
Python 3.x

Tkinter (usually included with Python standard library)

Installation
Clone or download this repository.

Run the Python script:

bash
Copy
Edit
python range_xp_calculator.py
Usage
Enter the following values in the input fields:

Range Strength Bonus

Current Range Level

Range Attack Bonus

Boosts (e.g., from potions)

Prayer Multiplier

Target’s Defense

Target’s Ranged Defense

Weapon Attack Speed (seconds per attack)

Target Level Goal (the ranged level you want to reach)

Click the Calculate button.

The detailed calculations and estimated hours to level will be displayed in the scrollable text box.

Notes
The calculator uses a predefined XP table for ranged levels to estimate XP requirements.

The Void set multipliers are hardcoded as 1.1 for Void and 1.125 for Elite Void.

Attack speeds less than 0.6 seconds are adjusted in DPS calculations.

All calculations assume 4 XP gained per damage dealt.
