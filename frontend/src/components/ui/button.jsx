import React from 'react'

export const Button = React.forwardRef(({ className, variant, size, asChild = false, ...props }, ref) => {
  const Comp = asChild ? "span" : "button"
  
  // Basic button styles that resemble shadcn/ui buttons
  let variantClasses = "bg-black text-white hover:bg-black/90"
  if (variant === "outline") variantClasses = "border border-gray-200 bg-white hover:bg-gray-100 text-gray-900"
  if (variant === "ghost") variantClasses = "hover:bg-gray-100 hover:text-gray-900"
  if (variant === "secondary") variantClasses = "bg-gray-100 text-gray-900 hover:bg-gray-200"
  if (variant === "destructive") variantClasses = "bg-red-500 text-white hover:bg-red-600"
  if (variant === "link") variantClasses = "text-black underline-offset-4 hover:underline"

  let sizeClasses = "h-10 px-4 py-2"
  if (size === "sm") sizeClasses = "h-9 rounded-md px-3"
  if (size === "lg") sizeClasses = "h-11 rounded-md px-8"
  if (size === "icon") sizeClasses = "h-10 w-10"

  const defaultClasses = `inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-white transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-gray-950 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 ${variantClasses} ${sizeClasses} ${className || ""}`
  
  return (
    <Comp
      className={defaultClasses}
      ref={ref}
      {...props}
    />
  )
})

Button.displayName = "Button"
