# interactive-sorting-quiz
An interactive command-line application that tests and validates step-by-step logic for sorting algorithms. Developed for the VITyarthi flipped course evaluation.
# 🎩 Hogwarts Sorting Quiz

A fun, interactive command-line quiz that sorts you into your true Hogwarts house — Gryffindor, Hufflepuff, Ravenclaw, or Slytherin — based on how you'd react to classic wizarding-world scenarios.

## ✨ Features

- ASCII art Sorting Hat that greets you when the program starts
- A short introduction to each of the four Hogwarts houses before the quiz begins
- 8 scenario-based multiple-choice questions inspired by the wizarding world
- Input validation that keeps asking until you enter a valid A, B, C, or D
- A tie-breaking system so you always get a clear result

## 🧙 How it works

Each answer adds a point to one of the four houses. After all questions are answered, the house with the highest score is revealed as yours. If there's a tie, the Sorting Hat favors Gryffindor, then Hufflepuff, then Ravenclaw, then Slytherin.

## 🚀 Getting started

**Requirements:** Python 3.6+ (no external packages needed)

```bash
python3 hogwarts_sorting_quiz.py
```

Answer each question with A, B, C, or D and press Enter. At the end, the Sorting Hat will reveal your house!

## 🛠️ Customize it

Want to add your own questions? Follow the pattern already used in the script:
1. Add a `print()` block with your scenario and A–D options
2. Add a matching `while True:` input loop that increments the right house's score
3. Drop it in anywhere between Question 1 and the final scoring section

## 📜 Disclaimer

This is an unofficial, fan-made project created for fun and educational purposes. Harry Potter, Hogwarts, and all related names and terms are trademarks of Warner Bros. Entertainment Inc. and J.K. Rowling. This project is not affiliated with, endorsed by, or connected to the official Wizarding World franchise.

## 📄 License

Feel free to fork, modify, and share. Add a license of your choice (MIT is a common, permissive option) if you plan to share this more widely.
