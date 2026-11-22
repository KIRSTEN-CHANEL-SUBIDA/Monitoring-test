#include <iostream>
#include <string>
#include <limits>
#include <cctype>
#include <iomanip>
using namespace std;

// ===== MEMBER 4: INPUT VALIDATION (START) =====
double getValidTemperature() {
    double temp;
    while (true) {
        cout << "\nEnter temperature in Celsius (-1 to stop): ";
        if (cin >> temp) return temp;
        cout << "Error: Please enter a valid number.\n";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
}

double getValidVoltage() {
    double voltage;
    while (true) {
        cout << "Enter voltage: ";
        if (!(cin >> voltage)) {
            cout << "Error: Please enter a valid number.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        if (voltage < 0) {
            cout << "Error: Voltage cannot be negative.\n";
            continue;
        }
        return voltage;
    }
}

char getValidComm() {
    string input;
    while (true) {
        cout << "Is communication working? (Y/N): ";
        cin >> input;
        if (input.length() == 1) {
            char c = toupper(input[0]);
            if (c == 'Y' || c == 'N') return c;
        }
        cout << "Error: Please enter Y or N only.\n";
    }
}
// ===== MEMBER 4: INPUT VALIDATION (END) =====


// ===== MEMBER 1: CLASSIFICATION (START) =====
string classify(double temp, double voltage, char comm) {
    if (temp >= 50 || voltage < 10.5 || comm == 'N')
        return "CRITICAL";
    else if ((temp > 40 && temp < 50) || (voltage >= 10.5 && voltage < 11.5))
        return "WARNING";
    else
        return "NORMAL";
}
// ===== MEMBER 1: CLASSIFICATION (END) =====


// ===== MEMBER 3: COUNTERS AND SUMMARY (START) =====
int total = 0, normalCount = 0, warningCount = 0, criticalCount = 0;
double totalTemp = 0.0;

void recordReading(double temp, string status) {
    total++;
    totalTemp += temp;
    if (status == "NORMAL") normalCount++;
    else if (status == "WARNING") warningCount++;
    else criticalCount++;
}

void showSummary() {
    cout << "\n========== MONITORING SUMMARY ==========" << "\n";
    cout << "Total Readings: " << total << endl;
    cout << "Normal: " << normalCount << endl;
    cout << "Warning: " << warningCount << endl;
    cout << "Critical: " << criticalCount << endl;
    if (total > 0) {
        double average = totalTemp / total;
        cout << fixed << setprecision(2);
        cout << "Average Temperature: " << average << " C\n";
    } else {
        cout << "Average Temperature: N/A (no valid readings)\n";
    }
    cout << "========================================\n";
}
// ===== MEMBER 3: COUNTERS AND SUMMARY (END) =====


// ===== MEMBER 2: LOOP / MAIN (START) =====
int main() {
    cout << "SMART EQUIPMENT MONITORING SYSTEM\n";

    while (true) {
        double temp = getValidTemperature();
        if (temp == -1) break;

        double voltage = getValidVoltage();
        char comm = getValidComm();

        string status = classify(temp, voltage, comm);
        recordReading(temp, status);

        cout << "\nEquipment Status: " << status << endl;
    }

    showSummary();
    cout << "Monitoring session ended.\n";
    return 0;
}
// ===== MEMBER 2: LOOP / MAIN (END) =====
