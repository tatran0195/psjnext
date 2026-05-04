import { source } from './apps/docs/lib/source/index';

const lang = 'en';
const slugs = ['app', 'psj-command', 'ac-modeling', 'ACModeling.ACBoundary.FirstMethod'];
const page = source.getPage(slugs, lang);

console.log('Slugs:', slugs);
console.log('Page found:', page ? page.data.title : 'NOT FOUND');
if (page) {
    console.log('Version Introduced:', page.data.version_introduced);
}
