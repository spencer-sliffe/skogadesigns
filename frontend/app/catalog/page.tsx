"use client";

import * as React from "react";
import Image from "next/image";
import Link from "next/link";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";

/** Shape aligned to your generated models (snake_case) */
type CatalogItem = {
  id: number | string;
  name: string;
  price_cents: number;
  image_url: string;
  badge?: string;
};

const MOCK_ITEMS: CatalogItem[] = [
  {
    id: "ring-halo-1",
    name: "Halo Diamond Ring",
    price_cents: 129000,
    image_url:
      "https://images.unsplash.com/photo-1603566234499-78f3810d5b16?q=80&w=1600&auto=format&fit=crop",
    badge: "New",
  },
  {
    id: "necklace-pearl-1",
    name: "Pearl Drop Necklace",
    price_cents: 89000,
    image_url:
      "https://images.unsplash.com/photo-1599643477877-530eb83abc8e?q=80&w=1600&auto=format&fit=crop",
  },
  {
    id: "bracelet-gold-1",
    name: "18K Gold Bracelet",
    price_cents: 74000,
    image_url:
      "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?q=80&w=1600&auto=format&fit=crop",
    badge: "Bestseller",
  },
  {
    id: "earrings-sapphire-1",
    name: "Sapphire Stud Earrings",
    price_cents: 56000,
    image_url:
      "https://images.unsplash.com/photo-1606670952191-4e9b88da1f0d?q=80&w=1600&auto=format&fit=crop",
  },
];

/** Local component; NOTE: prop is { item }, and we guard missing props */
function CatalogItemCard({ item }: { item?: CatalogItem }) {
  if (!item) {
    return (
      <Card className="p-6 text-center text-muted-foreground">
        <p>Item not available</p>
      </Card>
    );
  }

  const price = ((item.price_cents ?? 0) / 100).toLocaleString(undefined, {
    style: "currency",
    currency: "USD",
  });

  return (
    <Card className="overflow-hidden hover:shadow-lg transition-shadow">
      <CardHeader className="p-0">
        <div className="relative aspect-[4/3] bg-muted">
          <Image
            src={item.image_url}
            alt={item.name}
            fill
            sizes="(min-width: 1024px) 25vw, 50vw"
            className="object-cover"
          />
          {item.badge ? (
            <span className="absolute left-2 top-2 rounded-full bg-black/80 px-2 py-1 text-xs text-white">
              {item.badge}
            </span>
          ) : null}
        </div>
      </CardHeader>

      <CardContent className="pt-4">
        <CardTitle className="text-base line-clamp-1">{item.name}</CardTitle>
        <p className="mt-1 text-sm text-muted-foreground">{price}</p>
      </CardContent>

      <CardFooter className="gap-2">
        <Link href={`/catalog/${item.id}`} className="w-full">
          {/* was: <Button variant="outline" ...> */}
          <Button className="w-full border">View</Button>
        </Link>
        <Button className="w-full">Add to cart</Button>
      </CardFooter>
    </Card>
  );
}

export default function CatalogPage() {
  const [query, setQuery] = React.useState("");

  const items = React.useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return MOCK_ITEMS;
    return MOCK_ITEMS.filter((i) => i.name.toLowerCase().includes(q));
  }, [query]);

  return (
    <main className="container mx-auto px-6 py-10">
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
          {/* was: <Button variant="outline" ...> */}
          <Button className="border" onClick={() => setQuery("")}>
            Clear
          </Button>
        </div>
      </header>

      <section className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {items.map((item) => (
          <CatalogItemCard key={item.id} item={item} />
        ))}
      </section>
    </main>
  );
}
