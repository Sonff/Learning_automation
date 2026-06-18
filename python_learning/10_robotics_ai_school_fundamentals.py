# =====================================================================
# TOPIC 10: PYTHON FUNDAMENTALS FOR KIDS (CLASS 6-10)
# (Robotics & AI Trainer Guide)
# =====================================================================
# Iss file me Python ke basic concepts ko Robotics aur AI ke real-world
# analogies (sensors, motors, decisions) ke sath bacho ke liye simple
# language me design kiya gaya hai.
#
# TEACHING TIP: Bacho ko batayein ki code likhna matlab "Robot ko instruction dena".

# ---------------------------------------------------------------------
# 1. Variables (Robot Ke Memory Drawers)
# ---------------------------------------------------------------------
# Analogy: Variables robot ke brain me chote box ya drawers hain jisme
# data (sensor readings, speed, names) temporary store kiya jata hai.

print("--- Lesson 1: Robot Memory (Variables) ---")
robot_name = "Robo-One"         # String (Text - Double quotes me)
battery_level = 100            # Integer (Pura number - battery percentage)
obstacle_distance = 15.6       # Float (Decimal number - distance in cm)
is_motor_on = True            # Boolean (Yes/No or True/False - motor status)

print(f"My Robot Name is: {robot_name}")
print(f"Current Battery Level: {battery_level}%")
print(f"Distance to Obstacle: {obstacle_distance} cm")
print(f"Is motor running? {is_motor_on}\n")


# ---------------------------------------------------------------------
# 2. Basic Calculations (Robot Calculations)
# ---------------------------------------------------------------------
# Robots coordinates, speed aur battery drainage calculate karne ke liye maths use karte hain.
print("--- Lesson 2: Robot Calculations ---")
speed = 20 # cm per second
time_running = 5 # seconds

# Distance = Speed * Time
distance_covered = speed * time_running
print(f"Robot traveled: {distance_covered} cm")

# Low battery warning calculation
current_battery = 85
drain_per_minute = 10
remaining_battery = current_battery - drain_per_minute
print(f"Battery remaining after 1 minute: {remaining_battery}%\n")


# ---------------------------------------------------------------------
# 3. Decision Making (Robot Decision - IF/ELSE)
# ---------------------------------------------------------------------
# Analogy: Robot ke pass sensors hote hain (jaise humare eyes/ears).
# Sensor data ke basis par robot self-decision leta hai.

print("--- Lesson 3: Robot Decisions (If/Else) ---")
# Man lijiye humare pass ek Obstacle Sensor hai
sensor_reading = 12.0 # Obstacle is at 12 cm

# AGAR (if) obstacle 15 cm se pass hai, toh ROBOT STOP ho jaye.
# WARNA (else) forward move kare.
if sensor_reading < 15.0:
    print("⚠️ ALERT: Obstacle detected close! Stopping motors.")
    is_motor_on = False
else:
    print("✅ PATH CLEAR: Motors moving forward.")
    is_motor_on = True
print(f"Motor Status: {is_motor_on}\n")


# ---------------------------------------------------------------------
# 4. Repetitive Tasks (Robot Loops - FOR and WHILE)
# ---------------------------------------------------------------------
# Analogy: Robots bored nahi hote! Woh ek hi kaam baar-baar (loops me) kar sakte hain.

print("--- Lesson 4: Loops (Repetitive Tasks) ---")

# A. FOR Loop: Jab humein pata ho ki kaam kitni baar karna hai.
# Example: Robot ki LED light ko 5 baar blink karwana.
print("Blinking LED lights:")
for blink in range(1, 6): # 1 se 5 tak
    print(f"💡 LED Blink {blink}!")

# B. WHILE Loop: Jab kaam tab tak chalana ho jab tak condition match kare.
# Example: Robot tab tak room clean karega jab tak battery empty na ho jaye.
print("\nRobot Cleaning Loop:")
room_dirt_level = 3 # clean scale (3 means dirty, 0 means fully clean)

while room_dirt_level > 0:
    print(f"🧹 Sweeping... Dirt level remaining: {room_dirt_level}")
    room_dirt_level -= 1 # Har sweep me dirt kam ho raha hai
print("🎉 Success: Room is clean! Returning to charging dock.\n")


# ---------------------------------------------------------------------
# 5. Functions (Robot Skills / Reusable Programs)
# ---------------------------------------------------------------------
# Analogy: Robot ko koi naya task sikhana (jaise sound make karna, dance karna).
# Ek baar define karo, aur jab chahe robot ko signal do to perform that skill.

print("--- Lesson 5: Robot Skills (Functions) ---")

# Skill Define karna (Function definition)
def make_turn(direction: str, angle: int):
    print(f"🔄 Executing Turn Skill...")
    print(f"Action: Turning {direction} by {angle} degrees.")
    print("Action complete.")

# Skill use karna (Calling the function)
make_turn("Left", 90)
print("-" * 15)
make_turn("Right", 180)
print()


# ---------------------------------------------------------------------
# 🌟 CLASS PROJECT: "Smart Vacuum Cleaner Simulation"
# ---------------------------------------------------------------------
# Bacho ke samne is function ko run karein aur unse responses input karwayein!

def run_vacuum_robot():
    print("=========================================")
    print("🤖 STARTING SMART VACUUM ROBOT (SIMULATOR)")
    print("=========================================")
    
    battery = 100
    cleaned_rooms = 0
    
    # 3 rooms clean karne ka target:
    for room in ["Living Room", "Kitchen", "Bedroom"]:
        print(f"\n📂 Entering room: {room}")
        print(f"🔋 Battery Level: {battery}%")
        
        # User input (Simulation of sensor reading)
        print(f"Does {room} have an obstacle? (yes/no): ")
        # School project simulation inputs
        obstacle = input("Sensor Input -> ").strip().lower()
        
        if obstacle == "yes" or obstacle == "y":
            print("⚠️ Robot path blocked! Activating steering control to bypass obstacle.")
            battery -= 15 # steering takes extra power
        else:
            print("🧹 Path clear. Sweeping the floor efficiently.")
            battery -= 10
            
        cleaned_rooms += 1
        print(f"✨ Finished cleaning {room}!")
        
        if battery <= 20:
            print("🚨 Low Battery Warning! Going to charging dock immediately.")
            break
            
    print("\n-----------------------------------------")
    print(f"📊 SUMMARY: Cleaned {cleaned_rooms} rooms. Remaining Battery: {battery}%")
    print("=========================================")

# Is file ko direct run karne par niche simulation open hoga:
if __name__ == "__main__":
    print("TEACHER NOTE: You can run this file directly in class. Let's start the simulation:")
    run_vacuum_robot()
