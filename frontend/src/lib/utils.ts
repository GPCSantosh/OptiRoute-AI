import { clsx, type ClassValue } from "clsx"

// Lightweight fallback for environments where 'tailwind-merge' types
// are unavailable. This preserves existing behavior by returning
// the computed class string. If 'tailwind-merge' is installed with
// types, replace this with: import { twMerge } from "tailwind-merge"
export function cn(...inputs: ClassValue[]) {
  return clsx(inputs)
}
