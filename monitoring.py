print("SMART EQUIPMENT MONITORING SYSTEM")

total = 0
normal = 0
warning = 0
critical = 0
total_temp = 0.0

while True:
    # Temperature
    try:
        temp = float(input("\nEnter temperature in Celsius (-1 to stop): "))
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    if temp == -1:
        break

    # Voltage
    try:
        voltage = float(input("Enter voltage: "))
    except ValueError:
        print("Error: Please enter a number only.")
        continue

    if voltage < 0:
        print("Error: Voltage cannot be negative.")
        continue

    # Communication
    comm = input("Is communication working? (Y/N): ").strip().upper()
    if comm != "Y" and comm != "N":
        print("Error: Please enter Y or N only.")
        continue

    # Classification (CRITICAL, WARNING, NORMAL)
    if temp >= 50 or voltage < 10.5 or comm == "N":
        status = "CRITICAL"
        critical += 1
    elif (temp > 40 and temp < 50) or (voltage >= 10.5 and voltage < 11.5):
        status = "WARNING"
        warning += 1
    else:
        status = "NORMAL"
        normal += 1

    total += 1
    total_temp += temp

    print("\nEquipment Status:", status)

# Summary
print("\n-------------- MONITORING SUMMARY --------------")

print("Total Readings:", total)
print("Normal:", normal)
print("Warning:", warning)
print("Critical:", critical)

if total <= 0:
    print("Average Temperature: N/A (no valid readings)")
else:
    average = total_temp / total
    print(f"Average Temperature: {average:.2f} C")

print("------------------------------------------------")

print("Monitoring session ended.")
