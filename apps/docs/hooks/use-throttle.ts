import { useEffect, useRef, useState } from 'react';

/**
 * Returns a throttled version of `value` that updates at most once every `interval` ms.
 *
 * @example
 * ```tsx
 * const throttledSearch = useThrottledValue(search, 300);
 * ```
 */
export function useThrottledValue<T>(value: T, interval: number): T {
    const [throttled, setThrottled] = useState(value);
    const lastUpdated = useRef<number | null>(null);

    useEffect(() => {
        const now = Date.now();
        if (lastUpdated.current === null || now - lastUpdated.current >= interval) {
            lastUpdated.current = now;
            setThrottled(value);
            return undefined;
        } else {
            const remaining = interval - (now - lastUpdated.current);
            const timer = setTimeout(() => {
                lastUpdated.current = Date.now();
                setThrottled(value);
            }, remaining);
            return () => clearTimeout(timer);
        }
    }, [value, interval]);

    return throttled;
}
