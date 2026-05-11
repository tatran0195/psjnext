import { ChevronRight, MousePointerClick } from 'lucide-react';

interface RibbonPathProps {
    ribbon: string;
    shortcut?: string;
    variant?: 'inline' | 'ghost';
    className?: string;
}

export function RibbonPath({ ribbon, shortcut, variant = 'inline', className = '' }: RibbonPathProps) {
    const segments = ribbon.split('>').map((s) => s.trim());
    const lastIndex = segments.length - 1;

    if (variant === 'ghost')
        return <GhostVariant segments={segments} shortcut={shortcut} className={className} lastIndex={lastIndex} />;

    return <InlineVariant segments={segments} shortcut={shortcut} className={className} lastIndex={lastIndex} />;
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
        <div className={`not-prose flex items-center gap-2 flex-wrap ${className}`}>
            <MousePointerClick size={12} style={{ color: 'var(--psj-text-3)' }} className="shrink-0" />
            {segments.map((seg, i) => {
                const isFinal = i === lastIndex;
                return (
                    <span key={i} className="flex items-center gap-2">
                        {i > 0 && (
                            <ChevronRight size={11} style={{ color: 'var(--psj-text-3)' }} className="shrink-0" />
                        )}
                        <span
                            className={`text-xs ${isFinal ? 'font-medium' : ''}`}
                            style={{ color: isFinal ? 'var(--psj-text-1)' : 'var(--psj-text-3)' }}
                        >
                            {seg}
                        </span>
                    </span>
                );
            })}
            {shortcut && (
                <kbd
                    className="ml-1 inline-flex items-center gap-0.5 px-1.5 py-0.5 font-mono text-[10px]"
                    style={{
                        border: '1px solid var(--psj-border)',
                        background: 'var(--psj-surface-1)',
                        color: 'var(--psj-text-2)',
                    }}
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
            className={`not-prose flex items-center gap-2 text-xs flex-wrap ${className}`}
            style={{ color: 'var(--psj-text-3)' }}
        >
            <MousePointerClick size={12} className="shrink-0" />
            {segments.map((seg, i) => (
                <span key={i} className="flex items-center gap-2">
                    {i > 0 && <span style={{ opacity: 0.3 }}>/</span>}
                    <span
                        className={i === lastIndex ? 'font-medium' : ''}
                        style={{
                            color: i === lastIndex ? 'var(--psj-text-1)' : 'var(--psj-text-3)',
                        }}
                    >
                        {seg}
                    </span>
                </span>
            ))}
            {shortcut && (
                <kbd
                    className="ml-1 px-1.5 py-0.5 font-mono text-[10px]"
                    style={{
                        border: '1px solid var(--psj-border)',
                        background: 'var(--psj-surface-1)',
                        color: 'var(--psj-text-2)',
                    }}
                >
                    {shortcut}
                </kbd>
            )}
        </p>
    );
}
