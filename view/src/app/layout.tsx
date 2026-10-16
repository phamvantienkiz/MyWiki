import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Engineer Knowledge Wiki — Andrej Karpathy Style",
  description: "Personal Knowledge Graph & Pedagogical Wiki for AI Engineers with 48 Core Concepts across 7 Domains.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="vi">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="antialiased selection:bg-[#1F5FFF]/20 selection:text-[#0B0B0F]">
        {children}
      </body>
    </html>
  );
}
