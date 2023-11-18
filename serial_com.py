import serial
import time
import serial.tools.list_ports


class SerialCom:
    def __init__(self, com_port: str = "COM8"):
        self.com_port = com_port
        self.baud_rate = 9600

        try:
            self.ser = serial.Serial(port=self.com_port, baudrate=self.baud_rate, timeout=1)
            time.sleep(2)
        except serial.serialutil.SerialException:
            print("Error: Microcontroller not connected or specified port not available.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def send_intensities(self, intensities: str) -> None:
        """
        Send the string of intensities to microcontroller
        :param intensities: comma separated string of PWM intensities for each motor
        :return: None
        """
        self.ser.write(intensities.encode())
        print(f"Sent intensities {intensities}")

    def close_com(self) -> None:
        """
        Close serial communication when finished
        :return: None
        """
        if self.ser.is_open:
            self.ser.close()

    def send_test(self) -> None:
        """
        Send test message for debugging
        :return: None
        """
        self.ser.write(b'gia sou' + "\n".encode())
        print(f"Sent test message")

    @staticmethod
    def find_available_ports() -> None:
        """
        Finds and prints the available COM ports
        :return: None
        """

        available_ports = list(serial.tools.list_ports.comports())

        if available_ports:
            print("Available COM ports:")
            for port in available_ports:
                print(port.device)
        else:
            print("No COM ports found.")

    def get_feedback(self) -> None:
        """
        Listens for and prints feedback from the microcontroller
        :return: None
        """
        received_data = self.ser.readline().decode('utf-8').strip()
        print(f"Received: {received_data}")


if __name__ == "__main__":
    # Tests serial communication with the microcontroller
    serial_com = SerialCom()
    serial_com.find_available_ports()
    serial_com.send_test()
    serial_com.get_feedback()
    serial_com.close_com()
