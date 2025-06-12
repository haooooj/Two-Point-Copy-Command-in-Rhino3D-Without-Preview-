# Two-Point Copy Command in Rhino3D (Without Preview)

This Rhino script performs a fast and efficient **2-point copy** by translating geometry along a vector defined by two user-specified points — all **without any live preview**. It is optimised for heavy models or repetitive workflows where viewport responsiveness is critical.

## What Does the Script Do?

The **Two-Point Copy** tool:

* Prompts you to select one or more objects.
* Lets you specify a **base point** (starting location).
* Lets you specify a **target point** (destination).
* Internally computes the vector from base to target and copies the geometry by that amount.

Unlike Rhino’s standard `Copy` command, this script **does not preview the object in real time**. This avoids UI lag and improves performance in complex models.

## Why Use It?

This tool is especially useful when:

* Working with **heavy geometry** or **dense scenes**.
* You require a **predictable copy operation** with **fixed input points**.
* Live previews cause delay or freezing on complex models.

By removing preview rendering during point selection, this version provides a streamlined, responsive workflow.

## How to Use the Script

### Load the Script in Rhino

**Method 1**:

1. Type `_RunPythonScript` in the command line.
2. Browse to the location where you saved the script and select it.

### Method 2 Creating a Button or Alias for Easy Access (Optional)

#### Creating a Toolbar Button

1. **Right-click** on an empty area of the toolbar and select **New Button**.
2. In the **Button Editor**:

   * **Left Button Command**:

     ```plaintext
     ! _-RunPythonScript "FullPathToYourScript\two_point_copy.py"
     ```

     Replace `FullPathToYourScript` with the actual path to your script file.
   * **Tooltip**: For example: `Copy objects with two-point vector (no preview)`.
   * **Icon (Optional)**: You can assign a custom icon if desired.

#### Creating an Alias

1. Go to **Tools > Options > Aliases**.

2. Create a new alias:

   * **Alias**: For example, `copy2p`
   * **Command Macro**:

     ```plaintext
     _-RunPythonScript "FullPathToYourScript\two_point_copy.py"
     ```

3. Use the alias by typing `copy2p` into the command line.

### Using the Command

1. **Select** the objects to copy.
2. **Click** to specify the **base point**.
3. **Click** again to specify the **target point**.
4. The script will instantly create copies by translating the selected geometry along the defined vector — with **no preview or live dragging**.

An undo record is created for the operation, allowing full reversal in one step.

## Key Advantage: No Preview Lag

This script eliminates real-time transformation previews. That means:

* No ghost geometry following the cursor.
* Faster input response.
* Ideal for scripting workflows, fabrication prep, and heavy geometry manipulation.
