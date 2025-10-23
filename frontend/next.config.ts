import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "encrypted-tbn0.gstatic.com" },
      { protocol: "https", hostname: "encrypted-tbn1.gstatic.com" },
      { protocol: "https", hostname: "encrypted-tbn2.gstatic.com" },
      { protocol: "https", hostname: "encrypted-tbn3.gstatic.com" },
    ],
    formats: ["image/avif", "image/webp"],
  },
  // (Optional) silence the workspace root warning by pointing Turbopack to frontend
  // experimental: { turbo: { root: __dirname } },
};

export default nextConfig;
