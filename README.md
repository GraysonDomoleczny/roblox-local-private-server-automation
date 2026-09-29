# Roblox Server Automation Tool

A Python-based automation tool for managing Roblox private servers. The tool uses PyAutoGUI and image recognition to navigate the Roblox website and automate server configuration tasks.

Currently, it supports disabling server joining and renaming private servers, with potential for additional features in the future.

## Features

* Automates disabling and renaming Roblox private servers
* Uses image recognition to locate and interact with buttons and settings
* Can process multiple pages of private servers
* Configurable server name and number of pages to process
* Includes reference images required for automation
* Handles servers that cannot be found or do not support the required settings

## Technologies

* **Python**
* **PyAutoGUI** – Mouse and keyboard automation
* **PyAutoGUI Image Recognition** – Locates interface elements using reference images

## Requirements

Due to its reliance on screen-based automation, the tool requires a specific environment to work correctly.

### Operating System

* Windows 10 recommended
* Display scaling should be set to **100%**

### Browser

* Google Chrome
* Browser zoom should be set to **100%**
* The tool is designed for the Roblox website and does not support the Roblox desktop application

### Roblox

* Requires access to Roblox private servers
* The tool is designed for the browser version of Roblox

## Reference Images

The `ReferenceImages` folder contains the screenshots used by the program to identify buttons and other elements on the Roblox website.

If an image fails to be recognized, a replacement can be created by taking a screenshot of the corresponding element and saving it with the **exact filename** expected by the program.

Changes to browser zoom, display scaling, or the Roblox interface may require new reference images.

## Usage

1. Install the required Python dependencies.
2. Set Windows display scaling to 100%.
3. Set Chrome zoom to 100%.
4. Open Roblox in Google Chrome.
5. Configure the desired server name and number of pages in the program.
6. Run the program and allow it to navigate and configure the servers.

## Limitations

Because the tool relies on screen coordinates and image recognition, it is sensitive to changes in:

* Screen resolution
* Windows display scaling
* Browser zoom
* Roblox's website layout
* Browser window position
* Reference images

The tool may need to be updated if Roblox changes its website interface.

## Project Purpose

This project was created to practice Python automation, GUI interaction, image recognition, and handling repetitive tasks through programmatic input.
