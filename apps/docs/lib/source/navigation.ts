export function getSection(path: string | undefined) {
    if (!path) return 'framework';
    const [dir] = path.split('/', 1);
    if (!dir) return 'framework';
    return (
        {
            api: 'api',
            guides: 'guides',
            dataType: 'data-type',
        }[dir] ?? 'framework'
    );
}
