"use client";

import * as React from "react";

type Variant = "default" | "outline" | "ghost";
type Size = "sm" | "md" | "lg";

type ButtonProps = Omit<
  React.ButtonHTMLAttributes<HTMLButtonElement>,
  "className"
> & {
  className?: string;
  variant?: Variant;
  size?: Size;
};

function variantClasses(variant: Variant) {
  switch (variant) {
    case "outline":
      return "border bg-transparent hover:bg-muted text-foreground";
    case "ghost":
      return "bg-transparent hover:bg-muted text-foreground";
    default:
      return "bg-black text-white hover:bg-neutral-800";
  }
}

function sizeClasses(size: Size) {
  switch (size) {
    case "sm":
      return "h-8 px-3 text-sm";
    case "lg":
      return "h-11 px-5 text-base";
    default:
      return "h-10 px-4 text-sm";
  }
}

export function Button({
  variant = "default",
  size = "md",
  className = "",
  ...rest
}: ButtonProps) {
  // NOTE: variant/size are consumed here and NOT spread to DOM
  const classes = [
    "inline-flex items-center justify-center rounded-md font-medium",
    "disabled:opacity-50 disabled:cursor-not-allowed",
    variantClasses(variant),
    sizeClasses(size),
    className,
  ]
    .filter(Boolean)
    .join(" ");

  return <button className={classes} {...rest} />;
}

export default Button;
