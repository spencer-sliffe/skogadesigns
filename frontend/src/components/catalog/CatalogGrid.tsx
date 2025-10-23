"use client";

import * as React from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import CatalogItemCard from "./CatalogItemCard";

/** Mocked items for now; later map API -> this shape */
const MOCK_ITEMS = [
  {
    id: "ring-halo-1",
    name: "Halo Diamond Ring",
    price_cents: 129000,
    image_url:
      "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcTtQCyLQqMT4NMb7wQNrxuZFeFpMJPYHQNcxI69mHRMQ-Gfj44HF5MKlsL4JRAw0zX-uBYaQQop0DuYdXCVxUIDr9a-1CUJ0GEEDI0O7dhzEG-V_R9Ard7D9_IB",
    badge: "New",
  },
  {
    id: "necklace-pearl-1",
    name: "Pearl Drop Necklace",
    price_cents: 89000,
    image_url:
      "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSonQkZ861rCjf00n7FZ6Rvw3dwDI15MbTg_ABsA_1w9KSalFrZROb_OWrfXwUc07j0k8rKO-YlJ0f6hNvRDC31DOi9XDQMG5jKIXhchQ30CKQE_X7SGhIU",
  },
  {
    id: "bracelet-gold-1",
    name: "18K Gold Bracelet",
    price_cents: 74000,
    image_url:
      "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQyRbk-QclMc91lOznDbqkIq4c5UbjtJ6f79O8CNovbxU0sy2TkOgrmBRuv8LbbYXCKi5IavqaSjseaUDhHsW7vRKnG_WznfeR-jZCZLY9K97A486HUiTOwLA",
    badge: "Bestseller",
  },
  {
    id: "earrings-sapphire-1",
    name: "Sapphire Stud Earrings",
    price_cents: 56000,
    image_url:
      "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQHufFAozllPAapHjJIccgqsUg7fnd2__Sp7NeBhgnyWAaJohlaG1naykzTQi_m4aDbPs_DTch7Zwqiw9FaJOyo_xAaOZUmAoIwPPj3zFE3a14GninwEChC",
  },
];

export default function CatalogGrid() {
  const [query, setQuery] = React.useState("");

  const items = React.useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return MOCK_ITEMS;
    return MOCK_ITEMS.filter((i) => i.name.toLowerCase().includes(q));
  }, [query]);

  return (
    <section className="container mx-auto px-6 py-10">
      <header className="mb-8 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 className="text-2xl font-semibold">Catalog</h1>
          <p className="text-sm text-muted-foreground">Browse jewelry (mocked for now).</p>
        </div>
        <div className="flex w-full max-w-md items-center gap-2">
          <Input
            placeholder="Search catalog…"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          {/* outline → border via Tailwind */}
          <Button className="border" onClick={() => setQuery("")}>
            Clear
          </Button>
        </div>
      </header>

      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {items.map((item) => (
          <CatalogItemCard key={item.id} item={item} />
        ))}
      </div>
    </section>
  );
}
