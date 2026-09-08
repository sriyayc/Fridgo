# Fridgo 

Ever open the fridge, stare at a random pile of vegetables, and have absolutely no idea what to make? That's the exact problem Fridgo tries to solve.

Snap a photo of whatever's in your fridge, and Fridgo tells you what vegetables it sees and throws back a few recipe ideas you could actually make with them — calories included, so you're not just guessing there either.

It's built on Streamlit for the interface and Google's Gemini 1.5 Flash model for the actual "looking at the photo and figuring out what's edible" part.

---

## What it does

- You upload a picture of your veggies
- It identifies what's in there
- It suggests a handful of recipes — veg and non-veg — using those ingredients
- It gives you a rough calorie count per recipe
- If you've got allergies or a health condition you're managing, you can mention it and it'll try to steer around that

It's not going to replace a nutritionist or a doctor. Think of it more as "what can I cook with this" on a lazy evening.

---

## Getting it running

**1. Grab the code**
```bash
git clone https://github.com/sriyayc/Fridgo.git
cd Fridgo
```

**2. Install what it needs**
```bash
pip install streamlit pillow google-generativeai python-dotenv
```

**3. Get yourself an API key**

This runs on Google's Gemini API, so you'll need your own key. Head to [Google AI Studio](https://aistudio.google.com/), grab a free key.

Once you have it, make a `.env` file in the project folder:
```
GOOGLE_API_KEY=paste_your_key_here
```

There's a `.env.example` file in the repo showing exactly what that should look like.

**Do not put your key directly in the code.** It'll get accidentally committed to git and then it's out in the world. Learned that one the hard way.

**4. Run it**
```bash
streamlit run fridge.py
```

It'll pop open in your browser.

---

## How to use it

1. If you've got allergies, type them in.
2. If there's a health thing you're working around, mention that too.
3. Upload a photo — just needs to have some vegetables visible.
4. Hit Submit.
5. Read what it found and pick something that sounds good.

---

## Built with

- **Streamlit** — for the whole front-end, no HTML/CSS needed
- **Gemini 1.5 Flash** — does the actual image recognition and recipe writing
- **Pillow** — handles the image on the Python side
- **python-dotenv** — keeps the API key out of the code

---

## A couple of honest notes

- The calorie numbers are AI estimates, not lab-tested nutrition facts. Close enough for casual cooking, not close enough for anything medical.
- Image recognition isn't perfect — weird lighting or an overly cluttered fridge shot might trip it up.
- This started as a small personal project, so don't expect production-grade error handling everywhere.
