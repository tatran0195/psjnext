import { NextResponse } from 'next/server';

import { getSiteOrigin } from '@/lib/site-url';
import { changelog } from '@/lib/source';

export async function GET() {
    const origin = getSiteOrigin();
    const entries = changelog
        .getPages()
        .sort((a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime())
        .filter((entry) => !entry.data.draft);

    const rssItems = entries
        .map((entry) => {
            const url = `${origin}/changelog/${entry.data.slug}`;
            const date = new Date(entry.data.date).toUTCString();

            return `
    <item>
      <title><![CDATA[${entry.data.version} - ${entry.data.title}]]></title>
      <link>${url}</link>
      <guid isPermaLink="true">${url}</guid>
      <pubDate>${date}</pubDate>
      <description><![CDATA[${entry.data.summary}]]></description>
      ${entry.data.tags ? entry.data.tags.map((tag) => `<category>${tag}</category>`).join('') : ''}
    </item>`;
        })
        .join('');

    const rss = `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>PSJ Product Changelog</title>
    <link>${origin}/changelog</link>
    <description>Stay up to date with the latest features, improvements, and fixes in PSJ.</description>
    <language>en-us</language>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
    <atom:link href="${origin}/api/changelog/feed" rel="self" type="application/rss+xml" />
    ${rssItems}
  </channel>
</rss>`;

    return new NextResponse(rss, {
        headers: {
            'Content-Type': 'application/xml',
            'Cache-Control': 'public, s-maxage=3600, stale-while-revalidate=59',
        },
    });
}
