import { ChevronRight, MousePointerClick, Option } from 'lucide-react';
import { z } from 'zod';

const ribbonItemSchema = z.object({
    label: z.string(), // Display label of the item
    icon: z.string().optional(), // Icon name (lucide, custom SVG key, etc.)
    shortcut: z.string().optional(), // Keyboard shortcut e.g. "Alt+M, N"
    tooltip: z.string().optional(), // Tooltip text shown on hover
});

const ribbonFlyoutSchema = ribbonItemSchema.extend({
    flyout: z.array(ribbonItemSchema).optional(), // Nested flyout/dropdown items
});

const ribbonGroupSchema = z.object({
    label: z.string(), // Panel/Group label e.g. "Geometry Tools"
    item: ribbonFlyoutSchema, // The button inside the group
});

const ribbonSchema = z.object({
    tab: z.string(), // Top-level tab e.g. "Mesh", "Analysis"
    panel: ribbonGroupSchema, // Panel and its item
    note: z.string().optional(), // Any extra navigation note
});

export type Ribbon = z.infer<typeof ribbonSchema>;
export type RibbonItem = z.infer<typeof ribbonItemSchema>;
export type RibbonFlyout = z.infer<typeof ribbonFlyoutSchema>;

export function RibbonPath({ ribbon }: { ribbon: string }) {
    const parsed = ribbonSchema.safeParse(ribbon);
    if (!parsed.success) {
        // If parsing fails, render the original string as a fallback
        return <>{ribbon}</>;
    }

    const ribbonData = parsed.data;
    const { tab, panel } = ribbonData;
    const { item } = panel;
    const hasFlyout = item.flyout && item.flyout.length > 0;

    // Build flat segment list
    const segments: { label: string; shortcut?: string }[] = [
        { label: tab },
        { label: panel.label },
        {
            label: item.label,
            shortcut: !hasFlyout ? item.shortcut : undefined,
        },
        ...(item.flyout?.map((f) => ({
            label: f.label,
            shortcut: f.shortcut,
        })) ?? []),
    ];

    const lastIndex = segments.length - 1;

    return (
        <div className="not-prose mt-2 mb-1 flex items-center gap-1 flex-wrap">
            {/* Icon label */}
            <span className="flex items-center gap-1 text-xs text-muted-foreground mr-1">
                <MousePointerClick className="h-3 w-3" />
                <span className="uppercase tracking-wider font-semibold text-[10px]">Ribbon</span>
            </span>

            {segments.map((seg, i) => {
                const isFinal = i === lastIndex;
                return (
                    <span key={i} className="flex items-center gap-1">
                        {i > 0 && (
                            <ChevronRight className="h-3 w-3 text-muted-foreground shrink-0" />
                        )}
                        {/* Segment pill */}
                        <span
                            className={`
                                inline-flex items-center gap-1 rounded px-2 py-0.5 text-xs font-medium
                                ${
                                    isFinal
                                        ? 'bg-(--color-fd-primary)/10 text-(--color-fd-primary) ring-1 ring-inset ring-(--color-fd-primary)/25'
                                        : 'text-muted-foreground'
                                }
                            `}
                        >
                            {seg.label}
                        </span>
                        {/* Shortcut badge — only on final segment */}
                        {isFinal && seg.shortcut && (
                            <span
                                className="inline-flex items-center gap-0.5 rounded bg-muted 
                               px-1.5 py-0.5 font-mono text-[10px] text-muted-foreground
                               ring-1 ring-inset ring-border"
                            >
                                <Option className="h-2.5 w-2.5" />
                                {seg.shortcut}
                            </span>
                        )}
                    </span>
                );
            })}
        </div>
    );
}
