# BC Pro → Forma Bid Feature Tracker

A temporary reference page for customers tracking which BuildingConnected Pro features are available in Forma Bid. Intended to provide clarity during the transition period as functionality moves from BuildingConnected Pro into the Forma platform.

## Live site

**https://cdkintz.github.io/bc-pro-forma-tracker/**

## Updating content

All content is driven by `data.json`. To make changes:

1. Start the local server: `python3 server.py`
2. Open `http://localhost:8899` — the page is fully editable (click any text, click status pills to cycle them)
3. Click **Save data.json** when done
4. Push to GitHub:
   ```
   git add -A && git commit -m "update tracker" && git push
   ```
5. The live site updates automatically within ~60 seconds

The editing UI only appears on localhost. The public site is read-only.

## Taking the site down

To remove public access immediately:

```
gh repo edit cdkintz/bc-pro-forma-tracker --visibility private --accept-visibility-change-consequences
```
