import { cn } from '@/lib/cn';

interface VersionBadgeProps {
    version: string;
    className?: string;
}

export function VersionBadge({ version, className }: VersionBadgeProps) {
    return (
        <div className={cn('flex', className)}>
            <span className="flex items-center gap-2 px-2 py-1 rounded-none bg-fd-secondary/30 border-l-2 border-l-fd-primary border-y border-r border-fd-border/50 text-[10px] font-bold uppercase tracking-wider text-fd-foreground group/version-badge hover:bg-fd-secondary transition-colors cursor-default">
                <span className="font-sans opacity-70">Since</span>
                <span className="font-mono text-[11px] font-bold text-fd-primary tracking-normal lowercase">
                    v{version}
                </span>
            </span>
        </div>
    );
}

export function DeprecatedBadge({ className }: { className?: string }) {
    return (
        <span
            className={cn(
                'text-[10.5px] font-bold text-red-600 dark:text-red-500 uppercase tracking-[0.15em] align-middle',
                className,
            )}
        >
            Deprecated
        </span>
    );
}
