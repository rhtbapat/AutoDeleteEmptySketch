# Auto Delete Empty Sketch — Autodesk Fusion Add-In

> Automatically keep Autodesk Fusion designs clean by deleting empty sketches whenever you click **Finish Sketch** — no buttons, dialogs, or configuration required.

---

## ✨ Features

* **Automatic cleanup** — detects and deletes empty sketches whenever **Finish Sketch** is clicked
* **Zero-click workflow** — no separate cleanup command needs to be run
* **No configuration required** — simply enable the add-in and continue working normally
* **Active-component cleanup** — checks sketches in the currently active component after finishing a sketch
* **Geometry-aware detection** — checks multiple Fusion sketch curve types before determining that a sketch is empty
* **Dimension-aware** — sketches containing dimensions are preserved
* **Text-aware** — sketches containing sketch text are preserved
* **Silent operation** — cleanup happens automatically without interrupting your workflow with dialogs
* **Startup support** — configured to start automatically with Fusion
* **Cross-platform** — supports both Windows and macOS
* **Simple enable/disable behavior** — run the add-in to enable automatic cleanup and stop it to disable the behavior

---

## 🔍 What Is Considered an Empty Sketch?

Auto Delete Empty Sketch checks sketches for supported sketch geometry, dimensions, and text.

A sketch is considered empty when it contains **none** of the following curve types:

* Lines
* Circles
* Arcs
* Ellipses
* Fitted splines
* Fixed splines
* Conic curves

The sketch must also contain:

* **No sketch dimensions**
* **No sketch text**

If all of these conditions are met, the sketch is automatically deleted.

---

## ⚙️ How It Works

The add-in listens for Fusion's **Finish Sketch** command.

When you click **Finish Sketch**:

1. Fusion finishes the current sketch
2. Auto Delete Empty Sketch detects that the **Finish Sketch** command has completed
3. The add-in accesses the currently active component
4. It checks the sketches in that component
5. Each sketch is inspected for:

   * Sketch curves
   * Dimensions
   * Sketch text
6. Sketches meeting the empty-sketch criteria are collected
7. Those sketches are automatically deleted

There are no additional buttons or confirmation dialogs — cleanup happens as part of the normal sketch workflow.

---

## 🚀 Installation

1. Download or clone this repository

2. Place the folder containing:

   * `DeleteEmptySketch.py`
   * `DeleteEmptySketch.manifest`

   in your Fusion add-ins directory:

   * **Mac:** `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/`
   * **Windows:** `%APPDATA%\Autodesk\Autodesk Fusion 360\API\AddIns/`

3. In Fusion, open **Utilities → Scripts and Add-Ins** (or press `Shift+S`)

4. Switch to the **Add-Ins** tab

5. Select **DeleteEmptySketch**

6. Click **Run**

The included manifest has `runOnStartup` set to `true`, so after installation the add-in is configured to start automatically when Fusion launches.

---

## 🎯 How to Use

Once the add-in is running, there is nothing else to configure.

1. Create or edit a sketch in Fusion
2. Add geometry as usual — or leave the sketch empty
3. Click **Finish Sketch**
4. If a sketch in the active component meets the empty-sketch criteria, it is automatically deleted
5. Continue modeling normally

That's it.

There is no toolbar command, settings dialog, tolerance, or cleanup window to manage.

---

## 🔄 Enable / Disable

### Enable

Open **Scripts and Add-Ins**, select **DeleteEmptySketch**, and click **Run**.

Once running, the add-in monitors the **Finish Sketch** command automatically.

### Disable

Open **Scripts and Add-Ins**, select **DeleteEmptySketch**, and click **Stop**.

Stopping the add-in removes the event listener, and empty sketches will no longer be automatically deleted.

---

## 💡 Why Use It?

It is easy to accidentally create empty sketches while:

* Starting a sketch and immediately cancelling the intended geometry
* Experimenting with different modeling approaches
* Creating temporary construction sketches
* Reworking existing geometry
* Deleting all geometry from an existing sketch
* Iterating quickly during design

These unused sketches can gradually clutter the Fusion Browser and make larger designs harder to navigate.

Auto Delete Empty Sketch handles that housekeeping automatically so you can focus on modeling instead of manually removing unused sketches.

---

## ⚠️ Notes

* The add-in performs its check when Fusion's **Finish Sketch** command completes.
* It checks sketches in the **currently active component**.
* Cleanup is automatic and does not ask for confirmation before deleting an empty sketch.
* Sketches containing supported curves, dimensions, or sketch text are preserved.
* The current implementation does **not** include sketch points in its empty-sketch test. A sketch containing only sketch points may therefore be considered empty.
* Because the add-in checks sketches in the active component, cleanup is not necessarily limited only to the sketch you just finished.
* A `run.log` file is created in the add-in directory for basic runtime and error logging.
* The add-in is configured to run automatically when Fusion starts.
* Supported operating systems are Windows and macOS.
* The current add-in version is `1.4.0`.

---

## 🆚 Auto Delete Empty Sketch vs. Empty Sketch Finder

These two add-ins serve slightly different workflows:

| Add-In                       | Best For                                                                     |
| ---------------------------- | ---------------------------------------------------------------------------- |
| **Auto Delete Empty Sketch** | Automatically preventing empty sketches from accumulating while you work     |
| **Empty Sketch Finder**      | Scanning an existing design and reviewing empty sketches before bulk cleanup |

Use **Auto Delete Empty Sketch** when you want cleanup to happen continuously in the background as part of your normal modeling workflow.

Use **Empty Sketch Finder** when you want to inspect and clean an existing design on demand.

---

## 📄 License

MIT License — free to use, modify, and distribute.
