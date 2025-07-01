# Super Mario Sunshine Multiworld Setup Guide

## Required Software
- [Latest release of Archipelago Multiworld Suite](https://github.com/ArchipelagoMW/Archipelago/releases). 
- [Dolphin Gamecube/Wii Emulator](https://dolphin-emu.org/)
- Your **Legally** obtained American ISO file, likely named `Super Mario Sunshine (USA).iso`

## Setup process
1. Download and install the latest release of Archipelago Multiworld from the link above.

2. Download and install the latest release of Dolphin Emulator from the link above.

3. Unzip the APWorld downloaded from the [releases](https://github.com/Joshark/archipelago-sms/releases/latest) page and place it in your `custom_worlds` folder located in your Archipelago install directory

4. Drag and place the `lib` folder downloaded from releases straight to your Archipelago main directory. **This is necessary as the `dolphin_memory_engine` in this release is what works for this current implementation!!!**

5. Either copy the GMSE01.ini file that came with the download from releases into your Dolphin's GameSettings folder or copy the contents of it into the properities of your iso, in the Editor tab. **Make sure to have cheats enabled on Dolphin**

## Create a Config (.yaml) File

### What is a config file and why do I need one?

Your config file contains a set of configuration options which provide the generator with information about how it
should generate your game. Each player of a multiworld will provide their own config file. This setup allows each player
to enjoy an experience customized for their taste, and different players in the same multiworld can all have different
options.

### Where do I get a config file?

Run the ArchipelagoLauncher.exe from your Archipelago install and click `Generate Template Options`.
This will produce a `/Players/Templates` folder in your Archipelago install, which contains default config files for 
every game in your `custom_worlds` folder. You can manually edit the config file using a text editor of your choice.

### Verifying your config file

If you would like to validate your config file to make sure it works, you may do so on the
[YAML Validator](/mysterycheck) page.

## Generating a Single-Player Game

1. After modifying your yaml, place it into your Archipelago/player folder
   - Alternately, navigate to the [Player Settings](../player-settings) page, configure your options,
      and click the "Generate Game" button.
2. Open the Archipelago Launcher and click "Generate". This will create a zip file in Archipelago/output
3. Navigate to the Archipelago website and go to the Host Game page
4. Click upload file and pass it the .zip created in your output folder
5. Click the "Create New Room" link.
6. Open Dolphin and from Dolphin, open your Super Mario Sunshine ISO. Load up until you are in the File Select screen.
   - Ensure that "Enable GPU Overclock" and "Emulated Memory Size Override" are both off in your Dolphin settings
7. Open up your SMSClient from within your Archipelago Launcher
   - If you don't see the client in the Archipelago Launcher you did not properly set up the APWorld into `custom_worlds` folder, make sure it is the only one present and there isn't another sms.apworld inside your `lib`, for example
   - **MAKE ABSOLUTE SURE THE CLIENT IS OPENED AFTER THE GAME HAS STARTED, AT THE LEAST.** Preferably while in File Select 
8. In the server page, there will be a port number. Copy this port number into the top of your SMSClient. 
   - The field should read `archipelago.gg:<port number>`
9. Once you have loaded into the game, click the `Connect` button at the top of the SMSClient. Once it says you are connected you're free to play, choose a brand new file and start playing!

## Joining a MultiWorld Game

### Setup your .ini and ROM

When you join a multiworld game, you will be asked to provide your config file to whoever is hosting. Once that is done,
the host will provide you with a link to the room or the address and port necessary to connect.
**SMS at the moment does not require a patch of any kind to play in Archipelago, it works with the cheat codes provided from the .ini that is within the downloaded .zip from releases**

### Connect to the client

Open up your SMSClient and connect as per you would in a single player session. Any time you would need to connect to a new game it is necessary to relaunch the client once your game is back on the File Select Screen.

1. Open Dolphin and from Dolphin, launch your Super Mario Sunshine ISO (Don't forget to have Cheats enabled)
2. Open your SMSClient, making sure to launch it only after you've launched Super Mario Sunshine and are waiting in the File Select. In the server page, there will be a port number. Copy this port number into the top of your SMSClient. 
   - The field should read `archipelago.gg:<port number>`
3. Once you have loaded into the game, the client should log that Dolphin has been connected. Click the `Connect` button
at the top of the SMSClient. If the port number is correct, you are now connected and ready to play!

### Play the game

Remember to start the game up and have it fully running **BEFORE** opening the client at all.