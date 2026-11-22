# ===== MEMBER 4: INPUT VALIDATION (START) =====
def get_valid_temperature():
    while True:
        try:
            return float(input("\nEnter temperature in Celsius (-1 to stop): "))
        except ValueError:
            print("Error: Please enter a valid number.")


def get_valid_voltage():
    while True:
        try:
            voltage = float(input("Enter voltage: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        if voltage < 0:
            print("Error: Voltage cannot be negative.")
            continue
        return voltage


def get_valid_comm():
    while True:
        comm = input("Is communication working? (Y/N): ").strip().upper()
        if comm == "Y" or comm == "N":
            return comm
        print("Error: Please enter Y or N only.")
# ===== MEMBER 4: INPUT VALIDATION (END) =====


# ===== MEMBER 1: CLASSIFICATION (START) =====
def classify(temp, voltage, comm):
    if temp >= 50 or voltage < 10.5 or comm == "N":
        return "CRITICAL"
    elif (temp > 40 and temp < 50) or (voltage >= 10.5 and voltage < 11.5):
        return "WARNING"
    else:
        return "NORMAL"
# ===== MEMBER 1: CLASSIFICATION (END) =====


# ===== MEMBER 3: COUNTERS AND SUMMARY (START) =====
stats = {"total": 0, "normal": 0, "warning": 0, "critical": 0, "total_temp": 0.0}


def record_reading(temp, status):
    stats["total"] += 1
    stats["total_temp"] += temp
    if status == "NORMAL":
        stats["normal"] += 1
    elif status == "WARNING":
        stats["warning"] += 1
    else:
        stats["critical"] += 1


def show_summary():
    print("\n========== MONITORING SUMMARY ==========")
    print("Total Readings:", stats["total"])
    print("Normal:", stats["normal"])
    print("Warning:", stats["warning"])
    print("Critical:", stats["critical"])
    if stats["total"] > 0:
        average = stats["total_temp"] / stats["total"]
        print(f"Average Temperature: {average:.2f} C")
    else:
        print("Average Temperature: N/A (no valid readings)")
    print("========================================")
# ===== MEMBER 3: COUNTERS AND SUMMARY (END) =====


# ===== MEMBER 2: LOOP / MAIN (START) =====
def main():
    print("SMART EQUIPMENT MONITORING SYSTEM")

    while True:
        temp = get_valid_temperature()
        if temp == -1:
            break

        voltage = get_valid_voltage()
        comm = get_valid_comm()

        status = classify(temp, voltage, comm)
        record_reading(temp, status)

        print("\nEquipment Status:", status)

    show_summary()
    print("Monitoring session ended.")
# ===== MEMBER 2: LOOP / MAIN (END) =====


main()
