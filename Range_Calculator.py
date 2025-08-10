import tkinter as tk
from tkinter import ttk, scrolledtext

list1 = [83, 91, 102, 112, 124, 138, 151, 168, 185, 204, 226, 249, 274, 304, 335, 369, 408, 450, 497, 548, 606, 667, 737, 814, 898, 990, 1094, 1207, 1332, 1470, 1623, 1791, 1977, 2182, 2409, 2658, 2935,3240, 3576, 3947, 4358, 4810, 5310, 5863, 6471, 7144, 7887, 8707, 9612, 10612, 11715, 12934, 14278, 15764, 17404, 19214, 21212, 23420, 25856, 28546, 31516, 34795,38416, 42413,46826,51669,57079,63019,69576, 76818, 84812, 93638, 103383, 114143, 126022, 139138, 153619, 169608,187260,206750,228269,252027,278259,307221,339198,374502,413482,456519,504037,556499,614422,678376,748985,826944, 913019, 1008052, 1112977, 1228825]

def hit_chance(atk_roll, def_roll):
    if atk_roll > def_roll:
        return 1 - (def_roll + 2) / (2 * atk_roll + 1)
    else:
        return atk_roll / (2 * def_roll + 1)

def calculate():
    try:
        # Fetch inputs from entry fields
        ranged_strength = float(entry_ranged_strength.get())
        range_level = int(float(entry_range_level.get()))
        range_attack = float(entry_range_attack.get())
        boost = float(entry_boost.get())
        prayer = float(entry_prayer.get())
        target_def = float(entry_target_def.get())
        target_ranged = float(entry_target_ranged.get())
        speed = float(entry_speed.get())
        lvl_goal = int(float(entry_lvl_goal.get()))
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error in input values: {e}")
        return
    
    output_text.delete(1.0, tk.END)  # clear output
    
    total_hours = 0.0
    void_mult = 1.1
    void_elite_mult = 1.125

    level = range_level
    while level < lvl_goal:
        boosts = (level + boost) * prayer
        ers_rapid = boosts + 8
        ers_accurate = boosts + 3 + 8
        
        # void multipliers
        ers_rapid_void = ers_rapid * void_mult
        ers_rapid_void_elite = ers_rapid * void_elite_mult
        ers_accurate_void = ers_accurate * void_mult
        ers_accurate_void_elite = ers_accurate * void_elite_mult
        
        # Max hits
        maxhit_rapid = ((ranged_strength + 64) * ers_rapid) / 640 + 0.5
        maxhit_accurate = ((ranged_strength + 64) * ers_accurate) / 640 + 0.5
        maxhit_rapid_void = ((ranged_strength + 64) * ers_rapid_void) / 640 + 0.5
        maxhit_rapid_void_elite = ((ranged_strength + 64) * ers_rapid_void_elite) / 640 + 0.5
        maxhit_accurate_void = ((ranged_strength + 64) * ers_accurate_void) / 640 + 0.5
        maxhit_accurate_void_elite = ((ranged_strength + 64) * ers_accurate_void_elite) / 640 + 0.5
        
        # Attack rolls
        atkroll_rapid = ers_rapid * (range_attack + 64)
        atkroll_accurate = ers_accurate * (range_attack + 64)
        atkroll_rapid_void = ers_rapid_void * (range_attack + 64)
        atkroll_rapid_void_elite = ers_rapid_void_elite * (range_attack + 64)
        atkroll_accurate_void = ers_accurate_void * (range_attack + 64)
        atkroll_accurate_void_elite = ers_accurate_void_elite * (range_attack + 64)
        
        # Defense roll
        defroll = (target_def + 9) * (target_ranged + 64)
        
        # Hit chances
        hitchance_rapid = hit_chance(atkroll_rapid, defroll)
        hitchance_accurate = hit_chance(atkroll_accurate, defroll)
        hitchance_rapid_void = hit_chance(atkroll_rapid_void, defroll)
        hitchance_rapid_void_elite = hit_chance(atkroll_rapid_void_elite, defroll)
        hitchance_accurate_void = hit_chance(atkroll_accurate_void, defroll)
        hitchance_accurate_void_elite = hit_chance(atkroll_accurate_void_elite, defroll)
        
        # DPH
        dph_rapid = (maxhit_rapid * hitchance_rapid) / 2
        dph_accurate = (maxhit_accurate * hitchance_accurate) / 2
        dph_rapid_void = (maxhit_rapid_void * hitchance_rapid_void) / 2
        dph_rapid_void_elite = (maxhit_rapid_void_elite * hitchance_rapid_void_elite) / 2
        dph_accurate_void = (maxhit_accurate_void * hitchance_accurate_void) / 2
        dph_accurate_void_elite = (maxhit_accurate_void_elite * hitchance_accurate_void_elite) / 2
        
        # DPS
        dps_rapid = dph_rapid / (speed - 0.6)
        dps_accurate = dph_accurate / speed
        dps_rapid_void = dph_rapid_void / (speed - 0.6)
        dps_rapid_void_elite = dph_rapid_void_elite / (speed - 0.6)
        dps_accurate_void = dph_accurate_void / speed
        dps_accurate_void_elite = dph_accurate_void_elite / speed
        
        # XP/hr (4 xp per damage)
        xp_per_hour_rapid = dps_rapid * 4 * 3600
        xp_per_hour_rapid_void = dps_rapid_void * 4 * 3600
        
        # XP needed for level
        xp_needed = list1[level - 1]
        
        # Hours to level
        hours_to_level_rapid = xp_needed / xp_per_hour_rapid
        hours_to_level_rapid_void = xp_needed / xp_per_hour_rapid_void
        
        total_hours += hours_to_level_rapid
        
        # Output per level
        output_text.insert(tk.END, f"Level {level}:\n")
        output_text.insert(tk.END, f"  XP needed: {xp_needed}\n")
        output_text.insert(tk.END, f"  Rapid DPS: {dps_rapid:.2f}, XP/hr: {xp_per_hour_rapid:.2f}, Hours to level: {hours_to_level_rapid:.2f}\n")
        output_text.insert(tk.END, f"  Rapid DPS (Void): {dps_rapid_void:.2f}, XP/hr (Void): {xp_per_hour_rapid_void:.2f}, Hours to level (Void): {hours_to_level_rapid_void:.2f}\n\n")
        
        level += 1
    
    output_text.insert(tk.END, f"Total hours to reach level {lvl_goal}: {total_hours:.2f}\n")

