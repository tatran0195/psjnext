import { ChevronRight, MousePointerClick } from 'lucide-react';

interface RibbonPathProps {
    ribbon: string;
    shortcut?: string;
    variant?: 'inline' | 'ghost';
    className?: string;
}

export function RibbonPath({
    ribbon,
    shortcut,
    variant = 'inline',
    className = '',
}: RibbonPathProps) {
    const segments = ribbon.split('>').map((s) => s.trim());
    const lastIndex = segments.length - 1;

    if (variant === 'ghost')
        return (
            <GhostVariant
                segments={segments}
                shortcut={shortcut}
                className={className}
                lastIndex={lastIndex}
            />
        );

    return (
        <InlineVariant
            segments={segments}
            shortcut={shortcut}
            className={className}
            lastIndex={lastIndex}
        />
    );
}

function InlineVariant({
    segments,
    shortcut,
    lastIndex,
    className,
}: {
    segments: string[];
    lastIndex: number;
    shortcut?: string;
    className?: string;
}) {
    return (
        <div className={`not-prose flex items-center gap-1 flex-wrap ${className}`}>
            <MousePointerClick className="h-3 w-3 text-muted-foreground shrink-0" />
            {segments.map((seg, i) => {
                const isFinal = i === lastIndex;
                return (
                    <span key={i} className="flex items-center gap-1">
                        {i > 0 && (
                            <ChevronRight className="h-3 w-3 text-muted-foreground/40 shrink-0" />
                        )}
                        <span
                            className={`text-xs font-medium ${
                                isFinal ? 'text-primary' : 'text-muted-foreground'
                            }`}
                        >
                            {seg}
                        </span>
                    </span>
                );
            })}
            {shortcut && (
                <kbd
                    className="ml-1 inline-flex items-center gap-0.5 rounded border 
                        border-border bg-muted px-1.5 py-0.5 
                        font-mono text-[10px] text-muted-foreground"
                >
                    {shortcut}
                </kbd>
            )}
        </div>
    );
}

function GhostVariant({
    segments,
    shortcut,
    lastIndex,
    className,
}: {
    segments: string[];
    shortcut?: string;
    lastIndex: number;
    className?: string;
}) {
    return (
        <p
            className={`not-prose flex items-center gap-1 text-xs 
                   text-muted-foreground flex-wrap ${className}`}
        >
            <MousePointerClick className="h-3 w-3 shrink-0" />
            {segments.map((seg, i) => (
                <span key={i} className="flex items-center gap-1">
                    {i > 0 && <span className="opacity-30">/</span>}
                    <span className={i === lastIndex ? 'text-foreground font-medium' : ''}>
                        {seg}
                    </span>
                </span>
            ))}
            {shortcut && (
                <kbd
                    className="ml-1 rounded border border-border bg-muted 
                        px-1.5 py-0.5 font-mono text-[10px]"
                >
                    {shortcut}
                </kbd>
            )}
        </p>
    );
}
