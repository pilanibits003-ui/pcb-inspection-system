import time

print("Initializing AI-Vision Smart Inspection System...")
time.sleep(1) 

print("System Online. Scanning high-speed PCB conveyor belt...")

for i in range(1, 6):
    print(f"[Frame {i}] Inspecting component alignment...")
    time.sleep(0.5) 

    if i == 3:
        print("⚠️ ALERT: Solder bridge defect detected on Resistor R12!")
    else:
        print("✅ Status: PASS")

print("Inspection cycle complete. Stream paused.")
