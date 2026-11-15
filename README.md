# Salvatore's Sinking Ships 🌊

A Discord bot that lets you play the minigame "Sinking Ships" from The Ledgend of Zelda: The Wind Waker, directly within Discord! 

## 🎮 Game Overview

Navigate a grid and sink all the hidden "Squids" before you run out of ammo. 

- **Sunk Squids:** 3
- **Ammo:** 30
- **Controls:** Use the interactive buttons to move the cursor and shoot!

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A Discord Bot Token

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sinking-ships
   ```

2. Install the required dependencies:
   ```bash
   pip install discord.py python-dotenv
   ```

3. Configure your environment:
   - Create a `.env` file in the root directory.
   - Add your Discord Bot Token:
     ```env
     DISCORD_TOKEN=your_token_here
     ```

### Running the Bot

Start the bot by running the main script:
```bash
python main.py
```

## 🕹️ How to Play

1. Invite the bot to your Discord server.
2. Use the `/start_game` command to begin a new match.
3. Use the directional buttons (⬆️, ⬇️, ⬅️, ➡️) to move your cursor (🏹).
4. Press the **SHOOT** (🔥) button to attack the current position.
5. **Win:** Sink all 3 squids!
6. **Loss:** Run out of ammo or press **End** (❌) to reveal the hidden squids.

## 🛠️ Technologies Used

- **Python**
- **discord.py**: For Discord bot integration.
- **python-dotenv**: For managing environment variables.

## 📜 License

This project is open-source.
