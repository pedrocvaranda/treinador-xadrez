# Chess Trainer — Queen's Gambit

**Interactive terminal-based chess trainer focused on the Queen's Gambit, with strategic move analysis and smart hints**

---

## What is This?

This is an **interactive chess trainer written in Python**, designed for learning and practicing classic openings in a didactic and engaging way, entirely in the terminal.

**Key Features:**

- **Trainer Mode** — teaches the Queen's Gambit step by step, explaining the strategic intent behind each move
- **Free Intelligent Mode** — play any opening freely; the system evaluates your moves and flags strategic weaknesses
- **On-demand hints** — detailed hints available at any time via the `hint` command
- **Board visualization** — updated board printed to the terminal after every move

---

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/pedrocvaranda/treinador-xadrez.git
cd treinador-xadrez

# Install dependency
pip install chess

# Run the trainer
python treinador_xadrez.py
```

### Your First Move

```text
Welcome to the Chess Trainer
Trainer Mode: focus on the Queen's Gambit

Current board:
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R

Your move: d4
You played: d4
Explanation: You are controlling the center of the board — a great foundation for dominating the game.
```

---

## Game Modes

### Mode 1 — Trainer (Queen's Gambit)

The trainer guides you through the Queen's Gambit sequence, explaining the strategic idea behind every move. Perfect for beginners who want to learn opening structure and principles.

### Mode 2 — Free Intelligent Mode

Play any opening freely. The system evaluates your moves in real time, pointing out misplaced pieces or strategic weaknesses. Detailed hints only appear when you type `hint`.

### Available Commands

| Command | Action |
|---------|--------|
| `d4`, `c4`, `Nf3` | Play a move in SAN notation |
| `hint` | Receive a strategic explanation |
| `quit` | Exit the game |

---

## Project Structure

```text
treinador-xadrez/
├── README.md
├── LICENSE
└── treinador_xadrez.py    # Core logic: modes, board, move analysis
```

---

## Examples

### Example 1: Queen's Gambit Sequence

```text
Your move: d4   → Central control
Your move: c4   → Queen's Gambit offered
Your move: Nc3  → Natural development
```

### Example 2: Free Mode with Hint

```text
Your move: e4
> Move accepted. King's Pawn Opening.

Your move: hint
> Hint: Consider developing your knight to f3 to pressure the center
  and prepare to castle. Pieces in the center control more squares.
```

---

## Prerequisites

- Python 3.7 or higher
- `python-chess` library

---

## About the Author

**Pedro Coutinho Varanda**

- **#1 Brazil** — National Astronomy Olympiad (OBA 2025, Perfect Score)
- **#2 Brazil** — OBA 2023
- **#3 Brazil** — OBA 2024
- **3x Selected** — International Olympiad on Astronomy and Astrophysics (IOAA)
- **4x Gold** — Canguru Mathematics Competition (2022–2025)

ML/AI enthusiast | Rio de Janeiro, Brazil

[GitHub](https://github.com/pedrocvaranda) • [ORCID](https://orcid.org/0009-0004-5199-1745) • [Email](mailto:pedrocvaranda@gmail.com)

---

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Related Projects

- [Varandian Optics Simulator](https://github.com/pedrocvaranda/varadian-optics-simulator) — Light propagation simulator in curved spaces
- [Cash Allocation Model](https://github.com/pedrocvaranda/modelo_alocacao_caixa) — ML-based financial optimizer

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18529071-blue?style=flat&logo=doi)](https://doi.org/10.5281/zenodo.19040991)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) [![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/pedrocvaranda/treinador-xadrez)
