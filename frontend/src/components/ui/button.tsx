import * as React from "react";

type Props = React.ButtonHTMLAttributes<HTMLButtonElement> & { asChild?: boolean };

export function Button({ className = "", ...props }: Props) {
  return (
    <button
      className={`inline-flex items-center justify-center rounded-md px-4 py-2 text-sm font-medium
                  bg-black text-white hover:bg-neutral-800 disabled:opacity-50 disabled:cursor-not-allowed ${className}`}
      {...props}
    />
  );
}
export default Button;
