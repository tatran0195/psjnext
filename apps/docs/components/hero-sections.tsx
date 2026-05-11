interface HeroSectionProps {
    label: string;
    title: string;
    description: string;
}

export function HeroSection({ label, title, description }: HeroSectionProps) {
    return (
        <section className="psj-subpage-hero">
            <div className="psj-container py-10 lg:py-14 relative z-10">
                <div className="max-w-4xl">
                    <div className="psj-label mb-2">{label}</div>
                    <h1 className="psj-h1 mb-4 text-4xl lg:text-5xl" style={{ color: 'var(--psj-text-1)' }}>
                        {title}
                    </h1>
                    <p
                        className="text-base lg:text-lg leading-relaxed max-w-2xl"
                        style={{ color: 'var(--psj-text-2)' }}
                    >
                        {description}
                    </p>
                </div>
            </div>
        </section>
    );
}
