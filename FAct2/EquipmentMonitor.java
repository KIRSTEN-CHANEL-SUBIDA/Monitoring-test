import java.util.Scanner;

public class EquipmentMonitor {

    static Scanner sc = new Scanner(System.in);

    // ===== MEMBER 4: INPUT VALIDATION (START) =====
    static double getValidTemperature() {
        while (true) {
            System.out.print("\nEnter temperature in Celsius (-1 to stop): ");
            try {
                return Double.parseDouble(sc.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("Error: Please enter a valid number.");
            }
        }
    }

    static double getValidVoltage() {
        while (true) {
            System.out.print("Enter voltage: ");
            double voltage;
            try {
                voltage = Double.parseDouble(sc.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("Error: Please enter a valid number.");
                continue;
            }
            if (voltage < 0) {
                System.out.println("Error: Voltage cannot be negative.");
                continue;
            }
            return voltage;
        }
    }

    static char getValidComm() {
        while (true) {
            System.out.print("Is communication working? (Y/N): ");
            String input = sc.nextLine().trim().toUpperCase();
            if (input.equals("Y") || input.equals("N")) return input.charAt(0);
            System.out.println("Error: Please enter Y or N only.");
        }
    }
    // ===== MEMBER 4: INPUT VALIDATION (END) =====


    // ===== MEMBER 1: CLASSIFICATION (START) =====
    static String classify(double temp, double voltage, char comm) {
        if (temp >= 50 || voltage < 10.5 || comm == 'N')
            return "CRITICAL";
        else if ((temp > 40 && temp < 50) || (voltage >= 10.5 && voltage < 11.5))
            return "WARNING";
        else
            return "NORMAL";
    }
    // ===== MEMBER 1: CLASSIFICATION (END) =====


    // ===== MEMBER 3: COUNTERS AND SUMMARY (START) =====
    static int total = 0, normal = 0, warning = 0, critical = 0;
    static double totalTemp = 0.0;

    static void recordReading(double temp, String status) {
        total++;
        totalTemp += temp;
        if (status.equals("NORMAL")) normal++;
        else if (status.equals("WARNING")) warning++;
        else critical++;
    }

    static void showSummary() {
        System.out.println("\n========== MONITORING SUMMARY ==========");
        System.out.println("Total Readings: " + total);
        System.out.println("Normal: " + normal);
        System.out.println("Warning: " + warning);
        System.out.println("Critical: " + critical);
        if (total > 0) {
            double average = totalTemp / total;
            System.out.printf("Average Temperature: %.2f C%n", average);
        } else {
            System.out.println("Average Temperature: N/A (no valid readings)");
        }
        System.out.println("========================================");
    }
    // ===== MEMBER 3: COUNTERS AND SUMMARY (END) =====


    // ===== MEMBER 2: LOOP / MAIN (START) =====
    public static void main(String[] args) {
        System.out.println("SMART EQUIPMENT MONITORING SYSTEM");

        while (true) {
            double temp = getValidTemperature();
            if (temp == -1) break;

            double voltage = getValidVoltage();
            char comm = getValidComm();

            String status = classify(temp, voltage, comm);
            recordReading(temp, status);

            System.out.println("\nEquipment Status: " + status);
        }

        showSummary();
        System.out.println("Monitoring session ended.");
    }
    // ===== MEMBER 2: LOOP / MAIN (END) =====

}
