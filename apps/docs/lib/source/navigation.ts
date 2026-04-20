export function getSection(path: string | undefined) {
    if (!path) return 'framework';
    const [dir] = path.split('/', 1);
    if (!dir) return 'framework';
    return (
        {
            api: 'api',
            guides: 'guides',
            'data-type': 'data-type',
        }[dir] ?? 'framework'
    );
}
