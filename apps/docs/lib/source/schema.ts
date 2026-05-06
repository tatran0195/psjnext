import { metaSchema, pageSchema } from 'fumadocs-core/source/schema';
import { z } from 'zod';

export const docsSchema = pageSchema.extend({
    index: z.boolean().default(false),
    ribbon: z.string().optional(),
    shortcut: z.string().optional(),
    introduced: z.string().optional(),
    deprecated: z.string().optional(),
    removed: z.string().optional(),
    _version: z.string().optional(),
    _status: z.string().optional(),
});

export const metaSchemaWithGroup = metaSchema.extend({
    group: z.boolean().optional(),
});
