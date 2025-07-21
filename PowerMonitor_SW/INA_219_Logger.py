import csv
import time
import smbus
import RPi.GPIO as GPIO

# GPIO Configuration for computatinal stage
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)

def read_state():
    return (GPIO.input(22) << 2) | (GPIO.input(27) << 1) | GPIO.input(17)

# INA219 Configuration
bus = smbus.SMBus(1)
INA219_ADDRESS = 0x40
INA219_REG_CONFIG = 0x00
INA219_REG_SHUNT_VOLTAGE = 0x01
INA219_REG_BUS_VOLTAGE = 0x02
INA219_REG_CALIBRATION = 0x05

CONFIG_10KSPS = (
    (0 << 13) |  # BRNG=16V
    (2 << 11) |  # PG=±160mV 
    (3 << 7)  |  # BADC=12bit
    (3 << 3)  |  # SADC=12bit
    7            # MODE=continuous
)

def write_reg(reg, value):
    bus.write_word_data(INA219_ADDRESS, reg, ((value >> 8) & 0xFF) | ((value & 0xFF) << 8))

def read_reg(reg):
    value = bus.read_word_data(INA219_ADDRESS, reg)
    return ((value << 8) & 0xFF00) | (value >> 8)

# INA219 Init
write_reg(INA219_REG_CONFIG, CONFIG_10KSPS)
write_reg(INA219_REG_CALIBRATION, 4096)

def read_raw_voltages():
    shunt_raw = read_reg(INA219_REG_SHUNT_VOLTAGE)
    bus_raw = read_reg(INA219_REG_BUS_VOLTAGE)
    return bus_raw & 0xFFFF, shunt_raw

def main():
    start_time = time.time()
    sample_count = 0
    interval_start_time = start_time
    interval_sample_count = 0
    interval_v_sum = 0
    interval_a_sum = 0
    interval_w_sum = 0

    with open('power_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'V', 'A', 'W', 'Exec_Stage'])

        while True:
            try:
                bus_raw, shunt_raw = read_raw_voltages()
                timestamp = time.time() - start_time
                state = read_state()

                if shunt_raw >= 32768:
                    shunt_raw -= 65536

                v_bus = (bus_raw >> 3) * 0.004
                v_shunt = shunt_raw * 0.00001
                current = v_shunt / 0.1
                watt = current * v_bus

                writer.writerow([f"{timestamp:.8f}", f"{v_bus:.3f}", f"{current:.4f}", f"{watt:.4f}", state])

                sample_count += 1
                interval_sample_count += 1
                interval_v_sum += v_bus
                interval_a_sum += current
                interval_w_sum += watt

                # Statisctics summary (every 5 seconds)
                if time.time() - interval_start_time >= 5:
                    interval_duration = time.time() - interval_start_time
                    avg_sample_rate = interval_sample_count / interval_duration
                    avg_v = interval_v_sum / interval_sample_count
                    avg_a = interval_a_sum / interval_sample_count
                    avg_w = interval_w_sum / interval_sample_count

                    print(f"\n[STATISTICS - Last 5s]")
                    print(f"Samples: {sample_count} (in interval: {interval_sample_count})")
                    print(f"Mean frequancy: {avg_sample_rate:.2f} Hz")
                    print(f"Mean V: {avg_v:.3f} V, Mean A: {avg_a:.4f} A, Mean W: {avg_w:.4f} W\n")

                    # Reset 
                    interval_start_time = time.time()
                    interval_sample_count = 0
                    interval_v_sum = 0
                    interval_a_sum = 0
                    interval_w_sum = 0

                    if sample_count > 220000:
                       exit()

            except Exception as e:
                print("Error:", e)
                time.sleep(1)

if __name__ == "__main__":
    main()
