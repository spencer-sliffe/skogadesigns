"use client";
import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function HomePage() {
  const router = useRouter();

  useEffect(() => {
    const token = typeof window !== "undefined" ? localStorage.getItem("access") : null;
    if (!token) router.replace("/signin"); // or "/signup"
  }, [router]);

  return (
    <main className="container mx-auto p-8">
      <h1 className="text-3xl font-semibold">Welcome to Skoga Designs</h1>
      <p className="text-red-600">You are not signed in</p>
    </main>
  );
}
