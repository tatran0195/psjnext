import { Suspense } from 'react';

import Link from 'fumadocs-core/link';
import { buttonVariants } from 'fumadocs-ui/components/ui/button';

import { cn } from '@/lib/cn';

export interface Suggestion {
    id: string;
    href: string;
    title: string;
}

export interface NotFoundProps {
    getSuggestions: () => Promise<Suggestion[]>;
}

export function NotFound(props: NotFoundProps) {
    return (
        <div className="mx-auto flex w-full max-w-3xl flex-col items-center px-6 py-20 [grid-area:main]">
            <div className="space-y-2 text-center">
                <h1 className="text-3xl font-semibold tracking-tight">Page not found</h1>

                <p className="text-sm text-fd-muted-foreground">We found some similar pages that might help.</p>
            </div>

            <div className="mt-8 w-full">
                <Suspense
                    fallback={
                        <div className="overflow-hidden rounded-none border bg-fd-card shadow-sm">
                            <div className="px-5 py-4 text-sm text-fd-muted-foreground">Finding alternatives...</div>
                        </div>
                    }
                >
                    <Alternative {...props} />
                </Suspense>
            </div>
        </div>
    );
}

async function Alternative({ getSuggestions }: NotFoundProps) {
    const suggestions = await getSuggestions();

    if (suggestions.length === 0) {
        return (
            <div className="rounded-none border bg-fd-card p-8 text-center shadow-sm">
                <p className="mb-4 text-sm text-fd-muted-foreground">No similar pages found.</p>

                <Link href="/" className={cn(buttonVariants({ variant: 'secondary' }))}>
                    Return home
                </Link>
            </div>
        );
    }

    return (
        <div className="overflow-hidden rounded-none border bg-fd-card shadow-sm">
            {suggestions.map((doc, index) => (
                <Link
                    key={doc.id}
                    href={doc.href}
                    className={cn(
                        'group relative flex items-start gap-4 px-5 py-4 transition-all duration-200',
                        'hover:bg-fd-accent/40 hover:shadow-sm',
                        index !== suggestions.length - 1 && 'border-b',
                    )}
                >
                    <div className="min-w-0 flex-1 text-left">
                        <p
                            className={cn(
                                'text-sm font-medium leading-5 text-fd-foreground',
                                '[&_mark]:rounded-none',
                                '[&_mark]:bg-fd-primary/15',
                                '[&_mark]:px-1',
                                '[&_mark]:py-0.5',
                                '[&_mark]:font-semibold',
                                '[&_mark]:text-fd-foreground',
                            )}
                            dangerouslySetInnerHTML={{
                                __html: doc.title,
                            }}
                        />

                        <code className="mt-1.5 block break-all text-[11px] leading-relaxed text-fd-muted-foreground">
                            {doc.href}
                        </code>
                    </div>

                    <div
                        className={cn(
                            'mt-0.5 shrink-0 text-fd-muted-foreground/60',
                            'transition-all duration-200',
                            'group-hover:translate-x-0.5',
                            'group-hover:text-fd-foreground',
                        )}
                    >
                        →
                    </div>
                </Link>
            ))}
        </div>
    );
}
