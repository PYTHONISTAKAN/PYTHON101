class Computer:
    def __init__(self, brand, model, ram, disk):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.disk = disk

    def power_on(self):
        """Turns on the computer"""
        print(f"{self.brand} {self.model} is powering on...")

    def power_off(self):
        """Turns off the computer"""
        print(f"{self.brand} {self.model} is shutting down...")

    def upgrade_ram(self, new_ram):
        """Upgrades the RAM"""
        if new_ram > self.ram:
            self.ram = new_ram
            print(f"RAM upgraded to {self.ram} GB.")
        else:
            print("New RAM cannot be smaller than the current RAM.")

    def upgrade_disk(self, new_disk):
        """Upgrades the disk"""
        if new_disk > self.disk:
            self.disk = new_disk
            print(f"Disk upgraded to {self.disk} GB.")
        else:
            print("New disk cannot be smaller than the current disk.")

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, RAM: {self.ram} GB, Disk: {self.disk} GB"

computer1 = Computer("Dell", "XPS 15", 16, 512)
print(computer1)