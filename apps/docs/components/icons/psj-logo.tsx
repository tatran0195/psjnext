export function PsjLogo() {
    return (
        <div className="flex items-center gap-3">
            <div className="w-9 h-9 bg-blue flex items-center justify-center shrink-0">
                <span className="text-white font-bold text-sm tracking-wider">PSJ</span>
            </div>
            <div className="hidden sm:block">
                <div className="text-sm font-bold leading-tight">e-TechnoStar</div>
                <div className="text-[10px] text-text-muted leading-tight tracking-wider uppercase">
                    CAE Engineering Services
                </div>
            </div>
        </div>
    );
}
