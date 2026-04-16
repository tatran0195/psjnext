import { metaSchema, pageSchema } from 'fumadocs-core/source/schema';
import { z } from 'zod';

const RibbonItemSchema = z.object({
    label: z.string(), // Display label of the item
    icon: z.string().optional(), // Icon name (lucide, custom SVG key, etc.)
    shortcut: z.string().optional(), // Keyboard shortcut e.g. "Alt+M, N"
    tooltip: z.string().optional(), // Tooltip text shown on hover
});

const RibbonFlyoutSchema = RibbonItemSchema.extend({
    flyout: z.array(RibbonItemSchema).optional(), // Nested flyout/dropdown items
});

const RibbonGroupSchema = z.object({
    label: z.string(), // Panel/Group label e.g. "Geometry Tools"
    item: RibbonFlyoutSchema, // The button inside the group
});

const RibbonSchema = z.object({
    tab: z.string(), // Top-level tab e.g. "Mesh", "Analysis"
    panel: RibbonGroupSchema, // Panel and its item
    note: z.string().optional(), // Any extra navigation note
});

export type Ribbon = z.infer<typeof RibbonSchema>;
export type RibbonItem = z.infer<typeof RibbonItemSchema>;
export type RibbonFlyout = z.infer<typeof RibbonFlyoutSchema>;

export const DocsSchema = pageSchema.extend({
    preview: z.string().optional(),
    index: z.boolean().default(false),
    method: z.string().optional(),
    ribbon: RibbonSchema.optional(),
});

export const MetaSchema = metaSchema.extend({
    description: z.string().optional(),
    group: z.boolean().optional(),
});
