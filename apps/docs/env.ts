import { createEnv } from '@t3-oss/env-nextjs';
import { z } from 'zod';

const csvArray = z.string().transform((value) =>
    value
        .split(',')
        .map((v) => v.trim())
        .filter(Boolean),
);

export const env = createEnv({
    server: {
        API_VERSIONS: csvArray.pipe(z.array(z.string())),
    },

    client: {
        NEXT_PUBLIC_SITE_URL: z.url().optional(),
    },

    runtimeEnv: {
        API_VERSIONS: process.env.API_VERSIONS,
        NEXT_PUBLIC_SITE_URL: process.env.NEXT_PUBLIC_SITE_URL,
    },
});
