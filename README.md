# AOD Backup Extractor & Compressor for HyperOS / MIUI

A simple Python toolset to extract, modify, and rebuild Always-On Display (AOD) backup files used in HyperOS / MIUI.

This project was made after discovering that AOD themes are stored inside system backup files and can be modified by unpacking and rebuilding them, since there is no official way to install custom AOD themes directly.

---

# What This Tool Does

This project includes two scripts:

## Extractor (extractor.py)

* Finds any `.bak` file in the same folder
* Automatically extracts its contents
* Keeps the original folder structure intact

## Compressor (compressor.py)

* Takes the modified `apps` folder
* Rebuilds it into a valid `.bak` backup file
* Produces a restore-ready backup for HyperOS / MIUI

---

# How AOD Themes Are Stored

Inside the extracted backup, the AOD data is located here:

Always-on display(com.miui.aod).bak/apps/com.miui.aod/miui_att/data/user_de/0/com.miui.aod/app_themes

Inside the `app_themes` folder, you will find files ending in:

.aodBackup

These are the actual Always on display themes. They are just ZIP files with a renamed extension.

---

# Editing Themes

To modify a theme:

1. Rename `.aodBackup` to `.zip`
2. Extract and edit the contents
3. Repack the ZIP file
4. Rename it back to `.aodBackup`

Important note:

* This method works reliably only when replacing existing themes
* Adding new themes does not consistently make them appear in the system
* So make sure that rename the your custom always on display theme ( if any) with name of a theme already present after removing that theme.

---

# Important Limitation

I tried but was unable to increase the number of themes in the backup.
So the safest method is always replacing existing themes instead of trying to add new ones.
However, anyone is welcome to modify the backup and it would be appreciated if anyone provides any working solution to remedy that.

---

# ⚠️ Critical Compatibility Warning

This tool only works correctly if the backup contains ONLY Always-On Display data.

If you use:

* A mixed backup containing other system data
* Any backup different from the expected structure

Then the restore may fail or behave unpredictably.

---

# ⚠️ Important Restore Warning

Restoring a modified AOD backup will:

* Delete all existing Always-On Display themes
* Replace your entire “My Themes” section

This happens because the backup fully overwrites the AOD theme database.

---

# Strong Recommendation (Very Important)

Before restoring:

* Always create a backup of your current AOD themes
* Make sure you can restore your original setup if needed
* Do NOT restore without a fallback backup

Reason:

* Your existing themes will be completely replaced
* Recovery without backup may require resetting or reinstalling themes

---

# Requirements

* Python 3.8 or newer
* Works on Windows, Linux, and Android (Termux)

No extra libraries required.

---

# Usage Instructions

## 1. Extract Backup

Put these two files in the same folder:

* extractor.py
* Always-on display(com.miui.aod).bak

Then run:
python extractor.py

---

## 2. Modify Themes

Go to:
apps/com.miui.aod/apps/miui_att/data/user_de/0/com.miui.aod/app_themes/

Rename:
.aodBackup → .zip

Edit the files, then rename back to:
.aodBackup

---

## 3. Compress Backup

Put these in the same folder:

* compressor.py
* modified "apps" folder

Then run:
python compressor.py

A new .bak file will be created.

---

# Installing / Restoring on HyperOS

## Important Step

After compression, rename the file exactly to:

Always-on display(com.miui.aod).bak

If the name is wrong, restore will not work.

---

## Move the file to:

MIUI/backup/AllBackup/20251012/

---

## Recommended folder structure:

MIUI/backup/AllBackup/20251012/
                             -----"Always-on display(com.miui.aod).bak"
                             -----"descript.xml"


Important:

* Keep only one backup inside the AllBackup folder as it would avoid searching for the correct backup when restoring.
* Restoration of the backup will also fail if the descript.xml is wrong or not present in the folder with .bak file.
* So use the descript.xml provided

---

# Restore Steps (Phone)

1. Go to Settings
2. Open About phone
3. Tap Backup & Restore
4. Select Mobile Phone
5. Select Restore
6. Choose the backup ( there should be only one backup present if no other backup were present in the AllBackup folder)
7. Restore it
8. Open Always-On Display settings
9. Your modified themes will appear

---

# Compatibility

Tested on:

* HyperOS 3.0.5.0

Other versions may or may not work properly.

---

# Disclaimer

This tool modifies system backup data.

Use at your own risk.

The author is not responsible for:

* failed restores
* corrupted backups
* missing themes
* system instability
* boot issues
* data loss
* HyperOS updates breaking compatibility
* any damage caused by using this tool

Always keep a safe backup before using it.

---

# License (MIT)

This project is open source under the MIT License.

You are free to:

* Use
* Modify
* Share
* Improve
* Fork

---

# Final Notes

* Works on HyperOS 3.0.5.0 (tested)
* Always keep backups before restoring
* Keep backup strictly AOD-only for best results
* System updates may break compatibility in future

---

If you want, I can also convert this into a **perfect GitHub README with badges, headings, and formatting that looks professional and ready to publish.**
