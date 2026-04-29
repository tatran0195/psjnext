import { metaSchema, pageSchema } from 'fumadocs-core/source/schema';
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

export const docsSchema = pageSchema.extend({
    preview: z.string().optional(),
    index: z.boolean().default(false),
    method: z.string().optional(),
    tag: z.string().optional(),
    ribbon: ribbonSchema.optional(),
});

export const metaSchemaWithGroup = metaSchema.extend({
    group: z.boolean().optional(),
    groupLevel: z.number().optional(),
});
