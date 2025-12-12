To run the modular, multi-file version of the project you just implemented, follow these steps on your VS Code

### Step 1: Create the Project Folder

1.  Create a new folder on your Desktop (or anywhere you like) named `Connect4_Project`.
2.  Open **VS Code**.
3.  Go to **File \> Open Folder...** and select `Connect4_Project`.

### Step 2: Create the 4 Python Files

Inside VS Code, create four new files in that folder and paste the code I provided in the previous answer into them. **The filenames must match exactly**:

  * `settings.py`
  * `board.py`
  * `ai.py`
  * `main.py`

### Step 3: Install Dependencies

You need the `pygame` and `numpy` libraries. Open the VS Code terminal (Control + `~`) and run:

```bash
pip install pygame numpy
```

*(If you used `pygame-ce` earlier to fix the error, that is fine too).*

### Step 4: Run the Game

In the terminal, make sure you are in the folder where your files are, then run:

```bash
python main.py
```

### Step 5: How to Play

1.  **The Menu:** The game will start with a black screen with text options.
      * Press **`1`** on your keyboard for **Human vs AI**.
      * Press **`2`** on your keyboard for **Human vs Human**.
2.  **The Board:**
      * **Move:** Slide your mouse left/right to position your piece.
      * **Drop:** Click the left mouse button to drop the piece.
      * **Win:** If someone wins, the game announces it and closes automatically after 3 seconds.
  

![Image 11-12-25 at 4 26 PM](https://github.com/user-attachments/assets/1c2a65a7-2b3a-4c70-8ca4-d41d35f5d456)
![Image 11-12-25 at 4 26 PM](https://github.com/user-attachments/assets/5b59acbc-731e-4f6f-9380-1825b78f61be)
