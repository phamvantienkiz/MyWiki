import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        page: "#F5F5F7",
        card: "#FFFFFF",
        subtle: "#F4F4F6",
        subtleHover: "#ECECEF",
        ink: "#111114",
        hairline: "#EFEFF2",
        borderCard: "#E9E9EE",
        textPrimary: "#0B0B0F",
        textSecondary: "#6B6B76",
        textTertiary: "#9A9AA5",
        
        // Sư phạm (Lecture Visualizer)
        intuition: {
          bg: "#F0FDF4",
          border: "#86EFAC",
          text: "#166534",
          accent: "#22C55E",
        },
        discrepancy: {
          bg: "#FEF2F2",
          border: "#FCA5A5",
          text: "#991B1B",
          accent: "#EF4444",
        },
        
        // 7 Miền Tri thức (Domain Palette)
        domain: {
          genai: "#1F5FFF",
          rag: "#B13BF0",
          agentic: "#FF8A1F",
          deeplearning: "#1FA63A",
          mlmath: "#0EA5E9",
          mlops: "#EC4899",
          software: "#64748B",
        },
      },
      borderRadius: {
        card: "28px",
        control: "16px",
        button: "12px",
      },
      boxShadow: {
        card: "0 1px 2px rgba(16, 16, 24, 0.04), 0 8px 24px rgba(16, 16, 24, 0.06)",
        control: "0 1px 2px rgba(16, 16, 24, 0.08), 0 0 0 1px rgba(16, 16, 24, 0.04)",
        primary: "0 6px 16px rgba(16, 16, 24, 0.22)",
      },
      fontFamily: {
        sans: ["Inter", "Geist", "system-ui", "-apple-system", "sans-serif"],
      },
    },
  },
  plugins: [],
};

export default config;
