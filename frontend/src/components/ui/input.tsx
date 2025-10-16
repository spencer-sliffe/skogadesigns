import * as React from "react";

type Props = React.InputHTMLAttributes<HTMLInputElement>;

export function Input({ className = "", ...props }: Props) {
  return (
    <input
      className={`w-full rounded-md border border-neutral-300 bg-white px-3 py-2 text-sm
                  focus:outline-none focus:ring-2 focus:ring-neutral-800 ${className}`}
      {...props}
    />
  );
}
export default Input;
