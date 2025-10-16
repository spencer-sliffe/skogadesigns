import type { Metadata } from "next";
import { GeistSans } from "geist/font/sans";
import { GeistMono } from "geist/font/mono";
import "@styles/globals.css";
import ClientApiInit from "@components/client-api-init";

export const metadata: Metadata = {
  title: "Skoga — Jewelry",
  description: "A modern jewelry marketplace.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html
      lang="en"
      className={`${GeistSans.variable} ${GeistMono.variable}`}  // ← exposes --font-geist-*
    >
      <body className="antialiased">
        <ClientApiInit />
        {children}
      </body>
    </html>
  );
}
