import os
import logging
import subprocess

# Initialize logging
logging.basicConfig(level=logging.INFO)


class OPIGPIO:
    def __init__(self) -> None:
        self.base_path: str = "/sys/class/gpio"
        logging.info("OPIGPIO initialized.")

    def _change_permissions(self, path: str) -> None:
        try:
            subprocess.run(["sudo", "chmod", "666", path])
            logging.info(f"Changed permissions for {path}.")
        except Exception as e:
            logging.error(f"Failed to change permissions for {path}: {e}")

    def _write_to_file(self, path: str, value: str) -> None:
        try:
            with open(path, "w") as f:
                f.write(str(value))
            logging.info(f"Successfully wrote {value} to {path}.")
        except PermissionError:
            logging.warning(
                f"Permission error while trying to write to {path}. Changing permissions..."
            )
            self._change_permissions(path)
            self._write_to_file(path, value)
        except IOError as e:
            logging.error(f"Failed to write to {path}: {e}")

    def _read_from_file(self, path: str) -> str:
        try:
            with open(path, "r") as f:
                val = f.read().strip()
            logging.info(f"Successfully read value {val} from {path}.")
            return val
        except PermissionError:
            logging.warning(
                f"Permission error while trying to read from {path}. Changing permissions..."
            )
            self._change_permissions(path)
            return self._read_from_file(path)
        except IOError as e:
            logging.error(f"Failed to read from {path}: {e}")
            return ""

    def setup(self) -> None:
        # Placeholder for any initialization code
        logging.info("Setup complete.")

    def pinMode(self, pin: int, mode: str) -> None:
        export_path = os.path.join(self.base_path, "export")
        self._write_to_file(export_path, str(pin))

        gpio_path = os.path.join(self.base_path, f"gpio{pin}")
        direction_path = os.path.join(gpio_path, "direction")
        self._write_to_file(direction_path, mode)

        logging.info(f"Set mode {mode} for pin {pin}.")

    def digitalWrite(self, pin: int, value: int) -> None:
        gpio_path = os.path.join(self.base_path, f"gpio{pin}")
        value_path = os.path.join(gpio_path, "value")
        self._write_to_file(value_path, str(value))

        logging.info(f"Wrote value {value} to pin {pin}.")

    def digitalRead(self, pin: int) -> int:
        gpio_path = os.path.join(self.base_path, f"gpio{pin}")
        value_path = os.path.join(gpio_path, "value")
        value = int(self._read_from_file(value_path))

        logging.info(f"Read value {value} from pin {pin}.")
        return value
