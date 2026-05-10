import { Globe2, Mail, Phone, ShieldCheck } from 'lucide-react';

/**
 * Global utility bar — shown above the main header on md+ screens.
 * Uses PSJ design tokens. Dark mode handled via CSS variables.
 */
export function TopBar() {
    return (
        <div className="hidden md:block border-b"
            style={{
                background: 'var(--psj-surface-3)',
                borderColor: 'var(--psj-border)',
            }}
        >
            <div className="max-w-[1280px] mx-auto px-6 lg:px-10 py-1.5 flex items-center justify-between">
                <div className="flex items-center gap-5">
                    <a
                        href="tel:+81312345678"
                        className="flex items-center gap-1.5 text-[11px] transition-colors"
                        style={{ color: 'var(--psj-text-3)' }}
                    >
                        <Phone size={9} strokeWidth={2.5} />
                        +81 3-1234-5678
                    </a>
                    <a
                        href="mailto:contact@e-technostar.com"
                        className="flex items-center gap-1.5 text-[11px] transition-colors"
                        style={{ color: 'var(--psj-text-3)' }}
                    >
                        <Mail size={9} strokeWidth={2.5} />
                        contact@e-technostar.com
                    </a>
                </div>
                <div className="flex items-center gap-5">
                    <span className="flex items-center gap-1.5 text-[11px]"
                        style={{ color: 'var(--psj-text-3)' }}>
                        <Globe2 size={9} strokeWidth={2.5} />
                        EN / JP
                    </span>
                    <span className="flex items-center gap-1.5 text-[11px] font-medium"
                        style={{ color: 'var(--psj-text-3)' }}>
                        <ShieldCheck size={9} strokeWidth={2.5} />
                        ISO 9001:2015
                    </span>
                </div>
            </div>
        </div>
    );
}
