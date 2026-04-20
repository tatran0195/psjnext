/**
 * Minimal structured logger with step timing.
 *
 * Keeps output clean and machine-parseable without pulling in a heavy
 * logging framework.
 */

const START = Date.now();

function elapsed(): string {
    return `+${(Date.now() - START).toString().padStart(5)}ms`;
}

export const logger = {
    info(message: string, meta?: Record<string, unknown>): void {
        const suffix = meta ? ` ${JSON.stringify(meta)}` : '';
        console.log(`[${elapsed()}] [i]  ${message}${suffix}`);
    },

    step(message: string): void {
        console.log(`[${elapsed()}] [>]  ${message}`);
    },

    ok(message: string, meta?: Record<string, unknown>): void {
        const suffix = meta ? ` ${JSON.stringify(meta)}` : '';
        console.log(`[${elapsed()}] [✓]  ${message}${suffix}`);
    },

    warn(message: string): void {
        console.warn(`[${elapsed()}] [!]  ${message}`);
    },

    error(message: string, err?: unknown): void {
        console.error(`[${elapsed()}] [✗]  ${message}`);
        if (err instanceof Error) {
            console.error(`       ${err.message}`);
            if (err.stack) console.error(err.stack);
        } else if (err !== undefined) {
            console.error(err);
        }
    },
};
