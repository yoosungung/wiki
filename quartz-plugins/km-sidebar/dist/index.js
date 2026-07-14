import fs from "fs"
import path from "path"
import { fileURLToPath } from "url"
import {
  STORAGE_KEY,
  DEFAULT_WIDTH,
  MIN_WIDTH,
  MAX_WIDTH,
  clampWidth,
  parseStoredWidth,
} from "../logic.js"

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const SIDEBAR_CSS = fs.readFileSync(path.join(__dirname, "../sidebar.css"), "utf8")

const CLIENT_SCRIPT = `
(function () {
  const STORAGE_KEY = ${JSON.stringify(STORAGE_KEY)};
  const DEFAULT_WIDTH = ${DEFAULT_WIDTH};
  const MIN_WIDTH = ${MIN_WIDTH};
  const MAX_WIDTH = ${MAX_WIDTH};

  function clampWidth(width) {
    const n = Number(width);
    if (!Number.isFinite(n)) return DEFAULT_WIDTH;
    return Math.min(MAX_WIDTH, Math.max(MIN_WIDTH, Math.round(n)));
  }

  function applyWidth(px) {
    document.documentElement.style.setProperty("--km-sidebar-width", px + "px");
  }

  function readAppliedWidth() {
    const raw = getComputedStyle(document.documentElement).getPropertyValue("--km-sidebar-width");
    return clampWidth(parseInt(raw, 10));
  }

  function setTruncatedTitles(root) {
    const scope = root || document;
    scope.querySelectorAll(".explorer-content a, .folder-container div > a, .backlinks ul li > a").forEach((el) => {
      const text = el.textContent?.trim();
      if (text) el.setAttribute("title", text);
    });
    scope.querySelectorAll(".folder-container div > button span").forEach((el) => {
      const text = el.textContent?.trim();
      if (text) el.setAttribute("title", text);
    });
  }

  function ensureHandle(sidebar) {
    let handle = sidebar.querySelector(".km-sidebar-handle");
    if (!handle) {
      handle = document.createElement("div");
      handle.className = "km-sidebar-handle";
      handle.setAttribute("aria-hidden", "true");
      sidebar.appendChild(handle);
    }
    return handle;
  }

  function initResize() {
    if (window.matchMedia("(max-width: 799px)").matches) return;

    const sidebar = document.querySelector(".sidebar.left");
    if (!sidebar) return;

    const saved = localStorage.getItem(STORAGE_KEY);
    applyWidth(saved ? clampWidth(parseInt(saved, 10)) : DEFAULT_WIDTH);

    const handle = ensureHandle(sidebar);
    let dragging = false;

    handle.addEventListener("mousedown", (event) => {
      dragging = true;
      event.preventDefault();
    });

    document.addEventListener("mousemove", (event) => {
      if (!dragging) return;
      applyWidth(clampWidth(event.clientX));
    });

    document.addEventListener("mouseup", () => {
      if (!dragging) return;
      dragging = false;
      localStorage.setItem(STORAGE_KEY, String(readAppliedWidth()));
    });
  }

  function boot() {
    initResize();
    setTruncatedTitles(document);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  document.addEventListener("nav", () => {
    setTruncatedTitles(document);
    initResize();
  });
})();
`

export default function KmSidebar() {
  return {
    name: "KmSidebar",
    async *emit() {},
    externalResources() {
      return {
        css: [{ content: SIDEBAR_CSS, inline: true }],
        js: [
          {
            loadTime: "afterDOMReady",
            contentType: "inline",
            script: CLIENT_SCRIPT,
          },
        ],
      }
    },
  }
}

export { clampWidth, parseStoredWidth }
