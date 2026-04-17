import fs from 'node:fs';
import { createHighlighter } from 'shiki';

export const psjGrammar = JSON.parse(fs.readFileSync('./lib/shiki/psj.json', 'utf8'));

export const getPSJHighlighter = createHighlighter({
    langs: [psjGrammar],
    themes: ['github-light', 'github-dark'],
});
