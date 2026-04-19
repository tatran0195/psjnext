// app/[lang]/api/[version]/[[...slug]]/layout.tsx
//
// Pass-through layout wrapper ở slug level.
// DocsLayout đã được mount ở [version]/layout.tsx — file này chỉ cần
// tồn tại để Next.js App Router nhận đúng layout segment chain.
// Nếu thiếu file này, DocsLayout của [version] sẽ không wrap được [[...slug]].

import type { ReactNode } from 'react'

export default function SlugLayout({ children }: { children: ReactNode }) {
  return <>{children}</>
}