# Create main window
window = tk.Tk()
window.title("Range XP Calculator")
window.geometry("600x600")

# Input labels and entries
labels = [
    "Range Strength Bonus",
    "Range Level",
    "Range Attack Bonus",
    "Boost",
    "Prayer Multiplier",
    "Target Defense",
    "Target Ranged Defense",
    "Weapon Attack Speed (sec)",
    "Target Level Goal"
]

entries = []
for i, label_text in enumerate(labels):
    lbl = ttk.Label(window, text=label_text)
    lbl.grid(row=i, column=0, padx=5, pady=5, sticky='w')
    ent = ttk.Entry(window)
    ent.grid(row=i, column=1, padx=5, pady=5)
    entries.append(ent)

# Assign entries to variables for easier reference
(entry_ranged_strength, entry_range_level, entry_range_attack, entry_boost,
 entry_prayer, entry_target_def, entry_target_ranged, entry_speed,
 entry_lvl_goal) = entries

# Default values for quick testing
entry_ranged_strength.insert(0, "22")
entry_range_level.insert(0, "20")
entry_range_attack.insert(0, "22")
entry_boost.insert(0, "0")
entry_prayer.insert(0, "1")
entry_target_def.insert(0, "50")
entry_target_ranged.insert(0, "-55")
entry_speed.insert(0, "3.6")
entry_lvl_goal.insert(0, "50")

# Calculate button
btn_calculate = ttk.Button(window, text="Calculate", command=calculate)
btn_calculate.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Output text box (scrollable)
output_text = scrolledtext.ScrolledText(window, width=70, height=20)
output_text.grid(row=len(labels)+1, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
