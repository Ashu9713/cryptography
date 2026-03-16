import time

class TemperatureSensor:
    def __init__(self, initial_temp):
        self.current_temp = initial_temp

    def read_temperature(self):
        return self.current_temp

    def update_temperature(self, change):
        self.current_temp += change


class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    def calculate(self, setpoint, current_temp):
        error = setpoint - current_temp
        self.integral += error
        derivative = error - self.previous_error
        self.previous_error = error

        return (self.kp * error +
                self.ki * self.integral +
                self.kd * derivative)


class CANBus:
    def send_message(self, temp, output):
        print(f"[CAN BUS] Temp: {temp:.2f} °C | Output: {output:.2f}")


def main():

    sensor = TemperatureSensor(35.0)
    pid = PIDController(0.4, 0.02, 0.1)
    setpoint = 25.0
    can = CANBus()

    print("HVAC PID Simulation Started...\n")

    for i in range(40):

        current_temp = sensor.read_temperature()
        output = pid.calculate(setpoint, current_temp)

        # Proper cooling response
        sensor.update_temperature(output * 0.05)

        can.send_message(current_temp, output)

        time.sleep(0.5)


if __name__ == "__main__":
    main()
