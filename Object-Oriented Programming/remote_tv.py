import random
import time

class RemoteControl:
    def __init__(self, tv_status="Off", tv_volume=0, channel_list=["TRT"], channel="TRT"):
        print("Remote control is being created...")
        self.tv_volume = tv_volume
        self.tv_status = tv_status
        self.channel_list = channel_list
        self.channel = channel

    def increase_decrease_volume(self):
        while True:
            action = input("Press '+' to increase volume, '-' to decrease, or 'q' to exit: ")
            if action == "+" and self.tv_volume < 32:
                self.tv_volume += 1
                print("Volume:", self.tv_volume)
            elif action == "-" and self.tv_volume > 0:
                self.tv_volume -= 1
                print("Volume:", self.tv_volume)
            elif action == "q":
                print("Exiting volume control...")
                break
            else:
                print("Invalid input.")

    def __str__(self):
        return f"TV Status: {self.tv_status}\nVolume: {self.tv_volume}\nChannels: {self.channel_list}\nCurrent Channel: {self.channel}\n"

    def turn_on_tv(self):
        if self.tv_status == "Off":
            print("Turning on the TV...")
            self.tv_status = "On"
        else:
            print("The TV is already on!")

    def turn_off_tv(self):
        if self.tv_status == "On":
            print("Turning off the TV...")
            self.tv_status = "Off"
        else:
            print("The TV is already off!")

    def add_channel(self, channel):
        print(f"{channel} has been added.")
        self.channel_list.append(channel)

    def sleep_timer(self, duration):
        print(f"The TV will turn off in {duration} seconds...")
        time.sleep(duration)
        self.turn_off_tv()
        print("The TV has been turned off.")

    def remove_channel(self):
        print("Available channels:", self.channel_list)
        channel_to_remove = input("Enter the channel you want to remove: ")
        if channel_to_remove in self.channel_list:
            self.channel_list.remove(channel_to_remove)
            print(f"{channel_to_remove} has been removed.")
        else:
            print(f"{channel_to_remove} was not found.")

    def change_channel(self):
        print("Available channels:", self.channel_list)
        selected_channel = input("Enter the channel you want to switch to: ")
        if selected_channel in self.channel_list:
            self.channel = selected_channel
            print(f"Switched to {selected_channel}.")
        else:
            print(f"{selected_channel} was not found.")

    def random_channel(self):
        random_index = random.randint(0, len(self.channel_list) - 1)
        self.channel = self.channel_list[random_index]
        print("Current Channel:", self.channel)

    def __len__(self):
        return len(self.channel_list)


remote = RemoteControl()

print("""*******************

TV Application

Options:

1. Turn on the TV

2. Turn off the TV

3. TV Information

4. Check Number of Channels

5. Add a Channel

6. Switch to a Random Channel

7. Increase or Decrease Volume

8. Remove a Channel

9. Change Channel

10. Set Sleep Timer

Press 'q' to exit.
*******************""")

while True:
    action = input("Please select an option: ")
    if action == "1":
        remote.turn_on_tv()
    elif action == "2":
        remote.turn_off_tv()
    elif action == "3":
        print(remote)
    elif action == "4":
        print("Number of channels:", len(remote))
    elif action == "5":
        channels = input("Enter the channels you want to add, separated by commas: ")
        channels_to_add = channels.split(",")
        for ch in channels_to_add:
            remote.add_channel(ch.strip())
        print("Channel list has been updated.")
    elif action == "6":
        remote.random_channel()
    elif action == "7":
        remote.increase_decrease_volume()
    elif action == "8":
        remote.remove_channel()
    elif action == "9":
        remote.change_channel()
    elif action == "10":
        duration = int(input("How many seconds until the TV turns off? "))
        remote.sleep_timer(duration)
    elif action == "q":
        break
    else:
        print("Invalid option.")