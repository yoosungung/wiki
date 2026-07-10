export const STORAGE_KEY = "km-sidebar-width"
export const DEFAULT_WIDTH = 320
export const MIN_WIDTH = 240
export const MAX_WIDTH = 480

export function clampWidth(width) {
  const n = Number(width)
  if (!Number.isFinite(n)) return DEFAULT_WIDTH
  return Math.min(MAX_WIDTH, Math.max(MIN_WIDTH, Math.round(n)))
}

export function parseStoredWidth(raw) {
  if (raw === null || raw === undefined || raw === "") return DEFAULT_WIDTH
  return clampWidth(parseInt(String(raw), 10))
}
