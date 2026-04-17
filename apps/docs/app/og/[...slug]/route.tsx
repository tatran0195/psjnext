import { notFound } from 'next/navigation';

import { ImageResponse } from '@takumi-rs/image-response';

import { getPageImage } from '@/lib/metadata';
import { source } from '@/lib/source';

import { generate as MetadataImage, getImageResponseOptions } from './generate';

export const revalidate = false;

export async function GET(_req: Request, props: { params: Promise<{ slug: string[] }> }) {
    const params = await props.params;
    const { slug } = params;
    const lang = slug[0];
    const pageSlugs = slug.slice(1, -1);
    const page = source.getPage(pageSlugs, lang);
    if (!page) notFound();

    return new ImageResponse(
        <MetadataImage title={page.data.title} description={page.data.description} />,
        await getImageResponseOptions(),
    );
}

export function generateStaticParams(): {
    slug: string[];
}[] {
    return source.getPages().map((page) => ({
        slug: getPageImage(page).segments.map(String),
    }));
}
