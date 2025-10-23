"use client";

import Link from "next/link";
import Image from "next/image";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export type CatalogItem = {
  id: number | string;
  name: string;
  price_cents: number; // match backend
  image_url: string;
  badge?: string;
};

export default function CatalogItemCard({ item }: { item?: CatalogItem }) {
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
          {/* outline → border; keep full width */}
          <Button className="w-full border">View</Button>
        </Link>
        <Button className="w-full">Add to cart</Button>
      </CardFooter>
    </Card>
  );
}
