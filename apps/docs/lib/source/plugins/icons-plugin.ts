import { createElement } from 'react';

import { LoaderPlugin } from 'fumadocs-core/source';
import { icons } from 'lucide-react';

import { Icons } from '@/components/icons';
import { iconPlugin } from '@/lib/source/plugins/icon-plugin';

/**
 * Convert icon names into Lucide Icons, requires `lucide-react` to be installed.
 */
export function iconsPlugin(
    options: {
        defaultIcon?: keyof typeof icons;
    } = {},
): LoaderPlugin {
    const { defaultIcon } = options;
    return iconPlugin((icon = defaultIcon) => {
        if (icon === undefined) return;
        const Icon = icons[icon as keyof typeof icons] || Icons[icon as keyof typeof Icons];
        if (!Icon) {
            console.warn(`[icons-plugin] Unknown icon detected: ${icon}.`);
            return;
        }

        return createElement(Icon);
    });
}
