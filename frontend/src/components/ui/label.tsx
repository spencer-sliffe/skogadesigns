import * as React from "react";

type Props = React.LabelHTMLAttributes<HTMLLabelElement>;

export function Label({ className = "", ...props }: Props) {
  return <label className={`text-sm font-medium ${className}`} {...props} />;
}
export default Label;
