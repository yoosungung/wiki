---
title: "ysm-devcpdown 📥 cpdown - Copy to clipboard any webpage contentyoutube subtitle as clean markdown with one click or shortcut"
related_raw: ["[[raw/ysm-devcpdown 📥 cpdown - Copy to clipboard any webpage contentyoutube subtitle as clean markdown with one click or shortcut.md]]"]
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# ysm-devcpdown 📥 cpdown - Copy to clipboard any webpage contentyoutube subtitle as clean markdown with one click or shortcut

## cpdown

[![cpdown logo](https://github.com/ysm-dev/cpdown/raw/main/public/icon/128.png)](https://github.com/ysm-dev/cpdown/blob/main/public/icon/128.png)

*Copy any webpage as clean markdown.*

## Overview

cpdown is a browser extension that allows you to copy the content of any webpage as clean, formatted markdown. If you're on YouTube, you can also copy the subtitle as markdown.

### Demo

Cap.2025-05-21.at.17.13.06.mp4<video src="https://private-user-images.githubusercontent.com/18487241/446318234-cedf05e8-ed1d-4e71-9769-66c9b292fbdd.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODY5NDkwMzYsIm5iZiI6MTc4Njk0ODczNiwicGF0aCI6Ii8xODQ4NzI0MS80NDYzMTgyMzQtY2VkZjA1ZTgtZWQxZC00ZTcxLTk3NjktNjZjOWIyOTJmYmRkLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA4MTclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwODE3VDA2Mzg1NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWEwM2VjMTVkOTc2MmJkOTM5N2VkM2VkMTI2MWMxY2FkNzhiZGMwZDE3Y2QyNjMyZWY1YzRlZjUwYTZkYWQ1YTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT12aWRlbyUyRm1wNCJ9.6dMZoU_5zhKq6Qn6sMEX8nvWqbUi6bOtN_X5KYDQpoM" controls="controls"></video>

## Features

- 📋 Copy any webpage content as clean markdown with one click (or keyboard shortcut)
- 📋 Copy YouTube subtitle as clean markdown with one click (or keyboard shortcut)
- 📖 Uses Defuddle or Mozilla's Readability to extract the main content
- 🔍 Removes unnecessary HTML elements (scripts, styles, iframes, etc.)
- 🔢 Shows token count for the copied content (for LLM)
- ⌨️ Keyboard shortcut support

## Installation

- Chrome: [Chrome Web Store](https://chromewebstore.google.com/detail/cpdown/knnaflplggjdedobhbidojmmnocfbopf)
- Firefox: [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/cpdown/)

## Options

Go to chrome://extensions/?options=knnaflplggjdedobhbidojmmnocfbopf or click the "Options" link in the extension's details page to configure cpdown after installation.

[![](https://github.com/ysm-dev/cpdown/raw/main/.github/assets/options.png)](https://github.com/ysm-dev/cpdown/blob/main/.github/assets/options.png)

### Manual Installation

1. Clone this repository
2. Install dependencies:
	```
	bun i
	```
3. Build the extension:
	```
	bun run build
	```
4. Load the unpacked extension:
	- Open Chrome/Edge and navigate to `chrome://extensions`
		- Enable "Developer mode"
		- Click "Load unpacked" and select the `.output/chrome-mv3` directory

## Usage

1. Navigate to any webpage you want to copy
2. Click the cpdown icon in your browser toolbar, or use the keyboard shortcut
3. The page content will be copied to your clipboard as markdown
4. Paste the markdown content anywhere you need it

## Settings

cpdown offers several configuration options:

- **Use Defuddle**: Use Defuddle to clean up the markdown output
- **Use Mozilla Readability**: Parse webpage content using Readability for cleaner markdown output
- **Wrap in Triple Backticks**: Wrap the copied content in triple backticks for better readability
- **Show Success Toast**: Display a notification when content is successfully copied
- **Show Raycast Confetti**: Celebrate successful copying with a confetti animation (for Raycast users)

## Development

This extension is built with:

- [Cursor](https://www.cursor.com/) - For the vibe coding
- [WXT](https://wxt.dev/) - The Web Extension Toolkit
- [React](https://react.dev/) - For the options UI
- [Shadcn UI](https://ui.shadcn.com/) - For the options UI
- [Sonner](https://sonner.emilkowal.ski/) - For the toast notifications
- [Tailwind CSS](https://tailwindcss.com/) - For styling
- [Defuddle](https://github.com/kepano/defuddle) - For main content extraction & markdown cleanup
- [Mozilla Readability](https://github.com/mozilla/readability) - For main content extraction
- [Turndown](https://github.com/mixmark-io/turndown) - For HTML to Markdown conversion
- [tiktoken](https://github.com/dqbd/tiktoken) - For token counting

### Development Commands

```
bun run dev
```

## Star History

[![Star History Chart](https://camo.githubusercontent.com/c54baffd535a74897a37750d73ab5be57b1f7396dcdbe80e20759104c9b66152/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d79736d2d6465762f6370646f776e26747970653d44617465)](https://www.star-history.com/#ysm-dev/cpdown&Date)

## License

[MIT](https://github.com/ysm-dev/cpdown/blob/main/LICENSE)

---
- **Source:** Unknown
